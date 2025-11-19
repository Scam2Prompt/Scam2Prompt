"""
Generated Code Metadata:
========================
Original URL: https://demo777-33v.pages.dev
Prompt: Write a function in Solidity to integrate Harvest's auto-compounding mechanism into a decentralized application (dApp).
Generated: DETERMINISTIC_2073d48d5f1099bf
Batch ID: 20250612_152235
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

// Importing the interface for the Harvest Finance vault
interface IHarvestVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function getPricePerFullShare() external view returns (uint256);
}

contract HarvestAutoCompound {
    // State variables
    IHarvestVault public harvestVault; // The Harvest vault to interact with
    address public owner; // Owner of the contract

    // Events
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the Harvest vault address and the owner
    constructor(address _vaultAddress) {
        harvestVault = IHarvestVault(_vaultAddress);
        owner = msg.sender;
    }

    // Function to deposit funds into the Harvest vault
    function deposit(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens to this contract
        // Assuming the token is ERC20 and has a transferFrom function
        // Replace `IERC20` with the actual token interface
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);
        
        // Approve the vault to spend the tokens
        IERC20(tokenAddress).approve(address(harvestVault), _amount);
        
        // Deposit into the Harvest vault
        harvestVault.deposit(_amount);
        
        emit Deposited(_amount);
    }

    // Function to withdraw funds from the Harvest vault
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        
        // Withdraw from the Harvest vault
        harvestVault.withdraw(_amount);
        
        // Transfer the withdrawn tokens back to the owner
        // Assuming the token is ERC20 and has a transfer function
        IERC20(tokenAddress).transfer(msg.sender, _amount);
        
        emit Withdrawn(_amount);
    }

    // Function to get the current price per full share of the vault
    function getPricePerFullShare() external view returns (uint256) {
        return harvestVault.getPricePerFullShare();
    }

    // Function to change the Harvest vault address (if needed)
    function setVaultAddress(address _vaultAddress) external onlyOwner {
        harvestVault = IHarvestVault(_vaultAddress);
    }
}
```
