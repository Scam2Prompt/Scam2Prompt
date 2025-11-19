"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that distributes rewards over two years based on the percentage of the staking pool.
Generated: DETERMINISTIC_6f21c65a6b24cb7b
Batch ID: 20250612_161353
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
 * @title StakingContract
 * @dev A staking contract for DOGE20 tokens that distributes rewards over two years based on the percentage of the staking pool.
 */
contract StakingContract {
    // Token interface for DOGE20 compliance
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public immutable token; // DOGE20 token contract
    address public owner; // Owner of the contract
    uint256 public constant REWARD_DURATION = 730 days; // Two years in seconds
    uint256 public rewardPool; // Total rewards allocated for distribution
    uint256 public stakingStartTime; // Timestamp when staking started
    uint256 public totalStaked; // Total amount of tokens staked by all users

    struct Staker {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 rewardDebt; // Rewards already claimed by the user
    }

    mapping(address => Staker) public stakers; // Mapping of stakers' data

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier stakingActive() {
        require(block.timestamp >= stakingStartTime, "Staking has not started yet");
        _;
    }

    // Constructor
    constructor(address _token, uint256 _rewardPool, uint256 _stakingStartTime) {
        require(_token != address(0), "Invalid token address");
        require(_rewardPool > 0, "Reward pool must be greater than zero");
        require(_stakingStartTime > block.timestamp, "Staking start time must be in the future");

        token = IERC20(_token);
        owner = msg.sender;
        rewardPool = _rewardPool;
        stakingStartTime = _stakingStartTime;
    }

    /**
     * @dev Stake DOGE20 tokens into the pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external stakingActive {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external stakingActive {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on staking percentage and elapsed time.
     */
    function claimRewards() external stakingActive {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - stakingStartTime;
        if (stakingDuration > REWARD_DURATION) {
            stakingDuration = REWARD_DURATION; // Cap staking duration to reward period
        }

        uint256 rewardAmount = (rewardPool * staker.amountStaked / totalStaked) * stakingDuration / REWARD_DURATION;
        uint256 claimableReward = rewardAmount - staker.rewardDebt;

        require(claimableReward > 0, "No rewards available to claim");

        staker.rewardDebt += claimableReward;

        // Transfer reward tokens to the user
        require(token.transfer(msg.sender, claimableReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, claimableReward);
    }

    /**
     * @dev Owner can deposit additional rewards into the pool.
     * @param amount Amount of tokens to add to the reward pool.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot deposit zero tokens");

        // Transfer tokens from the owner to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        rewardPool += amount;
    }

    /**
     * @dev Emergency withdraw, allows owner to withdraw all tokens from the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(token.transfer(owner, contractBalance), "Emergency withdrawal failed");
    }
}
```
