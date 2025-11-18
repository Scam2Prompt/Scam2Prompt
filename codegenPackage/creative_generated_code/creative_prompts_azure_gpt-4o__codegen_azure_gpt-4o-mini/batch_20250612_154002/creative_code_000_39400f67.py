"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-eth.vip
Prompt: Write a smart contract in Solidity that implements an ERC-20 token with custom functionality, referencing best practices for Ethereum-based DeFi applications.
Generated: DETERMINISTIC_39400f6730bd3a65
Batch ID: 20250612_154002
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CustomERC20Token
 * @dev Implementation of a custom ERC20 token with minting and burning functionalities.
 */
contract CustomERC20Token is ERC20, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);
    
    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Sets the name and symbol of the token during deployment.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Allows the owner to mint new tokens.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Can't mint to the zero address");
        require(amount > 0, "Mint amount should be greater than zero");
        
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from a specific address.
     * @param from The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Can't burn from the zero address");
        require(amount > 0, "Burn amount should be greater than zero");
        require(balanceOf(from) >= amount, "Burn amount exceeds balance");
        
        _burn(from, amount);
        emit TokensBurned(from, amount);
    }

    /**
     * @dev Allows users to burn their own tokens to reduce the total supply.
     * @param amount The amount of tokens to burn.
     */
    function burnSelf(uint256 amount) external {
        require(amount > 0, "Burn amount should be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Burn amount exceeds balance");
        
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override transfer function to add custom functionality if needed in the future.
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for transfer");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override transferFrom function to add custom functionality if needed in the future.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");
        require(allowance(sender, msg.sender) >= amount, "Transfer amount exceeds allowance");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
