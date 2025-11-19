"""
Generated Code Metadata:
========================
Original URL: https://anyinuairdrop.pages.dev
Prompt: Generate a smart contract code for a token with a fixed supply, similar to Any Inu's 420,690,000,000 tokens, on a blockchain platform like Ethereum or Binance Smart Chain.
Generated: DETERMINISTIC_0d296072ae52af44
Batch ID: 20250622_210802
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
 * @title FixedSupplyToken
 * @dev ERC20 token with a fixed supply of 420,690,000,000 tokens
 */
contract FixedSupplyToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 420690000000 * 10**18;

    /**
     * @dev Constructor that mints the total supply to the deployer
     */
    constructor() ERC20("Any Inu", "ANI") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Prevents any further minting of tokens
     * @param to The address that would receive the minted tokens
     * @param amount The amount of tokens to be minted
     */
    function _mint(address to, uint256 amount) internal virtual override {
        require(totalSupply() + amount <= MAX_SUPPLY, "FixedSupplyToken: Max supply exceeded");
        super._mint(to, amount);
    }

    /**
     * @dev Burns tokens from the caller's account
     * @param amount The amount of tokens to be burned
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burns tokens from a specified account (with allowance)
     * @param account The account to burn tokens from
     * @param amount The amount of tokens to be burned
     */
    function burnFrom(address account, uint256 amount) public {
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "FixedSupplyToken: burn amount exceeds allowance");
        _approve(account, msg.sender, currentAllowance - amount);
        _burn(account, amount);
    }
}
```
