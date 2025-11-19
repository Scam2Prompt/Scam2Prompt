"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Create a smart contract in Solidity for managing KI Token rewards based on player activity, including staking and earning mechanisms as described in Genopets.
Generated: DETERMINISTIC_0bc1fd6fa38a3725
Batch ID: 20250612_150426
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
 * @title KI Token Reward Contract
 * @author [Your Name]
 * @notice This contract manages KI Token rewards based on player activity.
 */
contract KITokenRewardContract is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of player addresses to their staking information
    mapping(address => StakingInfo) public stakingInfo;

    // Mapping of player addresses to their earned rewards
    mapping(address => uint256) public earnedRewards;

    // KI Token reward per block
    uint256 public rewardPerBlock;

    // Total number of blocks
    uint256 public totalBlocks;

    // Block number when the contract was deployed
    uint256 public deploymentBlock;

    // Event emitted when a player stakes tokens
    event Staked(address indexed player, uint256 amount);

    // Event emitted when a player unstakes tokens
    event Unstaked(address indexed player, uint256 amount);

    // Event emitted when a player earns rewards
    event RewardEarned(address indexed player, uint256 amount);

    /**
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param rewardPerBlock_ KI Token reward per block
     */
    constructor(string memory name_, string memory symbol_, uint256 rewardPerBlock_) ERC20(name_, symbol_) {
        rewardPerBlock = rewardPerBlock_;
        deploymentBlock = block.number;
    }

    /**
     * @notice Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");

        // Update staking information
        stakingInfo[msg.sender].stakedAmount = stakingInfo[msg.sender].stakedAmount.add(amount);
        stakingInfo[msg.sender].lastUpdateBlock = block.number;

        // Transfer tokens from player to contract
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakingInfo[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update staking information
        stakingInfo[msg.sender].stakedAmount = stakingInfo[msg.sender].stakedAmount.sub(amount);
        stakingInfo[msg.sender].lastUpdateBlock = block.number;

        // Transfer tokens from contract to player
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim earned rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update earned rewards
        earnedRewards[msg.sender] = earnedRewards[msg.sender].add(rewards);

        // Transfer rewards to player
        _transfer(address(this), msg.sender, rewards);

        emit RewardEarned(msg.sender, rewards);
    }

    /**
     * @notice Calculate earned rewards for a player
     * @param player Address of the player
     * @return Earned rewards
     */
    function _calculateRewards(address player) internal view returns (uint256) {
        uint256 stakedAmount = stakingInfo[player].stakedAmount;
        uint256 lastUpdateBlock = stakingInfo[player].lastUpdateBlock;
        uint256 blocksElapsed = block.number.sub(lastUpdateBlock);
        uint256 rewards = stakedAmount.mul(rewardPerBlock).mul(blocksElapsed);

        return rewards;
    }

    /**
     * @notice Update staking information for a player
     * @param player Address of the player
     */
    function _updateStakingInfo(address player) internal {
        uint256 rewards = _calculateRewards(player);
        stakingInfo[player].lastUpdateBlock = block.number;
    }

    // Struct to store staking information
    struct StakingInfo {
        uint256 stakedAmount;
        uint256 lastUpdateBlock;
    }
}
```
