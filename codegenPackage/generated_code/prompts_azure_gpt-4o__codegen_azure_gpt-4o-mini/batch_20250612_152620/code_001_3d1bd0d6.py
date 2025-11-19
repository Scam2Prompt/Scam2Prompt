"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-en.web.app
Prompt: Create a Solidity smart contract that implements a staking mechanism similar to InQubeta's $QUBE staking system, where rewards are distributed from a sell tax pool.
Generated: DETERMINISTIC_3d1bd0d6a3c173be
Batch ID: 20250612_152620
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

contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;
    // Token used for rewards
    IERC20 public rewardToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;
    // Total rewards distributed
    uint256 public totalRewards;

    // Sell tax percentage (in basis points, e.g., 500 = 5%)
    uint256 public sellTaxPercentage;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _sellTaxPercentage) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        sellTaxPercentage = _sellTaxPercentage;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update total staked and user's staked amount
        totalStaked = totalStaked.add(amount);
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update total staked and user's staked amount
        totalStaked = totalStaked.sub(amount);
        staker.amountStaked = staker.amountStaked.sub(amount);

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards from the sell tax pool
    function distributeRewards(uint256 totalSellTax) external onlyOwner {
        require(totalSellTax > 0, "Total sell tax must be greater than 0");
        uint256 rewardPerToken = totalSellTax.mul(1e18).div(totalStaked);

        for (address stakerAddress : getAllStakers()) {
            Staker storage staker = stakers[stakerAddress];
            if (staker.amountStaked > 0) {
                uint256 pendingReward = staker.amountStaked.mul(rewardPerToken).div(1e18);
                staker.rewardDebt = staker.rewardDebt.add(pendingReward);
            }
        }
        totalRewards = totalRewards.add(totalSellTax);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;

        require(reward > 0, "No rewards to claim");

        staker.rewardDebt = 0;
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to get all stakers (for reward distribution)
    function getAllStakers() internal view returns (address[] memory) {
        // This function should return the list of all stakers
        // Implementation depends on how you want to track stakers
    }
}
```
