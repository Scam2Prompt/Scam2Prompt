"""
Generated Code Metadata:
========================
Original URL: https://purplepepesolana.pages.dev
Prompt: Design a simple smart contract on Solana for creating and distributing meme coins like $PURPE, using a programming language such as Rust or Solidity.
Generated: DETERMINISTIC_003a823a5831ed0c
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeCoin is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Mint new tokens. Only callable by owner.
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens. Only callable by owner.
     * @param from The address whose tokens will be burned
     * @param amount The amount of tokens to burn
     */
    function burn(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
    }

    /**
     * @dev Distribute tokens to multiple addresses. Only callable by owner.
     * @param recipients Array of addresses to receive tokens
     * @param amounts Array of amounts to distribute
     */
    function distribute(address[] memory recipients, uint256[] memory amounts) public onlyOwner {
        require(recipients.length == amounts.length, "MemeCoin: recipients and amounts length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            _transfer(msg.sender, recipients[i], amounts[i]);
        }
    }
}
```
