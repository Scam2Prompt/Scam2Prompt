"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the DOGE20 staking mechanism, including features like distributing rewards based on the percentage of the staking pool.
Generated: DETERMINISTIC_092f05adfce60e01
Batch ID: 20250612_152710
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
 * @title DOGE20 Staking Contract
 * @author Expert Programmer
 * @notice This contract allows users to stake DOGE20 tokens and earn proportional rewards.
 */
contract DOGE20Staking {
    // Token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public immutable doge20Token; // DOGE20 token contract address

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => StakeInfo) public stakes; // Mapping of staker addresses to their stake info

    uint256 public totalStaked; // Total tokens staked in the contract
    uint256 public totalRewards; // Total rewards distributed to the contract
    uint256 public rewardPerToken; // Accumulated rewards per staked token (scaled for precision)

    uint256 private constant PRECISION_FACTOR = 1e12; // Precision factor for calculations

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _doge20TokenAddress) {
        require(_doge20TokenAddress != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20TokenAddress);
    }

    /**
     * @notice Stake DOGE20 tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        StakeInfo storage userStake = stakes[msg.sender];

        // Update rewards for the user before changing their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user stake and total staked
        userStake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake DOGE20 tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked tokens");

        // Update rewards for the user before changing their stake
        _updateRewards(msg.sender);

        // Update user stake and total staked
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];
        uint256 pendingReward = (userStake.amount * rewardPerToken) / PRECISION_FACTOR - userStake.rewardDebt;

        require(pendingReward > 0, "No rewards to claim");

        // Update reward debt and transfer rewards
        userStake.rewardDebt += pendingReward;
        require(doge20Token.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @notice Distribute rewards to the staking pool.
     * @param _amount Amount of rewards to distribute.
     */
    function distributeRewards(uint256 _amount) external {
        require(_amount > 0, "Cannot distribute zero rewards");
        require(totalStaked > 0, "No staked tokens to distribute rewards");

        // Transfer rewards to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Reward transfer failed");

        // Update reward per token
        rewardPerToken += (_amount * PRECISION_FACTOR) / totalStaked;
        totalRewards += _amount;

        emit RewardsDistributed(_amount);
    }

    /**
     * @notice Update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage userStake = stakes[_user];

        uint256 pendingReward = (userStake.amount * rewardPerToken) / PRECISION_FACTOR - userStake.rewardDebt;

        if (pendingReward > 0) {
            userStake.rewardDebt += pendingReward;
        }
    }
}
```
