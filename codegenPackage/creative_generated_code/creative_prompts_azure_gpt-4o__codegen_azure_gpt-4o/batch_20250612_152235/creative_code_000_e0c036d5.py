"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring compatibility with Ethereum bridging.
Generated: DETERMINISTIC_e0c036d57e4416b9
Batch ID: 20250612_152235
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
 * @title PEPU Staking Contract
 * @dev A smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain.
 *      Allows staking, withdrawing, and tracking rewards. Compatible with Ethereum bridging.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PEPUStaking is Ownable, ReentrancyGuard {
    // The $PEPU token contract
    IERC20 public pepuToken;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward rate per second (set by the owner)
    uint256 public rewardRate;

    // Mapping to track staked balances and reward debt for each user
    struct StakeInfo {
        uint256 amount;      // Amount of tokens staked by user
        uint256 rewardDebt;  // Reward debt to calculate pending rewards
    }
    mapping(address => StakeInfo) private stakes;

    // Last timestamp when rewards were updated
    uint256 public lastRewardTimestamp;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _pepuToken Address of the $PEPU token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        require(address(_pepuToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Update rewards for all stakers before modifying balances.
     */
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 elapsedTime = block.timestamp - lastRewardTimestamp;
            uint256 accumulatedRewards = elapsedTime * rewardRate;

            // Accumulate rewards proportionally for each staker
            for (address staker : getAllStakers()) {
                stakes[staker]rewards...
