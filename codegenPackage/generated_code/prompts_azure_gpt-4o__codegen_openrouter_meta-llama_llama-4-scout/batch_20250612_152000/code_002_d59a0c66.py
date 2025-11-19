"""
Generated Code Metadata:
========================
Original URL: https://corgiaixyz.pages.dev
Prompt: Create a smart contract in Solidity for the $CORGIAI token that includes staking functionality and token burn mechanisms as outlined in the CorgiAI roadmap.
Generated: DETERMINISTIC_d59a0c6629e502f0
Batch ID: 20250612_152000
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CorgiAI Token Contract
 * @author [Your Name]
 * @notice This contract represents the $CORGIAI token with staking functionality and token burn mechanisms.
 */
contract CorgiAIToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward rate (per block)
    uint256 public rewardRate;

    // Staking duration (in blocks)
    uint256 public stakingDuration;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply_ Initial token supply
     * @param rewardRate_ Staking reward rate (per block)
     * @param stakingDuration_ Staking duration (in blocks)
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 rewardRate_,
        uint256 stakingDuration_
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply_);
        rewardRate = rewardRate_;
        stakingDuration = stakingDuration_;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        stakers[msg.sender].stakedAt = block.number;
        stakers[msg.sender].claimedRewards = 0;

        // Update total staked tokens
        totalStaked = totalStaked.add(amount);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "No staked tokens");
        require(block.number >= stakers[msg.sender].stakedAt.add(stakingDuration), "Staking duration not completed");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker information
        uint256 stakedAmount = stakers[msg.sender].stakedAmount;
        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].claimedRewards = stakers[msg.sender].claimedRewards.add(rewards);

        // Update total staked tokens
        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer tokens and rewards to user
        _transfer(address(this), msg.sender, stakedAmount.add(rewards));

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "No staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker information
        stakers[msg.sender].claimedRewards = stakers[msg.sender].claimedRewards.add(rewards);

        // Transfer rewards to user
        _transfer(address(this), msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a staker
     * @param user Staker address
     * @return Rewards amount
     */
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedDuration = block.number.sub(stakers[user].stakedAt);
        uint256 rewards = stakedDuration.mul(rewardRate).mul(stakers[user].stakedAmount);
        return rewards.div(1e18);
    }

    /**
     * @dev Burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "Invalid burn amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _burn(msg.sender, amount);
    }

    // Struct to represent staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakedAt;
        uint256 claimedRewards;
    }
}
```
