"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Explain how to integrate the DigiToads tokenomics into a decentralized application (dApp) for managing presale transactions.
Generated: DETERMINISTIC_8038ebc860d56d5b
Batch ID: 20250612_155235
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DigiToadsToken contract inherits from ERC20 and Ownable
contract DigiToadsToken is ERC20, Ownable {
    // Define presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensForSale; // Total tokens allocated for the presale
    uint256 public tokensSold; // Track the number of tokens sold during presale

    // Mapping to track presale participants and their purchases
    mapping(address => uint256) public presaleBalances;

    // Events to log important actions
    event PresalePurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Constructor to initialize the token with parameters
    constructor(
        string memory name,
        string memory symbol,
        uint256 _totalTokensForSale,
        uint256 _tokenPrice
    ) ERC20(name, symbol) {
        totalTokensForSale = _totalTokensForSale;
        tokenPrice = _tokenPrice;

        // Mint the total tokens for sale to the contract address
        _mint(address(this), _totalTokensForSale);
    }

    // Function to start the presale
    function startPresale(uint256 durationInDays) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + (durationInDays * 1 days);
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 amount) external payable {
        // Ensure the presale is active
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        
        // Calculate the total price for the requested amount of tokens
        uint256 totalCost = amount * tokenPrice;

        // Ensure the value sent matches the total cost
        require(msg.value == totalCost, "Incorrect Ether value sent");

        // Ensure there are enough tokens available for sale
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens available");

        // Update presale balances and tokens sold
        presaleBalances[msg.sender] += amount;
        tokensSold += amount;

        // Transfer tokens from contract to buyer
        _transfer(address(this), msg.sender, amount);

        // Emit event for purchase
        emit PresalePurchased(msg.sender, amount);
    }

    // Function to end the presale, only callable by the owner
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        emit PresaleEnded();
        // Additional logic can go here if needed (e.g., withdrawing funds)
    }

    // Function to withdraw collected Ether (only owner)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens (only owner)
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalTokensForSale - tokensSold;
        _transfer(address(this), owner(), unsoldTokens);
    }
}
```

This Solidity smart contract provides a robust foundation for integrating DigiToads tokenomics into a dApp for managing presale transactions. It includes features for starting and ending a presale, purchasing tokens, and proper error handling and logging through events.
