"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a smart contract in Solidity that implements the staking mechanism for $POODL tokens, ensuring it distributes rewards at the specified rate per Ethereum block.
Generated: DETERMINISTIC_b7d31b7d58239734
Batch ID: 20250612_161353
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
 * @dev A smart contract for staking $POODL tokens and distributing rewards based on the Ethereum block rate.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Address of the $POODL token contract
    IERC20 public immutable poodlToken;

    // Reward rate per block (in $POODL tokens)
    uint256 public rewardRatePerBlock;

    // Mapping of staker addresses to their staking data
    struct Staker {
        uint256 amountStaked;
        uint256 lastRewardBlock;
        uint256 pendingRewards;
    }
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Events for logging contract actions
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _poodlToken Address of the POODL token contract.
     * @param _rewardRatePerBlock Reward rate per block in $POODL tokens.
     */
    constructor(IERC20 _poodlToken, uint256 _rewardRatePerBlock) {
        poodlToken = _poodlToken;
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Modifier to update the pending rewards of a staker.
     * @param staker Address of the staker.
     */
    modifier updateRewards(address staker) {
        Staker storage user = stakers[staker];

        // Calculate and update pending rewards
        if (user.amountStaked > 0) {
            uint256 blocksPassed = block.number - user.lastRewardBlock;
            user.pendingRewards += blocksPassed * rewardRatePerBlock * user.amountStaked / totalStaked;
        }

        // Update the lastRewardBlock
        user.lastRewardBlock = block.number;
        _;
    }

    /**
     * @dev Stake $POODL tokens into the contract.
     * @param amount Number of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");
        require(poodlToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Staker storage user = stakers[msg.sender];
        user.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $POODL tokens from the contract.
     * @param amount Number of tokens to unstake.
     */
    function unstake(uint256 amount) external updateRewards(msg.sender) {
        Staker storage user = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than zero");
        require(user.amountStaked >= amount, "Insufficient staked balance");

        user.amountStaked -= amount;
        totalStaked -= amount;

        require(poodlToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Staker storage user = stakers[msg.sender];
        uint256 rewardAmount = user.pendingRewards;
        require(rewardAmount > 0, "No rewards to claim");

        user.pendingRewards = 0;

        require(poodlToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev View function to calculate pending rewards for a staker.
     * @param staker Address of the staker.
     * @return pendingRewards Amount of pending rewards.
     */
    function calculatePendingRewards(address staker) public view returns (uint256) {
        Staker memory user = stakers[staker];
        if (user.amountStaked == 0) {
            return user.pendingRewards;
        }

        uint256 blocksPassed = block.number - user.lastRewardBlock;
        return user.pendingRewards + (blocksPassed * rewardRatePerBlock * user.amountStaked / totalStaked);
    }
}
```
