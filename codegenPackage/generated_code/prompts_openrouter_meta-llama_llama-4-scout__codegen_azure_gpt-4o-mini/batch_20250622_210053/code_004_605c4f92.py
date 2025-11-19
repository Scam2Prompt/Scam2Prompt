"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Develop a basic example of how to use RedStone's oracle data feeds for lending markets, specifically for yield-bearing collateral, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_605c4f92829f70a0
Batch ID: 20250622_210053
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for RedStone's oracle data feed
interface IRedStoneOracle {
    function getLatestPrice(string memory asset) external view returns (uint256);
}

// Lending contract for yield-bearing collateral using RedStone's oracle
contract YieldLending is Ownable {
    // State variables
    IERC20 public collateralToken; // The ERC20 token used as collateral
    IRedStoneOracle public oracle; // The oracle for fetching asset prices
    uint256 public collateralizationRatio; // Minimum collateralization ratio (in basis points)

    // Event emitted when collateral is deposited
    event CollateralDeposited(address indexed user, uint256 amount);
    // Event emitted when collateral is withdrawn
    event CollateralWithdrawn(address indexed user, uint256 amount);

    // Mapping to track user collateral balances
    mapping(address => uint256) private collateralBalances;

    // Constructor to initialize the contract
    constructor(
        address _collateralToken,
        address _oracle,
        uint256 _collateralizationRatio
    ) {
        require(_collateralToken != address(0), "Invalid collateral token address");
        require(_oracle != address(0), "Invalid oracle address");
        require(_collateralizationRatio > 0, "Collateralization ratio must be greater than 0");

        collateralToken = IERC20(_collateralToken);
        oracle = IRedStoneOracle(_oracle);
        collateralizationRatio = _collateralizationRatio;
    }

    // Function to deposit collateral
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer collateral tokens from user to this contract
        collateralToken.transferFrom(msg.sender, address(this), amount);
        collateralBalances[msg.sender] += amount;

        emit CollateralDeposited(msg.sender, amount);
    }

    // Function to withdraw collateral
    function withdrawCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(collateralBalances[msg.sender] >= amount, "Insufficient collateral balance");

        // Check collateralization ratio before allowing withdrawal
        uint256 currentPrice = oracle.getLatestPrice("collateralTokenSymbol"); // Replace with actual symbol
        uint256 requiredCollateral = (amount * currentPrice * collateralizationRatio) / 10000; // Basis points

        require(collateralBalances[msg.sender] - amount >= requiredCollateral, "Withdrawal would violate collateralization ratio");

        // Update balance and transfer tokens back to user
        collateralBalances[msg.sender] -= amount;
        collateralToken.transfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    // Function to get the collateral balance of a user
    function getCollateralBalance(address user) external view returns (uint256) {
        return collateralBalances[user];
    }
}
```
