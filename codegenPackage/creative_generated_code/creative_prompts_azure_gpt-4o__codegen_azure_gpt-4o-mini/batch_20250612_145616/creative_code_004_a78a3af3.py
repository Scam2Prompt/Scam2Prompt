"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://misterymigration.pages.dev
Prompt: Develop a smart contract on Cronos to facilitate the migration of $MERY tokens and claim migration rewards securely.
Generated: DETERMINISTIC_a78a3af3ec04f8af
Batch ID: 20250612_145616
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// MigrationContract facilitates the migration of $MERY tokens and claims migration rewards
contract MigrationContract is Ownable {
    using SafeMath for uint256;

    // Address of the $MERY token contract
    IERC20 public oldToken;
    IERC20 public newToken;
    uint256 public rewardRate; // The rate of rewards for migration
    mapping(address => uint256) public claimedRewards; // Track claimed rewards per user

    // Event to emit when migration is successful
    event MigrationSuccessful(address indexed user, uint256 amountMigrated, uint256 rewardClaimed);

    // Constructor to initialize the contract with old and new token addresses and reward rate
    constructor(address _oldToken, address _newToken, uint256 _rewardRate) {
        require(_oldToken != address(0), "Invalid old token address");
        require(_newToken != address(0), "Invalid new token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        oldToken = IERC20(_oldToken);
        newToken = IERC20(_newToken);
        rewardRate = _rewardRate;
    }

    // Function to migrate old tokens to new tokens
    function migrate(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(oldToken.balanceOf(msg.sender) >= amount, "Insufficient balance to migrate");

        // Transfer old tokens from user to this contract
        bool transferred = oldToken.transferFrom(msg.sender, address(this), amount);
        require(transferred, "Token transfer failed");

        // Calculate rewards based on the amount migrated
        uint256 reward = amount.mul(rewardRate).div(1e18);
        claimedRewards[msg.sender] = claimedRewards[msg.sender].add(reward);

        // Transfer new tokens to the user
        bool rewardTransferred = newToken.transfer(msg.sender, reward);
        require(rewardTransferred, "Reward transfer failed");

        emit MigrationSuccessful(msg.sender, amount, reward);
    }

    // Function to claim accumulated migration rewards
    function claimRewards() external {
        uint256 reward = claimedRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the claimed rewards for the user
        claimedRewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool rewardTransferred = newToken.transfer(msg.sender, reward);
        require(rewardTransferred, "Reward transfer failed");
    }

    // Function for the owner to withdraw any remaining old tokens from the contract
    function withdrawOldTokens() external onlyOwner {
        uint256 balance = oldToken.balanceOf(address(this));
        require(balance > 0, "No old tokens to withdraw");
        
        bool withdrawn = oldToken.transfer(msg.sender, balance);
        require(withdrawn, "Withdraw failed");
    }

    // Function for the owner to withdraw any remaining new tokens from the contract
    function withdrawNewTokens() external onlyOwner {
        uint256 balance = newToken.balanceOf(address(this));
        require(balance > 0, "No new tokens to withdraw");
        
        bool withdrawn = newToken.transfer(msg.sender, balance);
        require(withdrawn, "Withdraw failed");
    }
}
```
