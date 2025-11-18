"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.tech
Prompt: Write a Solidity smart contract to implement a staking mechanism similar to LooksRare, where users can stake tokens and earn rewards in both the staked token and a share of platform fees.
Generated: DETERMINISTIC_c4d65d4f7eacbc2c
Batch ID: 20250612_145121
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
 * @title StakingContract
 * @dev A staking contract that allows users to stake tokens and earn rewards.
 * Rewards are distributed as the staked token and a share of the platform fees.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    IERC20 public stakingToken; // Token to be staked
    IERC20 public rewardToken;  // Token used for platform fee rewards

    uint256 public totalStaked; // Total staked balance
    uint256 public rewardPool;  // Total reward token pool
    uint256 public feePool;     // Total platform fee pool (in rewardToken)

    uint256 public rewardRate;  // Reward rate for staked tokens (rewardToken per block)
    uint256 public feeRate;     // Fee distribution rate (rewardToken per block)

    struct Stake {
        uint256 amount;          // Amount of staked tokens
        uint256 rewardDebt;      // Reward debt for the staked token rewards
        uint256 feeDebt;         // Reward debt for the platform fee rewards
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 stakingReward, uint256 feeReward);
    event RewardsAdded(uint256 amount);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _feeRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        feeRate = _feeRate;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);
        userStake.amount += amount;
        userStake.rewardDebt = (userStake.amount * rewardRate) / 1e18;
        userStake.feeDebt = (userStake.amount * feeRate) / 1e18;

        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        _updateRewards(msg.sender);
        userStake.amount -= amount;
        userStake.rewardDebt = (userStake.amount * rewardRate) / 1e18;
        userStake.feeDebt = (userStake.amount * feeRate) / 1e18;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking and fee rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 stakingReward = (userStake.amount * rewardRate) / 1e18 - userStake.rewardDebt;
        uint256 feeReward = (userStake.amount * feeRate) / 1e18 - userStake.feeDebt;

        require(stakingReward > 0 || feeReward > 0, "No rewards available");

        if (stakingReward > 0) {
            rewardPool -= stakingReward;
            rewardToken.transfer(msg.sender, stakingReward);
        }

        if (feeReward > 0) {
            feePool -= feeReward;
            rewardToken.transfer(msg.sender, feeReward);
        }

        userStake.rewardDebt += stakingReward;
        userStake.feeDebt += feeReward;

        emit RewardsClaimed(msg.sender, stakingReward, feeReward);
    }

    /**
     * @dev Add reward tokens to the pool.
     * @param amount Amount of tokens to add to the reward pool.
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        rewardToken.transferFrom(msg.sender, address(this), amount);
        rewardPool += amount;

        emit RewardsAdded(amount);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 stakingReward = (userStake.amount * rewardRate) / 1e18 - userStake.rewardDebt;
            uint256 feeReward = (userStake.amount * feeRate) / 1e18 - userStake.feeDebt;

            rewardPool -= stakingReward;
            feePool -= feeReward;

            userStake.rewardDebt += stakingReward;
            userStake.feeDebt += feeReward;
        }
    }
}
```
