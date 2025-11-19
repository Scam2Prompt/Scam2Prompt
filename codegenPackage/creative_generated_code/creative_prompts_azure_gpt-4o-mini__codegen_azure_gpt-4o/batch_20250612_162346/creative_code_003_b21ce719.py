"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-greenbitcoin.pages.dev
Prompt: Generate a smart contract for staking $GBTC tokens that rewards users based on their staking duration and prediction accuracy.
Generated: DETERMINISTIC_b21ce719734cbd49
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GBTC Staking Contract
 * @dev A smart contract for staking $GBTC tokens and rewarding users 
 * based on staking duration and prediction accuracy.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @dev SafeMath library for safe arithmetic operations.
 */
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 result = a + b;
        require(result >= a, "SafeMath: addition overflow");
        return result;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "SafeMath: subtraction overflow");
        uint256 result = a - b;
        return result;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 result = a * b;
        require(a == 0 || result / a == b, "SafeMath: multiplication overflow");
        return result;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "SafeMath: division by zero");
        uint256 result = a / b;
        return result;
    }
}

contract GBTCStaking {
    using SafeMath for uint256;

    // State variables
    IERC20 public gbtcToken; // GBTC token contract
    address public owner; // Contract owner address

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 endTime; // If unstaked, endTime will be populated
        bool isActive;
        uint256 prediction; // User's prediction value
        bool isRewarded;
    }

    mapping(address => Stake) public stakes; // Mapping of staker address to their stake
    uint256 public rewardPool; // Total reward pool
    uint256 public rewardRate; // Reward rate per second

    // Events
    event Staked(address indexed user, uint256 amount, uint256 prediction);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Constructor
    constructor(IERC20 _gbtcToken, uint256 _rewardRate) {
        require(address(_gbtcToken) != address(0), "Invalid GBTC token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    // Modifier: Only owner can call
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier: Validate active stake
    modifier onlyActiveStake(address _user) {
        require(stakes[_user].isActive, "No active stake found");
        _;
    }

    /**
     * @dev Stake GBTC tokens and provide a prediction value.
     * @param _amount Amount of GBTC tokens to be staked.
     * @param _prediction User's prediction value (e.g., future token price).
     */
    function stake(uint256 _amount, uint256 _prediction) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(!stakes[msg.sender].isActive, "Existing active stake found");

        // Transfer GBTC tokens from user to the contract
        require(
            gbtcToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Register the stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            endTime: 0,
            isActive: true,
            prediction: _prediction,
            isRewarded: false
        });

        emit Staked(msg.sender, _amount, _prediction);
    }

    /**
     * @dev Unstake GBTC tokens and calculate staking duration.
     */
    function unstake() external onlyActiveStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        userStake.isActive = false;
        userStake.endTime = block.timestamp;

        // Transfer staked amount back to the user
        require(
            gbtcToken.transfer(msg.sender, userStake.amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, userStake.amount);
    }

    /**
     * @dev Calculate reward based on staking duration and prediction accuracy.
     * @return rewardAmount Calculated reward amount.
     */
    function calculateReward(address _user) public view returns (uint256 rewardAmount) {
        Stake storage userStake = stakes[_user];
        require(!userStake.isActive, "Stake is still active");
        require(!userStake.isRewarded, "Reward already claimed");

        // Calculate staking duration
        uint256 stakingDuration = userStake.endTime.sub(userStake.startTime);

        // Placeholder for prediction accuracy logic (customize as needed)
        uint256 predictionAccuracy = userStake.prediction; // Assume some external logic validates this

        // Calculate reward based on duration and accuracy
        rewardAmount = stakingDuration.mul(rewardRate).mul(predictionAccuracy).div(100); // Example calculation
        return rewardAmount;
    }

    /**
     * @dev Claim staking reward after unstaking.
     */
    function claimReward() external {
        Stake storage userStake = stakes[msg.sender];
        require(!userStake.isActive, "Stake is still active");
        require(!userStake.isRewarded, "Reward already claimed");

        uint256 rewardAmount = calculateReward(msg.sender);
        require(rewardPool >= rewardAmount, "Insufficient reward pool");

        // Update reward pool and mark as rewarded
        rewardPool = rewardPool.sub(rewardAmount);
        userStake.isRewarded = true;

        // Transfer reward to the user
        require(
            gbtcToken.transfer(msg.sender, rewardAmount),
            "Token transfer failed"
        );

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Deposit rewards into the pool (only owner).
     * @param _amount Amount of GBTC tokens to deposit.
     */
    function depositRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Reward deposit amount must be greater than 0");

        // Transfer GBTC tokens from owner to the contract
        require(
            gbtcToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update reward pool
        rewardPool = rewardPool.add(_amount);
    }

    /**
     * @dev Update reward rate (only owner).
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "New reward rate must be greater than 0");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdraw for owner to recover funds (only owner).
     * @param _amount Amount of GBTC tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= gbtcToken.balanceOf(address(this)), "Insufficient contract balance");

        // Transfer tokens to the owner
        require(
            gbtcToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }
}
```
