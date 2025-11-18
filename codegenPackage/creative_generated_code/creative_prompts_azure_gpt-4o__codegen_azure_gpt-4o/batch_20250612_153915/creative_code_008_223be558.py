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

/**
 * @title SwapBoxReward
 * @dev Smart contract to handle the reward logic for swapping boxes
 *      Users can claim rewards up to a maximum of 17,500 TONCOIN per swap.
 */
contract SwapBoxReward {
    // State variables
    uint256 public constant MAX_REWARD = 17500 * (10 ** 18); // Maximum reward in TONCOIN (adjusted for decimals)
    address public owner; // Owner of the contract
    mapping(address => uint256) public rewardsClaimed; // Tracks rewards claimed by each user

    // Events
    event RewardClaimed(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "SwapBoxReward: Caller is not the owner");
        _;
    }

    // Constructor to initialize the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to claim rewards for swapping boxes.
     * @param user The user's address claiming the reward.
     * @param amount The amount of TONCOIN the user is claiming.
     */
    function claimReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "SwapBoxReward: Invalid user address");
        require(amount > 0, "SwapBoxReward: Amount must be greater than zero");
        require(amount <= MAX_REWARD, "SwapBoxReward: Amount exceeds maximum reward");
        require(rewardsClaimed[user] + amount <= MAX_REWARD, "SwapBoxReward: User cannot claim more than maximum reward");

        // Update the rewards claimed by the user
        rewardsClaimed[user] += amount;

        emit RewardClaimed(user, amount);
    }

    /**
     * @dev Function to reset a user's claimed rewards (only callable by the owner).
     * @param user The user's address whose rewards are being reset.
     */
    function resetReward(address user) external onlyOwner {
        require(user != address(0), "SwapBoxReward: Invalid user address");

        rewardsClaimed[user] = 0;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "SwapBoxReward: New owner is the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to reject incoming ether.
     */
    receive() external payable {
        revert("SwapBoxReward: Contract does not accept Ether");
    }
}
```
