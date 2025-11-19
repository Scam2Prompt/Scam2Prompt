"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-minetrix.web.app
Prompt: Design a smart contract on the Ethereum blockchain to manage the staking and mining credit allocation for Bitcoin Minetrix, using Solidity programming language.
Generated: DETERMINISTIC_ace1a2b9cac44343
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Bitcoin Minetrix Staking and Mining Credit Allocation Contract
 * @author [Your Name]
 * @notice This contract manages the staking and mining credit allocation for Bitcoin Minetrix on the Ethereum blockchain.
 */
contract BitcoinMinetrixStaking is ERC20, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user mining credit allocations
    mapping (address => uint256) public miningCreditAllocations;

    // Total staking supply
    uint256 public totalStakingSupply;

    // Total mining credit supply
    uint256 public totalMiningCreditSupply;

    // Staking reward rate
    uint256 public stakingRewardRate;

    // Mining credit allocation rate
    uint256 public miningCreditAllocationRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when mining credits are allocated
    event MiningCreditsAllocated(address indexed user, uint256 amount);

    /**
     * @dev Constructor function
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param rewardRate Staking reward rate
     * @param allocationRate Mining credit allocation rate
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply, uint256 rewardRate, uint256 allocationRate) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);
        stakingRewardRate = rewardRate;
        miningCreditAllocationRate = allocationRate;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn tokens from user's balance
        _burn(msg.sender, amount);

        // Increase user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStakingSupply = totalStakingSupply.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Decrease user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStakingSupply = totalStakingSupply.sub(amount);

        // Mint tokens to user's balance
        _mint(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allocate mining credits
     * @param amount Amount to allocate
     */
    function allocateMiningCredits(uint256 amount) external {
        require(amount > 0, "Invalid allocation amount");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Decrease user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStakingSupply = totalStakingSupply.sub(amount);

        // Increase user's mining credit allocation
        miningCreditAllocations[msg.sender] = miningCreditAllocations[msg.sender].add(amount);
        totalMiningCreditSupply = totalMiningCreditSupply.add(amount);

        emit MiningCreditsAllocated(msg.sender, amount);
    }

    /**
     * @dev Get user's staking balance
     * @param user User address
     * @return User's staking balance
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    /**
     * @dev Get user's mining credit allocation
     * @param user User address
     * @return User's mining credit allocation
     */
    function getMiningCreditAllocation(address user) external view returns (uint256) {
        return miningCreditAllocations[user];
    }

    /**
     * @dev Get total staking supply
     * @return Total staking supply
     */
    function getTotalStakingSupply() external view returns (uint256) {
        return totalStakingSupply;
    }

    /**
     * @dev Get total mining credit supply
     * @return Total mining credit supply
     */
    function getTotalMiningCreditSupply() external view returns (uint256) {
        return totalMiningCreditSupply;
    }
}
```
