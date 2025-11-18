"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogeclaim.pages.dev
Prompt: Create a smart contract on Ethereum (ERC20) that facilitates the purchase of $0DOG tokens during the presale and ensures token transfer to a connected BRC20 wallet address.
Generated: DETERMINISTIC_ed661dba6e2b6fde
Batch ID: 20250612_151343
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

/**
 * @title ERC20PresaleWithBRC20Transfer
 * @dev A smart contract for presale of $0DOG tokens with the ability to bind a connected BRC20 wallet address for token transfers.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract $0DOGPresale {
    // Address of the $0DOG ERC20 token contract
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Price per token (in wei)
    uint256 public tokenPrice;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Mapping to store connected BRC20 wallet addresses for users
    mapping(address => string) public brc20Wallets;

    // Event for successful purchase
    event TokensPurchased(address indexed purchaser, uint256 amount, string brc20Wallet);

    // Event for BRC20 wallet binding
    event BRC20WalletBound(address indexed user, string brc20Wallet);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Constructor to initialize contract properties
    constructor(address _tokenAddress, uint256 _tokenPrice) {
        require(_tokenAddress != address(0), "Token contract address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        token = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * @param amount The number of tokens to purchase.
     * @param brc20Wallet The connected BRC20 wallet address for token transfers.
     */
    function purchaseTokens(uint256 amount, string calldata brc20Wallet) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(brc20Wallet).length > 0, "BRC20 wallet address cannot be empty");
        require(msg.value == amount * tokenPrice, "Incorrect ETH amount sent");

        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance >= amount, "Not enough tokens available for sale");

        // Store the BRC20 wallet address
        brc20Wallets[msg.sender] = brc20Wallet;

        // Transfer tokens to the purchaser
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Update total tokens sold
        totalTokensSold += amount;

        emit TokensPurchased(msg.sender, amount, brc20Wallet);
    }

    /**
     * @dev Allows users to bind or update their connected BRC20 wallet address.
     * @param brc20Wallet The connected BRC20 wallet address.
     */
    function bindBRC20Wallet(string calldata brc20Wallet) external {
        require(bytes(brc20Wallet).length > 0, "BRC20 wallet address cannot be empty");

        // Store the BRC20 wallet address
        brc20Wallets[msg.sender] = brc20Wallet;

        emit BRC20WalletBound(msg.sender, brc20Wallet);
    }

    /**
     * @dev Allows the owner to withdraw collected ETH from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Allows the owner to retrieve unsold tokens.
     */
    function retrieveUnsoldTokens() external onlyOwner {
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance > 0, "No tokens available for retrieval");

        require(token.transfer(owner, tokenBalance), "Token transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfer not allowed");
    }

    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
