"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-lnds.pages.dev
Prompt: Write a smart contract in Solidity to implement a token presale similar to the $DOG token presale described on the webpage, including features like a presale cap, ETH-to-token conversion rates, and wallet connection functionality.
Generated: DETERMINISTIC_cd1af7502abd27a6
Batch ID: 20250612_153400
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

// Importing OpenZeppelin ERC20 token contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for the token
contract TokenPresale is Ownable {
    // The token being sold
    ERC20 public token;

    // Presale parameters
    uint256 public presaleCap; // Maximum amount of ETH that can be raised
    uint256 public tokenPrice;  // Price of one token in wei
    uint256 public totalRaised;  // Total ETH raised in presale
    bool public presaleActive;    // Status of the presale

    // Mapping of participant addresses to their contributions
    mapping(address => uint256) public contributions;

    // Event for logging purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the presale with parameters
    constructor(
        ERC20 _token,
        uint256 _presaleCap,
        uint256 _tokenPrice
    ) {
        token = _token;
        presaleCap = _presaleCap;
        tokenPrice = _tokenPrice;
        presaleActive = true; // Start the presale as active
    }

    // Modifier to check if the presale is active
    modifier isActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Function to buy tokens during the presale
    function buyTokens() external payable isActive {
        require(msg.value > 0, "Must send ETH to buy tokens");
        require(totalRaised + msg.value <= presaleCap, "Presale cap reached");

        // Calculate the number of tokens to purchase
        uint256 tokenAmount = (msg.value * 1 ether) / tokenPrice;

        // Update total raised and contributions
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance in presale contract");
        token.transfer(msg.sender, tokenAmount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw remaining ETH after presale ends
    function withdrawFunds() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        presaleActive = false;
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }
}
```
