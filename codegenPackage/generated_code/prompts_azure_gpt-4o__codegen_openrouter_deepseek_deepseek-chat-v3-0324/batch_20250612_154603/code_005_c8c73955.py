"""
Generated Code Metadata:
========================
Original URL: https://karak-node.network
Prompt: Develop a smart contract that integrates Karak's restaking mechanism to boost yield for stakers while securing decentralized protocols.
Generated: DETERMINISTIC_c8c7395583b79340
Batch ID: 20250612_154603
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title KarakRestakingContract
 * @dev A smart contract that integrates with Karak's restaking mechanism to boost yields
 * for stakers while securing decentralized protocols.
 */
contract KarakRestakingContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store staker information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStakedTime; // Last time the user staked
    }

    // The staking token (e.g., KARAK or liquid staking token)
    IERC20 public stakingToken;

    // The reward token (could be same as staking token or different)
    IERC20 public rewardToken;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Last reward calculation block
    uint256 public lastRewardBlock;

    // Reward tokens per block
    uint256 public rewardPerBlock;

    // Precision factor for reward calculations
    uint256 public constant PRECISION_FACTOR = 1e18;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Protocol whitelist for restaking destinations
    mapping(address => bool) public whitelistedProtocols;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ProtocolWhitelisted(address indexed protocol);
    event ProtocolRemoved(address indexed protocol);
    event RewardPerBlockUpdated(uint256 newRewardPerBlock);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward tokens distributed per block
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update the reward variables of the pool
     */
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 multiplier = block.number - lastRewardBlock;
        uint256 reward = multiplier * rewardPerBlock;
        accRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens into the contract
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        Staker storage user = stakers[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastStakedTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage user = stakers[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp > user.lastStakedTime, "Cannot unstake immediately after staking");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        totalStaked -= _amount;

        stakingToken.safeTransfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        Staker storage user = stakers[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        safeRewardTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw without caring about rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage user = stakers[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;

        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
     * @param _to Address to transfer rewards to
     * @param _amount Amount of rewards to transfer
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (_amount > rewardBalance) {
            rewardToken.safeTransfer(_to, rewardBalance);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    /**
     * @dev Whitelist a protocol for restaking
     * @param _protocol Address of the protocol to whitelist
     */
    function whitelistProtocol(address _protocol) external onlyOwner {
        require(_protocol != address(0), "Invalid protocol address");
        whitelistedProtocols[_protocol] = true;
        emit ProtocolWhitelisted(_protocol);
    }

    /**
     * @dev Remove a protocol from whitelist
     * @param _protocol Address of the protocol to remove
     */
    function removeProtocol(address _protocol) external onlyOwner {
        require(whitelistedProtocols[_protocol], "Protocol not whitelisted");
        whitelistedProtocols[_protocol] = false;
        emit ProtocolRemoved(_protocol);
    }

    /**
     * @dev Update reward per block
     * @param _rewardPerBlock New reward per block value
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardPerBlockUpdated(_rewardPerBlock);
    }

    /**
     * @dev View function to see pending rewards for a user
     * @param _user Address of the user
     * @return Pending rewards for user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage user = stakers[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 multiplier = block.number - lastRewardBlock;
            uint256 reward = multiplier * rewardPerBlock;
            currentAccRewardPerShare += (reward * PRECISION_FACT
