"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shib-army.pages.dev
Prompt: Develop a smart contract to facilitate the automatic distribution of rewards earned from staking SHIB tokens on ShibaSwap.
Generated: DETERMINISTIC_ddcc40ead2f56788
Batch ID: 20250612_151143
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ShibaSwapRewardDistributor
 * @dev A smart contract to facilitate automatic distribution of rewards earned from staking SHIB tokens.
 */
contract ShibaSwapRewardDistributor is Ownable {
    // Declare the SHIB token interface
    IERC20 public shibToken;

    // Mapping from user address to staked amount
    mapping(address => uint256) private stakedAmounts;

    // Total amount of staked SHIB tokens
    uint256 public totalStaked;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Reward rate in wei per token staked (you can adjust this value)
    uint256 public rewardRate = 1e16; // Example: 0.01 rewards per token per block

    /**
     * @dev Constructor to set the SHIB token address.
     * @param _shibToken The address of the SHIB token contract.
     */
    constructor(address _shibToken) {
        require(_shibToken != address(0), "Invalid SHIB token address");
        shibToken = IERC20(_shibToken);
    }

    /**
     * @dev Stake SHIB tokens to earn rewards.
     * @param amount The amount of SHIB tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(shibToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staked amount for the user
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked SHIB tokens and rewards.
     */
    function withdraw() external {
        uint256 stakedAmount = stakedAmounts[msg.sender];
        require(stakedAmount > 0, "No tokens to withdraw");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        require(shibToken.balanceOf(address(this)) >= stakedAmount + reward, "Insufficient balance for withdrawal");

        // Reset user staked amount
        stakedAmounts[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards
        shibToken.transfer(msg.sender, stakedAmount);
        shibToken.transfer(msg.sender, reward);

        emit TokensWithdrawn(msg.sender, stakedAmount);
        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards for a user based on staked amount.
     * @param user The address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 userStaked = stakedAmounts[user];
        return (userStaked * rewardRate); // Example calculation (can be modified)
    }

    /**
     * @dev Allow the owner to set a new reward rate.
     * @param newRewardRate The new reward rate in wei per token staked.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev View function to check the staked amount of a user.
     * @param user The address of the user.
     * @return The amount of SHIB tokens staked by the user.
     */
    function stakedAmountOf(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    /**
     * @dev View function to check total staked tokens.
     * @return The total number of staked SHIB tokens.
     */
    function totalStakedAmount() external view returns (uint256) {
        return totalStaked;
    }
}
```
