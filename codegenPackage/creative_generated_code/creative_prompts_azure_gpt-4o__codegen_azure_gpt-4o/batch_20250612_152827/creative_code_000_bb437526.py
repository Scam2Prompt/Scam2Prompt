"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Write an Ethereum smart contract for staking ERC-20 tokens that distributes rewards proportionally to stakers over a fixed period, similar to the DOGE20 staking mechanism.
Generated: DETERMINISTIC_bb43752663fec071
Batch ID: 20250612_152827
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

contract StakingRewards {
    
    // State variables
    IERC20 public stakingToken;         // ERC-20 token used for staking
    IERC20 public rewardToken;          // ERC-20 token used for rewards
    uint256 public rewardRate;          // Reward rate per second
    uint256 public lastUpdateTime;      // Timestamp of the last update
    uint256 public rewardPerTokenStored; // Accumulated reward per token
    uint256 public stakingEndTime;      // Timestamp when staking ends

    mapping(address => uint256) public userStakeBalance;       // Stake balance for each user
    mapping(address => uint256) public userRewardPaid;         // Tracks the rewards paid to a user
    mapping(address => uint256) public userRewards;            // Reward balance for each user

    uint256 public totalStaked;        // Total staked tokens

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to update rewards before state changes
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Constructor
    constructor(
        address _stakingToken, 
        address _rewardToken, 
        uint256 _rewardRate, 
        uint256 _stakingDuration
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        stakingEndTime = block.timestamp + _stakingDuration;
    }

    // View function to calculate the reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) /
            totalStaked;
    }

    // View function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return 
            ((userStakeBalance[account] * (rewardPerToken() - userRewardPaid[account])) / 1e18) +
            userRewards[account];
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        require(block.timestamp < stakingEndTime, "Staking period has ended");

        // Transfer staking tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        userStakeBalance[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(userStakeBalance[msg.sender] >= amount, "Insufficient staked balance");

        userStakeBalance[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        require(reward > 0, "No rewards available");

        userRewards[msg.sender] = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Emergency withdrawal function (for admin or users in case of issues)
    function emergencyWithdraw(uint256 amount) external {
        require(userStakeBalance[msg.sender] >= amount, "Insufficient staked balance");

        userStakeBalance[msg.sender] -= amount;
        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }
}
```
