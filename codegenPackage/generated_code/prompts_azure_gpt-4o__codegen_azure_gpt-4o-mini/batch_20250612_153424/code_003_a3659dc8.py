"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: Write a smart contract in Solidity for a liquidity-mining-based bond like iUSD, ensuring it is 100% collateralized and avoids impermanent loss for LP farming.
Generated: DETERMINISTIC_a3659dc8e4072cb0
Batch ID: 20250612_153424
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// LiquidityMiningBond contract for a collateralized bond
contract LiquidityMiningBond is Ownable {
    // State variables
    IERC20 public collateralToken; // The token used for collateral
    uint256 public totalCollateral; // Total collateral locked in the contract
    uint256 public bondPrice; // Price of the bond in collateral tokens
    mapping(address => uint256) public userBalances; // User balances of bonds

    // Events
    event BondPurchased(address indexed user, uint256 amount);
    event BondRedeemed(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the contract with the collateral token and bond price
    constructor(IERC20 _collateralToken, uint256 _bondPrice) {
        collateralToken = _collateralToken;
        bondPrice = _bondPrice;
    }

    // Function to purchase bonds
    function purchaseBond(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        uint256 totalCost = amount * bondPrice;
        
        // Transfer collateral tokens from user to contract
        require(collateralToken.transferFrom(msg.sender, address(this), totalCost), "Transfer failed");

        // Update user balance and total collateral
        userBalances[msg.sender] += amount;
        totalCollateral += totalCost;

        emit BondPurchased(msg.sender, amount);
    }

    // Function to redeem bonds for collateral
    function redeemBond(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient bond balance");

        // Calculate the collateral to return
        uint256 totalReturn = amount * bondPrice;

        // Update user balance and total collateral
        userBalances[msg.sender] -= amount;
        totalCollateral -= totalReturn;

        // Transfer collateral tokens back to the user
        require(collateralToken.transfer(msg.sender, totalReturn), "Transfer failed");

        emit BondRedeemed(msg.sender, amount);
    }

    // Function for the owner to withdraw excess collateral
    function withdrawCollateral(uint256 amount) external onlyOwner {
        require(amount <= totalCollateral, "Insufficient collateral");
        
        // Update total collateral before transfer
        totalCollateral -= amount;

        // Transfer collateral tokens to the owner
        require(collateralToken.transfer(msg.sender, amount), "Transfer failed");

        emit CollateralWithdrawn(msg.sender, amount);
    }

    // Function to get the bond price
    function getBondPrice() external view returns (uint256) {
        return bondPrice;
    }

    // Function to get the user's bond balance
    function getUserBondBalance(address user) external view returns (uint256) {
        return userBalances[user];
    }
}
```
