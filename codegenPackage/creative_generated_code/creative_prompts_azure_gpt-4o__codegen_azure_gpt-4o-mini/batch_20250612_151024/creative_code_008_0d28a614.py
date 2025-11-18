"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gen-da6.pages.dev
Prompt: Write a Solidity function to handle token rewards events for "$ENTS," ensuring proper distribution to eligible addresses.
Generated: DETERMINISTIC_0d28a614a8facaf3
Batch ID: 20250612_151024
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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenRewardDistributor {
    // Token to be used for rewards
    IERC20 public rewardToken;

    // Mapping to track eligible addresses and their reward amounts
    mapping(address => uint256) public rewards;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to set rewards for eligible addresses
    function setRewards(address[] calldata _recipients, uint256[] calldata _amounts) external {
        require(_recipients.length == _amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < _recipients.length; i++) {
            require(_recipients[i] != address(0), "Recipient cannot be zero address");
            require(_amounts[i] > 0, "Amount must be greater than zero");
            rewards[_recipients[i]] += _amounts[i];
        }
    }

    // Function to distribute rewards to eligible addresses
    function distributeRewards() external {
        for (uint256 i = 0; i < rewards.length; i++) {
            address recipient = rewards[i];
            uint256 amount = rewards[recipient];

            // Check if the contract has enough balance to transfer rewards
            require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance for rewards");

            // Reset rewards after distribution
            rewards[recipient] = 0;

            // Transfer the reward amount to the recipient
            bool success = rewardToken.transfer(recipient, amount);
            require(success, "Token transfer failed");

            emit RewardsDistributed(recipient, amount);
        }
    }
}
```
