"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a total supply of 1 billion, similar to the $COW token on Cow On Base.
Generated: DETERMINISTIC_a3b676e3bf9ce10d
Batch ID: 20250612_163840
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
 * @title CowToken
 * @dev A simple ERC20 token with a fixed supply of 1 billion tokens.
 */
contract CowToken is ERC20, Ownable {

    // Total supply of the token
    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * (10 ** uint256(decimals()));

    /**
     * @dev Constructor that gives the msg.sender all of the existing tokens.
     */
    constructor() ERC20("Cow Token", "$COW") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens. Only the owner can call this function.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens from a specific account.
     * @param account The address of the account whose tokens will be burned.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) external {
        uint256 decreasedAllowance = allowance(account, msg.sender) - amount;
        require(decreasedAllowance >= 0, "ERC20: burn amount exceeds allowance");
        _approve(account, msg.sender, decreasedAllowance);
        _burn(account, amount);
    }
}
```
