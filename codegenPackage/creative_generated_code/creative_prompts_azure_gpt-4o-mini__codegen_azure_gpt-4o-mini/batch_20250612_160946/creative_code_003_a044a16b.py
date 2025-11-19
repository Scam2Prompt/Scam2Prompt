"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Develop a Solidity contract that allows users to stake Super Trump Coin and earn rewards based on the tokenomics outlined on the website.
Generated: DETERMINISTIC_a044a16bc3057823
Batch ID: 20250612_160946
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SuperTrumpStaking
 * @dev A contract that allows users to stake Super Trump Coin (STC) and earn rewards based on staking duration.
 */
contract SuperTrumpStaking is Ownable {
    // Declare variables for the staking contract
    IERC20 public stcToken; // The Super Trump Coin token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount staked
    uint256 public totalRewards; // Total rewards distributed

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount of STC staked
        uint256 rewardDebt; // Reward debt to calculate rewards
        uint256 lastStakedTime; // Last time the user staked
    }

    mapping(address => Staker) public stakers; // Mapping of stakers

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the STC token and reward rate.
     * @param _stcToken The address of the Super Trump Coin (STC) token.
     * @param _rewardRate The reward rate per second.
     */
    constructor(IERC20 _stcToken, uint256 _rewardRate) {
        stcToken = _stcToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake STC tokens.
     * @param _amount The amount of STC tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        require(stcToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update total staked
        totalStaked += _amount;

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.rewardDebt += calculateReward(msg.sender);
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake STC tokens and claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        require(stcToken.transfer(msg.sender, staker.amount), "Transfer failed");
        
        // Update total staked and staker information
        totalStaked -= staker.amount;
        totalRewards += reward;
        delete stakers[msg.sender];

        emit Unstaked(msg.sender, staker.amount);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to calculate the rewards for a staker.
     * @param _staker The address of the staker.
     * @return The calculated rewards.
     */
    function calculateReward(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        return (block.timestamp - staker.lastStakedTime) * rewardRate * staker.amount / 1e18;
    }

    /**
     * @dev Function to withdraw earned rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        // Update reward debt and transfer rewards
        staker.rewardDebt += reward;
        require(stcToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to withdraw contract balance in case of emergency.
     * Only accessible by the contract owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stcToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(stcToken.transfer(owner(), balance), "Transfer failed");
    }

    /**
     * @dev Function to set new reward rate.
     * Only accessible by the contract owner.
     * @param _newRewardRate The new reward rate per second.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
