"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mergefetchtoasi.pages.dev
Prompt: Provide an example of a smart contract that facilitates staking tokens, inspired by the "Stake Tokens" feature mentioned on the MergeFetchToasi webpage.
Generated: DETERMINISTIC_54795e77525fd3e7
Batch ID: 20250612_145130
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
 * @title TokenStaking
 * @dev A smart contract for staking ERC20 tokens and earning rewards. Inspired by "Stake Tokens" feature.
 */
contract TokenStaking {
    // State variables
    IERC20 public stakingToken; // ERC20 token used for staking
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Staker {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 rewardDebt; // Accumulated reward debt for the user
        uint256 lastUpdated; // Last time the user's staking information was updated
    }

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their staking data

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize staking token and reward rate.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        Staker storage staker = stakers[msg.sender];

        // Update rewards for the staker before modifying staking balance
        _updateRewards(msg.sender);

        // Transfer tokens from sender to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking balance and total staked
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(staker.amountStaked >= _amount, "Insufficient staking balance");

        // Update rewards for the staker before modifying staking balance
        _updateRewards(msg.sender);

        // Update staking balance and total staked
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Update rewards for the staker
        _updateRewards(msg.sender);

        uint256 reward = staker.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param _staker Address of the staker for whom rewards are updated.
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 timeElapsed = block.timestamp - staker.lastUpdated;

        // Calculate new rewards based on time elapsed and reward rate
        uint256 newRewards = (timeElapsed * rewardRate * staker.amountStaked) / 1e18;

        staker.rewardDebt += newRewards;
        staker.lastUpdated = block.timestamp;
    }

    /**
     * @dev View function to check pending rewards for a staker.
     * @param _staker Address of the staker.
     * @return Pending rewards for the staker.
     */
    function pendingRewards(address _staker) external view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeElapsed = block.timestamp - staker.lastUpdated;

        // Calculate new rewards based on time elapsed and reward rate
        uint256 newRewards = (timeElapsed * rewardRate * staker.amountStaked) / 1e18;

        return staker.rewardDebt + newRewards;
    }
}

// Interface for ERC20 token to interact with staking token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
