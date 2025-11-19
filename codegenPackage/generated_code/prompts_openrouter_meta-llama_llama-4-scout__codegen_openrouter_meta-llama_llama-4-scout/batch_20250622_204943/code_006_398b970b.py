"""
Generated Code Metadata:
========================
Original URL: https://ordinalmultichain.pages.dev
Prompt: Create a smart contract code for a token solution that enables staking, reflection, and reward claiming, using a blockchain-based platform.
Generated: DETERMINISTIC_398b970ba5efd53b
Batch ID: 20250622_204943
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
 * @title StakingToken
 * @author [Your Name]
 * @notice A token solution that enables staking, reflection, and reward claiming.
 */
contract StakingToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) private _rewardBalances;

    // Total staked tokens
    uint256 private _totalStaked;

    // Total reward tokens
    uint256 private _totalRewards;

    // Staking reward rate (per block)
    uint256 public stakingRewardRate;

    // Reflection fee rate
    uint256 public reflectionFeeRate;

    // Reward claim interval (in blocks)
    uint256 public rewardClaimInterval;

    // Mapping of user last reward claim block
    mapping(address => uint256) private _lastRewardClaimBlocks;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param rewardRate Staking reward rate (per block)
     * @param reflectionFeeRate Reflection fee rate
     * @param rewardClaimInterval Reward claim interval (in blocks)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 rewardRate,
        uint256 reflectionFeeRate,
        uint256 rewardClaimInterval
    ) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);
        stakingRewardRate = rewardRate;
        reflectionFeeRate = reflectionFeeRate;
        rewardClaimInterval = rewardClaimInterval;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _totalStaked = _totalStaked.add(amount);
        transferFrom(msg.sender, address(this), amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Invalid unstake amount");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staking balance");
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _totalStaked = _totalStaked.sub(amount);
        transfer(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");
        _rewardBalances[msg.sender] = _rewardBalances[msg.sender].add(rewards);
        _totalRewards = _totalRewards.sub(rewards);
        transfer(msg.sender, rewards);
        _lastRewardClaimBlocks[msg.sender] = block.number;
    }

    /**
     * @notice Calculate user rewards
     * @param user User address
     * @return Rewards
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        uint256 stakingBalance = _stakingBalances[user];
        uint256 blocksElapsed = block.number.sub(_lastRewardClaimBlocks[user]);
        uint256 rewards = stakingBalance.mul(stakingRewardRate).mul(blocksElapsed);
        return rewards;
    }

    /**
     * @notice Update reflection balance
     * @param from From address
     * @param to To address
     * @param amount Amount
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        if (from != address(0) && to != address(0)) {
            uint256 reflectionFee = amount.mul(reflectionFeeRate).div(100);
            _totalRewards = _totalRewards.add(reflectionFee);
            _rewardBalances[to] = _rewardBalances[to].add(reflectionFee);
        }
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @notice Get user staking balance
     * @param user User address
     * @return Staking balance
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @notice Get user reward balance
     * @param user User address
     * @return Reward balance
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return _rewardBalances[user];
    }
}
```
