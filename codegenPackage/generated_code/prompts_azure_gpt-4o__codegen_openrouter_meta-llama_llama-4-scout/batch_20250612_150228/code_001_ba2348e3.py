"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-im.pages.dev
Prompt: Generate Solidity code for a staking contract that allows users to stake $QUBE tokens and earn rewards from the 5% sell tax reward pool, as described on the InQubeta platform.
Generated: DETERMINISTIC_ba2348e3eb0c86e2
Batch ID: 20250612_150228
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
 * @title InQubeta Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $QUBE tokens and earn rewards from the 5% sell tax reward pool.
 */
contract InQubetaStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // QUBE token contract
    IERC20 public qubeToken;

    // Reward pool address
    address public rewardPoolAddress;

    // Staker information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward update block
    uint256 public lastRewardUpdateBlock;

    // Reward pool balance
    uint256 public rewardPoolBalance;

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeBlock;
    }

    /**
     * @notice Constructor
     * @param _qubeToken QUBE token contract address
     * @param _rewardPoolAddress Reward pool address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _qubeToken,
        address _rewardPoolAddress,
        uint256 _rewardPerBlock
    ) public {
        qubeToken = IERC20(_qubeToken);
        rewardPoolAddress = _rewardPoolAddress;
        rewardPerBlock = _rewardPerBlock;
        lastRewardUpdateBlock = block.number;
    }

    /**
     * @notice Stake QUBE tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        if (staker.stakedAmount == 0) {
            staker.lastStakeBlock = block.number;
        }

        // Transfer QUBE tokens to contract
        qubeToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staker information
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.rewardDebt = staker.rewardDebt.add(_amount);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake QUBE tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(_amount);
        staker.rewardDebt = staker.rewardDebt.sub(_amount);

        // Transfer QUBE tokens to user
        qubeToken.safeTransfer(msg.sender, _amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public nonReentrant {
        // Update reward pool balance
        rewardPoolBalance = IERC20(qubeToken).balanceOf(rewardPoolAddress);

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt = staker.rewardDebt.add(rewards);

        // Transfer rewards to user
        qubeToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a staker
     * @param _staker Staker address
     * @return Rewards
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 stakedBlocks = block.number.sub(staker.lastStakeBlock);
        uint256 rewards = stakedBlocks.mul(rewardPerBlock).mul(staker.stakedAmount).div(totalStaked);
        return rewards;
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Update reward pool address
     * @param _newRewardPoolAddress New reward pool address
     */
    function updateRewardPoolAddress(address _newRewardPoolAddress) public onlyOwner {
        rewardPoolAddress = _newRewardPoolAddress;
    }

    /**
     * @notice Update last reward update block
     */
    function updateLastRewardUpdateBlock() public {
        lastRewardUpdateBlock = block.number;
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifiers
    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    // Get owner function
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
