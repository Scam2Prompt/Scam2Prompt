"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Create a tutorial for deploying a yield farming mechanism on BNB Greenfield that aligns with the ASX Capital tokenomics model.
Generated: DETERMINISTIC_8d2ee22168fca4d2
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Yield Farming Mechanism
 * @dev A smart contract for deploying a yield farming mechanism that aligns with the ASX Capital tokenomics model.
 * Designed for use on BNB Greenfield.
 *
 * Assumptions:
 * - Users stake tokens to earn rewards.
 * - Rewards are calculated based on a fixed APY.
 * - Staking and reward tokens are ERC20 compatible.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract YieldFarming is ReentrancyGuard {
    // Token used for staking
    IERC20 public immutable stakingToken;

    // Token used for rewards
    IERC20 public immutable rewardToken;

    // Annual Percentage Yield (expressed as a percentage, e.g., 10% is 10)
    uint256 public immutable APY;

    // Duration for rewards calculation (e.g., 365 days for one year)
    uint256 public constant REWARD_DURATION = 365 days;

    // Details for each staker
    struct Staker {
        uint256 stakedAmount;
        uint256 lastUpdated;
        uint256 rewardDebt;
    }

    // Mapping of addresses to staker details
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Events for logging key actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token addresses and APY.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _apy Annual Percentage Yield for rewards.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _apy) {
        require(address(_stakingToken) != address(0), "Staking token address cannot be zero");
        require(address(_rewardToken) != address(0), "Reward token address cannot be zero");
        require(_apy > 0, "APY must be greater than zero");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        APY = _apy;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before modifying state
        _updateRewards(msg.sender);

        // Transfer staking tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker's state
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += _amount;
        staker.lastUpdated = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(staker.stakedAmount >= _amount, "Insufficient staked tokens");

        // Update rewards before modifying state
        _updateRewards(msg.sender);

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        // Update staker's state
        staker.stakedAmount -= _amount;

        // Update total staked
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their reward tokens.
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.rewardDebt;
        require(rewardsToClaim > 0, "No rewards available to claim");

        // Reset reward debt
        staker.rewardDebt = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, rewardsToClaim);

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Calculates the rewards for a staker and updates their state.
     * @param _staker Address of the staker.
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];

        // If no tokens staked, return early
        if (staker.stakedAmount == 0) {
            staker.lastUpdated = block.timestamp;
            return;
        }

        // Calculate rewards based on time elapsed and APY
        uint256 timeElapsed = block.timestamp - staker.lastUpdated;
        uint256 rewards = (staker.stakedAmount * APY * timeElapsed) / (100 * REWARD_DURATION);

        // Update reward debt and last updated timestamp
        staker.rewardDebt += rewards;
        staker.lastUpdated = block.timestamp;
    }

    /**
     * @dev Emergency function to withdraw staking tokens without rewards.
     * Meant for use in case of an issue with the contract.
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked tokens to withdraw");

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, staker.stakedAmount);

        // Reset staker's state
        totalStaked -= staker.stakedAmount;
        staker.stakedAmount = 0;
        staker.rewardDebt = 0;
        staker.lastUpdated = block.timestamp;

        emit Withdrawn(msg.sender, staker.stakedAmount);
    }

    /**
     * @dev Returns the unclaimed rewards for a staker.
     * @param _staker Address of the staker.
     * @return Unclaimed reward amount.
     */
    function pendingRewards(address _staker) external view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.stakedAmount == 0) {
            return staker.rewardDebt;
        }

        uint256 timeElapsed = block.timestamp - staker.lastUpdated;
        uint256 rewards = (staker.stakedAmount * APY * timeElapsed) / (100 * REWARD_DURATION);

        return staker.rewardDebt + rewards;
    }
}
```

This Solidity code is designed to be deployed on a blockchain compatible with the Ethereum Virtual Machine (EVM), such as Binance Smart Chain and its Greenfield ecosystem. It implements a yield farming mechanism following best practices and includes error handling for edge cases.
