"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-live.web.app
Prompt: Create a Solidity smart contract snippet that allows users to stake $KANG tokens and earn rewards based on their participation in the Kangamoon community.
Generated: DETERMINISTIC_70f722eb5a95ee88
Batch ID: 20250612_162854
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

/**
 * @title KangamoonStaking
 * @notice This contract allows users to stake $KANG tokens and earn rewards.
 */
contract KangamoonStaking is Ownable {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public kangToken;

    // Reward rate per block (in wei)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // User staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes;

    // Events for staking and rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @param _kangToken Address of the $KANG token contract
     * @param _rewardRate Reward rate per block
     */
    constructor(IERC20 _kangToken, uint256 _rewardRate) {
        kangToken = _kangToken;
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake tokens to earn rewards.
     * @param amount Amount of $KANG tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update user's stake
        _updateReward(msg.sender);

        // Transfer tokens from user to contract
        kangToken.transferFrom(msg.sender, address(this), amount);

        // Update total staked and user stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards.
     * @param amount Amount of $KANG tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's reward before unstaking
        _updateReward(msg.sender);

        // Transfer tokens back to user
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        kangToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards.
     */
    function claimRewards() external {
        _updateReward(msg.sender);
    }

    /**
     * @notice Update the user's rewards.
     * @param user Address of the user
     */
    function _updateReward(address user) internal {
        Stake storage userStake = stakes[user];

        // Calculate pending rewards
        uint256 pendingRewards = userStake.amount.mul(rewardRate).div(1e18).sub(userStake.rewardDebt);

        // Pay the rewards if there are any
        if (pendingRewards > 0) {
            // Transfer rewards to user
            // Assuming rewards are paid in $KANG tokens
            kangToken.transfer(user, pendingRewards);
            emit RewardClaimed(user, pendingRewards);
        }

        // Update user's reward debt
        userStake.rewardDebt = userStake.amount.mul(rewardRate).div(1e18);
    }

    /**
     * @notice Admin function to set reward rate.
     * @param newRewardRate New reward rate per block
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
