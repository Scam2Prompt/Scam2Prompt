"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinetf-chain.pages.dev
Prompt: Create a Solidity smart contract that implements the staking mechanism for Bitcoin ETF Token, allowing users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_ed4f1f16bab762d8
Batch ID: 20250612_160853
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
 * @title Bitcoin ETF Staking Contract
 * @dev This contract allows users to stake Bitcoin ETF Tokens and earn rewards based on their staked amount.
 */
contract BitcoinETFStaking {
    // Token interface
    IERC20 public token;

    // Reward rate (e.g., 10% annual)
    uint256 public rewardRatePerSecond;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staking details
    struct StakeInfo {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for the user
        uint256 lastStaked;   // Timestamp of the last staking activity
    }
    mapping(address => StakeInfo) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the token and reward rate
    constructor(IERC20 _token, uint256 _annualRewardRate) {
        token = _token;
        // Convert annual reward rate to per-second rate (e.g., annualRate / 365 days / 24 hours / 3600 seconds)
        rewardRatePerSecond = _annualRewardRate / 365 / 24 / 3600;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before modifying the stake
        updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStaked = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the user before modifying the stake
        updateRewards(msg.sender);

        // Update stake information
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        // Update total staked tokens
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        updateRewards(msg.sender);

        // Calculate reward to be claimed
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Update rewards for the user based on their staked amount and staking duration.
     * @param _user Address of the user to update rewards for.
     */
    function updateRewards(address _user) internal {
        uint256 stakedAmount = stakes[_user].amount;
        uint256 lastStakedTime = stakes[_user].lastStaked;

        if (stakedAmount > 0 && lastStakedTime > 0) {
            // Calculate rewards based on staking duration
            uint256 duration = block.timestamp - lastStakedTime;
            uint256 reward = (stakedAmount * rewardRatePerSecond * duration) / 1e18;

            // Update reward debt
            stakes[_user].rewardDebt += reward;

            // Update last staked timestamp
            stakes[_user].lastStaked = block.timestamp;
        }
    }
    
    /**
     * @dev Retrieve staked amount and pending rewards for a user.
     * @param _user Address of the user.
     * @return staked Amount of tokens staked.
     * @return pendingRewards Pending rewards for the user.
     */
    function getStakeInfo(address _user) external view returns (uint256 staked, uint256 pendingRewards) {
        staked = stakes[_user].amount;
        
        uint256 pendingReward = stakes[_user].rewardDebt;
        uint256 stakedAmount = stakes[_user].amount;
        uint256 lastStakedTime = stakes[_user].lastStaked;

        if (stakedAmount > 0 && lastStakedTime > 0) {
            uint256 duration = block.timestamp - lastStakedTime;
            pendingReward += (stakedAmount * rewardRatePerSecond * duration) / 1e18;
        }

        pendingRewards = pendingReward;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
