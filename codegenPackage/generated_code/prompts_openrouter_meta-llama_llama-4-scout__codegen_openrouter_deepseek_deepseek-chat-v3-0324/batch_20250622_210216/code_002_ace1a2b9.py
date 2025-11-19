"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-minetrix.web.app
Prompt: Design a smart contract on the Ethereum blockchain to manage the staking and mining credit allocation for Bitcoin Minetrix, using Solidity programming language.
Generated: DETERMINISTIC_ace1a2b9cac44343
Batch ID: 20250622_210216
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

contract BitcoinMinetrixStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent staking position
    struct Stake {
        uint256 amount;
        uint256 credit;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    // Token used for staking
    IERC20 public stakingToken;

    // Reward token (mining credits)
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public maxStakeAmount;
    uint256 public stakingDuration;
    uint256 public rewardRate; // Rewards per second per token

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ParametersUpdated(
        uint256 minStakeAmount,
        uint256 maxStakeAmount,
        uint256 stakingDuration,
        uint256 rewardRate
    );

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_minStakeAmount > 0, "Min stake amount must be > 0");
        require(_maxStakeAmount > _minStakeAmount, "Max stake must be > min stake");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens to earn mining credits
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(amount <= maxStakeAmount, "Amount exceeds maximum stake");
        require(stakes[msg.sender].amount == 0, "Already staked");

        stakes[msg.sender] = Stake({
            amount: amount,
            credit: 0,
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        });

        totalStaked += amount;
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim remaining rewards
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.stakedAt + stakingDuration, "Staking period not ended");

        uint256 reward = calculateRewards(msg.sender);
        if (reward > 0) {
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }

        totalStaked -= userStake.amount;
        stakingToken.safeTransfer(msg.sender, userStake.amount);

        delete stakes[msg.sender];
        emit Unstaked(msg.sender, userStake.amount);
    }

    /**
     * @dev Claim mining credit rewards
     */
    function claimRewards() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        userStake.lastClaimed = block.timestamp;
        rewardToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param staker Address of the staker
     * @return Amount of rewards available
     */
    function calculateRewards(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimed;
        uint256 remainingStakingPeriod = (userStake.stakedAt + stakingDuration) - block.timestamp;

        // Cap timeElapsed to remaining staking period
        if (timeElapsed > remainingStakingPeriod && remainingStakingPeriod > 0) {
            timeElapsed = remainingStakingPeriod;
        }

        return userStake.amount * rewardRate * timeElapsed;
    }

    /**
     * @dev Update staking parameters (owner only)
     */
    function updateParameters(
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardRate
    ) external onlyOwner {
        require(_minStakeAmount > 0, "Min stake amount must be > 0");
        require(_maxStakeAmount > _minStakeAmount, "Max stake must be > min stake");

        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;

        emit ParametersUpdated(_minStakeAmount, _maxStakeAmount, _stakingDuration, _rewardRate);
    }

    /**
     * @dev Emergency withdraw stuck tokens (owner only)
     */
    function emergencyWithdraw(address token) external onlyOwner {
        require(token != address(stakingToken), "Cannot withdraw staking token");
        IERC20(token).safeTransfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
