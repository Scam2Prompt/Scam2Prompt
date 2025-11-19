"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasclub.xyz
Prompt: Create a smart contract in Solidity for managing FEG token staking on Binance Smart Chain, considering the transition details discussed.
Generated: DETERMINISTIC_89095541cb61ee25
Batch ID: 20250612_153314
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
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title FEGTokenStakingContract
 * @author [Your Name]
 * @notice A smart contract for managing FEG token staking on Binance Smart Chain.
 */
contract FEGTokenStakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // FEG token contract instance
    IERC20 public fegToken;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Event emitted when user stakes FEG tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes FEG tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims reward
    event RewardClaimed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastRewardBlock;
    }

    /**
     * @notice Constructor function
     * @param _fegTokenAddress FEG token contract address
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _fegTokenAddress,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock,
        uint256 _rewardPerBlock
    ) public {
        require(_fegTokenAddress != address(0), "FEG token address cannot be zero");
        require(_stakingStartBlock > 0, "Staking start block must be greater than zero");
        require(_stakingEndBlock > _stakingStartBlock, "Staking end block must be greater than start block");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        fegToken = IERC20(_fegTokenAddress);
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Stake FEG tokens
     * @param _amount Amount of FEG tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(block.number >= stakingStartBlock, "Staking has not started yet");
        require(block.number <= stakingEndBlock, "Staking has ended");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Update reward debt and last reward block if user has staked before
        if (userStakingInfo.stakedAmount > 0) {
            _updateReward(msg.sender);
        }

        // Transfer FEG tokens from user to contract
        require(fegToken.transferFrom(msg.sender, address(this), _amount), "FEG token transfer failed");

        // Update user's staking information
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.lastRewardBlock = block.number;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake FEG tokens
     * @param _amount Amount of FEG tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "User does not have enough staked tokens");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // Update reward debt and last reward block
        _updateReward(msg.sender);

        // Update user's staking information
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);
        userStakingInfo.lastRewardBlock = block.number;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        // Transfer FEG tokens from contract to user
        require(fegToken.transfer(msg.sender, _amount), "FEG token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        require(msg.sender != address(0), "User address cannot be zero");

        _updateReward(msg.sender);

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        uint256 reward = userStakingInfo.rewardDebt;
        userStakingInfo.rewardDebt = 0;

        // Transfer reward to user
        require(fegToken.transfer(msg.sender, reward), "FEG token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Update reward
     * @param _user User address
     */
    function _updateReward(address _user) internal {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];

        if (userStakingInfo.stakedAmount == 0) {
            return;
        }

        uint256 currentBlock = block.number;
        uint256 reward = userStakingInfo.stakedAmount.mul(rewardPerBlock).mul(currentBlock.sub(userStakingInfo.lastRewardBlock));

        userStakingInfo.rewardDebt = reward;
        userStakingInfo.lastRewardBlock = currentBlock;
    }

    /**
     * @notice Update staking end block
     * @param _newStakingEndBlock New staking end block
     */
    function updateStakingEndBlock(uint256 _newStakingEndBlock) external onlyOwner {
        require(_newStakingEndBlock > stakingStartBlock, "New staking end block must be greater than start block");
        stakingEndBlock = _newStakingEndBlock;
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        require(_newRewardPerBlock > 0, "New reward per block must be greater than zero");
        rewardPerBlock = _newRewardPerBlock;
    }
}
```
