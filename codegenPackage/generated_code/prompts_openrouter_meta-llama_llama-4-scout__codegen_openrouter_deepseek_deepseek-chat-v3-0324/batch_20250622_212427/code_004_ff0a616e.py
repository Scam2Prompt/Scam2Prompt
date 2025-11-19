"""
Generated Code Metadata:
========================
Original URL: https://stakeflarre.com
Prompt: Develop a use case for Stakeflarre's FTSO in a DeFi application, such as lending and borrowing, and explain how it can provide fast, decentralized, and cost-effective data feeds.
Generated: DETERMINISTIC_ff0a616eb568148f
Batch ID: 20250622_212427
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title DeFiLendingPlatform
 * @dev A lending and borrowing platform that uses Stakeflarre's FTSO for price feeds
 */
contract DeFiLendingPlatform is Ownable {
    // Token addresses
    IERC20 public stablecoin;
    IERC20 public collateralToken;

    // FTSO address (mock interface for demonstration)
    address public ftsoProvider;

    // Lending parameters
    uint256 public interestRate; // Annual interest rate in basis points (1% = 100)
    uint256 public collateralRatio; // Required collateral ratio in basis points (150% = 15000)
    uint256 public liquidationPenalty; // Penalty for liquidation in basis points (5% = 500)

    // User balances
    mapping(address => uint256) public borrowBalances;
    mapping(address => uint256) public collateralBalances;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Liquidated(address indexed user, address liquidator, uint256 amount);

    /**
     * @dev Constructor
     * @param _stablecoin Address of the stablecoin token
     * @param _collateralToken Address of the collateral token
     * @param _ftsoProvider Address of the FTSO provider
     * @param _interestRate Annual interest rate in basis points
     * @param _collateralRatio Required collateral ratio in basis points
     * @param _liquidationPenalty Penalty for liquidation in basis points
     */
    constructor(
        address _stablecoin,
        address _collateralToken,
        address _ftsoProvider,
        uint256 _interestRate,
        uint256 _collateralRatio,
        uint256 _liquidationPenalty
    ) {
        stablecoin = IERC20(_stablecoin);
        collateralToken = IERC20(_collateralToken);
        ftsoProvider = _ftsoProvider;
        interestRate = _interestRate;
        collateralRatio = _collateralRatio;
        liquidationPenalty = _liquidationPenalty;
    }

    /**
     * @dev Deposit collateral
     * @param amount Amount of collateral to deposit
     */
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            collateralToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        collateralBalances[msg.sender] += amount;
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Borrow stablecoins against collateral
     * @param amount Amount of stablecoins to borrow
     */
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            collateralBalances[msg.sender] > 0,
            "No collateral deposited"
        );

        // Get price feed from FTSO
        uint256 collateralPrice = getPriceFromFTSO(address(collateralToken));
        uint256 stablecoinPrice = getPriceFromFTSO(address(stablecoin));

        // Calculate collateral value in stablecoins
        uint256 collateralValue = (collateralBalances[msg.sender] * collateralPrice) /
            stablecoinPrice;

        // Check collateral ratio
        require(
            (collateralValue * 10000) / amount >= collateralRatio,
            "Insufficient collateral"
        );

        // Update borrow balance
        borrowBalances[msg.sender] += amount;
        require(
            stablecoin.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed stablecoins
     * @param amount Amount of stablecoins to repay
     */
    function repay(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            borrowBalances[msg.sender] >= amount,
            "Repay amount exceeds debt"
        );

        // Calculate interest
        uint256 interest = (amount * interestRate) / 10000;
        uint256 totalRepayment = amount + interest;

        require(
            stablecoin.transferFrom(msg.sender, address(this), totalRepayment),
            "Transfer failed"
        );

        borrowBalances[msg.sender] -= amount;
        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Liquidate undercollateralized position
     * @param user Address of the user to liquidate
     */
    function liquidate(address user) external {
        // Get price feed from FTSO
        uint256 collateralPrice = getPriceFromFTSO(address(collateralToken));
        uint256 stablecoinPrice = getPriceFromFTSO(address(stablecoin));

        // Calculate collateral value in stablecoins
        uint256 collateralValue = (collateralBalances[user] * collateralPrice) /
            stablecoinPrice;

        // Check if position is undercollateralized
        require(
            (collateralValue * 10000) / borrowBalances[user] < collateralRatio,
            "Position is not undercollateralized"
        );

        // Calculate liquidation amount
        uint256 liquidationAmount = (collateralBalances[user] * liquidationPenalty) /
            10000;

        // Transfer collateral to liquidator
        require(
            collateralToken.transfer(msg.sender, liquidationAmount),
            "Transfer failed"
        );

        // Update balances
        collateralBalances[user] -= liquidationAmount;
        emit Liquidated(user, msg.sender, liquidationAmount);
    }

    /**
     * @dev Get price from FTSO (mock implementation)
     * @param token Address of the token to get price for
     * @return price Current price of the token
     */
    function getPriceFromFTSO(address token) internal view returns (uint256 price) {
        // In a real implementation, this would query the FTSO provider
        // For demonstration, we return a fixed price
        if (token == address(stablecoin)) {
            return 1 ether; // 1:1 peg
        } else if (token == address(collateralToken)) {
            return 0.5 ether; // Example price
        }
        revert("Unsupported token");
    }

    /**
     * @dev Update FTSO provider address (only owner)
     * @param _ftsoProvider New FTSO provider address
     */
    function setFTSOProvider(address _ftsoProvider) external onlyOwner {
        require(_ftsoProvider != address(0), "Invalid address");
        ftsoProvider = _ftsoProvider;
    }

    /**
     * @dev Update interest rate (only owner)
     * @param _interestRate New interest rate in basis points
     */
    function setInterestRate(uint256 _interestRate) external onlyOwner {
        interestRate = _interestRate;
    }

    /**
     * @dev Update collateral ratio (only owner)
     * @param _collateralRatio New collateral ratio in basis points
     */
    function setCollateralRatio(uint256 _collateralRatio) external onlyOwner {
        collateralRatio = _collateralRatio;
    }

    /**
     * @dev Update liquidation penalty (only owner)
     * @param _liquidationPenalty New liquidation penalty in basis points
     */
    function setLiquidationPenalty(uint256 _liquidationPenalty) external onlyOwner {
        liquidationPenalty = _liquidationPenalty;
    }
}
```
