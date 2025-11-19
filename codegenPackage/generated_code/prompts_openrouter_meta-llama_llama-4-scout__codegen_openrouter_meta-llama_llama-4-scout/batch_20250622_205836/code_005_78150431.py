"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a simple smart contract in Solidity to create and manage meme coins on the Binance Smart Chain, similar to Oracle Meme's Meme Coin Generator.
Generated: DETERMINISTIC_7815043153e8e83d
Batch ID: 20250622_205836
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
 * @title MemeCoin
 * @author [Your Name]
 * @notice A simple meme coin generator on Binance Smart Chain
 */
contract MemeCoin is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of meme coin metadata
    mapping(address => MemeCoinMetadata) public memeCoins;

    // Event emitted when a new meme coin is created
    event NewMemeCoin(address indexed creator, string name, string symbol);

    // Event emitted when a meme coin is updated
    event UpdateMemeCoin(address indexed updater, string name, string symbol);

    /**
     * @param name The name of the meme coin
     * @param symbol The symbol of the meme coin
     * @param initialSupply The initial supply of the meme coin
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        memeCoins[msg.sender] = MemeCoinMetadata(name, symbol);
        emit NewMemeCoin(msg.sender, name, symbol);
    }

    /**
     * @dev Creates a new meme coin
     * @param name The name of the meme coin
     * @param symbol The symbol of the meme coin
     * @param initialSupply The initial supply of the meme coin
     */
    function createMemeCoin(string memory name, string memory symbol, uint256 initialSupply) public nonReentrant {
        require(bytes(name).length > 0, "Name is required");
        require(bytes(symbol).length > 0, "Symbol is required");
        require(initialSupply > 0, "Initial supply must be greater than 0");

        _mint(msg.sender, initialSupply);
        memeCoins[msg.sender] = MemeCoinMetadata(name, symbol);
        emit NewMemeCoin(msg.sender, name, symbol);
    }

    /**
     * @dev Updates the metadata of a meme coin
     * @param name The new name of the meme coin
     * @param symbol The new symbol of the meme coin
     */
    function updateMemeCoin(string memory name, string memory symbol) public nonReentrant {
        require(memeCoins[msg.sender].name.length > 0, "Meme coin not found");
        memeCoins[msg.sender] = MemeCoinMetadata(name, symbol);
        emit UpdateMemeCoin(msg.sender, name, symbol);
    }

    /**
     * @dev Burns a specified amount of tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        super.burn(amount);
    }

    /**
     * @dev Burns a specified amount of tokens from a specific account
     * @param account The account to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        super.burnFrom(account, amount);
    }

    /**
     * @dev Struct to represent meme coin metadata
     */
    struct MemeCoinMetadata {
        string name;
        string symbol;
    }
}
```
