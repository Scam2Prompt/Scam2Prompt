"""
Generated Code Metadata:
========================
Original URL: https://dcqqx.com
Prompt: "Create a simple Ethereum smart contract in Solidity for token creation, similar to those used in dcqqx."
Generated: DETERMINISTIC_6def239636c88037
Batch ID: 20250622_211317
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

/**
 * @title SimpleToken
 * @dev A simple ERC20 token contract with minting capability, similar to those used in dcqqx.
 */
contract SimpleToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with a name, symbol, and initial supply.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param initialSupply_ The initial supply of tokens to mint to the deployer.
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply_);
    }

    /**
     * @dev Function to mint new tokens. Only callable by the owner.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens. Only callable by the owner.
     * @param from The address whose tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burn(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
    }
}
```
