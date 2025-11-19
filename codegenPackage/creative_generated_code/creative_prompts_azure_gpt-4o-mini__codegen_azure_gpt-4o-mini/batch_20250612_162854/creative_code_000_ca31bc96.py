"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: How can I implement the Moxie Protocol to create Fan Tokens for my Farcaster channel using smart contracts?
Generated: DETERMINISTIC_ca31bc9678edc68b
Batch ID: 20250612_162854
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
 * @title FanToken
 * @dev Implementation of the Moxie Protocol to create Fan Tokens.
 */
contract FanToken is ERC20, Ownable {
    // Mapping of addresses to their respective token balances
    mapping(address => uint256) private _balances;

    /**
     * @dev Emitted when tokens are minted.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens minted.
     */
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Emitted when tokens are burned.
     * @param from The address that burned the tokens.
     * @param amount The amount of tokens burned.
     */
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /**
     * @dev Mint new tokens.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burn tokens from the message sender's account.
     * @param amount The amount of tokens to burn.
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function getBalance(address account) external view returns (uint256) {
        require(account != address(0), "Cannot query the zero address");
        return balanceOf(account);
    }
}
```

In this Solidity smart contract code, we implement the Moxie Protocol to create a Fan Token system. The `FanToken` contract allows for minting and burning of tokens and includes events for tracking token transactions. The contract is structured according to best practices and includes error handling to ensure safe operations.
