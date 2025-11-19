"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate a smart contract for a decentralized betting platform that allows users to stake $BCB tokens and receive rewards in stable coins.
Generated: DETERMINISTIC_b7a11231a0d2b817
Batch ID: 20250612_163616
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DecentralizedBetting is Ownable, ReentrancyGuard {
    // Token interfaces
    IERC20 public bcbToken;
    IERC20 public stableCoin;

    // Betting parameters
    uint256 public minStakeAmount;
    uint256 public maxStakeAmount;
    uint256 public rewardMultiplier; // Multiplier in basis points (10000 = 1x)
    uint256 public houseFee; // Fee in basis points (100 = 1%)

    // Betting round structure
    struct BettingRound {
        uint256 roundId;
        uint256 totalStaked;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
        bool rewardsDistributed;
    }

    // User bets
    struct UserBet {
        uint256 amountStaked;
        bool hasClaimed;
    }

    // Current and past rounds
    mapping(uint256 => BettingRound) public bettingRounds;
    mapping(uint256 => mapping(address => UserBet)) public userBets;
    uint256 public currentRoundId;

    // Events
    event RoundStarted(uint256 roundId, uint256 startTime, uint256 endTime);
    event Staked(address indexed user, uint256 roundId, uint256 amount);
    event RewardsDistributed(uint256 roundId, uint256 totalRewards);
    event RewardClaimed(address indexed user, uint256 roundId, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 roundId, uint256 amount);

    constructor(
        address _bcbToken,
        address _stableCoin,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _rewardMultiplier,
        uint256 _houseFee
    ) {
        require(_bcbToken != address(0), "Invalid BCB token address");
        require(_stableCoin != address(0), "Invalid stable coin address");
        require(_minStakeAmount > 0, "Min stake must be > 0");
        require(_maxStakeAmount > _minStakeAmount, "Max stake must be > min stake");
        require(_rewardMultiplier > 0, "Reward multiplier must be > 0");
        require(_houseFee < 10000, "House fee must be < 100%");

        bcbToken = IERC20(_bcbToken);
        stableCoin = IERC20(_stableCoin);
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        rewardMultiplier = _rewardMultiplier;
        houseFee = _houseFee;
    }

    /**
     * @dev Start a new betting round
     * @param duration Duration of the round in seconds
     */
    function startNewRound(uint256 duration) external onlyOwner {
        require(duration > 0, "Duration must be > 0");
        currentRoundId++;

        bettingRounds[currentRoundId] = BettingRound({
            roundId: currentRoundId,
            totalStaked: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + duration,
            isActive: true,
            rewardsDistributed: false
        });

        emit RoundStarted(currentRoundId, block.timestamp, block.timestamp + duration);
    }

    /**
     * @dev Stake BCB tokens to participate in current round
     * @param amount Amount of BCB tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(amount <= maxStakeAmount, "Amount exceeds maximum stake");
        require(bettingRounds[currentRoundId].isActive, "No active round");
        require(block.timestamp < bettingRounds[currentRoundId].endTime, "Round has ended");

        // Transfer BCB tokens from user to contract
        require(bcbToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user bet and round totals
        userBets[currentRoundId][msg.sender].amountStaked += amount;
        bettingRounds[currentRoundId].totalStaked += amount;

        emit Staked(msg.sender, currentRoundId, amount);
    }

    /**
     * @dev Distribute rewards for a completed round
     */
    function distributeRewards(uint256 roundId) external onlyOwner nonReentrant {
        require(roundId <= currentRoundId, "Invalid round ID");
        require(bettingRounds[roundId].isActive, "Round not active");
        require(block.timestamp >= bettingRounds[roundId].endTime, "Round not ended");
        require(!bettingRounds[roundId].rewardsDistributed, "Rewards already distributed");

        bettingRounds[roundId].isActive = false;
        bettingRounds[roundId].rewardsDistributed = true;

        uint256 totalStaked = bettingRounds[roundId].totalStaked;
        if (totalStaked == 0) {
            return;
        }

        // Calculate total rewards (minus house fee)
        uint256 totalRewards = (totalStaked * rewardMultiplier) / 10000;
        uint256 houseCut = (totalRewards * houseFee) / 10000;
        uint256 netRewards = totalRewards - houseCut;

        // Transfer stable coins from owner to contract
        require(stableCoin.transferFrom(owner(), address(this), netRewards), "Reward transfer failed");

        emit RewardsDistributed(roundId, netRewards);
    }

    /**
     * @dev Claim rewards for a completed round
     * @param roundId Round ID to claim rewards from
     */
    function claimReward(uint256 roundId) external nonReentrant {
        require(roundId <= currentRoundId, "Invalid round ID");
        require(!bettingRounds[roundId].isActive, "Round still active");
        require(bettingRounds[roundId].rewardsDistributed, "Rewards not distributed");
        require(userBets[roundId][msg.sender].amountStaked > 0, "No stake in this round");
        require(!userBets[roundId][msg.sender].hasClaimed, "Reward already claimed");

        userBets[roundId][msg.sender].hasClaimed = true;

        uint256 userStake = userBets[roundId][msg.sender].amountStaked;
        uint256 totalStaked = bettingRounds[roundId].totalStaked;
        uint256 totalRewards = (bettingRounds[roundId].totalStaked * rewardMultiplier) / 10000;
        uint256 houseCut = (totalRewards * houseFee) / 10000;
        uint256 netRewards = totalRewards - houseCut;

        uint256 userReward = (userStake * netRewards) / totalStaked;

        require(stableCoin.transfer(msg.sender, userReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, roundId, userReward);
    }

    /**
     * @dev Emergency withdraw stake from an active round
     * @param roundId Round ID to withdraw from
     */
    function emergencyWithdraw(uint256 roundId) external nonReentrant {
        require(bettingRounds[roundId].isActive, "Round not active");
        require(userBets[roundId][msg.sender].amountStaked > 0, "No stake to withdraw");

        uint256 amount = userBets[roundId][msg.sender].amountStaked;
        userBets[roundId][msg.sender].amountStaked = 0;
        bettingRounds[roundId].totalStaked -= amount;

        require(bcbToken.transfer(msg.sender, amount), "Withdrawal failed");

        emit EmergencyWithdraw(msg.sender, roundId, amount);
    }

    /**
     * @dev Update contract parameters (owner only)
     */
    function updateParameters(
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _rewardMultiplier,
        uint256 _houseFee
    ) external onlyOwner {
        require(_minStakeAmount > 0, "Min stake must be > 0");
        require(_maxStakeAmount > _minStakeAmount, "Max stake must be > min stake");
        require(_rewardMultiplier > 0, "Reward multiplier must be > 0");
        require(_houseFee < 10000, "House fee must be < 100%");

        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        rewardMultiplier = _rewardMultiplier;
        houseFee = _houseFee;
    }

    /**
     * @dev Withdraw any ERC20 tokens (owner only)
     */
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress
