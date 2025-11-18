"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claiming.pages.dev
Prompt: Generate code to integrate DOGE20 token staking functionality into a decentralized wallet, ensuring compatibility with the ERC-20 standard.
Generated: DETERMINISTIC_c84f9a36a8368111
Batch ID: 20250612_153420
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
 * @title DOGE20 Token Staking Contract
 * @dev This contract allows users to stake ERC-20 tokens (DOGE20) and earn rewards.
 * It assumes compatibility with the ERC-20 standard for DOGE20 tokens.
 */
 
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract DOGE20Staking {
    IERC20 public immutable doge20Token; // DOGE20 Token contract address
    uint256 public rewardRate; // Reward rate per second per token
    uint256 public totalStaked; // Total tokens staked in the contract

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Accumulated rewards debt
        uint256 lastStakedTime; // Timestamp of the last staking
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user addresses to staking info

    event Stake(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event ClaimRewards(address indexed user, uint256 amount);

    modifier updateRewards(address _user) {
        if (stakes[_user].amount > 0) {
            uint256 pendingRewards = calculateRewards(_user);
            stakes[_user].rewardDebt += pendingRewards;
        }
        stakes[_user].lastStakedTime = block.timestamp;
        _;
    }

    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake DOGE20 tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");

        doge20Token.transferFrom(msg.sender, address(this), _amount);
        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked DOGE20 tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        doge20Token.transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = stakes[msg.sender].rewardDebt;
        require(rewards > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0;

        doge20Token.transfer(msg.sender, rewards);

        emit ClaimRewards(msg.sender, rewards);
    }

    /**
     * @dev Calculates pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        StakeInfo memory stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }

        uint256 stakingTime = block.timestamp - stake.lastStakedTime;
        return (stakingTime * stake.amount * rewardRate) / 1 ether; // Scale by 1 ether for precision
    }

    /**
     * @dev Returns the total staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance.
     */
    function stakedBalance(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    /**
     * @dev Sets a new reward rate (only owner).
     * @param _newRewardRate New reward rate in tokens per second.
     */
    function setRewardRate(uint256 _newRewardRate) external {
        require(_newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRewardRate;
    }
}
```
