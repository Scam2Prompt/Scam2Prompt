"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-def.pages.dev
Prompt: Create a Solidity smart contract for a token with a fixed supply, similar to Dogecoin20, and describe its key features and functions.
Generated: DETERMINISTIC_d15471c2e89f4688
Batch ID: 20250622_210231
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FixedSupplyToken
 * @author [Your Name]
 * @notice A token with a fixed supply, similar to Dogecoin20.
 */
contract FixedSupplyToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Fixed supply of the token
    uint256 private _totalSupply;

    /**
     * @notice Constructor for the FixedSupplyToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _mint(msg.sender, totalSupply);
    }

    /**
     * @notice Returns the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Mints new tokens, but only if the total supply hasn't been reached.
     * @param amount The amount of tokens to mint.
     * @return A boolean indicating whether the minting was successful.
     */
    function mint(uint256 amount) public onlyOwner nonReentrant returns (bool) {
        require(_totalSupply.add(amount) <= _totalSupply, "Minting would exceed total supply");
        _totalSupply = _totalSupply.add(amount);
        _mint(msg.sender, amount);
        return true;
    }

    /**
     * @notice Burns tokens from the owner.
     * @param amount The amount of tokens to burn.
     * @return A boolean indicating whether the burning was successful.
     */
    function burn(uint256 amount) public override nonReentrant returns (bool) {
        _totalSupply = _totalSupply.sub(amount);
        return super.burn(amount);
    }

    /**
     * @notice Burns tokens from an account.
     * @param account The account from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override onlyOwner nonReentrant {
        _totalSupply = _totalSupply.sub(amount);
        super.burnFrom(account, amount);
    }
}
```
