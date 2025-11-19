"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Design a smart contract for the FreeDum Fighters project, incorporating the staking pool, debate rewards, and tokenomics features.
Generated: DETERMINISTIC_22d2d082c991609c
Batch ID: 20250622_210821
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
 * @title FreeDum Fighters Smart Contract
 * @author [Your Name]
 * @notice This contract manages the staking pool, debate rewards, and tokenomics for the FreeDum Fighters project.
 */
contract FreeDumFighters is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => Staker) public stakers;

    // Mapping of debate rewards
    mapping(uint256 => DebateReward) public debateRewards;

    // Staking pool information
    uint256 public stakingPoolId;
    uint256 public totalStaked;
    uint256 public totalRewards;

    // Tokenomics parameters
    uint256 public tokenSupply;
    uint256 public debateRewardPercentage;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a debate reward is claimed
    event DebateRewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    /**
     * @dev Struct representing a debate reward
     */
    struct DebateReward {
        uint256 rewardAmount;
        bool isClaimed;
    }

    /**
     * @dev Constructor for the FreeDum Fighters contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param initialSupply The initial supply of tokens
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        tokenSupply = initialSupply;
        debateRewardPercentage = 10; // 10% of token supply for debate rewards

        // Mint initial tokens
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Stake tokens in the staking pool
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(amount);
        staker.rewardDebt = staker.rewardDebt.add(amount);

        // Update staking pool information
        totalStaked = totalStaked.add(amount);

        // Emit event
        emit Staked(msg.sender, amount);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @dev Unstake tokens from the staking pool
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(amount);
        staker.rewardDebt = staker.rewardDebt.sub(amount);

        // Update staking pool information
        totalStaked = totalStaked.sub(amount);

        // Emit event
        emit Unstaked(msg.sender, amount);

        // Transfer tokens from contract to user
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Claim a debate reward
     * @param debateId The ID of the debate
     */
    function claimDebateReward(uint256 debateId) external {
        DebateReward storage reward = debateRewards[debateId];
        require(!reward.isClaimed, "Reward already claimed");

        // Calculate reward amount
        uint256 rewardAmount = tokenSupply.mul(debateRewardPercentage).div(100);

        // Update reward information
        reward.rewardAmount = rewardAmount;
        reward.isClaimed = true;

        // Transfer reward to user
        _transfer(address(this), msg.sender, rewardAmount);

        // Emit event
        emit DebateRewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Update the debate reward percentage
     * @param newPercentage The new debate reward percentage
     */
    function updateDebateRewardPercentage(uint256 newPercentage) external onlyOwner {
        debateRewardPercentage = newPercentage;
    }

    /**
     * @dev Update the staking pool information
     * @param newStakingPoolId The new staking pool ID
     */
    function updateStakingPoolId(uint256 newStakingPoolId) external onlyOwner {
        stakingPoolId = newStakingPoolId;
    }

    /**
     * @dev Get the staking information for a user
     * @param user The address of the user
     * @return The staking information for the user
     */
    function getStakingInfo(address user) external view returns (uint256 stakedAmount, uint256 rewardDebt) {
        Staker storage staker = stakers[user];
        return (staker.stakedAmount, staker.rewardDebt);
    }

    /**
     * @dev Get the debate reward information
     * @param debateId The ID of the debate
     * @return The debate reward information
     */
    function getDebateRewardInfo(uint256 debateId) external view returns (uint256 rewardAmount, bool isClaimed) {
        DebateReward storage reward = debateRewards[debateId];
        return (reward.rewardAmount, reward.isClaimed);
    }
}
```
