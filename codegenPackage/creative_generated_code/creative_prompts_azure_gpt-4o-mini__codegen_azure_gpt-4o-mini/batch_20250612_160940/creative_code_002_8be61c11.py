"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to create their own meme coin on the Oracle Meme's Meme Coin Generator.
Generated: DETERMINISTIC_8be61c11772ef7af
Batch ID: 20250612_160940
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
 * @title MemeCoin
 * @dev This contract provides a simple structure to create a meme coin.
 * It extends the ERC20 standard from OpenZeppelin and is owned by the creator.
 */
contract MemeCoin is ERC20, Ownable {

    // Event to emit when a new meme coin is created
    event MemeCoinCreated(address indexed creator, string name, string symbol, uint256 initialSupply);

    /**
     * @dev Constructor to set the name and symbol of the token
     * @param name The name of the meme coin
     * @param symbol The symbol of the meme coin
     * @param initialSupply The initial supply of the meme coin in wei (1 token = 10^18 wei)
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply * 10 ** decimals()); // Mint initial supply to the creator
        emit MemeCoinCreated(msg.sender, name, symbol, initialSupply);
    }

    /**
     * @dev Allows the owner to mint new coins
     * @param account The account to which the new coins will be minted
     * @param amount The amount of new coins to mint
     */
    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn coins from an account
     * @param account The account from which the coins will be burned
     * @param amount The amount of coins to burn
     */
    function burn(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(account, amount);
    }
}

/**
 * @title MemeCoinGenerator
 * @dev This contract allows users to create their own meme coins.
 */
contract MemeCoinGenerator {
    
    // Mapping to keep track of created meme coins
    mapping(address => address[]) public userMemeCoins;

    /**
     * @dev Function to create a new meme coin
     * @param name The name of the meme coin
     * @param symbol The symbol of the meme coin
     * @param initialSupply The initial supply of the meme coin
     * @return newCoin Address of the newly created meme coin contract
     */
    function createMemeCoin(string memory name, string memory symbol, uint256 initialSupply) external returns (address newCoin) {
        // Create new MemeCoin contract
        MemeCoin memeCoin = new MemeCoin(name, symbol, initialSupply);
        userMemeCoins[msg.sender].push(address(memeCoin)); // Track the created coin
        return address(memeCoin);
    }

    /**
     * @dev Function to get all meme coins created by a user
     * @param user The address of the user
     * @return coins Array of addresses of the meme coins created by the user
     */
    function getUserMemeCoins(address user) external view returns (address[] memory coins) {
        return userMemeCoins[user];
    }
}
```
