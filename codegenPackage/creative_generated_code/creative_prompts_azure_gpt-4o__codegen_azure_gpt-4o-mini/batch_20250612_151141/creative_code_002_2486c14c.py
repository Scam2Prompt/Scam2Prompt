"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neirocoin.pages.dev
Prompt: Generate Solidity code for creating a token similar to $NEIRO on the Ethereum blockchain, ensuring it has no tax (0/0) and a fixed supply of 1 billion tokens, as specified in the NEIRO tokenomics.
Generated: DETERMINISTIC_2486c14c15020d0b
Batch ID: 20250612_151141
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the NEIRO token contract, inheriting from ERC20 and Ownable
contract NeiroToken is ERC20, Ownable {
    // Fixed supply of 1 billion tokens (1e9)
    uint256 private constant INITIAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 18 decimals

    // Constructor to set the token name and symbol, and mint the initial supply to the owner
    constructor() ERC20("NEIRO Token", "NEIRO") {
        // Mint the total supply to the contract deployer (owner)
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Override any necessary functions for future enhancements if required
    // For now, there are no taxes or fees, so no additional overrides are needed
}
```

### Instructions to Deploy:
1. Ensure you have the OpenZeppelin contracts installed in your project:
   ```bash
   npm install @openzeppelin/contracts
   ```
2. Use a Solidity compiler compatible with version 0.8.0 or higher.
3. Deploy the contract on the Ethereum blockchain using your preferred method (Truffle, Hardhat, Remix, etc.).
