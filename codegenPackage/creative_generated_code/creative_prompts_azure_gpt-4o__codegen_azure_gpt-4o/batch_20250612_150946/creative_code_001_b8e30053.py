"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the staking mechanism of Bitcoin BSC, where rewards are distributed every 10 minutes based on the percentage of the staking pool.
Generated: DETERMINISTIC_b8e3005399f3de53
Batch ID: 20250612_150946
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
 * @dev A smart contract to mimic a staking mechanism with rewards distribution every 10 minutes.
 */
contract StakingContract {
    // State variables
    uint256 public totalStaked; // Total staked tokens in the pool
    uint256 public rewardRatePer10Minutes; // Reward rate per 10 minutes (in tokens)
    uint256 constant REWARD_INTERVAL = 10 minutes;

    mapping(address => uint256) public stakedBalances; // Tracks staked tokens per user
    mapping(address => uint256) public lastClaimed; // Tracks last reward claim timestamp per user

    IERC20 public token; // Token to be staked and rewarded

    // Events
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event ClaimReward(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with token address and reward rate.
     * @param _token Address of the ERC20 token contract.
     * @param _rewardRatePer10Minutes Reward rate per 10 minutes (in tokens).
     */
    constructor(IERC20 _token, uint256 _rewardRatePer10Minutes) {
        token = _token;
        rewardRatePer10Minutes = _rewardRatePer10Minutes;
    }

    /**
     * @dev Modifier to ensure positive staking balance.
     */
    modifier hasStake(address _user) {
        require(stakedBalances[_user] > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staked balances and total staked
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        // Initialize last claimed timestamp if staking for the first time
        if (lastClaimed[msg.sender] == 0) {
            lastClaimed[msg.sender] = block.timestamp;
        }

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external hasStake(msg.sender) {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(_amount <= stakedBalances[msg.sender], "Insufficient staked balance");

        // Claim any pending rewards before unstaking
        claimReward();

        // Update staked balances and total staked
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer unstaked tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        if (totalStaked == 0 || stakedBalances[_user] == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - lastClaimed[_user];
        uint256 rewardIntervals = timeElapsed / REWARD_INTERVAL;

        uint256 userShare = (stakedBalances[_user] * 1e18) / totalStaked; // Calculate percentage share (scaled by 1e18)
        uint256 totalReward = rewardIntervals * rewardRatePer10Minutes;

        return (totalReward * userShare) / 1e18; // Scale back to normal value
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimReward() public hasStake(msg.sender) {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, reward), "Reward transfer failed");

        emit ClaimReward(msg.sender, reward);
    }

    /**
     * @dev Function to get the user's staking balance.
     * @param _user Address of the user.
     * @return Staking balance of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Function to get the user's last claimed timestamp.
     * @param _user Address of the user.
     * @return Last claimed timestamp of the user.
     */
    function getLastClaimed(address _user) external view returns (uint256) {
        return lastClaimed[_user];
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
