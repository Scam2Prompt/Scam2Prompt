"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: Generate Solidity code for a staking smart contract compatible with the PEPE Ascension Layer 2 blockchain that incorporates double rewards programs as described in the presale phase.
Generated: DETERMINISTIC_b650abedce3a02f2
Batch ID: 20250612_154010
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PEPE Ascension Staking Contract
 * @author [Your Name]
 * @notice This contract is for staking and earning rewards on the PEPE Ascension Layer 2 blockchain.
 * @dev This contract uses OpenZeppelin's SafeMath and ReentrancyGuard to ensure security.
 */
contract PepeAscensionStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of reward token information
    mapping(address => RewardTokenInfo) public rewardTokenInfo;

    // Staking token address
    address public stakingToken;

    // Reward token addresses
    address[] public rewardTokens;

    // Total staked amount
    uint256 public totalStaked;

    // Staking start time
    uint256 public stakingStartTime;

    // Staking end time
    uint256 public stakingEndTime;

    // Double rewards program start and end times
    uint256 public doubleRewardsStartTime;
    uint256 public doubleRewardsEndTime;

    // Reward rates for each reward token
    mapping(address => uint256) public rewardRates;

    // Reward multipliers for double rewards program
    uint256 public doubleRewardsMultiplier;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, address indexed rewardToken, uint256 amount);

    // Struct to store user staking information
    struct UserInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        mapping(address => uint256) rewardTokenBalances;
    }

    // Struct to store reward token information
    struct RewardTokenInfo {
        uint256 rewardPerBlock;
        uint256 lastRewardBlock;
    }

    /**
     * @notice Constructor for the PepeAscensionStaking contract.
     * @param _stakingToken Address of the staking token.
     * @param _rewardTokens Addresses of the reward tokens.
     * @param _stakingStartTime Start time of the staking period.
     * @param _stakingEndTime End time of the staking period.
     * @param _doubleRewardsStartTime Start time of the double rewards program.
     * @param _doubleRewardsEndTime End time of the double rewards program.
     * @param _rewardRates Reward rates for each reward token.
     */
    constructor(
        address _stakingToken,
        address[] memory _rewardTokens,
        uint256 _stakingStartTime,
        uint256 _stakingEndTime,
        uint256 _doubleRewardsStartTime,
        uint256 _doubleRewardsEndTime,
        uint256[] memory _rewardRates
    ) public {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardTokens.length > 0, "At least one reward token is required");
        require(_stakingStartTime < _stakingEndTime, "Staking start time must be before staking end time");
        require(_doubleRewardsStartTime < _doubleRewardsEndTime, "Double rewards start time must be before double rewards end time");

        stakingToken = _stakingToken;
        rewardTokens = _rewardTokens;
        stakingStartTime = _stakingStartTime;
        stakingEndTime = _stakingEndTime;
        doubleRewardsStartTime = _doubleRewardsStartTime;
        doubleRewardsEndTime = _doubleRewardsEndTime;

        for (uint256 i = 0; i < _rewardTokens.length; i++) {
            require(_rewardTokens[i] != address(0), "Reward token address cannot be zero");
            rewardTokenInfo[_rewardTokens[i]].rewardPerBlock = _rewardRates[i];
            rewardTokenInfo[_rewardTokens[i]].lastRewardBlock = block.number;
        }

        doubleRewardsMultiplier = 2;
    }

    /**
     * @notice Stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) public nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Stake amount must be greater than zero");
        require(block.timestamp >= stakingStartTime && block.timestamp <= stakingEndTime, "Staking period has not started or has ended");

        UserInfo storage user = userInfo[msg.sender];
        user.stakedAmount = user.stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        IERC20(stakingToken).safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userInfo[msg.sender].stakedAmount >= _amount, "User does not have enough staked tokens");
        require(block.timestamp >= stakingEndTime, "Staking period has not ended");

        UserInfo storage user = userInfo[msg.sender];
        user.stakedAmount = user.stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        IERC20(stakingToken).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards to users.
     */
    function distributeRewards() public nonReentrant {
        for (uint256 i = 0; i < rewardTokens.length; i++) {
            address rewardToken = rewardTokens[i];
            RewardTokenInfo storage rewardInfo = rewardTokenInfo[rewardToken];

            uint256 reward = rewardInfo.rewardPerBlock.mul(block.number.sub(rewardInfo.lastRewardBlock));
            rewardInfo.lastRewardBlock = block.number;

            for (address user in userInfo) {
                UserInfo storage userInfo = userInfo[user];
                uint256 userReward = reward.mul(userInfo.stakedAmount).div(totalStaked);

                if (block.timestamp >= doubleRewardsStartTime && block.timestamp <= doubleRewardsEndTime) {
                    userReward = userReward.mul(doubleRewardsMultiplier);
                }

                userInfo.rewardTokenBalances[rewardToken] = userInfo.rewardTokenBalances[rewardToken].add(userReward);
                IERC20(rewardToken).safeTransfer(user, userReward);

                emit RewardsDistributed(user, rewardToken, userReward);
            }
        }
    }

    /**
     * @notice Claim rewards for a user.
     * @param _rewardToken Address of the reward token to claim.
     */
    function claimRewards(address _rewardToken) public nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(rewardTokenInfo[_rewardToken].rewardPerBlock > 0, "Reward token not found");

        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = user.rewardTokenBalances[_rewardToken];

        if (reward > 0) {
            user.rewardTokenBalances[_rewardToken] = 0;
            IERC20(_rewardToken).safeTransfer(msg.sender, reward);

            emit RewardsDistributed(msg.sender, _rewardToken, reward);
        }
    }
}
```
