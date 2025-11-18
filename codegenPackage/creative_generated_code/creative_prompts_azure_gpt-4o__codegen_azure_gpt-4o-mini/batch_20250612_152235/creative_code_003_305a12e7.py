"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-dogeverse-claim.pages.dev
Prompt: Provide an example of a smart contract in Solidity that distributes 6088 $DOGEVERSE rewards per Ethereum block, as described in the Dogeverse staking system.
Generated: DETERMINISTIC_305a12e71eec7231
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DogeverseStaking is Ownable {
    // The token that will be distributed as rewards
    IERC20 public dogeverseToken;

    // Reward amount per block
    uint256 public constant REWARD_PER_BLOCK = 6088 * (10 ** 18); // Adjusting for decimals

    // Track last rewarded block for each staker
    mapping(address => uint256) public lastRewardBlock;

    // Track total rewards earned by each staker
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Constructor to set the token address
    constructor(address _dogeverseToken) {
        require(_dogeverseToken != address(0), "Invalid token address");
        dogeverseToken = IERC20(_dogeverseToken);
    }

    // Function to stake tokens (for demonstration purposes, not implemented)
    function stake(uint256 amount) external {
        // Implementation of staking logic should be done here
        // For simplicity, we assume the staking logic is handled elsewhere
    }

    // Function to distribute rewards to the caller based on the last block claimed
    function claimRewards() external {
        uint256 currentBlock = block.number;
        uint256 blocksSinceLastClaim = currentBlock - lastRewardBlock[msg.sender];

        require(blocksSinceLastClaim > 0, "No rewards to claim");

        // Calculate the total rewards for the staker
        uint256 totalRewards = blocksSinceLastClaim * REWARD_PER_BLOCK;

        // Update last reward block for the staker
        lastRewardBlock[msg.sender] = currentBlock;

        // Update the staker's total rewards
        rewards[msg.sender] += totalRewards;

        // Transfer the rewards to the staker
        require(dogeverseToken.balanceOf(address(this)) >= totalRewards, "Insufficient contract balance");
        dogeverseToken.transfer(msg.sender, totalRewards);

        emit RewardsClaimed(msg.sender, totalRewards);
    }

    // Function to withdraw funds in case of emergency (only owner can call)
    function withdrawToken(address _token, uint256 amount) external onlyOwner {
        require(_token != address(dogeverseToken), "Cannot withdraw reward token");
        IERC20(_token).transfer(owner(), amount);
    }

    // Function to withdraw remaining DOGEVERSE tokens from the contract (only owner can call)
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = dogeverseToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");
        dogeverseToken.transfer(owner(), remainingBalance);
    }
}
```
