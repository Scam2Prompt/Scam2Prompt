"""
Generated Code Metadata:
========================
Original URL: https://cowonbasenets.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a total supply of 1 billion, similar to the $COW token on Cow On Base.
Generated: DETERMINISTIC_a3b676e3bf9ce10d
Batch ID: 20250612_163840
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
 * @title COWToken
 * @dev ERC20 token with a fixed supply of 1 billion tokens, similar to $COW on Cow On Base.
 */
contract COWToken is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that mints the total supply to the deployer.
     */
    constructor() ERC20("COW Token", "COW") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Destroys `amount` tokens from the caller's account, reducing total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Destroys `amount` tokens from `account`, deducting from the caller's allowance.
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public {
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
    }
}
```
