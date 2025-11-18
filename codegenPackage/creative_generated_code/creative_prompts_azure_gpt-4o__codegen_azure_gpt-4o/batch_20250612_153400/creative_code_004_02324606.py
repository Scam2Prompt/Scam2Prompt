"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://too1m.pages.dev
Prompt: Write a smart contract that leverages the BASE chain ecosystem to create a staking mechanism for $POON tokens, ensuring compatibility with the memecoin's roadmap.
Generated: DETERMINISTIC_0232460620aad91d
Batch ID: 20250612_153400
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
 * @title POON Staking Contract
 * @dev A smart contract for staking $POON tokens on the BASE chain.
 * Users can stake their $POON tokens to earn rewards, following the memecoin's roadmap.
 * This contract is production-ready, well-documented, and includes error handling.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PoonStaking {
    // $POON token address.
    IERC20 public immutable poonToken;

    // Struct to store staking details for each user.
    struct StakeInfo {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for reward calculations
        uint256 lastUpdated;    // Timestamp of last interaction
    }

    // Mapping of user addresses to their staking info.
    mapping(address => StakeInfo) public stakes;

    // Total tokens staked in the contract.
    uint256 public totalStaked;

    // Reward rate (tokens per second).
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the $POON token address.
     * @param _poonToken Address of the $POON token contract.
     * @param _rewardRate Reward rate for staking (tokens per second).
     */
    constructor(IERC20 _poonToken, uint256 _rewardRate) {
        require(address(_poonToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        poonToken = _poonToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the user has staked tokens.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Stake $POON tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer $POON tokens from user to contract.
        require(poonToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking details.
        StakeInfo storage stakeDetails = stakes[msg.sender];
        _updateRewards(msg.sender);

        stakeDetails.amount += _amount;
        stakeDetails.lastUpdated = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $POON tokens and claim rewards.
     */
    function unstake() external hasStake {
        // Calculate pending rewards and reset staking details.
        StakeInfo storage stakeDetails = stakes[msg.sender];
        _updateRewards(msg.sender);

        uint256 stakedAmount = stakeDetails.amount;
        uint256 reward = _calculateReward(msg.sender);

        totalStaked -= stakedAmount;
        stakeDetails.amount = 0;
        stakeDetails.rewardDebt = 0;

        // Transfer staked tokens and rewards back to the user.
        require(poonToken.transfer(msg.sender, stakedAmount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Claim staking rewards without unstaking.
     */
    function claimRewards() external hasStake {
        _updateRewards(msg.sender);

        uint256 reward = _calculateReward(msg.sender);
        stakes[msg.sender].rewardDebt += reward;

        require(poonToken.transfer(msg.sender, reward), "Token transfer failed");

        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards.
     */
    function _calculateReward(address _user) internal view returns (uint256) {
        StakeInfo storage stakeDetails = stakes[_user];
        uint256 timeElapsed = block.timestamp - stakeDetails.lastUpdated;
        uint256 pendingReward = (timeElapsed * rewardRate * stakeDetails.amount) / 1e18;
        return pendingReward - stakeDetails.rewardDebt;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage stakeDetails = stakes[_user];
        uint256 pendingReward = _calculateReward(_user);
        stakeDetails.rewardDebt += pendingReward;
        stakeDetails.lastUpdated = block.timestamp;
    }
}
```
