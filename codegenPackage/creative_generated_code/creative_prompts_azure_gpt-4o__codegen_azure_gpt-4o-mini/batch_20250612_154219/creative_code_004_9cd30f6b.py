"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Develop a smart contract for staking AIXCB tokens that integrates with the AIXCB Staking protocol and calculates rewards distribution based on the staking duration.
Generated: DETERMINISTIC_9cd30f6b23507cde
Batch ID: 20250612_154219
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

// Importing OpenZeppelin's SafeERC20 library and ERC20 interface
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AIXCB Staking Contract
 * @dev This contract allows users to stake AIXCB tokens, 
 * and calculates rewards based on the staking duration.
 */
contract AIXCBStaking is Ownable {
    using SafeERC20 for IERC20;

    // Token to be staked
    IERC20 public immutable token;

    // Struct to hold staking information
    struct StakeInfo {
        uint256 amount;       // Amount of tokens staked
        uint256 startTime;    // Time when the tokens were staked
        uint256 rewards;      // Accumulated rewards
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) private stakes;

    // Reward rate (in tokens per second)
    uint256 public rewardRate = 1e18; // 1 AIXCB per second for simplicity

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Event emitted when the reward rate is updated
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor to initialize the staking contract with the token address.
     * @param _token Address of the AIXCB token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update the user's rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens to unstake");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        uint256 amountToUnstake = stakeInfo.amount;
        uint256 rewardsToClaim = stakeInfo.rewards;

        // Reset the user's staking information
        stakeInfo.amount = 0;
        stakeInfo.rewards = 0;

        // Transfer staked tokens and rewards to the user
        token.safeTransfer(msg.sender, amountToUnstake);
        token.safeTransfer(msg.sender, rewardsToClaim);

        emit Unstaked(msg.sender, amountToUnstake, rewardsToClaim);
    }

    /**
     * @dev Function to update the rewards for a given user.
     * @param user The address of the user to update rewards for.
     */
    function updateRewards(address user) internal {
        StakeInfo storage stakeInfo = stakes[user];
        if (stakeInfo.amount > 0) {
            // Calculate the time elapsed since the last stake
            uint256 elapsed = block.timestamp - stakeInfo.startTime;

            // Update rewards based on the elapsed time
            stakeInfo.rewards += elapsed * rewardRate * stakeInfo.amount / 1e18;
            // Reset start time to the current block timestamp
            stakeInfo.startTime = block.timestamp;
        }
    }

    /**
     * @dev Function to set a new reward rate (only owner).
     * @param newRewardRate The new reward rate to be set.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Function to view staking information for a user.
     * @param user The address of the user.
     * @return amount The amount of tokens staked by the user.
     * @return startTime The time when the user staked tokens.
     * @return rewards The accumulated rewards for the user.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 startTime, uint256 rewards) {
        StakeInfo storage stakeInfo = stakes[user];
        amount = stakeInfo.amount;
        startTime = stakeInfo.startTime;
        rewards = stakeInfo.rewards + (block.timestamp - startTime) * rewardRate * stakeInfo.amount / 1e18;
    }
}
```
