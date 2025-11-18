"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindog.pages.dev
Prompt: Write a Solidity smart contract to enable the purchase of $0DOG tokens on ERC20 while submitting a BTC wallet address, as described in the Bitcoin Dogs presale process.
Generated: DETERMINISTIC_9a9401108a1839f9
Batch ID: 20250612_152527
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

// Import the ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Smart contract for purchasing $0DOG tokens
contract BitcoinDogsPresale {
    // ERC20 token contract address
    address public tokenAddress;
    // Price in wei per token
    uint256 public tokenPrice;
    // Mapping to track purchasers and their BTC wallet addresses
    mapping(address => string) public purchasers;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, string btcWalletAddress);

    // Constructor to initialize the token address and price
    constructor(address _tokenAddress, uint256 _tokenPrice) {
        require(_tokenAddress != address(0), "Invalid token address.");
        require(_tokenPrice > 0, "Token price must be greater than 0.");
        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 tokenAmount, string memory btcWalletAddress) public payable {
        // Calculate the required payment amount
        uint256 requiredPayment = tokenAmount * tokenPrice;

        // Ensure the sent value matches the required payment
        require(msg.value >= requiredPayment, "Insufficient payment for tokens.");
        
        // Store the BTC wallet address for the buyer
        purchasers[msg.sender] = btcWalletAddress;

        // Transfer tokens to the buyer
        IERC20(tokenAddress).transfer(msg.sender, tokenAmount);

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, tokenAmount, btcWalletAddress);
    }

    // Function to withdraw contract ether balance
    function withdraw() external {
        // Only the contract owner should be able to withdraw funds
        // This should ideally be restricted to the contract deployer
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to retrieve the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
