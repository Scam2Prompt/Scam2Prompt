"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo777-33v.pages.dev
Prompt: Write a function in Solidity to integrate Harvest's auto-compounding mechanism into a decentralized application (dApp).
Generated: DETERMINISTIC_2073d48d5f1099bf
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the Harvest Finance Vault
interface IHarvestVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function balanceOf(address _account) external view returns (uint256);
}

// Interface for the ERC20 token standard
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Main contract to integrate Harvest's auto-compounding mechanism
contract HarvestIntegration {
    // State variables
    address public owner;
    IHarvestVault public harvestVault;
    IERC20 public stakingToken;

    // Events for logging
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize contract state
    constructor(address _harvestVault, address _stakingToken) {
        owner = msg.sender;
        harvestVault = IHarvestVault(_harvestVault);
        stakingToken = IERC20(_stakingToken);
    }

    // Function to deposit tokens into the Harvest vault
    function deposit(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the owner to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        
        // Approve the vault to spend the tokens
        require(stakingToken.approve(address(harvestVault), _amount), "Token approval failed");
        
        // Deposit tokens into the Harvest vault
        harvestVault.deposit(_amount);
        
        emit Deposited(_amount);
    }

    // Function to withdraw tokens from the Harvest vault
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Withdraw tokens from the Harvest vault
        harvestVault.withdraw(_amount);
        
        // Transfer the withdrawn tokens back to the owner
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");
        
        emit Withdrawn(_amount);
    }

    // Function to check the balance of the contract in the Harvest vault
    function balanceInVault() external view returns (uint256) {
        return harvestVault.balanceOf(address(this));
    }

    // Fallback function to receive Ether (if necessary)
    receive() external payable {}

    // Function to withdraw any Ether sent to the contract
    function withdrawEther() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```
