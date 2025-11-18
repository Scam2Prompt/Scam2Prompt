"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.pages.dev
Prompt: Create a smart contract that implements the "maximum reward for swap" logic, ensuring users can claim up to 17,500 TONCOIN for swapping boxes, as outlined on the Swapbox page.
Generated: DETERMINISTIC_223be5581ffa0461
Batch ID: 20250612_153915
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

contract SwapBox is Ownable {
    // Maximum reward for swaps
    uint256 public constant MAX_REWARD = 17500 * 10**18; // Assuming TONCOIN has 18 decimals

    // Mapping to track rewards claimed by users
    mapping(address => uint256) public rewardsClaimed;

    // Event to log rewards claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // ERC20 token for TONCOIN
    IERC20 public toncoinToken;

    // Constructor to initialize the contract with the TONCOIN token address
    constructor(address _toncoinToken) {
        require(_toncoinToken != address(0), "Invalid token address");
        toncoinToken = IERC20(_toncoinToken);
    }

    // Function to swap boxes and claim rewards
    function swapAndClaim(uint256 boxCount) external {
        require(boxCount > 0, "Box count must be greater than zero");

        // Calculate potential reward based on box count
        uint256 reward = calculateReward(boxCount);

        // Check if the user has already claimed rewards
        require(rewardsClaimed[msg.sender] + reward <= MAX_REWARD, "Reward limit exceeded");

        // Update the claimed rewards for the user
        rewardsClaimed[msg.sender] += reward;

        // Transfer the reward to the user
        require(toncoinToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Calculate the reward based on the number of boxes swapped
    function calculateReward(uint256 boxCount) internal pure returns (uint256) {
        // Define a simple reward logic (e.g., 100 TONCOIN per box)
        return boxCount * 100 * 10**18; // Assuming TONCOIN has 18 decimals
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(toncoinToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of TONCOIN to the owner
        require(toncoinToken.transfer(owner(), amount), "Withdraw failed");
    }

    // Function to check the reward balance of a user
    function getRewardBalance(address user) external view returns (uint256) {
        return MAX_REWARD - rewardsClaimed[user];
    }
}
```
