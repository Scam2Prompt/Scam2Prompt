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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title KenduInuStakingContract
 * @author [Your Name]
 * @notice A staking contract for $KENDU tokens, allowing users to lock their tokens for rewards and withdraw them after a specified period.
 */
contract KenduInuStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates for different staking periods
    mapping(uint256 => RewardRate) public rewardRates;

    // $KENDU token contract
    IERC20 public kenduToken;

    // Minimum staking amount
    uint256 public minStakingAmount;

    // Maximum staking amount
    uint256 public maxStakingAmount;

    // Staking period in seconds
    uint256 public stakingPeriod;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Event emitted when a user stakes $KENDU tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked $KENDU tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _kenduToken $KENDU token contract address
     * @param _minStakingAmount Minimum staking amount
     * @param _maxStakingAmount Maximum staking amount
     * @param _stakingPeriod Staking period in seconds
     */
    constructor(
        address _kenduToken,
        uint256 _minStakingAmount,
        uint256 _maxStakingAmount,
        uint256 _stakingPeriod
    ) public {
        kenduToken = IERC20(_kenduToken);
        minStakingAmount = _minStakingAmount;
        maxStakingAmount = _maxStakingAmount;
        stakingPeriod = _stakingPeriod;

        // Initialize reward rates for different staking periods
        rewardRates[30 days] = RewardRate(10, 100); // 10% APY for 30 days
        rewardRates[60 days] = RewardRate(20, 100); // 20% APY for 60 days
        rewardRates[90 days] = RewardRate(30, 100); // 30% APY for 90 days
    }

    /**
     * @dev Stake $KENDU tokens for a specified period
     * @param _amount Amount of $KENDU tokens to stake
     * @param _period Staking period in seconds
     */
    function stake(uint256 _amount, uint256 _period) public nonReentrant {
        require(_amount >= minStakingAmount, "Staking amount is less than the minimum");
        require(_amount <= maxStakingAmount, "Staking amount exceeds the maximum");
        require(rewardRates[_period].rate > 0, "Invalid staking period");

        // Transfer $KENDU tokens to the contract
        kenduToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = _amount;
        userStakingInfos[msg.sender].stakingPeriod = _period;
        userStakingInfos[msg.sender].stakedAt = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $KENDU tokens after the specified period
     */
    function withdraw() public nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked tokens");
        require(block.timestamp >= userStakingInfos[msg.sender].stakedAt.add(userStakingInfos[msg.sender].stakingPeriod), "Staking period not over");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked $KENDU tokens and rewards to the user
        kenduToken.safeTransfer(msg.sender, userStakingInfos[msg.sender].stakedAmount.add(rewards));

        // Reset user's staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakingPeriod = 0;
        userStakingInfos[msg.sender].stakedAt = 0;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(userStakingInfos[msg.sender].stakedAmount);

        emit Withdrawn(msg.sender, userStakingInfos[msg.sender].stakedAmount.add(rewards));
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked tokens");
        require(block.timestamp >= userStakingInfos[msg.sender].stakedAt.add(userStakingInfos[msg.sender].stakingPeriod), "Staking period not over");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer rewards to the user
        kenduToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakingPeriod = userStakingInfos[_user].stakingPeriod;
        uint256 stakedAmount = userStakingInfos[_user].stakedAmount;
        RewardRate memory rewardRate = rewardRates[stakingPeriod];

        // Calculate rewards
        uint256 rewards = stakedAmount.mul(rewardRate.rate).div(rewardRate.divisor);

        return rewards;
    }

    // Struct for user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingPeriod;
        uint256 stakedAt;
    }

    // Struct for reward rate
    struct RewardRate {
        uint256 rate;
        uint256 divisor;
    }
}
```
