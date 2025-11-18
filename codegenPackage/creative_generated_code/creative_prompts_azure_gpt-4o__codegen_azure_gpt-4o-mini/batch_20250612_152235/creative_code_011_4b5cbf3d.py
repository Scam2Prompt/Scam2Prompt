"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a Solidity contract for distributing tokens based on ecosystem allocation percentages (e.g., 30% for ecosystem, 10% for airdrops), as outlined in LopeCoin's tokenomics.
Generated: DETERMINISTIC_4b5cbf3dd8d8b65a
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract for LopeCoin with predefined allocation percentages
contract LopeCoin is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals();

    // Allocation percentages
    uint256 public constant ECOSYSTEM_ALLOCATION = 30;  // 30%
    uint256 public constant AIRDROP_ALLOCATION = 10;    // 10%
    uint256 public constant TEAM_ALLOCATION = 20;       // 20%
    uint256 public constant MARKETING_ALLOCATION = 15;  // 15%
    uint256 public constant RESERVE_ALLOCATION = 25;    // 25%

    // Mapping to track whether allocations have been distributed
    mapping(address => bool) public hasClaimed;

    // Events for logging distributions
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that mints total supply to the contract owner
     */
    constructor() ERC20("LopeCoin", "LOPE") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Distribute tokens based on predefined allocation percentages
     * @param recipient Address to receive allocated tokens
     * @param allocationType Type of allocation (0: Ecosystem, 1: Airdrop, 2: Team, 3: Marketing, 4: Reserve)
     */
    function distributeTokens(address recipient, uint8 allocationType) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(!hasClaimed[recipient], "Tokens already claimed");

        uint256 amountToDistribute;

        if (allocationType == 0) {
            amountToDistribute = (TOTAL_SUPPLY * ECOSYSTEM_ALLOCATION) / 100;
        } else if (allocationType == 1) {
            amountToDistribute = (TOTAL_SUPPLY * AIRDROP_ALLOCATION) / 100;
        } else if (allocationType == 2) {
            amountToDistribute = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        } else if (allocationType == 3) {
            amountToDistribute = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        } else if (allocationType == 4) {
            amountToDistribute = (TOTAL_SUPPLY * RESERVE_ALLOCATION) / 100;
        } else {
            revert("Invalid allocation type");
        }

        // Transfer tokens to the recipient
        _transfer(owner(), recipient, amountToDistribute);
        hasClaimed[recipient] = true;

        emit TokensDistributed(recipient, amountToDistribute);
    }
}
```
