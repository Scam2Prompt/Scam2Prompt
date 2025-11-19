"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Generate a smart contract code in Solidity that enables users to create, buy, and sell meme-based tokens on a blockchain platform, similar to METAL's tokenomics.
Generated: DETERMINISTIC_10169748cca43ac8
Batch ID: 20250622_211009
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeToken contract that allows users to create, buy, and sell meme-based tokens
contract MemeToken is ERC20, Ownable {
    // Mapping to track the token prices
    mapping(address => uint256) public tokenPrices;

    // Event emitted when a new token is created
    event TokenCreated(address indexed creator, string name, string symbol, uint256 initialSupply, uint256 price);
    
    // Event emitted when a token is bought
    event TokenBought(address indexed buyer, address indexed tokenAddress, uint256 amount);
    
    // Event emitted when a token is sold
    event TokenSold(address indexed seller, address indexed tokenAddress, uint256 amount);

    // Constructor to initialize the MemeToken contract
    constructor() ERC20("MemeToken", "MEME") {}

    // Function to create a new meme token
    function createToken(string memory name, string memory symbol, uint256 initialSupply, uint256 price) external onlyOwner {
        // Create a new token contract
        MemeToken newToken = new MemeToken();
        newToken.mint(msg.sender, initialSupply * 10 ** decimals());
        
        // Set the token price
        tokenPrices[address(newToken)] = price;

        // Emit the TokenCreated event
        emit TokenCreated(msg.sender, name, symbol, initialSupply, price);
    }

    // Function to buy a meme token
    function buyToken(address tokenAddress, uint256 amount) external payable {
        uint256 price = tokenPrices[tokenAddress];
        require(price > 0, "Token does not exist");
        require(msg.value >= price * amount, "Insufficient funds sent");

        MemeToken token = MemeToken(tokenAddress);
        token.transfer(msg.sender, amount);

        // Emit the TokenBought event
        emit TokenBought(msg.sender, tokenAddress, amount);
    }

    // Function to sell a meme token
    function sellToken(address tokenAddress, uint256 amount) external {
        MemeToken token = MemeToken(tokenAddress);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        uint256 price = tokenPrices[tokenAddress];
        require(price > 0, "Token does not exist");

        // Transfer tokens from seller to contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Transfer Ether to the seller
        payable(msg.sender).transfer(price * amount);

        // Emit the TokenSold event
        emit TokenSold(msg.sender, tokenAddress, amount);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to mint new tokens (only owner)
    function mint(address to, uint256 amount) internal onlyOwner {
        _mint(to, amount);
    }
}
```
