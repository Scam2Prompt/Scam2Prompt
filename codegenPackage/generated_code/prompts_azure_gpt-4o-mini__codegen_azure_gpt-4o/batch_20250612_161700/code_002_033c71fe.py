"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a Solidity contract that allows users to stake their $MGLS tokens and earn rewards based on their share of the staking pool.
Generated: DETERMINISTIC_033c71fe902a85d2
Batch ID: 20250612_161700
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

/**
 * @title StakingContract
 * @dev A contract that allows users to stake $MGLS tokens and earn rewards based on their share of the staking pool.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Address of the $MGLS token contract
    IERC20 public immutable mglsToken;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Reward rate per token staked (e.g., 1 reward token per block per staked token)
    uint256 public rewardRate;

    // Last block number when rewards were calculated
    uint256 public lastRewardBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $MGLS token address and reward rate.
     * @param _mglsToken Address of the $MGLS token contract.
     * @param _rewardRate Reward rate per token staked per block.
     */
    constructor(IERC20 _mglsToken, uint256 _rewardRate) {
        mglsToken = _mglsToken;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Modifier to update rewards for all stakers before executing a function.
     */
    modifier updateRewards() {
        _updateRewards();
        _;
    }

    /**
     * @dev Internal function to update rewards for all stakers.
     */
    function _updateRewards() internal {
        if (totalStaked > 0) {
            uint256 blocksPassed = block.number - lastRewardBlock;
            uint256 totalRewards = blocksPassed * rewardRate * totalStaked;

            // Distribute rewards proportionally to stakers
            for (address staker : _getAllStakers()) {
                uint256 userShare = stakedBalances[staker] / totalStaked;
                rewardBalances[staker] += userShare * totalRewards;
            }
        }
        lastRewardBlock = block.number;
    }

    /**
     * @dev Function to stake $MGLS tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot stake 0 tokens");

        // Transfer tokens from the user to the contract
        require(mglsToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(mglsToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to claim earned rewards.
     */
    function claimRewards() external updateRewards {
        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to the user
        require(mglsToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to get the staked balance of a user.
     * @param user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Function to get the reward balance of a user.
     * @param user Address of the user.
     * @return Reward balance of the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
