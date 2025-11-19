"""
Generated Code Metadata:
========================
Original URL: https://kenduinu-an.web.app
Prompt: Write a smart contract in Solidity for staking $KENDU tokens as described in the Kendu Inu ecosystem, ensuring users can lock their tokens for rewards and withdraw them after a specified period.
Generated: DETERMINISTIC_37c08c563ab22756
Batch ID: 20250612_153812
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title KENDU Staking Contract
 * @dev Allows users to stake KENDU tokens and earn rewards
 */
contract KenduStaking is Ownable, ReentrancyGuard {
    IERC20 public kenduToken;

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lockPeriod;
        uint256 rewardRate;
        bool withdrawn;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public userStakes;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rates (percentage per second) for different lock periods
    uint256 public constant SHORT_TERM_RATE = 1; // 0.0001% per second (~31.5% APR)
    uint256 public constant MEDIUM_TERM_RATE = 2; // 0.0002% per second (~63% APR)
    uint256 public constant LONG_TERM_RATE = 3; // 0.0003% per second (~94.5% APR)

    // Lock periods in seconds
    uint256 public constant SHORT_TERM = 30 days;
    uint256 public constant MEDIUM_TERM = 90 days;
    uint256 public constant LONG_TERM = 180 days;

    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Withdrawn(address indexed user, uint256 stakeIndex, uint256 amount, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 stakeIndex, uint256 amount);

    /**
     * @dev Constructor
     * @param _kenduToken Address of the KENDU token contract
     */
    constructor(address _kenduToken) {
        require(_kenduToken != address(0), "KENDU token address cannot be zero");
        kenduToken = IERC20(_kenduToken);
    }

    /**
     * @dev Stake KENDU tokens
     * @param amount Amount of tokens to stake
     * @param lockPeriodIndex 0 = short, 1 = medium, 2 = long term
     */
    function stake(uint256 amount, uint256 lockPeriodIndex) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(lockPeriodIndex < 3, "Invalid lock period");

        uint256 lockPeriod;
        uint256 rewardRate;

        if (lockPeriodIndex == 0) {
            lockPeriod = SHORT_TERM;
            rewardRate = SHORT_TERM_RATE;
        } else if (lockPeriodIndex == 1) {
            lockPeriod = MEDIUM_TERM;
            rewardRate = MEDIUM_TERM_RATE;
        } else {
            lockPeriod = LONG_TERM;
            rewardRate = LONG_TERM_RATE;
        }

        // Transfer tokens from user to contract
        require(
            kenduToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        userStakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            lockPeriod: lockPeriod,
            rewardRate: rewardRate,
            withdrawn: false
        }));

        totalStaked += amount;

        emit Staked(msg.sender, amount, lockPeriod);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param stakeIndex Index of the stake to withdraw
     */
    function withdraw(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(!userStake.withdrawn, "Already withdrawn");
        require(
            block.timestamp >= userStake.startTime + userStake.lockPeriod,
            "Lock period not ended"
        );

        uint256 reward = calculateReward(msg.sender, stakeIndex);
        uint256 totalAmount = userStake.amount + reward;

        userStake.withdrawn = true;
        totalStaked -= userStake.amount;

        require(
            kenduToken.transfer(msg.sender, totalAmount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, stakeIndex, userStake.amount, reward);
    }

    /**
     * @dev Emergency withdraw without rewards (penalty)
     * @param stakeIndex Index of the stake to withdraw
     */
    function emergencyWithdraw(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(!userStake.withdrawn, "Already withdrawn");

        userStake.withdrawn = true;
        totalStaked -= userStake.amount;

        // Only return 90% of staked amount as penalty
        uint256 penaltyAmount = (userStake.amount * 90) / 100;

        require(
            kenduToken.transfer(msg.sender, penaltyAmount),
            "Token transfer failed"
        );

        emit EmergencyWithdraw(msg.sender, stakeIndex, penaltyAmount);
    }

    /**
     * @dev Calculate reward for a stake
     * @param user Address of the user
     * @param stakeIndex Index of the stake
     * @return reward Calculated reward amount
     */
    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");

        Stake memory userStake = userStakes[user][stakeIndex];
        if (userStake.withdrawn) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        if (stakingDuration > userStake.lockPeriod) {
            stakingDuration = userStake.lockPeriod;
        }

        // reward = amount * rate * duration / 1,000,000 (rate is per million)
        return (userStake.amount * userStake.rewardRate * stakingDuration) / 1_000_000;
    }

    /**
     * @dev Get all stakes for a user
     * @param user Address of the user
     * @return Array of user's stakes
     */
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return userStakes[user];
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(kenduToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
