"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visualprocurator.pages.dev
Prompt: Provide an example of using Multichain's veMULTI governance token in a staking contract, including reward claiming functionality.
Generated: DETERMINISTIC_8c2c380932f85ae8
Batch ID: 20250612_151117
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
 * @title veMULTI Staking Contract
 * @dev This contract allows users to stake veMULTI tokens and claim rewards.
 */
contract veMULTIStaking {
    // Interfaces for the veMULTI token and the reward token
    IERC20 public veMULTI;
    IERC20 public rewardToken;

    // Total amount of veMULTI staked in the contract
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Data structure to track user balances and rewards
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    // Mapping to store staker information
    mapping(address => Staker) public stakers;

    // Last block number when rewards were distributed
    uint256 public lastRewardBlock;

    // Accumulated rewards per veMULTI token staked (scaled by 1e18 for precision)
    uint256 public accRewardPerToken;

    // Event declarations
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event ClaimReward(address indexed user, uint256 reward);

    /**
     * @param _veMULTI Address of the veMULTI token contract
     * @param _rewardToken Address of the reward token contract
     * @param _rewardRate Rewards per block
     */
    constructor(
        IERC20 _veMULTI,
        IERC20 _rewardToken,
        uint256 _rewardRate
    ) {
        veMULTI = _veMULTI;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Updates the reward variables to be current up to this block.
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocks = block.number - lastRewardBlock;
        uint256 reward = blocks * rewardRate;

        accRewardPerToken += (reward * 1e18) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Allows a user to stake veMULTI tokens.
     * @param amount Amount of veMULTI tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update rewards before changing state
        updateRewards();

        // Transfer veMULTI tokens to the contract
        require(veMULTI.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's staked amount and reward debt
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.rewardDebt += (amount * accRewardPerToken) / 1e18;

        // Update total staked
        totalStaked += amount;

        emit Stake(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake veMULTI tokens.
     * @param amount Amount of veMULTI tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        // Update rewards before changing state
        updateRewards();

        // Calculate pending rewards
        uint256 pendingReward = ((staker.stakedAmount * accRewardPerToken) / 1e18) - staker.rewardDebt;

        // Update user's staked amount and reward debt
        staker.stakedAmount -= amount;
        staker.rewardDebt = (staker.stakedAmount * accRewardPerToken) / 1e18;

        // Update total staked
        totalStaked -= amount;

        // Transfer veMULTI tokens back to the user
        require(veMULTI.transfer(msg.sender, amount), "Transfer failed");

        // Transfer pending rewards
        if (pendingReward > 0) {
            require(rewardToken.transfer(msg.sender, pendingReward), "Reward transfer failed");
        }

        emit Unstake(msg.sender, amount);
        emit ClaimReward(msg.sender, pendingReward);
    }

    /**
     * @dev Allows a user to claim rewards without unstaking.
     */
    function claimRewards() external {
        // Update rewards before changing state
        updateRewards();

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards
        uint256 pendingReward = ((staker.stakedAmount * accRewardPerToken) / 1e18) - staker.rewardDebt;

        require(pendingReward > 0, "No rewards available");

        // Update reward debt
        staker.rewardDebt = (staker.stakedAmount * accRewardPerToken) / 1e18;

        // Transfer pending rewards
        require(rewardToken.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit ClaimReward(msg.sender, pendingReward);
    }

    /**
     * @dev Emergency function to allow the owner to withdraw tokens in case of issues.
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
