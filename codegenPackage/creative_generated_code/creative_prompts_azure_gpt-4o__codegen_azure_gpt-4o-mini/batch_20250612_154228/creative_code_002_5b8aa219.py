"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blums-xray.xyz
Prompt: Generate Solidity code for a smart contract that handles reward distribution based on a spin-to-win mechanism, ensuring wallet integration for claiming prizes.
Generated: DETERMINISTIC_5b8aa219f4f12896
Batch ID: 20250612_154228
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// SpinToWin contract allows users to spin for rewards
contract SpinToWin is Ownable {
    using SafeMath for uint256;

    // Event emitted when a user wins
    event SpinResult(address indexed player, uint256 rewardAmount);
    
    // Mapping to track claimed rewards
    mapping(address => uint256) public claimedRewards;

    // Total rewards pool
    uint256 public rewardsPool;

    // Minimum and maximum reward values
    uint256 public minReward;
    uint256 public maxReward;

    // Constructor to initialize the contract
    constructor(uint256 _minReward, uint256 _maxReward, uint256 _rewardsPool) {
        require(_minReward > 0 && _maxReward > _minReward, "Invalid reward limits");
        require(_rewardsPool > 0, "Rewards pool must be greater than zero");

        minReward = _minReward;
        maxReward = _maxReward;
        rewardsPool = _rewardsPool;
    }

    // Function to spin for rewards
    function spin() external {
        require(rewardsPool > 0, "No rewards available");

        // Generate a random reward amount
        uint256 rewardAmount = _getRandomReward();
        require(rewardAmount <= rewardsPool, "Insufficient rewards in pool");

        // Update rewards pool
        rewardsPool = rewardsPool.sub(rewardAmount);

        // Update claimed rewards
        claimedRewards[msg.sender] = claimedRewards[msg.sender].add(rewardAmount);

        // Emit the spin result event
        emit SpinResult(msg.sender, rewardAmount);
    }

    // Internal function to get a random reward within specified limits
    function _getRandomReward() internal view returns (uint256) {
        // Generate a random number
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % (maxReward - minReward + 1);
        return random.add(minReward);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = claimedRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset claimed rewards for the user
        claimedRewards[msg.sender] = 0;

        // Transfer the reward to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        // Emit the event after successful claim
        emit SpinResult(msg.sender, rewardAmount);
    }

    // Function to withdraw remaining rewards by the owner
    function withdrawRemainingRewards() external onlyOwner {
        require(rewardsPool > 0, "No rewards left to withdraw");

        uint256 amountToWithdraw = rewardsPool;
        rewardsPool = 0;

        // Transfer the remaining rewards to the owner
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");
    }

    // Function to receive Ether. msg.value is added to rewardsPool
    receive() external payable {
        rewardsPool = rewardsPool.add(msg.value);
    }
}
```
