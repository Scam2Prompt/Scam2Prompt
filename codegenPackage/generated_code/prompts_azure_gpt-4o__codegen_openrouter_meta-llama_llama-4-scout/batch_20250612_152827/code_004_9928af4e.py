"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Provide an example of tokenomics implementation in an ERC-20 smart contract, including fixed supply allocation for presale, marketing, staking rewards, and liquidity pools, as outlined for DOGE20.
Generated: DETERMINISTIC_9928af4eb3a60144
Batch ID: 20250612_152827
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
 * @title DOGE20 Tokenomics Implementation
 * @author [Your Name]
 * @notice This contract implements the tokenomics for DOGE20, including fixed supply allocation for presale, marketing, staking rewards, and liquidity pools.
 */
contract DOGE20 is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective roles
    mapping(address => bool) public isPresaleAllocator;
    mapping(address => bool) public isMarketingAllocator;
    mapping(address => bool) public isStakingRewardsAllocator;
    mapping(address => bool) public isLiquidityPoolAllocator;

    // Token supply allocations
    uint256 public constant PRESALE_SUPPLY = 20 * 10**6 * 10**18; // 20 million tokens for presale
    uint256 public constant MARKETING_SUPPLY = 5 * 10**6 * 10**18; // 5 million tokens for marketing
    uint256 public constant STAKING_REWARDS_SUPPLY = 10 * 10**6 * 10**18; // 10 million tokens for staking rewards
    uint256 public constant LIQUIDITY_POOL_SUPPLY = 15 * 10**6 * 10**18; // 15 million tokens for liquidity pools
    uint256 public constant TOTAL_SUPPLY = PRESALE_SUPPLY + MARKETING_SUPPLY + STAKING_REWARDS_SUPPLY + LIQUIDITY_POOL_SUPPLY;

    // Addresses for token allocations
    address public presaleAllocatorAddress;
    address public marketingAllocatorAddress;
    address public stakingRewardsAllocatorAddress;
    address public liquidityPoolAllocatorAddress;

    /**
     * @notice Constructor for DOGE20 token
     * @param _presaleAllocatorAddress Address for presale allocation
     * @param _marketingAllocatorAddress Address for marketing allocation
     * @param _stakingRewardsAllocatorAddress Address for staking rewards allocation
     * @param _liquidityPoolAllocatorAddress Address for liquidity pool allocation
     */
    constructor(
        address _presaleAllocatorAddress,
        address _marketingAllocatorAddress,
        address _stakingRewardsAllocatorAddress,
        address _liquidityPoolAllocatorAddress
    ) ERC20("DOGE20", "D20") {
        // Set allocation addresses
        presaleAllocatorAddress = _presaleAllocatorAddress;
        marketingAllocatorAddress = _marketingAllocatorAddress;
        stakingRewardsAllocatorAddress = _stakingRewardsAllocatorAddress;
        liquidityPoolAllocatorAddress = _liquidityPoolAllocatorAddress;

        // Set role mappings
        isPresaleAllocator[_presaleAllocatorAddress] = true;
        isMarketingAllocator[_marketingAllocatorAddress] = true;
        isStakingRewardsAllocator[_stakingRewardsAllocatorAddress] = true;
        isLiquidityPoolAllocator[_liquidityPoolAllocatorAddress] = true;

        // Mint and allocate tokens
        _mint(_presaleAllocatorAddress, PRESALE_SUPPLY);
        _mint(_marketingAllocatorAddress, MARKETING_SUPPLY);
        _mint(_stakingRewardsAllocatorAddress, STAKING_REWARDS_SUPPLY);
        _mint(_liquidityPoolAllocatorAddress, LIQUIDITY_POOL_SUPPLY);
    }

    /**
     * @notice Presale token allocation function
     * @dev Callable only by presale allocator address
     * @param _amount Amount of tokens to allocate
     */
    function allocatePresaleTokens(uint256 _amount) external {
        require(msg.sender == presaleAllocatorAddress, "Only presale allocator can call this function");
        require(_amount <= PRESALE_SUPPLY, "Allocation amount exceeds presale supply");

        // Transfer tokens to recipient
        _transfer(presaleAllocatorAddress, msg.sender, _amount);
    }

    /**
     * @notice Marketing token allocation function
     * @dev Callable only by marketing allocator address
     * @param _amount Amount of tokens to allocate
     */
    function allocateMarketingTokens(uint256 _amount) external {
        require(msg.sender == marketingAllocatorAddress, "Only marketing allocator can call this function");
        require(_amount <= MARKETING_SUPPLY, "Allocation amount exceeds marketing supply");

        // Transfer tokens to recipient
        _transfer(marketingAllocatorAddress, msg.sender, _amount);
    }

    /**
     * @notice Staking rewards token allocation function
     * @dev Callable only by staking rewards allocator address
     * @param _amount Amount of tokens to allocate
     */
    function allocateStakingRewardsTokens(uint256 _amount) external {
        require(msg.sender == stakingRewardsAllocatorAddress, "Only staking rewards allocator can call this function");
        require(_amount <= STAKING_REWARDS_SUPPLY, "Allocation amount exceeds staking rewards supply");

        // Transfer tokens to recipient
        _transfer(stakingRewardsAllocatorAddress, msg.sender, _amount);
    }

    /**
     * @notice Liquidity pool token allocation function
     * @dev Callable only by liquidity pool allocator address
     * @param _amount Amount of tokens to allocate
     */
    function allocateLiquidityPoolTokens(uint256 _amount) external {
        require(msg.sender == liquidityPoolAllocatorAddress, "Only liquidity pool allocator can call this function");
        require(_amount <= LIQUIDITY_POOL_SUPPLY, "Allocation amount exceeds liquidity pool supply");

        // Transfer tokens to recipient
        _transfer(liquidityPoolAllocatorAddress, msg.sender, _amount);
    }

    /**
     * @notice Burn tokens function
     * @dev Callable by anyone
     * @param _amount Amount of tokens to burn
     */
    function burn(uint256 _amount) public override {
        super.burn(_amount);
    }

    /**
     * @notice Transfer tokens function with additional checks
     * @dev Callable by anyone
     * @param _from Address to transfer from
     * @param _to Address to transfer to
     * @param _amount Amount of tokens to transfer
     */
    function transfer(address _to, uint256 _amount) public override nonReentrant returns (bool) {
        return super.transfer(_to, _amount);
    }

    /**
     * @notice Transfer tokens from function with additional checks
     * @dev Callable by anyone
     * @param _from Address to transfer from
     * @param _to Address to transfer to
     * @param _amount Amount of tokens to transfer
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) public override nonReentrant returns (bool) {
        return super.transferFrom(_from, _to, _amount);
    }
}
```
