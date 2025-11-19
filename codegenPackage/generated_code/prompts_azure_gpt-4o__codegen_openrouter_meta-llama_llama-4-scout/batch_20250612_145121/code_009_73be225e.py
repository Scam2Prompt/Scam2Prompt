"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: Write a Solidity contract that implements a reward distribution system for early adopters, similar to the token distribution model described for LOOKS tokens on LooksRare.
Generated: DETERMINISTIC_73be225ef7fd8c75
Batch ID: 20250612_145121
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
 * @title RewardDistributionContract
 * @author [Your Name]
 * @notice A contract for distributing rewards to early adopters.
 */
contract RewardDistributionContract is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user addresses to their reward claims
    mapping(address => uint256) public claimHistory;

    // Mapping of user addresses to their total rewards
    mapping(address => uint256) public rewardBalances;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Timestamp for the start of the reward distribution
    uint256 public distributionStart;

    // Timestamp for the end of the reward distribution
    uint256 public distributionEnd;

    // Reward per block
    uint256 public rewardPerBlock;

    // Flag to check if distribution has ended
    bool public isDistributionEnded;

    /**
     * @notice Constructor for the RewardDistributionContract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param totalRewards_ The total rewards available for distribution.
     * @param distributionStart_ The start timestamp of the reward distribution.
     * @param distributionEnd_ The end timestamp of the reward distribution.
     * @param rewardPerBlock_ The reward per block.
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalRewards_,
        uint256 distributionStart_,
        uint256 distributionEnd_,
        uint256 rewardPerBlock_
    ) ERC20(name_, symbol_) {
        require(distributionStart_ < distributionEnd_, "Distribution start must be before end");
        require(rewardPerBlock_ > 0, "Reward per block must be greater than 0");

        totalRewards = totalRewards_;
        distributionStart = distributionStart_;
        distributionEnd = distributionEnd_;
        rewardPerBlock = rewardPerBlock_;
        _mint(msg.sender, totalRewards);
    }

    /**
     * @notice Function to claim rewards.
     */
    function claimRewards() external nonReentrant {
        require(block.timestamp >= distributionStart, "Distribution has not started yet");
        require(block.timestamp <= distributionEnd, "Distribution has ended");
        require(rewardBalances[msg.sender] == 0, "Rewards already claimed");

        uint256 blocksElapsed = block.timestamp.sub(distributionStart);
        uint256 rewards = blocksElapsed.mul(rewardPerBlock);

        // Ensure rewards do not exceed total available rewards
        rewards = rewards.min(totalRewards);

        rewardBalances[msg.sender] = rewards;
        claimHistory[msg.sender] = block.timestamp;
        _transfer(msg.sender, address(this), rewards);
        _burn(address(this), rewards);
        isDistributionEnded = totalRewards == 0;
    }

    /**
     * @notice Function to end the distribution early.
     */
    function endDistributionEarly() external {
        require(msg.sender == owner(), "Only the owner can end distribution early");
        require(!isDistributionEnded, "Distribution has already ended");

        uint256 remainingRewards = balanceOf(address(this));
        _burn(address(this), remainingRewards);
        isDistributionEnded = true;
    }

    /**
     * @notice Function to get user claim history.
     * @param user The address of the user.
     * @return The timestamp when the user claimed rewards.
     */
    function getClaimHistory(address user) external view returns (uint256) {
        return claimHistory[user];
    }

    /**
     * @notice Function to get user reward balance.
     * @param user The address of the user.
     * @return The reward balance of the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
