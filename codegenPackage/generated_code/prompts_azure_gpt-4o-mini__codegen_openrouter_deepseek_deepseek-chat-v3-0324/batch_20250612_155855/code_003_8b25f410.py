"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity contract that incorporates the "B2B Booster" strategy for investing in real-world assets while ensuring token buyback and burn functionality.
Generated: DETERMINISTIC_8b25f41011fca767
Batch ID: 20250612_155855
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract B2BBooster is Ownable, ReentrancyGuard {
    // Token contract
    IERC20 public token;

    // Real world asset investment details
    struct Investment {
        address assetManager;
        uint256 amountInvested;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping of investment IDs to Investment struct
    mapping(uint256 => Investment) public investments;

    // Total investments count
    uint256 public investmentCount;

    // Total tokens burned
    uint256 public totalBurned;

    // Buyback and burn parameters
    uint256 public buybackPercentage; // Percentage of profits for buyback (1-100)
    uint256 public burnPercentage;    // Percentage of bought back tokens to burn (1-100)

    // Events
    event InvestmentMade(
        uint256 indexed investmentId,
        address indexed assetManager,
        uint256 amount
    );
    event ProfitRealized(
        uint256 indexed investmentId,
        uint256 profitAmount
    );
    event BuybackAndBurn(
        uint256 amountBought,
        uint256 amountBurned
    );
    event ParametersUpdated(
        uint256 buybackPercentage,
        uint256 burnPercentage
    );

    constructor(
        address _tokenAddress,
        uint256 _buybackPercentage,
        uint256 _burnPercentage
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_buybackPercentage <= 100, "Buyback percentage must be <= 100");
        require(_burnPercentage <= 100, "Burn percentage must be <= 100");

        token = IERC20(_tokenAddress);
        buybackPercentage = _buybackPercentage;
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Invest in a real world asset
     * @param _assetManager Address managing the asset
     * @param _amount Amount to invest
     */
    function invest(address _assetManager, uint256 _amount) external onlyOwner nonReentrant {
        require(_assetManager != address(0), "Invalid asset manager");
        require(_amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        investmentCount++;
        investments[investmentCount] = Investment({
            assetManager: _assetManager,
            amountInvested: _amount,
            timestamp: block.timestamp,
            isActive: true
        });

        emit InvestmentMade(investmentCount, _assetManager, _amount);
    }

    /**
     * @dev Realize profits from an investment
     * @param _investmentId ID of the investment
     * @param _profitAmount Profit amount realized
     */
    function realizeProfit(uint256 _investmentId, uint256 _profitAmount) external nonReentrant {
        require(_investmentId > 0 && _investmentId <= investmentCount, "Invalid investment ID");
        Investment storage investment = investments[_investmentId];
        require(investment.isActive, "Investment is not active");
        require(msg.sender == investment.assetManager, "Only asset manager can realize profits");
        require(_profitAmount > 0, "Profit amount must be greater than 0");

        // Transfer profit to contract
        require(token.transferFrom(msg.sender, address(this), _profitAmount), "Transfer failed");

        // Calculate buyback amount
        uint256 buybackAmount = (_profitAmount * buybackPercentage) / 100;
        if (buybackAmount > 0) {
            _buybackAndBurn(buybackAmount);
        }

        emit ProfitRealized(_investmentId, _profitAmount);
    }

    /**
     * @dev Internal function to handle buyback and burn
     * @param _amount Amount to use for buyback
     */
    function _buybackAndBurn(uint256 _amount) internal {
        require(_amount <= token.balanceOf(address(this)), "Insufficient balance for buyback");

        // Calculate burn amount
        uint256 burnAmount = (_amount * burnPercentage) / 100;
        if (burnAmount > 0) {
            // Burn tokens by sending to dead address
            require(token.transfer(address(0xdead), burnAmount), "Burn transfer failed");
            totalBurned += burnAmount;
        }

        // Remaining amount stays in contract for future operations
        emit BuybackAndBurn(_amount, burnAmount);
    }

    /**
     * @dev Update buyback and burn parameters
     * @param _buybackPercentage New buyback percentage (1-100)
     * @param _burnPercentage New burn percentage (1-100)
     */
    function updateParameters(uint256 _buybackPercentage, uint256 _burnPercentage) external onlyOwner {
        require(_buybackPercentage <= 100, "Buyback percentage must be <= 100");
        require(_burnPercentage <= 100, "Burn percentage must be <= 100");

        buybackPercentage = _buybackPercentage;
        burnPercentage = _burnPercentage;

        emit ParametersUpdated(_buybackPercentage, _burnPercentage);
    }

    /**
     * @dev Close an investment
     * @param _investmentId ID of the investment to close
     */
    function closeInvestment(uint256 _investmentId) external onlyOwner {
        require(_investmentId > 0 && _investmentId <= investmentCount, "Invalid investment ID");
        require(investments[_investmentId].isActive, "Investment already closed");

        investments[_investmentId].isActive = false;
    }

    /**
     * @dev Withdraw tokens from contract (emergency use only)
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(token.transfer(owner(), _amount), "Transfer failed");
    }
}
```
