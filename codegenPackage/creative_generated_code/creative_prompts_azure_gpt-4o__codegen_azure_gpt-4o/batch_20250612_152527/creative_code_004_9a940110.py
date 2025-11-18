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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BitcoinDogsPresale {
    // Address of the $0DOG token contract
    IERC20 public zeroDogToken;

    // Owner of the presale contract
    address public owner;

    // Mapping to store submitted BTC wallet addresses for each participant
    mapping(address => string) public btcWallets;

    // Event emitted when a purchase is made
    event TokensPurchased(
        address indexed buyer,
        uint256 amount,
        string btcWallet
    );

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    // Takes the address of the $0DOG token contract as input
    constructor(address _zeroDogToken) {
        require(_zeroDogToken != address(0), "Invalid token address");
        zeroDogToken = IERC20(_zeroDogToken);
        owner = msg.sender;
    }

    // Function to purchase $0DOG tokens
    // Requires the buyer to submit their BTC wallet address
    function purchaseTokens(uint256 amount, string calldata btcWallet) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(btcWallet).length > 0, "BTC wallet address is required");
        require(
            zeroDogToken.balanceOf(address(this)) >= amount,
            "Insufficient token balance in presale contract"
        );

        // Transfer the tokens to the buyer
        bool success = zeroDogToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Store the BTC wallet address of the buyer
        btcWallets[msg.sender] = btcWallet;

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, amount, btcWallet);
    }

    // Function for the owner to withdraw leftover $0DOG tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            zeroDogToken.balanceOf(address(this)) >= amount,
            "Insufficient token balance in presale contract"
        );

        // Transfer the tokens to the owner
        bool success = zeroDogToken.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }

    // Function for the owner to update the $0DOG token contract address
    function updateTokenAddress(address _zeroDogToken) external onlyOwner {
        require(_zeroDogToken != address(0), "Invalid token address");
        zeroDogToken = IERC20(_zeroDogToken);
    }
}
```
