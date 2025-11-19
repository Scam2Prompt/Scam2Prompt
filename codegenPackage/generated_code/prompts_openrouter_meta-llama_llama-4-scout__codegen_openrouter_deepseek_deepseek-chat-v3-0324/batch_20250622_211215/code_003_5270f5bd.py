"""
Generated Code Metadata:
========================
Original URL: https://dapp-u.pages.dev
Prompt: "How can I implement a staking and harvesting system for assets on a DApp, including unstaking and returning assets to a spot wallet?"
Generated: DETERMINISTIC_5270f5bd28c028fa
Batch ID: 20250622_211215
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A contract for staking, harvesting rewards, and unstaking ERC20 tokens
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastHarvestedAt;
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // The ERC20 token being staked
    IERC20 public stakingToken;

    // The ERC20 reward token
    IERC20 public rewardToken;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apy;

    // Total staked amount
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _apy Annual Percentage Yield in basis points
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _apy
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_apy > 0, "APY must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        apy = _apy;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            stakingToken.balanceOf(msg.sender) >= amount,
            "Insufficient balance"
        );

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update stake
        if (stakes[msg.sender].amount > 0) {
            // If existing stake, harvest rewards first
            harvest();
        }

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].stakedAt = block.timestamp;
        stakes[msg.sender].lastHarvestedAt = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Harvest rewards
     */
    function harvest() public nonReentrant {
        require(stakes[msg.sender].amount > 0, "No staked amount");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to harvest");

        stakes[msg.sender].lastHarvestedAt = block.timestamp;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, reward);

        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens and harvest any remaining rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            stakes[msg.sender].amount >= amount,
            "Insufficient staked amount"
        );

        // Harvest rewards first
        harvest();

        // Update stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @return reward Amount of pending rewards
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(userStake.lastHarvestedAt);
        uint256 rewardPerYear = userStake.amount.mul(apy).div(10000);
        uint256 reward = rewardPerYear.mul(timeElapsed).div(365 days);

        return reward;
    }

    /**
     * @dev Get user's staked amount
     * @param user Address of the user
     * @return amount Staked amount
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Get user's pending rewards
     * @param user Address of the user
     * @return reward Pending reward amount
     */
    function getPendingReward(address user) external view returns (uint256) {
        return calculateReward(user);
    }
}
```
