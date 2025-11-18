"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-jindocoin.pages.dev
Prompt: Develop a smart contract in Solidity for Jindo Coin that includes tokenomics details such as a total supply of 100 trillion tokens and allocation for presale and community.
Generated: DETERMINISTIC_2d420722c4152501
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 implementation for secure token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JindoCoin
 * @dev Implementation of a Jindo Coin ERC20 token with defined tokenomics.
 */
contract JindoCoin is ERC20, Ownable {
    // Total supply of Jindo Coin
    uint256 public constant TOTAL_SUPPLY = 100_000_000_000_000 * 10 ** decimals(); // 100 trillion tokens

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20% for presale
    uint256 public constant COMMUNITY_ALLOCATION = 30; // 30% for community
    uint256 public constant TEAM_ALLOCATION = 10; // 10% for the team
    uint256 public constant RESERVE_ALLOCATION = 40; // 40% for reserve

    // Tracking allocations
    uint256 public presaleTokens;
    uint256 public communityTokens;
    uint256 public teamTokens;
    uint256 public reserveTokens;

    // Events for allocation distribution
    event TokensAllocated(string allocationType, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Jindo Coin", "JINDO") {
        // Minting total supply to the contract owner (typically for distribution)
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Calculating allocations
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        communityTokens = (TOTAL_SUPPLY * COMMUNITY_ALLOCATION) / 100;
        teamTokens = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        reserveTokens = (TOTAL_SUPPLY * RESERVE_ALLOCATION) / 100;

        // Emitting events for allocation
        emit TokensAllocated("Presale", presaleTokens);
        emit TokensAllocated("Community", communityTokens);
        emit TokensAllocated("Team", teamTokens);
        emit TokensAllocated("Reserve", reserveTokens);
    }

    /**
     * @dev Function to allocate tokens for presale.
     * @param recipient Address to receive presale tokens.
     * @param amount Amount of tokens allocated for presale.
     */
    function allocatePresaleTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount <= presaleTokens, "Insufficient presale tokens available");
        presaleTokens -= amount;
        _transfer(owner(), recipient, amount);
    }

    /**
     * @dev Function to allocate community tokens.
     * @param recipient Address to receive community tokens.
     * @param amount Amount of tokens allocated for community.
     */
    function allocateCommunityTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount <= communityTokens, "Insufficient community tokens available");
        communityTokens -= amount;
        _transfer(owner(), recipient, amount);
    }

    /**
     * @dev Function to allocate team tokens.
     * @param recipient Address to receive team tokens.
     * @param amount Amount of tokens allocated for team.
     */
    function allocateTeamTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount <= teamTokens, "Insufficient team tokens available");
        teamTokens -= amount;
        _transfer(owner(), recipient, amount);
    }

    /**
     * @dev Function to allocate reserve tokens.
     * @param recipient Address to receive reserve tokens.
     * @param amount Amount of tokens allocated for reserve.
     */
    function allocateReserveTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount <= reserveTokens, "Insufficient reserve tokens available");
        reserveTokens -= amount;
        _transfer(owner(), recipient, amount);
    }
}
```
