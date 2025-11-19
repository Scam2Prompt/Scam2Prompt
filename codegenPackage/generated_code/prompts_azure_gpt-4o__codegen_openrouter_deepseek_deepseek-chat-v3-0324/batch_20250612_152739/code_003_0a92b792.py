"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoindapp.pages.dev
Prompt: Create a smart contract in Solidity for implementing a gamified staking mechanism with prediction-based rewards, inspired by Green Bitcoin’s staking model.
Generated: DETERMINISTIC_0a92b792355ca041
Batch ID: 20250612_152739
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

contract GamifiedStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedTimestamp;
        uint256 totalRewardsEarned;
        uint256 pendingRewards;
        uint256[] predictionHistory;
    }

    struct Round {
        uint256 startTime;
        uint256 endTime;
        uint256 targetPrice;
        uint256 actualPrice;
        bool isFinalized;
        uint256 totalStaked;
        uint256 rewardPool;
    }

    uint256 public currentRoundId;
    uint256 public minStakeDuration = 7 days;
    uint256 public maxStakeDuration = 30 days;
    uint256 public baseAPY = 10; // 10% base APY
    uint256 public predictionBonusMultiplier = 2; // 2x bonus for correct predictions

    mapping(address => Staker) public stakers;
    mapping(uint256 => Round) public rounds;
    mapping(uint256 => mapping(address => uint256)) public predictions;

    event Staked(address indexed user, uint256 amount, uint256 roundId);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event PredictionMade(address indexed user, uint256 roundId, uint256 predictedPrice);
    event RoundCreated(uint256 roundId, uint256 startTime, uint256 endTime);
    event RoundFinalized(uint256 roundId, uint256 actualPrice);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        _createNewRound(block.timestamp, block.timestamp + 7 days);
    }

    function stake(uint256 _amount, uint256 _predictedPrice) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(block.timestamp >= rounds[currentRoundId].startTime, "Round not started");
        require(block.timestamp < rounds[currentRoundId].endTime, "Round ended");

        stakingToken.transferFrom(msg.sender, address(this), _amount);

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.lastStakedTimestamp = block.timestamp;

        if (predictions[currentRoundId][msg.sender] == 0) {
            predictions[currentRoundId][msg.sender] = _predictedPrice;
            staker.predictionHistory.push(currentRoundId);
            emit PredictionMade(msg.sender, currentRoundId, _predictedPrice);
        }

        rounds[currentRoundId].totalStaked += _amount;
        emit Staked(msg.sender, _amount, currentRoundId);
    }

    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No stake to withdraw");

        uint256 stakedAmount = staker.amountStaked;
        uint256 reward = calculateReward(msg.sender);

        stakingToken.transfer(msg.sender, stakedAmount);
        if (reward > 0) {
            rewardToken.transfer(msg.sender, reward);
            staker.totalRewardsEarned += reward;
        }

        staker.amountStaked = 0;
        staker.pendingRewards = 0;
        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    function calculateReward(address _user) public view returns (uint256) {
        Staker memory staker = stakers[_user];
        if (staker.amountStaked == 0) return 0;

        uint256 reward = 0;
        for (uint256 i = 0; i < staker.predictionHistory.length; i++) {
            uint256 roundId = staker.predictionHistory[i];
            if (rounds[roundId].isFinalized) {
                uint256 stakedInRound = getStakedAmountInRound(_user, roundId);
                if (stakedInRound > 0) {
                    uint256 baseReward = (stakedInRound * baseAPY * (rounds[roundId].endTime - rounds[roundId].startTime)) / (365 days * 100);
                    
                    if (predictions[roundId][_user] == rounds[roundId].actualPrice) {
                        baseReward *= predictionBonusMultiplier;
                    }
                    
                    reward += baseReward;
                }
            }
        }
        return reward;
    }

    function getStakedAmountInRound(address _user, uint256 _roundId) public view returns (uint256) {
        if (_roundId == currentRoundId) {
            return stakers[_user].amountStaked;
        }
        
        // For previous rounds, we'd need to track historical staking amounts
        // This is a simplified version - in production you'd need proper historical tracking
        return 0;
    }

    function createNewRound(uint256 _durationInDays, uint256 _targetPrice) external onlyOwner {
        require(_durationInDays * 1 days >= minStakeDuration, "Duration too short");
        require(_durationInDays * 1 days <= maxStakeDuration, "Duration too long");
        
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + (_durationInDays * 1 days);
        
        _createNewRound(startTime, endTime);
        rounds[currentRoundId].targetPrice = _targetPrice;
    }

    function _createNewRound(uint256 _startTime, uint256 _endTime) private {
        currentRoundId++;
        rounds[currentRoundId] = Round({
            startTime: _startTime,
            endTime: _endTime,
            targetPrice: 0,
            actualPrice: 0,
            isFinalized: false,
            totalStaked: 0,
            rewardPool: 0
        });
        emit RoundCreated(currentRoundId, _startTime, _endTime);
    }

    function finalizeRound(uint256 _actualPrice) external onlyOwner {
        require(block.timestamp >= rounds[currentRoundId].endTime, "Round not ended");
        require(!rounds[currentRoundId].isFinalized, "Round already finalized");

        rounds[currentRoundId].actualPrice = _actualPrice;
        rounds[currentRoundId].isFinalized = true;
        
        emit RoundFinalized(currentRoundId, _actualPrice);
        
        // Create new round automatically
        _createNewRound(block.timestamp, block.timestamp + 7 days);
    }

    function depositRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        rewardToken.transferFrom(msg.sender, address(this), _amount);
        rounds[currentRoundId].rewardPool += _amount;
    }

    function setBaseAPY(uint256 _newAPY) external onlyOwner {
        require(_newAPY <= 100, "APY cannot exceed 100%");
        baseAPY = _newAPY;
    }

    function setPredictionBonusMultiplier(uint256 _newMultiplier) external onlyOwner {
        require(_newMultiplier > 0, "Multiplier must be greater than 0");
        predictionBonusMultiplier = _newMultiplier;
    }

    function setStakeDurationLimits(uint256 _minDays, uint256 _maxDays) external onlyOwner {
        require(_minDays > 0, "Min duration must be > 0");
        require(_maxDays > _minDays, "Max must be > min");
        minStakeDuration = _minDays * 1 days;
        maxStakeDuration = _maxDays * 1 days;
    }
}
```
