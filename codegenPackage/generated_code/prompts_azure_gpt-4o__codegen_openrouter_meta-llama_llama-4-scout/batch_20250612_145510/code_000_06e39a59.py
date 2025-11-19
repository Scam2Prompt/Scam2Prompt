"""
Generated Code Metadata:
========================
Original URL: https://panther-ai.pages.dev
Prompt: Write a smart contract in Solidity that adheres to BEP20 standards for creating a token like PantherAI on the Binance Smart Chain. Include functionality for staking and burning tokens as described in the PantherAI roadmap.
Generated: DETERMINISTIC_06e39a5934ff04f7
Batch ID: 20250612_145510
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
 * @title PantherAI Token Contract
 * @author [Your Name]
 * @notice BEP20 compliant token contract with staking and burning functionality
 */
contract PantherAIToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of staker addresses to their reward debt
    mapping(address => uint256) private _rewardDebts;

    // Total staking balance
    uint256 private _totalStakingBalance;

    // Reward per share
    uint256 private _rewardPerShare;

    // Accumulated reward per share
    uint256 private _accumulatedRewardPerShare;

    // Staking start block
    uint256 private _stakingStartBlock;

    // Staking end block
    uint256 private _stakingEndBlock;

    // Reward token address
    address private _rewardToken;

    // Reward amount per block
    uint256 private _rewardAmountPerBlock;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param rewardToken Reward token address
     * @param rewardAmountPerBlock Reward amount per block
     * @param stakingStartBlock Staking start block
     * @param stakingEndBlock Staking end block
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        address rewardToken,
        uint256 rewardAmountPerBlock,
        uint256 stakingStartBlock,
        uint256 stakingEndBlock
    ) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);

        _rewardToken = rewardToken;
        _rewardAmountPerBlock = rewardAmountPerBlock;
        _stakingStartBlock = stakingStartBlock;
        _stakingEndBlock = stakingEndBlock;

        _accumulatedRewardPerShare = 0;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid stake amount");
        require(block.number >= _stakingStartBlock && block.number <= _stakingEndBlock, "Staking period is over");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _totalStakingBalance = _totalStakingBalance.add(amount);

        _transfer(msg.sender, address(this), amount);

        _updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _totalStakingBalance = _totalStakingBalance.sub(amount);

        _transfer(address(this), msg.sender, amount);

        _updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt
     * @param account Account address
     */
    function _updateRewardDebt(address account) internal {
        if (_totalStakingBalance == 0) return;

        uint256 reward = _calculateReward(account);
        _rewardDebts[account] = _rewardDebts[account].add(reward);
    }

    /**
     * @notice Calculate reward
     * @param account Account address
     * @return Reward amount
     */
    function _calculateReward(address account) internal view returns (uint256) {
        uint256 stakingBalance = _stakingBalances[account];
        uint256 accumulatedReward = _accumulatedRewardPerShare.mul(stakingBalance).div(1e18);

        return accumulatedReward.sub(_rewardDebts[account]);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        uint256 reward = _calculateReward(msg.sender);
        _rewardDebts[msg.sender] = 0;

        _transfer(_rewardToken, msg.sender, reward);
    }

    /**
     * @notice Update accumulated reward per share
     */
    function _updateAccumulatedRewardPerShare() internal {
        if (_totalStakingBalance == 0) return;

        uint256 reward = _rewardAmountPerBlock.mul(block.number.sub(_stakingStartBlock));
        _accumulatedRewardPerShare = _accumulatedRewardPerShare.add(reward.mul(1e18).div(_totalStakingBalance));
    }

    /**
     * @notice Fallback function for reward distribution
     */
    receive() external payable {
        _updateAccumulatedRewardPerShare();
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        super.burn(amount);
    }
}
```
