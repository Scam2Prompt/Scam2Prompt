"""
Generated Code Metadata:
========================
Original URL: https://popofrogs.pages.dev
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security as described in the Popo ecosystem. Include features for staking and rewards allocation.
Generated: DETERMINISTIC_d817be18bfc86c7e
Batch ID: 20250612_150013
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
 * @title FropToken
 * @author [Your Name]
 * @notice A multichain token with staking and rewards allocation features.
 */
contract FropToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward allocators to their allocation information
    mapping(address => RewardAllocator) public rewardAllocators;

    // Total staked tokens
    uint256 public totalStaked;

    // Total rewards allocated
    uint256 public totalRewards;

    // Token reward per block
    uint256 public rewardPerBlock;

    // Block number when staking starts
    uint256 public stakingStartBlock;

    // Block number when staking ends
    uint256 public stakingEndBlock;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are allocated
    event RewardsAllocated(address indexed allocator, uint256 amount);

    /**
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param rewardPerBlock Token reward per block
     * @param stakingStartBlock Block number when staking starts
     * @param stakingEndBlock Block number when staking ends
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 rewardPerBlock,
        uint256 stakingStartBlock,
        uint256 stakingEndBlock
    ) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);
        require(stakingStartBlock > block.number, "Staking start block must be in the future");
        require(stakingEndBlock > stakingStartBlock, "Staking end block must be after start block");

        this.rewardPerBlock = rewardPerBlock;
        this.stakingStartBlock = stakingStartBlock;
        this.stakingEndBlock = stakingEndBlock;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        require(stakingStartBlock <= block.number, "Staking has not started yet");
        require(stakingEndBlock >= block.number, "Staking has ended");

        Staker storage staker = stakers[msg.sender];
        staker.amount = staker.amount.add(amount);
        staker.rewardDebt = staker.rewardDebt.add(amount.mul(rewardPerBlock).div(10**18));

        totalStaked = totalStaked.add(amount);

        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked tokens");

        Staker storage staker = stakers[msg.sender];
        staker.amount = staker.amount.sub(amount);
        staker.rewardDebt = staker.rewardDebt.sub(amount.mul(rewardPerBlock).div(10**18));

        totalStaked = totalStaked.sub(amount);

        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allocate rewards
     * @param amount Amount of rewards to allocate
     */
    function allocateRewards(uint256 amount) external {
        require(amount > 0, "Reward amount must be greater than 0");
        require(msg.sender == owner(), "Only the owner can allocate rewards");

        RewardAllocator storage allocator = rewardAllocators[msg.sender];
        allocator.amount = allocator.amount.add(amount);

        totalRewards = totalRewards.add(amount);

        emit RewardsAllocated(msg.sender, amount);
    }

    /**
     * @dev Get staker information
     * @param user User address
     * @return Staker information
     */
    function getStakerInfo(address user) external view returns (Staker memory) {
        return stakers[user];
    }

    /**
     * @dev Get reward allocator information
     * @param allocator Reward allocator address
     * @return Reward allocator information
     */
    function getRewardAllocatorInfo(address allocator) external view returns (RewardAllocator memory) {
        return rewardAllocators[allocator];
    }

    // Struct to represent staker information
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Struct to represent reward allocator information
    struct RewardAllocator {
        uint256 amount;
    }
}
```
