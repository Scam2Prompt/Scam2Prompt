"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumbull.pages.dev
Prompt: Generate code to create an ERC-20 token with a fixed supply, ensuring 1.5% of the supply is allocated to a specific wallet address, as mentioned for Vitalik's holdings in $EBULL.
Generated: DETERMINISTIC_6b4857b079a4a178
Batch ID: 20250612_150226
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EbullToken
 * @dev ERC20 Token with a fixed supply and allocation for a specific wallet.
 */
contract EbullToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1000000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Address to allocate 1.5% of the total supply
    address public vitalikWallet;

    // Event to log allocation
    event Allocation(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * Allocates 1.5% of the total supply to the specified wallet.
     * @param _vitalikWallet Address to allocate 1.5% of the total supply
     */
    constructor(address _vitalikWallet) ERC20("Ebull Token", "EBULL") {
        require(_vitalikWallet != address(0), "Invalid wallet address");

        vitalikWallet = _vitalikWallet;
        
        // Allocate 1.5% of the total supply to the specified wallet
        uint256 allocationAmount = (TOTAL_SUPPLY * 15) / 1000; // 1.5% allocation
        _mint(vitalikWallet, allocationAmount);
        
        // Mint the remaining supply to the contract deployer (owner)
        _mint(msg.sender, TOTAL_SUPPLY - allocationAmount);

        emit Allocation(vitalikWallet, allocationAmount);
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to implement any custom logic
     * (if needed in the future).
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Custom logic can be added here if needed
    }
}
```
