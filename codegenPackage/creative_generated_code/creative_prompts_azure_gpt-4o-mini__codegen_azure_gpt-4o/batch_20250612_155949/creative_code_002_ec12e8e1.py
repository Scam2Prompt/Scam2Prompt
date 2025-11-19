"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Create a Solidity smart contract for staking $MEMEX tokens and earning rewards.
Generated: DETERMINISTIC_ec12e8e1ba9916e1
Batch ID: 20250612_155949
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
 * @title MEMEX Staking Contract
 * @dev A smart contract for staking MEMEX tokens and earning rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MEMEXStaking {
    // State variables
    IERC20 public immutable memexToken; // MEMEX token contract
    address public owner;                // Contract owner
    uint256 public rewardRate;           // Reward rate (tokens per block)
    uint256 public totalStaked;          // Total amount of tokens staked

    struct Stake {
        uint256 amount;                  // Amount of tokens staked by a user
        uint256 rewardDebt;              // Reward debt (used for reward calculation)
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    constructor(IERC20 _memexToken, uint256 _rewardRate) {
        memexToken = _memexToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Updates the reward rate. Can only be called by the owner.
     * @param _newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Allows a user to stake MEMEX tokens. The user must approve the contract beforehand.
     * @param _amount The amount of MEMEX tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer MEMEX tokens from user to contract
        require(memexToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = _calculatePendingReward(msg.sender);
        userStake.rewardDebt += pendingReward; // Update reward debt
        userStake.amount += _amount;          // Update staked amount
        totalStaked += _amount;               // Update total staked

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked MEMEX tokens.
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(_amount > 0, "Amount must be greater than 0");
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update staking information
        uint256 pendingReward = _calculatePendingReward(msg.sender);
        userStake.rewardDebt += pendingReward; // Update reward debt
        userStake.amount -= _amount;          // Decrease staked amount
        totalStaked -= _amount;               // Update total staked

        // Transfer tokens back to user
        require(memexToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim their rewards.
     */
    function claimReward() external {
        uint256 reward = _calculatePendingReward(msg.sender) + stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer reward tokens to user
        require(memexToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user The address of the user.
     * @return The pending reward amount.
     */
    function _calculatePendingReward(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount * rewardRate);
    }

    /**
     * @dev Emergency owner function to withdraw all tokens from the contract.
     * @notice This should only be used if there is an issue with the contract logic.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = memexToken.balanceOf(address(this));
        require(memexToken.transfer(owner, contractBalance), "Token transfer failed");
    }
}
```
