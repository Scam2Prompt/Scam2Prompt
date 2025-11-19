"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-brc20.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the public sale of the $BRC20DEX token, accepting ETH, BSC, BUSD, and USDT as payment methods.
Generated: DETERMINISTIC_a07d986141c444d8
Batch ID: 20250612_160656
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BRC20DEXSale is Ownable {
    // The token being sold
    IERC20 public brc20Token;

    // Price of the token in ETH
    uint256 public tokenPriceETH;
    
    // Price of the token in BSC (assumed to be 1:1 for simplicity)
    uint256 public tokenPriceBSC;

    // Mapping to keep track of total tokens sold
    uint256 public tokensSold;

    // Event to log token purchase
    event TokensPurchased(address indexed buyer, uint256 amount, string paymentMethod);

    // Constructor to initialize the token and prices
    constructor(IERC20 _token, uint256 _tokenPriceETH, uint256 _tokenPriceBSC) {
        brc20Token = _token;
        tokenPriceETH = _tokenPriceETH;
        tokenPriceBSC = _tokenPriceBSC;
    }

    // Modifier to check if the sale is active (can be implemented as needed)
    modifier saleActive() {
        // Placeholder for sale active check
        require(tokensSold < brc20Token.balanceOf(address(this)), "Sale has ended");
        _;
    }

    // Function to purchase tokens with ETH
    function purchaseWithETH(uint256 amount) external payable saleActive {
        require(msg.value == amount * tokenPriceETH, "Incorrect ETH amount sent");
        
        tokensSold += amount;

        // Transfer tokens to buyer
        require(brc20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount, "ETH");
    }

    // Function to purchase tokens with BUSD
    function purchaseWithBUSD(IERC20 busdToken, uint256 amount) external saleActive {
        require(busdToken.transferFrom(msg.sender, address(this), amount * tokenPriceBSC), "BUSD Transfer failed");
        
        tokensSold += amount;

        // Transfer tokens to buyer
        require(brc20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount, "BUSD");
    }

    // Function to withdraw ETH and BUSD from the contract
    function withdrawFunds(IERC20 busdToken) external onlyOwner {
        // Withdraw ETH
        payable(owner()).transfer(address(this).balance);

        // Withdraw BUSD
        uint256 busdBalance = busdToken.balanceOf(address(this));
        require(busdBalance > 0, "No BUSD to withdraw");
        require(busdToken.transfer(owner(), busdBalance), "BUSD transfer failed");
    }

    // Function to withdraw unsold tokens
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = brc20Token.balanceOf(address(this));
        require(unsoldTokens > 0, "No tokens to withdraw");
        require(brc20Token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    // Function to set new token prices (onlyOwner)
    function setTokenPrices(uint256 newPriceETH, uint256 newPriceBSC) external onlyOwner {
        tokenPriceETH = newPriceETH;
        tokenPriceBSC = newPriceBSC;
    }
}
```
