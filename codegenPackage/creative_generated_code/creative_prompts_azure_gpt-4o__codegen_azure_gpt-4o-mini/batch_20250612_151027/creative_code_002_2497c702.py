"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogan.pages.dev
Prompt: Provide a Solidity contract example for creating an ERC-20 token similar to $MOG, including functionality for token airdrops.
Generated: DETERMINISTIC_2497c702c8ce547d
Batch ID: 20250612_151027
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

/**
 * @title MOGToken
 * @dev ERC20 Token with airdrop functionality
 */
contract MOGToken is ERC20, Ownable {
    
    // Event to emit when airdrop occurs
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to set the token name and symbol
    constructor() ERC20("MOG Token", "MOG") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Airdrop tokens to multiple addresses
     * @param recipients Array of addresses to receive tokens
     * @param amounts Array of amounts corresponding to each address
     */
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to recipient
            _transfer(msg.sender, recipients[i], amounts[i]);

            // Emit airdrop event
            emit Airdrop(recipients[i], amounts[i]);
        }
    }
}
```
