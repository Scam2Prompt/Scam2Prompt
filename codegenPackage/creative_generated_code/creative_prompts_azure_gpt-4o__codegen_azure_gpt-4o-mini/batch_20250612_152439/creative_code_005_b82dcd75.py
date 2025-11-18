"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe20-vip.web.app
Prompt: Develop a function in Solidity to handle token purchases and integrate it with a frontend wallet connection system.
Generated: DETERMINISTIC_b82dcd7577fb54bc
Batch ID: 20250612_152439
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

// Contract for handling token purchases
contract TokenSale is Ownable {
    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // State variables
    IERC20 public token;          // The token being sold
    uint256 public rate;          // Number of tokens per Ether
    uint256 public tokensSold;    // Total tokens sold

    // Constructor to initialize the token sale
    constructor(IERC20 _token, uint256 _rate) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rate > 0, "Rate must be greater than 0");
        
        token = _token;
        rate = _rate;
    }

    // Function to purchase tokens
    function buyTokens() external payable {
        // Validate the purchase amount
        require(msg.value > 0, "Ether value must be greater than 0");

        // Calculate the amount of tokens to purchase
        uint256 tokenAmount = msg.value * rate;
        
        // Ensure the contract has enough tokens for sale
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokenAmount);
        
        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);

        // Forward the Ether to the owner
        payable(owner()).transfer(msg.value);
    }

    // Function to withdraw unsold tokens after the sale
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        token.transfer(owner(), unsoldTokens);
    }

    // Function to update the token sale rate (only owner)
    function updateRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rate = newRate;
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEther() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        payable(owner()).transfer(contractBalance);
    }

    // Fallback function to accept Ether
    receive() external payable {
        buyTokens();
    }
}
```

**Frontend Integration:**
To connect this contract with a frontend wallet connection system (e.g., using Web3.js or Ethers.js), you can use the following JavaScript snippet as an example:

```javascript
import { ethers } from 'ethers';

// Connect to wallet
async function connectWallet() {
    if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        return signer;
    } else {
        alert("Please install MetaMask!");
    }
}

// Function to purchase tokens
async function purchaseTokens(tokenSaleAddress, amount) {
    const signer = await connectWallet();
    const tokenSaleContract = new ethers.Contract(tokenSaleAddress, tokenSaleABI, signer);

    const transaction = {
        value: ethers.utils.parseEther(amount.toString()) // Convert amount to Wei
    };

    try {
        const txResponse = await tokenSaleContract.buyTokens(transaction);
        await txResponse.wait(); // Wait for transaction to be mined
        console.log('Tokens purchased successfully!');
    } catch (error) {
        console.error('Transaction failed:', error);
    }
}
```

Make sure to replace `tokenSaleABI` with the actual ABI of your `TokenSale` contract and the `tokenSaleAddress` with the deployed contract address.
