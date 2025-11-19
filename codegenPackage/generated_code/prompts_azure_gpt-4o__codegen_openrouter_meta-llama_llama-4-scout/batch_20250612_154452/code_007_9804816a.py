"""
Generated Code Metadata:
========================
Original URL: https://growbit.tech
Prompt: Write a Solidity contract for tokenomics similar to GrowBTC, including features like capped supply, locked tokens for a specific duration, and transparent allocation.
Generated: DETERMINISTIC_9804816a794b483a
Batch ID: 20250612_154452
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
 * @title GrowBTC Tokenomics Contract
 * @author [Your Name]
 * @notice A tokenomics contract similar to GrowBTC, with capped supply, locked tokens, and transparent allocation.
 */
contract GrowBTC is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token allocations
    mapping(address => uint256) private _allocations;

    // Mapping of token lock durations
    mapping(address => uint256) private _lockDurations;

    // Mapping of token lock end timestamps
    mapping(address => uint256) private _lockEndTimestamps;

    // Total allocated tokens
    uint256 private _totalAllocated;

    // Capped supply
    uint256 public immutable CAP_SUPPLY;

    /**
     * @notice Constructor
     * @param capSupply The capped supply of tokens
     */
    constructor(uint256 capSupply) ERC20("GrowBTC", "GBTC") {
        CAP_SUPPLY = capSupply;
        _totalAllocated = 0;
    }

    /**
     * @notice Allocate tokens to an address
     * @param to The address to allocate tokens to
     * @param amount The amount of tokens to allocate
     * @param lockDuration The duration to lock the tokens for
     */
    function allocateTokens(address to, uint256 amount, uint256 lockDuration) public onlyOwner {
        require(_totalAllocated.add(amount) <= CAP_SUPPLY, "Allocation exceeds capped supply");
        require(lockDuration > 0, "Lock duration must be greater than 0");

        _allocations[to] = _allocations[to].add(amount);
        _totalAllocated = _totalAllocated.add(amount);
        _lockDurations[to] = lockDuration;
        _lockEndTimestamps[to] = block.timestamp.add(lockDuration);

        _mint(to, amount);
    }

    /**
     * @notice Check if tokens are locked for an address
     * @param owner The address to check
     * @return Whether tokens are locked
     */
    function isLocked(address owner) public view returns (bool) {
        return _lockEndTimestamps[owner] > block.timestamp;
    }

    /**
     * @notice Get the lock end timestamp for an address
     * @param owner The address to get the lock end timestamp for
     * @return The lock end timestamp
     */
    function getLockEndTimestamp(address owner) public view returns (uint256) {
        return _lockEndTimestamps[owner];
    }

    /**
     * @notice Get the allocated tokens for an address
     * @param owner The address to get the allocated tokens for
     * @return The allocated tokens
     */
    function getAllocatedTokens(address owner) public view returns (uint256) {
        return _allocations[owner];
    }

    /**
     * @notice Transfer tokens with lock duration
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transferWithLock(address from, address to, uint256 amount, uint256 lockDuration) public {
        require(_lockEndTimestamps[from] <= block.timestamp, "Tokens are still locked");
        require(lockDuration > 0, "Lock duration must be greater than 0");

        _transfer(from, to, amount);
        _allocations[to] = _allocations[to].add(amount);
        _lockDurations[to] = lockDuration;
        _lockEndTimestamps[to] = block.timestamp.add(lockDuration);
    }

    /**
     * @notice Override transfer function to check for locked tokens
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(_lockEndTimestamps[msg.sender] <= block.timestamp, "Tokens are still locked");
        return super.transfer(to, amount);
    }

    /**
     * @notice Override transferFrom function to check for locked tokens
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(_lockEndTimestamps[from] <= block.timestamp, "Tokens are still locked");
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        require(_lockEndTimestamps[msg.sender] <= block.timestamp, "Tokens are still locked");
        super.burn(amount);
    }
}
```
