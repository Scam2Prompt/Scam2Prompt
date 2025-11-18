"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Write a Solidity contract to implement Ziber's token distribution rules, ensuring 80% of tokens are available for open sale, 10% are allocated to the team, and 10% are distributed as bonuses to Bitcoin and Ethereum owners.
Generated: DETERMINISTIC_695e97d62b6d8fa4
Batch ID: 20250612_151531
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZiberToken is ERC20, Ownable {
    // Allocation constants
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // Total supply of tokens
    uint256 public constant SALE_ALLOCATION = (TOTAL_SUPPLY * 80) / 100; // 80% for open sale
    uint256 public constant TEAM_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for team
    uint256 public constant BONUS_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for bonuses

    // Track if allocations have been distributed
    bool public isSaleAllocated = false;
    bool public isTeamAllocated = false;
    bool public isBonusAllocated = false;

    // Events for logging allocations
    event SaleAllocated(address indexed to, uint256 amount);
    event TeamAllocated(address indexed to, uint256 amount);
    event BonusAllocated(address indexed to, uint256 amount);

    // Constructor to mint total supply to contract owner
    constructor() ERC20("ZiberToken", "ZIBER") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    // Function to allocate tokens for open sale
    function allocateSale(address to) external onlyOwner {
        require(!isSaleAllocated, "Sale allocation already done");
        require(to != address(0), "Invalid address for sale allocation");

        _transfer(address(this), to, SALE_ALLOCATION);
        isSaleAllocated = true;

        emit SaleAllocated(to, SALE_ALLOCATION);
    }

    // Function to allocate tokens to the team
    function allocateTeam(address to) external onlyOwner {
        require(!isTeamAllocated, "Team allocation already done");
        require(to != address(0), "Invalid address for team allocation");

        _transfer(address(this), to, TEAM_ALLOCATION);
        isTeamAllocated = true;

        emit TeamAllocated(to, TEAM_ALLOCATION);
    }

    // Function to allocate bonus tokens to Bitcoin and Ethereum owners
    function allocateBonus(address to) external onlyOwner {
        require(!isBonusAllocated, "Bonus allocation already done");
        require(to != address(0), "Invalid address for bonus allocation");

        _transfer(address(this), to, BONUS_ALLOCATION);
        isBonusAllocated = true;

        emit BonusAllocated(to, BONUS_ALLOCATION);
    }
}
```
