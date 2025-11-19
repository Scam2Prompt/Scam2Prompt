"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-xyz-en.pages.dev
Prompt: Generate a Solidity smart contract for implementing a gamified staking mechanism similar to Green Bitcoin's "Predict-To-Earn" model, where users can predict Bitcoin price trends and earn rewards based on their accuracy.
Generated: DETERMINISTIC_b7cc8a80c72afc7d
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract GamifiedStaking is Ownable, ReentrancyGuard {
    // Chainlink BTC/USD price feed
    AggregatorV3Interface internal priceFeed;
    
    // Staking token (e.g., project's native token)
    IERC20 public stakingToken;
    
    // Reward token (can be same as staking token)
    IERC20 public rewardToken;
    
    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public maxStakeAmount;
    uint256 public stakingLockPeriod;
    uint256 public totalStaked;
    
    // Prediction parameters
    uint256 public predictionWindow; // Time window for predictions (in seconds)
    uint256 public currentEpoch;
    uint256 public rewardMultiplier = 2; // 2x reward for correct predictions
    
    // Epoch data
    struct Epoch {
        uint256 startTime;
        uint256 endTime;
        uint256 startPrice;
        uint256 endPrice;
        bool priceSet;
        uint256 totalStaked;
    }
    
    // User data
    struct UserStake {
        uint256 amount;
        uint256 epoch;
        bool predictedUp;
        bool rewardClaimed;
    }
    
    // Mappings
    mapping(uint256 => Epoch) public epochs;
    mapping(address => UserStake[]) public userStakes;
    mapping(address => uint256) public userTotalStaked;
    
    // Events
    event Staked(address indexed user, uint256 amount, uint256 epoch, bool predictedUp);
    event RewardClaimed(address indexed user, uint256 amount, uint256 epoch);
    event EpochStarted(uint256 indexed epoch, uint256 startTime, uint256 endTime);
    event EpochEnded(uint256 indexed epoch, uint256 endPrice);
    event PriceFeedUpdated(address newPriceFeed);
    
    constructor(
        address _stakingToken,
        address _rewardToken,
        address _priceFeed,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _stakingLockPeriod,
        uint256 _predictionWindow
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        priceFeed = AggregatorV3Interface(_priceFeed);
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        stakingLockPeriod = _stakingLockPeriod;
        predictionWindow = _predictionWindow;
        
        // Initialize first epoch
        _startNewEpoch();
    }
    
    // Stake tokens and make a price prediction
    function stakeAndPredict(uint256 amount, bool predictedUp) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(amount <= maxStakeAmount, "Amount exceeds maximum stake");
        require(block.timestamp < epochs[currentEpoch].endTime, "Prediction window closed");
        
        // Transfer tokens from user
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staking data
        totalStaked += amount;
        userTotalStaked[msg.sender] += amount;
        epochs[currentEpoch].totalStaked += amount;
        
        // Record user stake and prediction
        userStakes[msg.sender].push(UserStake({
            amount: amount,
            epoch: currentEpoch,
            predictedUp: predictedUp,
            rewardClaimed: false
        }));
        
        emit Staked(msg.sender, amount, currentEpoch, predictedUp);
    }
    
    // Claim rewards for a specific epoch
    function claimReward(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        
        UserStake storage stake = userStakes[msg.sender][stakeIndex];
        require(!stake.rewardClaimed, "Reward already claimed");
        require(block.timestamp >= epochs[stake.epoch].endTime + stakingLockPeriod, "Lock period not over");
        require(epochs[stake.epoch].priceSet, "Epoch price not finalized");
        
        // Calculate reward
        uint256 reward = calculateReward(msg.sender, stakeIndex);
        
        // Mark reward as claimed
        stake.rewardClaimed = true;
        
        // Transfer reward if any
        if (reward > 0) {
            rewardToken.transfer(msg.sender, reward);
        }
        
        emit RewardClaimed(msg.sender, reward, stake.epoch);
    }
    
    // Calculate reward for a specific stake
    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256) {
        UserStake memory stake = userStakes[user][stakeIndex];
        Epoch memory epoch = epochs[stake.epoch];
        
        if (!epoch.priceSet) return 0;
        
        bool priceWentUp = epoch.endPrice > epoch.startPrice;
        bool correctPrediction = (stake.predictedUp == priceWentUp);
        
        if (correctPrediction) {
            return stake.amount * rewardMultiplier;
        }
        
        return 0;
    }
    
    // Start a new epoch (can be called by anyone after previous epoch ends)
    function startNewEpoch() external {
        require(block.timestamp >= epochs[currentEpoch].endTime, "Current epoch not ended");
        _startNewEpoch();
    }
    
    // Internal function to start new epoch
    function _startNewEpoch() internal {
        currentEpoch++;
        
        epochs[currentEpoch] = Epoch({
            startTime: block.timestamp,
            endTime: block.timestamp + predictionWindow,
            startPrice: getLatestPrice(),
            endPrice: 0,
            priceSet: false,
            totalStaked: 0
        });
        
        emit EpochStarted(currentEpoch, block.timestamp, block.timestamp + predictionWindow);
    }
    
    // Finalize epoch with end price (can be called by anyone after epoch ends)
    function finalizeEpoch() external {
        require(block.timestamp >= epochs[currentEpoch].endTime, "Epoch not ended");
        require(!epochs[currentEpoch].priceSet, "Epoch already finalized");
        
        epochs[currentEpoch].endPrice = getLatestPrice();
        epochs[currentEpoch].priceSet = true;
        
        emit EpochEnded(currentEpoch, epochs[currentEpoch].endPrice);
    }
    
    // Get latest BTC/USD price from Chainlink
    function getLatestPrice() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return uint256(price);
    }
    
    // Admin functions
    function updatePriceFeed(address newPriceFeed) external onlyOwner {
        priceFeed = AggregatorV3Interface(newPriceFeed);
        emit PriceFeedUpdated(newPriceFeed);
    }
    
    function updateRewardMultiplier(uint256 newMultiplier) external onlyOwner {
        require(newMultiplier > 0, "Multiplier must be positive");
        rewardMultiplier = newMultiplier;
    }
    
    function updateStakingLimits(uint256 newMin, uint256 newMax) external onlyOwner {
        require(newMin <= newMax, "Min must be <= max");
        minStakeAmount = newMin;
        maxStakeAmount = newMax;
    }
    
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
    
    // View functions
    function getUserStakes(address user) external view returns (UserStake[] memory) {
        return userStakes[user];
    }
    
    function getCurrentEpochDetails() external view returns (Epoch memory) {
        return epochs[currentEpoch];
    }
    
    function getEpochDetails(uint256 epoch) external view returns (Epoch memory) {
        return epochs[epoch];
    }
}
```
