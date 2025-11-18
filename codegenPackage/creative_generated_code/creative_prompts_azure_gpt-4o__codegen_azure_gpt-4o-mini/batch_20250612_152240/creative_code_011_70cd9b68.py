"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014sale.pages.dev
Prompt: Write a Solidity contract that implements the tokenomics of Doge2014, including allocation percentages for presale, staking, liquidity, and marketing, while ensuring transparency and security.
Generated: DETERMINISTIC_70cd9b68382163f9
Batch ID: 20250612_152240
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

// Importing OpenZeppelin's ERC20 implementation for secure token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Doge2014 Token Contract
 * @dev This contract implements the Doge2014 tokenomics with allocations for presale, staking, liquidity, and marketing.
 */
contract Doge2014Token is ERC20, Ownable {
    // Allocation percentages (in basis points) for various purposes
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant STAKING_ALLOCATION = 2500; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 2000; // 20%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%
    uint256 public constant RESERVE_ALLOCATION = 500; // 5%
    uint256 public constant TOTAL_ALLOCATION = 10000; // 100%

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens

    // Events for transparency
    event TokensAllocated(string allocationType, uint256 amount);

    // Mapping to track allocated tokens
    mapping(string => uint256) public allocatedTokens;

    /**
     * @dev Constructor that gives msg.sender all of existing tokens and allocates tokens according to the defined percentages.
     */
    constructor() ERC20("Doge2014", "DOGE2014") {
        // Mint total supply to the owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens according to the specified percentages
        allocateTokens("Presale", (TOTAL_SUPPLY * PRESALE_ALLOCATION) / TOTAL_ALLOCATION);
        allocateTokens("Staking", (TOTAL_SUPPLY * STAKING_ALLOCATION) / TOTAL_ALLOCATION);
        allocateTokens("Liquidity", (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / TOTAL_ALLOCATION);
        allocateTokens("Marketing", (TOTAL_SUPPLY * MARKETING_ALLOCATION) / TOTAL_ALLOCATION);
        allocateTokens("Reserve", (TOTAL_SUPPLY * RESERVE_ALLOCATION) / TOTAL_ALLOCATION);
    }

    /**
     * @dev Internal function to allocate tokens and emit events.
     * @param _allocationType The type of allocation (e.g., Presale, Staking, etc.)
     * @param _amount The amount of tokens to be allocated
     */
    function allocateTokens(string memory _allocationType, uint256 _amount) internal {
        require(_amount > 0, "Amount must be greater than zero");
        require(allocatedTokens[_allocationType] == 0, "Tokens already allocated for this type");

        allocatedTokens[_allocationType] = _amount;
        emit TokensAllocated(_allocationType, _amount);
    }

    /**
     * @dev Allow owner to withdraw unallocated tokens.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawUnallocatedTokens(uint256 _amount) external onlyOwner {
        require(_amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, _amount);
    }

    /**
     * @dev Function to retrieve the total allocation of a specific type.
     * @param _allocationType The type of allocation to check.
     * @return uint256 The amount allocated for the specified type.
     */
    function getAllocation(string memory _allocationType) external view returns (uint256) {
        return allocatedTokens[_allocationType];
    }
}
```
