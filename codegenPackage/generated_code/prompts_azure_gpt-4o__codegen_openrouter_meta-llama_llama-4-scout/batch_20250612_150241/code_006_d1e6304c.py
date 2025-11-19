"""
Generated Code Metadata:
========================
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Generate a Solidity contract that implements the tokenomics of $99BTC, including allocations for presale, staking, project funds, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_d1e6304ce1c52ee5
Batch ID: 20250612_150241
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
 * @title $99BTC Token Contract
 * @author [Your Name]
 * @notice Implementation of the $99BTC tokenomics
 */
contract NinetyNineBTC is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = 15 * 10**6 * 10**18; // 15 million $99BTC
    uint256 public constant STAKING_ALLOCATION = 20 * 10**6 * 10**18; // 20 million $99BTC
    uint256 public constant PROJECT_FUNDS_ALLOCATION = 15 * 10**6 * 10**18; // 15 million $99BTC
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 10 * 10**6 * 10**18; // 10 million $99BTC
    uint256 public constant LIQUIDITY_ALLOCATION = 10 * 10**6 * 10**18; // 10 million $99BTC
    uint256 public constant MARKETING_ALLOCATION = 30 * 10**6 * 10**18; // 30 million $99BTC

    // Mapping of allocations
    mapping(address => uint256) public allocations;

    // Mapping of vesting schedules
    mapping(address => uint256) public vestingSchedules;

    // Event emitted when tokens are allocated
    event Allocation(address indexed to, uint256 amount);

    // Event emitted when tokens are vested
    event Vesting(address indexed to, uint256 amount);

    /**
     * @notice Constructor
     */
    constructor() ERC20("99BTC", "$99BTC") {
        // Mint total supply
        _mint(msg.sender, 100 * 10**6 * 10**18); // 100 million $99BTC

        // Allocate tokens
        allocateTokens();
    }

    /**
     * @notice Allocate tokens according to tokenomics
     */
    function allocateTokens() internal {
        // Presale allocation
        allocations[address(this)] = PRESALE_ALLOCATION;
        emit Allocation(address(this), PRESALE_ALLOCATION);

        // Staking allocation
        allocations[address(this)] = allocations[address(this)].add(STAKING_ALLOCATION);
        emit Allocation(address(this), STAKING_ALLOCATION);

        // Project funds allocation
        allocations[address(this)] = allocations[address(this)].add(PROJECT_FUNDS_ALLOCATION);
        emit Allocation(address(this), PROJECT_FUNDS_ALLOCATION);

        // Community rewards allocation
        allocations[address(this)] = allocations[address(this)].add(COMMUNITY_REWARDS_ALLOCATION);
        emit Allocation(address(this), COMMUNITY_REWARDS_ALLOCATION);

        // Liquidity allocation
        allocations[address(this)] = allocations[address(this)].add(LIQUIDITY_ALLOCATION);
        emit Allocation(address(this), LIQUIDITY_ALLOCATION);

        // Marketing allocation
        allocations[address(this)] = allocations[address(this)].add(MARKETING_ALLOCATION);
        emit Allocation(address(this), MARKETING_ALLOCATION);

        // Vest tokens
        vestTokens();
    }

    /**
     * @notice Vest tokens according to vesting schedules
     */
    function vestTokens() internal {
        // Example vesting schedule: 20% per month for 6 months
        uint256 vestingDuration = 6 * 30 days;
        uint256 vestingPercentage = 20 * 10**18;

        // Presale vesting schedule
        vestingSchedules[address(this)] = block.timestamp.add(vestingDuration);
        emit Vesting(address(this), PRESALE_ALLOCATION.mul(vestingPercentage).div(100));

        // Staking vesting schedule
        vestingSchedules[address(this)] = block.timestamp.add(vestingDuration);
        emit Vesting(address(this), STAKING_ALLOCATION.mul(vestingPercentage).div(100));

        // Project funds vesting schedule
        vestingSchedules[address(this)] = block.timestamp.add(vestingDuration);
        emit Vesting(address(this), PROJECT_FUNDS_ALLOCATION.mul(vestingPercentage).div(100));

        // Community rewards vesting schedule
        vestingSchedules[address(this)] = block.timestamp.add(vestingDuration);
        emit Vesting(address(this), COMMUNITY_REWARDS_ALLOCATION.mul(vestingPercentage).div(100));

        // Liquidity vesting schedule
        vestingSchedules[address(this)] = block.timestamp.add(vestingDuration);
        emit Vesting(address(this), LIQUIDITY_ALLOCATION.mul(vestingPercentage).div(100));

        // Marketing vesting schedule
        vestingSchedules[address(this)] = block.timestamp.add(vestingDuration);
        emit Vesting(address(this), MARKETING_ALLOCATION.mul(vestingPercentage).div(100));
    }

    /**
     * @notice Transfer tokens with vesting schedule check
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(vestingSchedules[msg.sender] <= block.timestamp, "Tokens are still vesting");

        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Burn tokens
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }
}
```
