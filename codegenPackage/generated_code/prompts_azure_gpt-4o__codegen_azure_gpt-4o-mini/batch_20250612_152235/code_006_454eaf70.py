"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-claiim.pages.dev
Prompt: Write a Solidity smart contract to implement the presale mechanism for $GBTC tokens, ensuring users can purchase tokens with ETH, USDT, or card and stake them immediately for rewards.
Generated: DETERMINISTIC_454eaf70f839ec25
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for USDT token to allow transfers
interface IUSDT {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Interface for a hypothetical card payment processor
interface ICardPaymentProcessor {
    function processPayment(address payer, uint256 amount) external returns (bool);
}

// The GBTC presale contract
contract GBTCPresale is Ownable {
    // Token to be sold in the presale
    ERC20 public gbtcToken;

    // Presale parameters
    uint256 public presalePrice; // Price of 1 GBTC token in wei
    uint256 public totalTokensForSale; // Total tokens available for sale
    uint256 public tokensSold; // Total tokens sold during the presale

    // Events for logging purchases
    event TokensPurchased(address indexed buyer, uint256 amount, string paymentMethod);

    // Constructor to initialize the contract
    constructor(ERC20 _gbtcToken, uint256 _presalePrice, uint256 _totalTokensForSale) {
        gbtcToken = _gbtcToken;
        presalePrice = _presalePrice;
        totalTokensForSale = _totalTokensForSale;
    }

    // Function to purchase tokens with ETH
    function buyWithETH(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * presalePrice, "Incorrect ETH amount sent");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens available");

        tokensSold += amount;
        gbtcToken.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, "ETH");
    }

    // Function to purchase tokens with USDT
    function buyWithUSDT(uint256 amount, address usdtAddress) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens available");

        IUSDT usdt = IUSDT(usdtAddress);
        uint256 totalCost = amount * presalePrice;
        require(usdt.transferFrom(msg.sender, address(this), totalCost), "USDT transfer failed");

        tokensSold += amount;
        gbtcToken.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, "USDT");
    }

    // Function to purchase tokens with a card
    function buyWithCard(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens available");

        uint256 totalCost = amount * presalePrice;
        require(ICardPaymentProcessor(msg.sender).processPayment(msg.sender, totalCost), "Card payment failed");

        tokensSold += amount;
        gbtcToken.transfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount, "Card");
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw USDT from the contract
    function withdrawUSDT(address usdtAddress) external onlyOwner {
        IUSDT usdt = IUSDT(usdtAddress);
        uint256 balance = usdt.balanceOf(address(this));
        require(balance > 0, "No USDT to withdraw");
        usdt.transfer(owner(), balance);
    }

    // Function to withdraw GBTC tokens from the contract
    function withdrawGBTC(uint256 amount) external onlyOwner {
        require(amount <= gbtcToken.balanceOf(address(this)), "Not enough GBTC tokens to withdraw");
        gbtcToken.transfer(owner(), amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
