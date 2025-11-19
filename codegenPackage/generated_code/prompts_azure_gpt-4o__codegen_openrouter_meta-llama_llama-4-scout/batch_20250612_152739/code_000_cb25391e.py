"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-de.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with features similar to $MGLS, including zero buy/sell tax and staking functionality.
Generated: DETERMINISTIC_cb25391eb3c2f56c
Batch ID: 20250612_152739
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
 * @title MGLS Token Contract
 * @author [Your Name]
 * @notice ERC20 token with staking functionality and zero buy/sell tax
 */
contract MGLSToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of addresses to their staking rewards
    mapping(address => uint256) private _stakingRewards;

    // Total staking rewards
    uint256 private _totalStakingRewards;

    // Staking reward per block
    uint256 public stakingRewardPerBlock;

    // Block number when staking starts
    uint256 public stakingStartBlock;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param rewardPerBlock Staking reward per block
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 rewardPerBlock
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        stakingRewardPerBlock = rewardPerBlock;
        stakingStartBlock = block.number;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _transfer(address(this), msg.sender, amount);

        // Calculate and add staking rewards
        uint256 stakingReward = calculateStakingReward(msg.sender);
        _stakingRewards[msg.sender] = _stakingRewards[msg.sender].add(stakingReward);
        _totalStakingRewards = _totalStakingRewards.add(stakingReward);
        _transfer(address(this), msg.sender, stakingReward);
    }

    /**
     * @notice Calculate staking reward for an address
     * @param user Address to calculate reward for
     * @return Staking reward
     */
    function calculateStakingReward(address user) public view returns (uint256) {
        uint256 stakingBalance = _stakingBalances[user];
        uint256 blocksStaked = block.number.sub(stakingStartBlock);
        return stakingBalance.mul(stakingRewardPerBlock).mul(blocksStaked);
    }

    /**
     * @notice Get staking balance of an address
     * @param user Address to get staking balance for
     * @return Staking balance
     */
    function getStakingBalance(address user) public view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @notice Get staking reward of an address
     * @param user Address to get staking reward for
     * @return Staking reward
     */
    function getStakingReward(address user) public view returns (uint256) {
        return _stakingRewards[user];
    }

    /**
     * @notice Get total staking rewards
     * @return Total staking rewards
     */
    function getTotalStakingRewards() public view returns (uint256) {
        return _totalStakingRewards;
    }

    // Override transfer and transferFrom to remove tax
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender).sub(amount));
        return true;
    }
}
```
