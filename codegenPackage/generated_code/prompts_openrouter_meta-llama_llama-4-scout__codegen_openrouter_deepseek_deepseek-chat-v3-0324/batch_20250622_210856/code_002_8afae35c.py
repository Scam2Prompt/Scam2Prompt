"""
Generated Code Metadata:
========================
Original URL: https://presale-bybet0x5d.pages.dev
Prompt: Generate a smart contract code in Solidity for a token like $BBC, which can be used for payment, rewards, and voting rights on the Bybet platform.
Generated: DETERMINISTIC_8afae35cb441b0aa
Batch ID: 20250622_210856
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BBC is ERC20, ERC20Votes, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens

    constructor() ERC20("Bybet Coin", "BBC") ERC20Permit("Bybet Coin") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    // Overrides required by Solidity for ERC20Votes
    function _afterTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._afterTokenTransfer(from, to, amount);
    }

    function _mint(address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._mint(to, amount);
    }

    function _burn(address account, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._burn(account, amount);
    }

    /**
     * @dev Function to mint tokens (only owner)
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "BBC: Exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens from a specific account (only owner)
     * @param account The account to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public onlyOwner {
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
    }

    /**
     * @dev Function to transfer tokens to multiple addresses
     * @param recipients Array of recipient addresses
     * @param amounts Array of amounts to transfer
     */
    function batchTransfer(address[] memory recipients, uint256[] memory amounts) public {
        require(recipients.length == amounts.length, "BBC: Arrays length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            transfer(recipients[i], amounts[i]);
        }
    }
}
```
