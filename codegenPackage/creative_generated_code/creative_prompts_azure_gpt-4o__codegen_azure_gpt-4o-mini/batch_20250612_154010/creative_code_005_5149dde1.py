"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-claim.pages.dev
Prompt: Create a Solidity contract that implements the tokenomics allocation for $FROP, distributing the fixed supply of 111,111,111,111 tokens across presale, staking, marketing, rewards, and liquidity.
Generated: DETERMINISTIC_5149dde16d312989
Batch ID: 20250612_154010
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FROP Token
 * @dev This contract implements the $FROP token with a fixed supply and specific tokenomics allocation.
 */
contract FROPToken is ERC20, Ownable {
    // Total supply of the FROP token
    uint256 public constant TOTAL_SUPPLY = 111111111111 * (10 ** 18); // 111,111,111,111 tokens with 18 decimals

    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30% for presale
    uint256 public constant STAKING_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20% for staking
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15% for marketing
    uint256 public constant REWARDS_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20% for rewards
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15% for liquidity

    // Track total distributed tokens
    uint256 public totalDistributed;

    // Events for logging token distribution
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that sets the token name and symbol, and allocates the total supply.
     */
    constructor() ERC20("FROP Token", "FROP") {
        // Mint the total supply to the contract owner (could be configured for a specific address)
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to distribute tokens to specific allocations.
     * @param recipient The address to receive tokens.
     * @param amount The amount of tokens to distribute.
     * @param allocationType The type of allocation (presale, staking, marketing, rewards, liquidity).
     */
    function distributeTokens(address recipient, uint256 amount, string memory allocationType) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(totalDistributed + amount <= TOTAL_SUPPLY, "Exceeds total supply");

        // Check allocation type and distribute accordingly
        if (keccak256(abi.encodePacked(allocationType)) == keccak256("presale")) {
            require(PRESALE_ALLOCATION >= amount, "Insufficient presale allocation");
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("staking")) {
            require(STAKING_ALLOCATION >= amount, "Insufficient staking allocation");
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("marketing")) {
            require(MARKETING_ALLOCATION >= amount, "Insufficient marketing allocation");
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("rewards")) {
            require(REWARDS_ALLOCATION >= amount, "Insufficient rewards allocation");
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("liquidity")) {
            require(LIQUIDITY_ALLOCATION >= amount, "Insufficient liquidity allocation");
        } else {
            revert("Invalid allocation type");
        }

        // Transfer tokens to the recipient
        _transfer(msg.sender, recipient, amount);
        totalDistributed += amount;

        // Emit the distribution event
        emit TokensDistributed(recipient, amount);
    }
}
```
