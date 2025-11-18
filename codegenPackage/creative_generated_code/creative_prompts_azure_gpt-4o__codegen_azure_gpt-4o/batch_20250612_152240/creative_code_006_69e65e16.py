"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudverse-opseccomputer.pages.dev
Prompt: Develop a smart contract for "Treasury Staking" that could be used in a system like OpSec CloudVerse.
Generated: DETERMINISTIC_69e65e16249c2b72
Batch ID: 20250612_152240
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
 * @title TreasuryStaking
 * @dev A smart contract for staking tokens in a treasury system.
 * Users can stake tokens, earn rewards, and withdraw their stakes and rewards.
 */
contract TreasuryStaking {
    // State variables
    address public owner; // Contract owner address
    uint256 public rewardRate; // Reward rate (percentage per block or per time unit)
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards pending withdrawal
        uint256 lastUpdated; // Last update timestamp for the stake
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    mapping(address => bool) public authorizedTokens; // Tokens allowed for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event TokenAuthorized(address indexed token, bool isAuthorized);
    event RewardRateUpdated(uint256 newRate);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract owner and reward rate.
     * @param _rewardRate Initial reward rate
     */
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the treasury.
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");

        Stake storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);

        userStake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the treasury.
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked balance");

        _updateRewards(msg.sender);

        userStake.amount -= _amount;
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards from staking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);

        uint256 rewardToClaim = userStake.rewardDebt;
        require(rewardToClaim > 0, "No rewards to claim");

        userStake.rewardDebt = 0;

        emit RewardsClaimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Update the reward rate.
     * @param _newRate New reward rate
     */
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Authorize or deauthorize tokens for staking.
     * @param _token Token address
     * @param _isAuthorized Authorization status
     */
    function authorizeToken(address _token, bool _isAuthorized) external onlyOwner {
        authorizedTokens[_token] = _isAuthorized;
        emit TokenAuthorized(_token, _isAuthorized);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user User address
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];

        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 reward = (userStake.amount * timeElapsed * rewardRate) / 1e18;
            userStake.rewardDebt += reward;
        }

        userStake.lastUpdated = block.timestamp;
    }
}
```
