"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity smart contract that allows users to stake CRUDO tokens and earn rewards, as described in the Crudo Protocol documentation.
Generated: DETERMINISTIC_d9ab7931f601bf39
Batch ID: 20250612_163541
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CrudoStakingContract
 * @author [Your Name]
 * @notice This contract allows users to stake CRUDO tokens and earn rewards.
 */
contract CrudoStakingContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // CRUDO token contract
    IERC20 public crudoToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Total staked CRUDO tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Event emitted when user stakes CRUDO tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes CRUDO tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _crudoToken CRUDO token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        address _crudoToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        require(_crudoToken != address(0), "CRUDO token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_stakingStartBlock > block.number, "Staking start block must be in the future");
        require(_stakingEndBlock > _stakingStartBlock, "Staking end block must be greater than staking start block");

        crudoToken = IERC20(_crudoToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        lastRewardBlock = _stakingStartBlock;
    }

    /**
     * @dev Stake CRUDO tokens
     * @param _amount Amount of CRUDO tokens to stake
     */
    function stake(uint256 _amount) external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Stake amount must be greater than zero");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period has not started or has ended");
        require(crudoToken.balanceOf(msg.sender) >= _amount, "User does not have sufficient CRUDO tokens");

        // Update user's staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.amount = userStakingInfo.amount.add(_amount);
        userStakingInfo.rewardDebt = userStakingInfo.rewardDebt.add(_amount);

        // Transfer CRUDO tokens to the contract
        crudoToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update total staked CRUDO tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake CRUDO tokens
     * @param _amount Amount of CRUDO tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingInfos[msg.sender].amount >= _amount, "User does not have sufficient staked CRUDO tokens");

        // Update user's staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.amount = userStakingInfo.amount.sub(_amount);
        userStakingInfo.rewardDebt = userStakingInfo.rewardDebt.sub(_amount);

        // Transfer CRUDO tokens to the user
        crudoToken.safeTransfer(msg.sender, _amount);

        // Update total staked CRUDO tokens
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external {
        require(msg.sender != address(0), "User address cannot be zero");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's reward debt
        userStakingInfos[msg.sender].rewardDebt = userStakingInfos[msg.sender].rewardDebt.add(rewards);

        // Transfer rewards to the user
        rewardToken.safeTransfer(msg.sender, rewards);

        emit RewardsDistributed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards for the user
     */
    function calculateRewards(address _user) internal returns (uint256) {
        // Calculate accrued rewards
        uint256 accruedRewards = 0;
        uint256 currentBlock = block.number;
        if (currentBlock > lastRewardBlock && totalStaked > 0) {
            uint256 rewardBlocks = currentBlock.sub(lastRewardBlock);
            accruedRewards = totalStaked.mul(rewardPerBlock).mul(rewardBlocks);
        }

        // Update last reward block
        lastRewardBlock = currentBlock;

        return accruedRewards;
    }

    /**
     * @dev Get user's staking information
     * @param _user User address
     * @return User's staking information
     */
    function getUserStakingInfo(address _user) external view returns (uint256, uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];
        return (userStakingInfo.amount, userStakingInfo.rewardDebt);
    }

    struct UserStakingInfo {
        uint256 amount;
        uint256 rewardDebt;
    }
}
```
