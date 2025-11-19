"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Develop a smart contract in Solidity for a multi-token, multi-chain meme coin staking system similar to the MemeVault protocol.
Generated: DETERMINISTIC_1418acbbc1b50eb5
Batch ID: 20250622_211032
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title MemeStakingContract
 * @author [Your Name]
 * @notice A multi-token, multi-chain meme coin staking system.
 */
contract MemeStakingContract is Ownable {
    using SafeMath for uint256;
    using Address for address;

    // Mapping of token addresses to their respective staking info
    mapping(address => StakingInfo) public stakingInfo;

    // Mapping of user addresses to their staking balances
    mapping(address => mapping(address => uint256)) public userStakingBalances;

    // Mapping of user addresses to their pending rewards
    mapping(address => mapping(address => uint256)) public pendingRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, address indexed token, uint256 amount);

    // Struct to hold staking information for a token
    struct StakingInfo {
        uint256 totalStaked;
        uint256 rewardPerToken;
        uint256 lastRewardUpdate;
    }

    /**
     * @notice Initializes the contract.
     */
    constructor() {}

    /**
     * @notice Adds a new token to the staking system.
     * @param token The address of the token to add.
     * @param rewardPerToken The initial reward per token.
     */
    function addToken(address token, uint256 rewardPerToken) public onlyOwner {
        require(token.isContract(), "Token address must be a contract");
        require(stakingInfo[token].totalStaked == 0, "Token already added");

        stakingInfo[token] = StakingInfo({
            totalStaked: 0,
            rewardPerToken: rewardPerToken,
            lastRewardUpdate: block.timestamp
        });
    }

    /**
     * @notice Removes a token from the staking system.
     * @param token The address of the token to remove.
     */
    function removeToken(address token) public onlyOwner {
        require(stakingInfo[token].totalStaked == 0, "Cannot remove token with staked balance");

        delete stakingInfo[token];
    }

    /**
     * @notice Updates the reward per token for a given token.
     * @param token The address of the token to update.
     * @param newRewardPerToken The new reward per token.
     */
    function updateRewardPerToken(address token, uint256 newRewardPerToken) public onlyOwner {
        require(stakingInfo[token].totalStaked > 0, "Token must have staked balance");

        stakingInfo[token].rewardPerToken = newRewardPerToken;
        stakingInfo[token].lastRewardUpdate = block.timestamp;
    }

    /**
     * @notice Stakes tokens for a user.
     * @param token The address of the token to stake.
     * @param amount The amount of tokens to stake.
     */
    function stake(address token, uint256 amount) public {
        require(stakingInfo[token].totalStaked > 0, "Token not added to staking system");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");

        IERC20(token).transferFrom(msg.sender, address(this), amount);

        stakingInfo[token].totalStaked = stakingInfo[token].totalStaked.add(amount);
        userStakingBalances[msg.sender][token] = userStakingBalances[msg.sender][token].add(amount);

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @notice Unstakes tokens for a user.
     * @param token The address of the token to unstake.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(address token, uint256 amount) public {
        require(userStakingBalances[msg.sender][token] >= amount, "Insufficient staked balance");

        stakingInfo[token].totalStaked = stakingInfo[token].totalStaked.sub(amount);
        userStakingBalances[msg.sender][token] = userStakingBalances[msg.sender][token].sub(amount);

        IERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @notice Claims rewards for a user.
     * @param token The address of the token to claim rewards for.
     */
    function claimRewards(address token) public {
        uint256 reward = calculateReward(msg.sender, token);

        pendingRewards[msg.sender][token] = 0;
        IERC20(token).transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, token, reward);
    }

    /**
     * @notice Calculates the reward for a user.
     * @param user The address of the user.
     * @param token The address of the token.
     * @return The reward amount.
     */
    function calculateReward(address user, address token) internal view returns (uint256) {
        uint256 stakedBalance = userStakingBalances[user][token];
        uint256 rewardPerToken = stakingInfo[token].rewardPerToken;
        uint256 lastRewardUpdate = stakingInfo[token].lastRewardUpdate;

        uint256 reward = stakedBalance.mul(rewardPerToken).div(1e18);
        reward = reward.add(pendingRewards[user][token]);

        return reward;
    }

    /**
     * @notice Updates the pending rewards for a user.
     * @param user The address of the user.
     * @param token The address of the token.
     */
    function updatePendingRewards(address user, address token) internal {
        uint256 stakedBalance = userStakingBalances[user][token];
        uint256 rewardPerToken = stakingInfo[token].rewardPerToken;
        uint256 lastRewardUpdate = stakingInfo[token].lastRewardUpdate;

        uint256 pendingReward = stakedBalance.mul(rewardPerToken.sub(stakingInfo[token].rewardPerToken)).div(1e18);
        pendingRewards[user][token] = pendingReward;
    }

    /**
     * @notice Updates the staking info and pending rewards for a token.
     * @param token The address of the token to update.
     */
    function updateStakingInfo(address token) public {
        stakingInfo[token].lastRewardUpdate = block.timestamp;
    }
}
```
