"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Create a Solidity contract for a compliant tokenized fund that ensures security, transparency, and liquidity for investors, based on Singularity Finance's tokenization framework.
Generated: DETERMINISTIC_3b41d92eb6cc26c4
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CompliantTokenizedFund
 * @dev A compliant tokenized fund contract with security, transparency, and liquidity features
 */
contract CompliantTokenizedFund is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Fund manager details
    struct ManagerInfo {
        address managerAddress;
        uint256 performanceFee; // Basis points (e.g., 200 = 2%)
        uint256 managementFee;  // Basis points (e.g., 100 = 1%)
    }

    // Investor restrictions
    struct InvestorRestrictions {
        bool isWhitelisted;
        uint256 minInvestment;
        uint256 maxInvestment;
    }

    // Fund parameters
    uint256 public fundCreationDate;
    uint256 public fundCloseDate;
    uint256 public totalFundSize;
    uint256 public currentNav; // Net Asset Value
    uint256 public lastNavUpdate;

    // Fees and distributions
    uint256 public constant FEE_DENOMINATOR = 10000;
    uint256 public constant MAX_PERFORMANCE_FEE = 2000; // 20%
    uint256 public constant MAX_MANAGEMENT_FEE = 500;   // 5%

    // State variables
    ManagerInfo public manager;
    mapping(address => InvestorRestrictions) public investorRestrictions;
    mapping(address => bool) public authorizedOperators;

    // Events
    event NavUpdated(uint256 newNav, uint256 timestamp);
    event FeesDistributed(uint256 performanceFee, uint256 managementFee);
    event InvestorWhitelisted(address investor, uint256 minInvestment, uint256 maxInvestment);
    event InvestmentReceived(address investor, uint256 amount);
    event RedemptionProcessed(address investor, uint256 amount);

    /**
     * @dev Constructor to initialize the tokenized fund
     * @param _name Name of the fund token
     * @param _symbol Symbol of the fund token
     * @param _managerAddress Address of the fund manager
     * @param _performanceFee Performance fee in basis points
     * @param _managementFee Management fee in basis points
     * @param _fundCloseDate Date when fund closes for investments
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _managerAddress,
        uint256 _performanceFee,
        uint256 _managementFee,
        uint256 _fundCloseDate
    ) ERC20(_name, _symbol) {
        require(_managerAddress != address(0), "Invalid manager address");
        require(_performanceFee <= MAX_PERFORMANCE_FEE, "Performance fee too high");
        require(_managementFee <= MAX_MANAGEMENT_FEE, "Management fee too high");
        require(_fundCloseDate > block.timestamp, "Close date must be in future");

        fundCreationDate = block.timestamp;
        fundCloseDate = _fundCloseDate;
        
        manager = ManagerInfo({
            managerAddress: _managerAddress,
            performanceFee: _performanceFee,
            managementFee: _managementFee
        });

        // Mint initial supply to manager (can be zero)
        _mint(_managerAddress, 0);
    }

    /**
     * @dev Modifier to check if caller is manager or authorized operator
     */
    modifier onlyManagerOrOperator() {
        require(
            msg.sender == manager.managerAddress || authorizedOperators[msg.sender],
            "Not authorized"
        );
        _;
    }

    /**
     * @dev Update NAV (Net Asset Value) of the fund
     * @param newNav The new NAV value
     */
    function updateNav(uint256 newNav) external onlyManagerOrOperator {
        require(newNav > 0, "NAV must be positive");
        currentNav = newNav;
        lastNavUpdate = block.timestamp;
        emit NavUpdated(newNav, block.timestamp);
    }

    /**
     * @dev Whitelist an investor with investment restrictions
     * @param investor Address of the investor
     * @param minInvestment Minimum investment amount
     * @param maxInvestment Maximum investment amount
     */
    function whitelistInvestor(
        address investor,
        uint256 minInvestment,
        uint256 maxInvestment
    ) external onlyManagerOrOperator {
        require(investor != address(0), "Invalid investor address");
        require(minInvestment <= maxInvestment, "Invalid investment limits");

        investorRestrictions[investor] = InvestorRestrictions({
            isWhitelisted: true,
            minInvestment: minInvestment,
            maxInvestment: maxInvestment
        });

        emit InvestorWhitelisted(investor, minInvestment, maxInvestment);
    }

    /**
     * @dev Invest in the fund by sending ETH and receiving fund tokens
     */
    function invest() external payable whenNotPaused {
        require(block.timestamp <= fundCloseDate, "Fund closed for investments");
        InvestorRestrictions storage restrictions = investorRestrictions[msg.sender];
        require(restrictions.isWhitelisted, "Investor not whitelisted");
        require(
            msg.value >= restrictions.minInvestment,
            "Investment below minimum"
        );
        require(
            msg.value <= restrictions.maxInvestment,
            "Investment above maximum"
        );

        // Calculate tokens to mint based on current NAV
        uint256 tokensToMint = msg.value.mul(1e18).div(currentNav);
        _mint(msg.sender, tokensToMint);
        totalFundSize = totalFundSize.add(msg.value);

        emit InvestmentReceived(msg.sender, msg.value);
    }

    /**
     * @dev Redeem fund tokens for underlying assets
     * @param amount Amount of tokens to redeem
     */
    function redeem(uint256 amount) external whenNotPaused {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(amount > 0, "Amount must be positive");

        // Calculate ETH to send based on current NAV
        uint256 ethToSend = amount.mul(currentNav).div(1e18);
        require(address(this).balance >= ethToSend, "Insufficient fund liquidity");

        _burn(msg.sender, amount);
        totalFundSize = totalFundSize.sub(ethToSend);
        payable(msg.sender).transfer(ethToSend);

        emit RedemptionProcessed(msg.sender, amount);
    }

    /**
     * @dev Distribute fees to the fund manager
     */
    function distributeFees() external onlyManagerOrOperator {
        uint256 managementFeeAmount = totalFundSize.mul(manager.managementFee).div(FEE_DENOMINATOR);
        uint256 performanceFeeAmount = calculatePerformanceFee();

        if (managementFeeAmount > 0) {
            payable(manager.managerAddress).transfer(managementFeeAmount);
            totalFundSize = totalFundSize.sub(managementFeeAmount);
        }

        if (performanceFeeAmount > 0) {
            payable(manager.managerAddress).transfer(performanceFeeAmount);
            totalFundSize = totalFundSize.sub(performanceFeeAmount);
        }

        emit FeesDistributed(performanceFeeAmount, managementFeeAmount);
    }

    /**
     * @dev Calculate performance fee based on NAV increase
     */
    function calculatePerformanceFee() internal view returns (uint256) {
        // Implementation depends on specific performance calculation
        // This is a placeholder - actual implementation would compare
        // current NAV to some benchmark or previous high watermark
        return 0;
    }

    /**
     * @dev Authorize an operator address
     * @param operator Address to authorize
     */
    function authorizeOperator(address operator) external onlyOwner {
        require(operator != address(0), "Invalid operator address");
        authorizedOperators[operator] = true;
    }

    /**
     * @dev Revoke operator authorization
     * @param operator Address to revoke
     */
    function revokeOperator(address operator) external onlyOwner {
        require(operator != address(0), "Invalid operator address");
        authorizedOperators[operator] = false;
    }

    /**
     * @dev Pause fund operations
     */
    function pause() external onlyManagerOrOperator {
        _pause();
    }

    /**
     * @dev Unpause fund operations
     */
    function unpause() external onlyManagerOrOperator {
        _unpause();
    }

    /**
     * @dev Fallback function to reject direct ETH transfers
     */
    receive() external payable {
        revert("Use invest() function to invest in the fund");
    }
}
```
