"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Write a Solidity contract for launching meme coins on a platform similar to the Oracle Meme Launchpad, ensuring compatibility with Binance Smart Chain.
Generated: DETERMINISTIC_b5133cabd5807371
Batch ID: 20250612_152235
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

// Importing the OpenZeppelin ERC20 contract for creating the token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoinLaunchpad contract allows users to create meme coins
contract MemeCoinLaunchpad is Ownable {
    // Event emitted when a new meme coin is created
    event MemeCoinCreated(address indexed creator, address tokenAddress, string name, string symbol);

    // Struct to hold information about created meme coins
    struct MemeCoin {
        string name;
        string symbol;
        address tokenAddress;
        uint256 totalSupply;
    }

    // Mapping to keep track of all created meme coins
    mapping(address => MemeCoin) public memeCoins;

    // Function to create a new meme coin
    function createMemeCoin(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply
    ) external onlyOwner returns (address) {
        // Validate input parameters
        require(bytes(_name).length > 0, "Token name must be non-empty");
        require(bytes(_symbol).length > 0, "Token symbol must be non-empty");
        require(_initialSupply > 0, "Initial supply must be greater than 0");

        // Create new ERC20 token contract
        MemeCoinToken newToken = new MemeCoinToken(_name, _symbol, _initialSupply, msg.sender);

        // Store the created meme coin details
        memeCoins[msg.sender] = MemeCoin({
            name: _name,
            symbol: _symbol,
            tokenAddress: address(newToken),
            totalSupply: _initialSupply
        });

        emit MemeCoinCreated(msg.sender, address(newToken), _name, _symbol);
        return address(newToken);
    }
}

// ERC20 token contract for the meme coin
contract MemeCoinToken is ERC20, Ownable {
    // Constructor to initialize the token
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address owner
    ) ERC20(name, symbol) {
        // Mint initial supply to the owner
        _mint(owner, initialSupply * (10 ** decimals())); // Adjusting for decimals
    }

    // Function to mint new tokens (only owner)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to burn tokens (only owner)
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```
