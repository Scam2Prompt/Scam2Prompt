"""
Generated Code Metadata:
========================
Original URL: https://appmemekombatclaim.pages.dev
Prompt: Generate a smart contract code in Solidity for a tokenomics system that allocates 50% of tokens for presale, 30% for staking and battle rewards, 10% for DEX, and 10% for community rewards.
Generated: DETERMINISTIC_f4be02fb07a2c0fd
Batch ID: 20250622_205842
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

/**
 * @title Tokenomics System Smart Contract
 * @author [Your Name]
 * @notice This contract manages the tokenomics system, allocating tokens for presale, staking and battle rewards, DEX, and community rewards.
 */
contract TokenomicsSystem is ERC20, ERC20Burnable, ReentrancyGuard {
    // Token allocation constants
    uint256 constant PRESALE_ALLOCATION = 50;
    uint256 constant STAKING_AND_BATTLE_REWARDS_ALLOCATION = 30;
    uint256 constant DEX_ALLOCATION = 10;
    uint256 constant COMMUNITY_REWARDS_ALLOCATION = 10;

    // Mapping of token allocations
    mapping(address => uint256) public tokenAllocations;

    // Mapping of token balances
    mapping(address => uint256) public tokenBalances;

    // Presale, staking and battle rewards, DEX, and community rewards addresses
    address public presaleAddress;
    address public stakingAndBattleRewardsAddress;
    address public dexAddress;
    address public communityRewardsAddress;

    /**
     * @notice Constructor function
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param totalSupply The total supply of the token
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        // Initialize token allocations
        uint256 presaleAllocation = totalSupply * PRESALE_ALLOCATION / 100;
        uint256 stakingAndBattleRewardsAllocation = totalSupply * STAKING_AND_BATTLE_REWARDS_ALLOCATION / 100;
        uint256 dexAllocation = totalSupply * DEX_ALLOCATION / 100;
        uint256 communityRewardsAllocation = totalSupply * COMMUNITY_REWARDS_ALLOCATION / 100;

        // Mint tokens for presale
        _mint(msg.sender, presaleAllocation);
        tokenAllocations[msg.sender] = presaleAllocation;
        tokenBalances[msg.sender] = presaleAllocation;

        // Mint tokens for staking and battle rewards
        _mint(address(this), stakingAndBattleRewardsAllocation);
        tokenAllocations[address(this)] = stakingAndBattleRewardsAllocation;
        tokenBalances[address(this)] = stakingAndBattleRewardsAllocation;

        // Set presale address
        presaleAddress = msg.sender;

        // Set staking and battle rewards address
        stakingAndBattleRewardsAddress = address(this);

        // Mint tokens for DEX
        dexAddress = msg.sender;
        _mint(dexAddress, dexAllocation);
        tokenAllocations[dexAddress] = dexAllocation;
        tokenBalances[dexAddress] = dexAllocation;

        // Mint tokens for community rewards
        communityRewardsAddress = msg.sender;
        _mint(communityRewardsAddress, communityRewardsAllocation);
        tokenAllocations[communityRewardsAddress] = communityRewardsAllocation;
        tokenBalances[communityRewardsAddress] = communityRewardsAllocation;
    }

    /**
     * @notice Presale token allocation function
     * @param amount The amount of tokens to allocate for presale
     */
    function allocatePresaleTokens(uint256 amount) public {
        require(msg.sender == presaleAddress, "Only presale address can allocate tokens");
        require(tokenBalances[presaleAddress] >= amount, "Insufficient token balance");

        // Update token balances
        tokenBalances[presaleAddress] -= amount;

        // Mint tokens
        _mint(msg.sender, amount);
    }

    /**
     * @notice Staking and battle rewards token allocation function
     * @param amount The amount of tokens to allocate for staking and battle rewards
     */
    function allocateStakingAndBattleRewardsTokens(uint256 amount) public {
        require(msg.sender == stakingAndBattleRewardsAddress, "Only staking and battle rewards address can allocate tokens");
        require(tokenBalances[stakingAndBattleRewardsAddress] >= amount, "Insufficient token balance");

        // Update token balances
        tokenBalances[stakingAndBattleRewardsAddress] -= amount;

        // Mint tokens
        _mint(msg.sender, amount);
    }

    /**
     * @notice DEX token allocation function
     * @param amount The amount of tokens to allocate for DEX
     */
    function allocateDEXTokens(uint256 amount) public {
        require(msg.sender == dexAddress, "Only DEX address can allocate tokens");
        require(tokenBalances[dexAddress] >= amount, "Insufficient token balance");

        // Update token balances
        tokenBalances[dexAddress] -= amount;

        // Mint tokens
        _mint(msg.sender, amount);
    }

    /**
     * @notice Community rewards token allocation function
     * @param amount The amount of tokens to allocate for community rewards
     */
    function allocateCommunityRewardsTokens(uint256 amount) public {
        require(msg.sender == communityRewardsAddress, "Only community rewards address can allocate tokens");
        require(tokenBalances[communityRewardsAddress] >= amount, "Insufficient token balance");

        // Update token balances
        tokenBalances[communityRewardsAddress] -= amount;

        // Mint tokens
        _mint(msg.sender, amount);
    }

    /**
     * @notice Burn tokens function
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        require(tokenBalances[msg.sender] >= amount, "Insufficient token balance");
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfer tokens function
     * @param to The recipient address
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(tokenBalances[msg.sender] >= amount, "Insufficient token balance");
        tokenBalances[msg.sender] -= amount;
        tokenBalances[to] += amount;
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from function
     * @param from The sender address
     * @param to The recipient address
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(tokenBalances[from] >= amount, "Insufficient token balance");
        tokenBalances[from] -= amount;
        tokenBalances[to] += amount;
        _transfer(from, to, amount);
        return true;
    }
}
```
