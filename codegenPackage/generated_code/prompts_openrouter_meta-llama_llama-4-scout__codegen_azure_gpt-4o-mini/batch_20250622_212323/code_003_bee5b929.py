"""
Generated Code Metadata:
========================
Original URL: https://aria.fyi
Prompt: Develop a staking system for the Aria token, incorporating the information from the Arianee Protocol's FAQ and tokenomics.
Generated: DETERMINISTIC_bee5b929df2ce0ce
Batch ID: 20250622_212323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A staking contract for the Aria token, allowing users to stake their tokens and earn rewards.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // The Aria token contract
    IERC20 public ariaToken;

    // Staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in percentage) per year
    uint256 public rewardRate = 10; // 10% annual reward

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the Aria token address.
     * @param _ariaToken Address of the Aria token contract.
     */
    constructor(address _ariaToken) {
        require(_ariaToken != address(0), "Invalid token address");
        ariaToken = IERC20(_ariaToken);
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(ariaToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        ariaToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate and pay rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            ariaToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to user
        ariaToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Calculate the reward for a user based on their stake.
     * @param user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 reward = userStake.amount.mul(rewardRate).mul(stakingDuration).div(365 days).div(100);
        return reward;
    }

    /**
     * @dev Update the reward rate. Only owner can call this function.
     * @param newRate New reward rate in percentage.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRate;
    }

    /**
     * @dev Withdraw tokens in case of emergency. Only owner can call this function.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= ariaToken.balanceOf(address(this)), "Insufficient contract balance");
        ariaToken.transfer(msg.sender, amount);
    }
}
```
