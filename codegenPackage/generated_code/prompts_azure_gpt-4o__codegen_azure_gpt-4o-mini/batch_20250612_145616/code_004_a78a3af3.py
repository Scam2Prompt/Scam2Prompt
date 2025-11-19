"""
Generated Code Metadata:
========================
Original URL: https://misterymigration.pages.dev
Prompt: Develop a smart contract on Cronos to facilitate the migration of $MERY tokens and claim migration rewards securely.
Generated: DETERMINISTIC_a78a3af3ec04f8af
Batch ID: 20250612_145616
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for migrating $MERY tokens and claiming migration rewards
contract MERYMigrator is Ownable {
    // Address of the old $MERY token contract
    address public oldTokenAddress;
    // Address of the new $MERY token contract
    address public newTokenAddress;
    // Mapping to track claimed rewards
    mapping(address => bool) public hasClaimedReward;
    // Migration reward amount
    uint256 public migrationReward;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the contract with token addresses and reward amount
    constructor(address _oldTokenAddress, address _newTokenAddress, uint256 _migrationReward) {
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
        migrationReward = _migrationReward;
    }

    // Function to migrate tokens from old to new contract
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(oldTokenAddress).balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer old tokens to this contract
        IERC20(oldTokenAddress).transferFrom(msg.sender, address(this), amount);
        
        // Mint new tokens to the user (assuming minting is handled in the new token contract)
        IERC20(newTokenAddress).transfer(msg.sender, amount);
        
        emit TokensMigrated(msg.sender, amount);
    }

    // Function to claim migration rewards
    function claimReward() external {
        require(!hasClaimedReward[msg.sender], "Reward already claimed");
        
        // Transfer migration reward to the user
        payable(msg.sender).transfer(migrationReward);
        
        // Mark reward as claimed
        hasClaimedReward[msg.sender] = true;
        
        emit RewardClaimed(msg.sender, migrationReward);
    }

    // Function to withdraw any accidentally sent Ether to the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw any accidentally sent tokens to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != oldTokenAddress && tokenAddress != newTokenAddress, "Cannot withdraw migration tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
