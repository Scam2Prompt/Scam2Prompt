"""
Generated Code Metadata:
========================
Original URL: https://ondofoundkation.com
Prompt: Design a smart contract for a DeFi protocol that utilizes Ondo's tokenized RWAs as collateral, written in Solidity.
Generated: DETERMINISTIC_150aec67576e014c
Batch ID: 20250622_212813
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a DeFi protocol utilizing Ondo's tokenized RWAs as collateral
contract DeFiProtocol is Ownable {
    // Struct to hold user collateral information
    struct Collateral {
        uint256 amount; // Amount of collateral deposited
        bool isActive;   // Status of the collateral
    }

    // Mapping to track user collateral
    mapping(address => Collateral) public collaterals;

    // Event emitted when collateral is deposited
    event CollateralDeposited(address indexed user, uint256 amount);

    // Event emitted when collateral is withdrawn
    event CollateralWithdrawn(address indexed user, uint256 amount);

    // The address of the Ondo token contract
    IERC20 public ondoToken;

    // Constructor to set the Ondo token address
    constructor(address _ondoTokenAddress) {
        require(_ondoTokenAddress != address(0), "Invalid token address");
        ondoToken = IERC20(_ondoTokenAddress);
    }

    // Function to deposit collateral
    function depositCollateral(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer the specified amount of Ondo tokens from the user to this contract
        require(ondoToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the user's collateral information
        collaterals[msg.sender].amount += _amount;
        collaterals[msg.sender].isActive = true;

        // Emit the collateral deposited event
        emit CollateralDeposited(msg.sender, _amount);
    }

    // Function to withdraw collateral
    function withdrawCollateral(uint256 _amount) external {
        Collateral storage userCollateral = collaterals[msg.sender];

        require(userCollateral.isActive, "No active collateral");
        require(userCollateral.amount >= _amount, "Insufficient collateral");

        // Update the user's collateral amount
        userCollateral.amount -= _amount;

        // If the user's collateral amount is zero, deactivate it
        if (userCollateral.amount == 0) {
            userCollateral.isActive = false;
        }

        // Transfer the specified amount of Ondo tokens back to the user
        require(ondoToken.transfer(msg.sender, _amount), "Transfer failed");

        // Emit the collateral withdrawn event
        emit CollateralWithdrawn(msg.sender, _amount);
    }

    // Function to check the collateral balance of a user
    function getCollateralBalance(address _user) external view returns (uint256) {
        return collaterals[_user].amount;
    }

    // Function to check if a user's collateral is active
    function isCollateralActive(address _user) external view returns (bool) {
        return collaterals[_user].isActive;
    }
}
```
