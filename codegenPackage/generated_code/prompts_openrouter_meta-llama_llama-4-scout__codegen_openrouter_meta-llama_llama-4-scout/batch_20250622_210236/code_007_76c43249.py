"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-net.web.app
Prompt: Develop a staking pool contract for EarthMeta tokens, including functionality for users to stake their tokens and earn rewards in the form of additional EMT tokens.
Generated: DETERMINISTIC_76c432498cc28bc9
Batch ID: 20250622_210236
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

/**
 * @title Staking Pool Contract for EarthMeta Tokens
 * @author [Your Name]
 * @notice This contract allows users to stake their EMT tokens and earn rewards in the form of additional EMT tokens.
 */
contract StakingPool is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // EMT token contract
    IERC20 public emtToken;

    // Total EMT tokens staked
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward distribution start block
    uint256 public rewardDistributionStartBlock;

    // Event emitted when user stakes EMT tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes EMT tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Struct to store user staking information
     */
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeBlock;
    }

    /**
     * @dev Constructor
     * @param _emtTokenAddress Address of EMT token contract
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     * @param _rewardDistributionStartBlock Reward distribution start block
     */
    constructor(
        address _emtTokenAddress,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock,
        uint256 _rewardDistributionStartBlock
    ) public {
        emtToken = IERC20(_emtTokenAddress);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        rewardDistributionStartBlock = _rewardDistributionStartBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake EMT tokens
     * @param _amount Amount of EMT tokens to stake
     */
    function stake(uint256 _amount) public {
        require(msg.sender != address(0), "StakingPool: staker address cannot be 0");
        require(_amount > 0, "StakingPool: stake amount must be greater than 0");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "StakingPool: staking period has not started or has ended");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];
        uint256 newStakedAmount = userInfo.stakedAmount.add(_amount);

        // Update user's staking information
        userInfo.stakedAmount = newStakedAmount;
        userInfo.lastStakeBlock = block.number;

        // Update total staked EMT tokens
        totalStaked = totalStaked.add(_amount);

        // Transfer EMT tokens to the contract
        emtToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake EMT tokens
     */
    function unstake() public {
        require(msg.sender != address(0), "StakingPool: staker address cannot be 0");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "StakingPool: user has not staked any EMT tokens");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];
        uint256 stakedAmount = userInfo.stakedAmount;

        // Update user's staking information
        userInfo.stakedAmount = 0;
        userInfo.rewardDebt = 0;

        // Update total staked EMT tokens
        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer EMT tokens back to the user
        emtToken.transfer(msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @dev Distribute rewards to users
     */
    function distributeRewards() public {
        require(block.number >= rewardDistributionStartBlock, "StakingPool: reward distribution has not started");

        uint256 currentBlock = block.number;
        uint256 rewards = 0;

        // Calculate rewards
        if (currentBlock > lastRewardBlock) {
            rewards = totalStaked.mul(currentBlock.sub(lastRewardBlock)).mul(rewardPerBlock);
            lastRewardBlock = currentBlock;
        }

        // Distribute rewards to users
        for (address user in userStakingInfos) {
            UserStakingInfo storage userInfo = userStakingInfos[user];

            if (userInfo.stakedAmount > 0) {
                uint256 userRewards = rewards.mul(userInfo.stakedAmount).div(totalStaked);
                userInfo.rewardDebt = userInfo.rewardDebt.add(userRewards);

                // Transfer rewards to the user
                emtToken.transfer(user, userRewards);

                emit RewardsDistributed(user, userRewards);
            }
        }
    }

    /**
     * @dev Get user's staking information
     * @param _user User address
     * @return User's staking information
     */
    function getUserStakingInfo(address _user) public view returns (UserStakingInfo memory) {
        return userStakingInfos[_user];
    }
}
```
