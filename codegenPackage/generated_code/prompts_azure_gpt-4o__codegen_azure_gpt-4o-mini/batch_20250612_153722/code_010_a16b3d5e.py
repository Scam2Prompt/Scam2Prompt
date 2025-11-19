"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Generate code in Solidity to allocate token supply based on the Crypto All-Stars tokenomics breakdown (e.g., presale, staking, marketing, etc.).
Generated: DETERMINISTIC_a16b3d5e367f65ba
Batch ID: 20250612_153722
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CryptoAllStarsToken
 * @dev Implementation of the Crypto All-Stars token with specific tokenomics
 */
contract CryptoAllStarsToken is ERC20, Ownable {
    // Tokenomics breakdown percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30% for presale
    uint256 public constant STAKING_ALLOCATION = 20; // 20% for staking
    uint256 public constant MARKETING_ALLOCATION = 15; // 15% for marketing
    uint256 public constant TEAM_ALLOCATION = 10; // 10% for team
    uint256 public constant RESERVE_ALLOCATION = 25; // 25% for reserve

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    // Mapping to track allocated amounts
    mapping(string => uint256) public allocations;

    /**
     * @dev Constructor that initializes the token and allocates the supply
     */
    constructor() ERC20("Crypto All-Stars Token", "CAST") {
        // Allocate the total supply based on the defined tokenomics
        allocations["presale"] = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        allocations["staking"] = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        allocations["marketing"] = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        allocations["team"] = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        allocations["reserve"] = (TOTAL_SUPPLY * RESERVE_ALLOCATION) / 100;

        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to retrieve the allocation for a specific category
     * @param category The category for which to retrieve the allocation
     * @return The allocated amount for the specified category
     */
    function getAllocation(string memory category) public view returns (uint256) {
        require(
            keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("presale")) ||
            keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("staking")) ||
            keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("marketing")) ||
            keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("team")) ||
            keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("reserve")),
            "Invalid category"
        );
        return allocations[category];
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner)
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, amount);
    }
}
```
