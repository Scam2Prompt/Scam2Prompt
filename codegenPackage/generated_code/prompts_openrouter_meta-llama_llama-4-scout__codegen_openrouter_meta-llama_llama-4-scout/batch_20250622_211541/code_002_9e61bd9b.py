"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Develop a smart contract using Solidity that enables multi-token, multi-chain meme coin staking, similar to the MemeVault protocol.
Generated: DETERMINISTIC_9e61bd9b6c65c819
Batch ID: 20250622_211541
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeStakingContract
 * @author [Your Name]
 * @notice A smart contract for multi-token, multi-chain meme coin staking.
 */
contract MemeStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective staking info
    mapping(address => StakingInfo) public stakingInfo;

    // Mapping of user addresses to their staking balances
    mapping(address => mapping(address => uint256)) public userStakingBalances;

    // Mapping of user addresses to their staking rewards
    mapping(address => mapping(address => uint256)) public userStakingRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, address indexed token, uint256 amount);

    /**
     * @dev Struct to store staking information for a token
     */
    struct StakingInfo {
        uint256 totalStaked;
        uint256 rewardsPerShare;
        uint256 lastRewardUpdate;
        uint256 rewardPerBlock;
        uint256 blocksPerReward;
    }

    /**
     * @dev Function to add a new token for staking
     * @param token The address of the token to add
     * @param rewardPerBlock The reward per block for the token
     * @param blocksPerReward The number of blocks per reward for the token
     */
    function addToken(address token, uint256 rewardPerBlock, uint256 blocksPerReward) public onlyOwner {
        require(IERC20(token).totalSupply() > 0, "Token does not exist");
        require(stakingInfo[token].totalStaked == 0, "Token already added");

        stakingInfo[token] = StakingInfo({
            totalStaked: 0,
            rewardsPerShare: 0,
            lastRewardUpdate: block.number,
            rewardPerBlock: rewardPerBlock,
            blocksPerReward: blocksPerReward
        });
    }

    /**
     * @dev Function to stake tokens
     * @param token The address of the token to stake
     * @param amount The amount of tokens to stake
     */
    function stake(address token, uint256 amount) public {
        require(stakingInfo[token].totalStaked > 0, "Token not added for staking");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(amount > 0, "Stake amount must be greater than 0");

        IERC20(token).transferFrom(msg.sender, address(this), amount);
        stakingInfo[token].totalStaked = stakingInfo[token].totalStaked.add(amount);
        userStakingBalances[msg.sender][token] = userStakingBalances[msg.sender][token].add(amount);

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Function to unstake tokens
     * @param token The address of the token to unstake
     * @param amount The amount of tokens to unstake
     */
    function unstake(address token, uint256 amount) public {
        require(userStakingBalances[msg.sender][token] >= amount, "Insufficient staked balance");
        require(amount > 0, "Unstake amount must be greater than 0");

        stakingInfo[token].totalStaked = stakingInfo[token].totalStaked.sub(amount);
        userStakingBalances[msg.sender][token] = userStakingBalances[msg.sender][token].sub(amount);
        IERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @dev Function to claim rewards
     * @param token The address of the token to claim rewards for
     */
    function claimRewards(address token) public {
        uint256 rewards = calculateRewards(msg.sender, token);
        require(rewards > 0, "No rewards to claim");

        userStakingRewards[msg.sender][token] = 0;
        IERC20(token).transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, token, rewards);
    }

    /**
     * @dev Function to calculate rewards for a user
     * @param user The address of the user
     * @param token The address of the token
     * @return The rewards for the user
     */
    function calculateRewards(address user, address token) internal view returns (uint256) {
        uint256 stakedBalance = userStakingBalances[user][token];
        uint256 rewards = stakedBalance.mul(stakingInfo[token].rewardsPerShare).div(1e18);
        return rewards.add(userStakingRewards[user][token]);
    }

    /**
     * @dev Function to update rewards for all users
     */
    function updateRewards() public {
        for (address token in stakingInfo) {
            StakingInfo storage info = stakingInfo[token];
            uint256 blocksElapsed = block.number.sub(info.lastRewardUpdate);
            uint256 rewards = blocksElapsed.mul(info.rewardPerBlock).mul(info.blocksPerReward);

            info.rewardsPerShare = info.rewardsPerShare.add(rewards.div(info.totalStaked));
            info.lastRewardUpdate = block.number;
        }
    }

    /**
     * @dev Fallback function to receive tokens
     */
    fallback() external payable {}

    /**
     * @dev Receive function to receive tokens
     */
    receive() external payable {}
}
```
