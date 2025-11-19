"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-in.pages.dev
Prompt: Generate a Solidity contract for a token with a fixed max supply and deflationary mechanics, similar to the $GFOX token described on Galaxy Fox's website.
Generated: DETERMINISTIC_dd9ad6ff12fcdf3a
Batch ID: 20250612_152235
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
 * @title Galaxy Fox Token Contract
 * @author [Your Name]
 * @notice A deflationary ERC20 token with a fixed max supply.
 */
contract GalaxyFoxToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    uint256 public _maxSupply;
    uint256 public _burnRate;

    /**
     * @notice Constructor for the Galaxy Fox Token contract.
     * @param maxSupply The maximum supply of tokens.
     * @param burnRate The burn rate for each transaction (in %).
     */
    constructor(uint256 maxSupply, uint256 burnRate) ERC20("Galaxy Fox Token", "GFOX") {
        require(maxSupply > 0, "Max supply must be greater than 0");
        require(burnRate >= 0 && burnRate <= 100, "Burn rate must be between 0 and 100");

        _maxSupply = maxSupply;
        _burnRate = burnRate;

        _mint(msg.sender, maxSupply);
    }

    /**
     * @notice Overrides the transfer function to apply deflationary mechanics.
     * @param from The sender of the tokens.
     * @param to The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = amount.mul(_burnRate).div(100);
        uint256 netAmount = amount.sub(burnAmount);

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, to, netAmount);

        return true;
    }

    /**
     * @notice Overrides the transferFrom function to apply deflationary mechanics.
     * @param from The sender of the tokens.
     * @param to The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 burnAmount = amount.mul(_burnRate).div(100);
        uint256 netAmount = amount.sub(burnAmount);

        _burn(from, burnAmount);
        _transfer(from, to, netAmount);

        return true;
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param account The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from the specified address, on behalf of the token owner.
     * @param account The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        _burnFrom(account, amount);
    }

    /**
     * @notice Internal function to burn tokens.
     * @param account The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "Cannot burn from the zero address");

        uint256 accountBalance = balanceOf(account);
        require(accountBalance >= amount, "Insufficient balance");

        _balances[account] = accountBalance.sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }

    /**
     * @notice Internal function to get the total supply of tokens.
     * @return The total supply of tokens.
     */
    function _totalSupply() internal view virtual override returns (uint256) {
        return _maxSupply - _balances[address(0)];
    }
}
```
