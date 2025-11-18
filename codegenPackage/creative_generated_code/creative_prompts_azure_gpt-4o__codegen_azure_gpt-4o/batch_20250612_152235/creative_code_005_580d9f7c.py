"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farm-sophon.web.app
Prompt: Develop a smart contract that supports farming pools for earning and redeeming tokens like SP and $SOPH, inspired by the Sophon Farming system.
Generated: DETERMINISTIC_580d9f7c98e9f3f9
Batch ID: 20250612_152235
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
 * @title Token Farming Contract
 * @dev Supports farming pools for earning and redeeming tokens (e.g., SP and SOPH).
 */
contract TokenFarming {
    // Variables
    address public spToken; // Address of SP token contract
    address public sophToken; // Address of SOPH token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked in the pool

    struct UserInfo {
        uint256 amount; // Tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => UserInfo) public users;

    uint256 public lastRewardTime; // Last timestamp rewards were distributed
    uint256 public accRewardPerShare; // Accumulated rewards per share

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event ClaimReward(address indexed user, uint256 reward);

    // Constructor
    constructor(address _spToken, address _sophToken, uint256 _rewardRate) {
        require(_spToken != address(0), "Invalid SP token address");
        require(_sophToken != address(0), "Invalid SOPH token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        spToken = _spToken;
        sophToken = _sophToken;
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
        accRewardPerShare = 0;
    }

    // Modifier to update pool before any major action
    modifier updatePool() {
        if (block.timestamp > lastRewardTime && totalStaked > 0) {
            uint256 timeDiff = block.timestamp - lastRewardTime;
            uint256 reward = timeDiff * rewardRate;
            accRewardPerShare += (reward * 1e12) / totalStaked;
            lastRewardTime = block.timestamp;
        }
        _;
    }

    /**
     * @dev Deposit tokens to start farming.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) external updatePool {
        require(_amount > 0, "Deposit amount must be greater than 0");

        UserInfo storage user = users[msg.sender];

        // Transfer SP tokens from user to contract
        IERC20(spToken).transferFrom(msg.sender, address(this), _amount);

        // Distribute pending rewards
        if (user.amount > 0) {
            uint256 pendingReward = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pendingReward > 0) {
                IERC20(sophToken).transfer(msg.sender, pendingReward);
                emit ClaimReward(msg.sender, pendingReward);
            }
        }

        // Update user state
        user.amount += _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        // Update total staked
        totalStaked += _amount;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Withdraw tokens from the farming pool.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updatePool {
        UserInfo storage user = users[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds staked amount");

        // Distribute pending rewards
        uint256 pendingReward = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pendingReward > 0) {
            IERC20(sophToken).transfer(msg.sender, pendingReward);
            emit ClaimReward(msg.sender, pendingReward);
        }

        // Transfer SP tokens back to the user
        IERC20(spToken).transfer(msg.sender, _amount);

        // Update user state
        user.amount -= _amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;

        // Update total staked
        totalStaked -= _amount;

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev View function to see pending rewards for a user.
     * @param _user Address of the user to query.
     * @return Pending reward amount.
     */
    function pendingReward(address _user) external view returns (uint256) {
        UserInfo storage user = users[_user];
        uint256 _accRewardPerShare = accRewardPerShare;
        if (block.timestamp > lastRewardTime && totalStaked > 0) {
            uint256 timeDiff = block.timestamp - lastRewardTime;
            uint256 reward = timeDiff * rewardRate;
            _accRewardPerShare += (reward * 1e12) / totalStaked;
        }
        return (user.amount * _accRewardPerShare) / 1e12 - user.rewardDebt;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
