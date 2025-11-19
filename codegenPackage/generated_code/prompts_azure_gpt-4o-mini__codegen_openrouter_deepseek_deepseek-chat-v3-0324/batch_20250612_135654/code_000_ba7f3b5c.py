"""
Generated Code Metadata:
========================
Original URL: https://cumcoin.io
Prompt: Generate a smart contract for a meme coin similar to CUM Coin, focusing on cross-border liquidity and zero tax on transactions.
Generated: DETERMINISTIC_ba7f3b5ca7c71626
Batch ID: 20250612_135654
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

contract MemeCoin is ERC20, Ownable {
    /**
     * @dev Initializes the contract with initial supply and assigns all tokens to the deployer.
     * @param initialSupply The initial token supply to be minted.
     */
    constructor(uint256 initialSupply) ERC20("MemeCoin", "MEME") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the transfer function to ensure zero tax on transactions.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides the transferFrom function to ensure zero tax on transactions.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    /**
     * @dev Adds liquidity to a cross-border liquidity pool.
     * @param amount The amount of tokens to add to the liquidity pool.
     */
    function addLiquidity(uint256 amount) external onlyOwner {
        _transfer(_msgSender(), address(this), amount);
    }

    /**
     * @dev Removes liquidity from the cross-border liquidity pool.
     * @param amount The amount of tokens to remove from the liquidity pool.
     */
    function removeLiquidity(uint256 amount) external onlyOwner {
        _transfer(address(this), _msgSender(), amount);
    }
}
```
