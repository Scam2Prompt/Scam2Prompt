"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherfi-app.github.io
Prompt: Generate a Solidity contract for a yield farming system that distributes rewards based on liquidity contributions, inspired by Ether Fi's staking and farming features.
Generated: DETERMINISTIC_1727d35989f33c54
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract YieldFarming is Ownable {
    using SafeMath for uint256;

    // Structure to hold user info
    struct UserInfo {
        uint256 amount; // Amount of tokens contributed by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Token to be used for farming
    IERC20 public stakingToken;
    // Token to be distributed as rewards
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;
    // Reward per share
    uint256 public accRewardPerShare;
    // Total rewards distributed
    uint256 public totalRewards;

    // Mapping of user info
    mapping(address => UserInfo) public userInfo;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
    }

    /**
     * @dev Update reward variables
     */
    function updateReward() internal {
        if (totalStaked == 0) {
            return;
        }

        // Calculate new reward per share
        uint256 reward = calculateReward(); // Implement your logic to fetch new rewards
        totalRewards = totalRewards.add(reward);
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked)); // 1e12 for precision
    }

    /**
     * @dev Stake tokens to the yield farming contract
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        updateReward();

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            // Pay pending rewards
            uint256 pending = user.amount.mul(accRewardPerShare).div(1e12).sub(user.rewardDebt);
            if (pending > 0) {
                rewardToken.transfer(msg.sender, pending);
                emit RewardDistributed(msg.sender, pending);
            }
        }

        // Transfer staking tokens
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the yield farming contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than 0");
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds staked amount");

        updateReward();

        // Pay pending rewards
        uint256 pending = user.amount.mul(accRewardPerShare).div(1e12).sub(user.rewardDebt);
        if (pending > 0) {
            rewardToken.transfer(msg.sender, pending);
            emit RewardDistributed(msg.sender, pending);
        }

        // Update user and total staked
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.sub(_amount);
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Calculate the new reward amount (dummy implementation)
     * @return uint256 Amount of new rewards to be distributed
     */
    function calculateReward() internal view returns (uint256) {
        // Implement your reward logic here
        return 0; // Placeholder: modify to return actual reward amount
    }

    /**
     * @dev Emergency withdrawal function for users to withdraw their staked tokens
     */
    function emergencyWithdraw() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "No tokens to withdraw");

        // Reset user info
        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked = totalStaked.sub(amount);

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, amount);
    }
}
```
