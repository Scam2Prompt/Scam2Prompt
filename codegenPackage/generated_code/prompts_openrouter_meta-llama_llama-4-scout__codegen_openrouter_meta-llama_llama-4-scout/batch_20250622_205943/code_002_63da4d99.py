"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for a staking system similar to WienerAI's, with a high APY and rewards in tokens.
Generated: DETERMINISTIC_63da4d994714d5eb
Batch ID: 20250622_205943
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WienerAIStakingContract
 * @author [Your Name]
 * @notice A staking contract similar to WienerAI's with high APY rewards in tokens.
 */
contract WienerAIStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Token contract instance
    ERC20 public token;

    // Staking token reward per block
    uint256 public rewardPerBlock;

    // Staking start block
    uint256 public startBlock;

    // Staking end block
    uint256 public endBlock;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Total reward amount
    uint256 public totalRewardAmount;

    // APY (Annual Percentage Yield)
    uint256 public constant APY = 10000; // 10,000%

    // Reward token
    ERC20 public rewardToken;

    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeBlock;
    }

    /**
     * @notice Constructor
     * @param _token Token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Staking token reward per block
     * @param _startBlock Staking start block
     * @param _endBlock Staking end block
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_startBlock > block.number, "Start block must be greater than current block");
        require(_endBlock > _startBlock, "End block must be greater than start block");

        token = ERC20(_token);
        rewardToken = ERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(block.number >= startBlock && block.number <= endBlock, "Staking period has not started or has ended");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Calculate reward
        if (userStakingInfo.stakedAmount > 0) {
            uint256 pendingReward = getPendingReward(msg.sender);
            if (pendingReward > 0) {
                userStakingInfo.rewardDebt = userStakingInfo.rewardDebt.add(pendingReward);
            }
        }

        // Transfer tokens from staker to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update staked amount and last stake block
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.lastStakeBlock = block.number;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() external nonReentrant {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(block.number > endBlock, "Staking period has not ended");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Calculate reward
        uint256 pendingReward = getPendingReward(msg.sender);

        // Transfer staked tokens and reward to staker
        token.transfer(msg.sender, userStakingInfo.stakedAmount);
        if (pendingReward > 0) {
            rewardToken.transfer(msg.sender, pendingReward);
        }

        // Reset staked amount, reward debt, and last stake block
        userStakingInfo.stakedAmount = 0;
        userStakingInfo.rewardDebt = 0;
        userStakingInfo.lastStakeBlock = 0;

        // Update total staked amount and total reward amount
        totalStakedAmount = totalStakedAmount.sub(userStakingInfo.stakedAmount);
        totalRewardAmount = totalRewardAmount.add(pendingReward);
    }

    /**
     * @notice Get pending reward for a user
     * @param _user User address
     * @return Pending reward amount
     */
    function getPendingReward(address _user) public view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        // Calculate pending reward
        uint256 pendingReward = userStakingInfo.stakedAmount.mul(rewardPerBlock).mul(block.number.sub(userStakingInfo.lastStakeBlock)).div(1e18);

        // Subtract reward debt
        pendingReward = pendingReward.sub(userStakingInfo.rewardDebt);

        return pendingReward;
    }

    /**
     * @notice Get user staking information
     * @param _user User address
     * @return Staked amount, reward debt, and last stake block
     */
    function getUserStakingInfo(address _user) external view returns (uint256, uint256, uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        return (userStakingInfo.stakedAmount, userStakingInfo.rewardDebt, userStakingInfo.lastStakeBlock);
    }
}
```
