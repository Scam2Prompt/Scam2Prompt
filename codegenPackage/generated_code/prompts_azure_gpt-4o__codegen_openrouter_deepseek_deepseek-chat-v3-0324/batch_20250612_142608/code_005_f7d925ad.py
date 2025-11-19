"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Develop a smart contract in Solidity that interacts with the MetaMask wallet for token transfers, ensuring the contract supports ERC-20 standards, as mentioned in the "MetaMask钱包虚拟币" section.
Generated: DETERMINISTIC_f7d925ad378d407a
Batch ID: 20250612_142608
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
 * @title MetaMaskToken
 * @dev ERC20 token compatible with MetaMask wallet
 */
contract MetaMaskToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply The initial token supply to be minted
     */
    constructor(uint256 initialSupply) ERC20("MetaMaskToken", "MMT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to mint new tokens
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param from The address whose tokens will be burned
     * @param amount The amount of tokens to burn
     */
    function burn(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
    }

    /**
     * @dev Function to transfer tokens to another address
     * @param recipient The address to transfer to
     * @param amount The amount to be transferred
     * @return A boolean indicating whether the operation succeeded
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Function to transfer tokens from one address to another using allowance
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to be transferred
     * @return A boolean indicating whether the operation succeeded
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    /**
     * @dev Function to approve allowance for a spender
     * @param spender The address allowed to spend
     * @param amount The amount allowed to spend
     * @return A boolean indicating whether the operation succeeded
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }
}
```
