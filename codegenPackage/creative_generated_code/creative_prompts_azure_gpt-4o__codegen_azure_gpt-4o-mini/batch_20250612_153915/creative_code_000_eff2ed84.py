"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.pages.dev
Prompt: Write a smart contract in Solidity that facilitates swapping tokens and distributing rewards, similar to the functionality described on the Swapbox webpage for TONCOIN rewards.
Generated: DETERMINISTIC_eff2ed841cb7adc0
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

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for Token Swap and Reward Distribution
contract TokenSwap is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public tokenA; // Token A to be swapped
    IERC20 public tokenB; // Token B to be received after swap
    address public rewardPool; // Address that holds the reward tokens
    uint256 public rewardRate; // Reward rate for token holders

    // Events for logging swaps and rewards
    event TokensSwapped(address indexed user, uint256 amountA, uint256 amountB);
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to check the swap amount validity
    modifier validSwapAmount(uint256 amountA) {
        require(amountA > 0, "Swap amount must be greater than 0");
        _;
    }

    // Constructor to initialize the contract with token addresses and reward parameters
    constructor(
        address _tokenA,
        address _tokenB,
        address _rewardPool,
        uint256 _rewardRate
    ) {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        rewardPool = _rewardPool;
        rewardRate = _rewardRate;
    }

    // Function to swap Token A for Token B
    function swapTokens(uint256 amountA) external validSwapAmount(amountA) {
        // Transfer Token A from user to the contract
        require(tokenA.transferFrom(msg.sender, address(this), amountA), "Transfer of Token A failed");

        // Calculate the amount of Token B to send
        uint256 amountB = calculateSwapAmount(amountA);

        // Transfer Token B from the contract to user
        require(tokenB.transfer(msg.sender, amountB), "Transfer of Token B failed");

        // Emit the swap event
        emit TokensSwapped(msg.sender, amountA, amountB);

        // Distribute rewards to the user
        distributeRewards(msg.sender);
    }

    // Function to calculate the amount of Token B to be received
    function calculateSwapAmount(uint256 amountA) internal view returns (uint256) {
        // Implement the logic for calculating Token B amount based on the swap rate
        // Placeholder logic: 1:1 swap rate for demonstration purposes
        return amountA; // Replace with actual swap logic
    }

    // Function to distribute rewards to the user
    function distributeRewards(address user) internal {
        uint256 rewardAmount = calculateReward(user);
        require(rewardAmount > 0, "No rewards to distribute");

        // Transfer reward tokens from the reward pool to the user
        require(IERC20(rewardPool).transfer(user, rewardAmount), "Transfer of rewards failed");

        // Emit the rewards distributed event
        emit RewardsDistributed(user, rewardAmount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        // Placeholder logic for reward calculation
        // Replace with actual logic based on user holdings or activity
        return rewardRate; // Replace with actual reward calculation
    }

    // Function to update the reward rate by the contract owner
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens from the contract (for owner only)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
