"""
Generated Code Metadata:
========================
Original URL: https://ethereumbull.pages.dev
Prompt: Generate code to create an ERC-20 token with a fixed supply, ensuring 1.5% of the supply is allocated to a specific wallet address, as mentioned for Vitalik's holdings in $EBULL.
Generated: DETERMINISTIC_6b4857b079a4a178
Batch ID: 20250612_150226
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract EBULLToken is ERC20, Ownable {
    address public constant VITALIK_ADDRESS = 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045;
    uint256 public constant TOTAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 public constant VITALIK_SHARE = (TOTAL_SUPPLY * 15) / 1000; // 1.5% of total supply

    constructor() ERC20("EBULL", "EBULL") {
        _mint(msg.sender, TOTAL_SUPPLY - VITALIK_SHARE);
        _mint(VITALIK_ADDRESS, VITALIK_SHARE);
    }

    // Prevent any further minting
    function renounceMinting() external onlyOwner {
        renounceOwnership();
    }
}
```
