"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordinalmarthub.pages.dev
Prompt: Generate code to fix issues related to presale token buying, claiming, and withdrawal using the rectification features outlined on the website.
Generated: DETERMINISTIC_d8e1b607af0f35c6
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready code snippet that addresses presale token buying, claiming, and withdrawal issues in Solidity (a common language for smart contracts). This example assumes ERC20-compatible tokens.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PresaleTokenManager
 * @dev Manages presale token buying, claiming, and withdrawal with proper error handling and security.
 */
contract PresaleTokenManager {
    // State variables
    address public owner;                        // Contract owner
    address public tokenAddress;                 // ERC20 token address for presale
    uint256 public presalePrice;                 // Price per token in wei
    uint256 public presaleCap;                   // Maximum tokens available for presale
    uint256 public totalSold;                    // Total tokens sold in presale
    bool public isClaimEnabled;                  // Flag for enabling/disabling claims

    mapping(address => uint256) public balances; // User balances for claiming tokens

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed user, uint256 amount);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleOpen() {
        require(totalSold < presaleCap, "Presale cap reached");
        _;
    }

    modifier claimEnabled() {
        require(isClaimEnabled, "Claiming is not enabled");
        _;
    }

    // Constructor
    constructor(address _tokenAddress, uint256 _presalePrice, uint256 _presaleCap) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presalePrice = _presalePrice;
        presaleCap = _presaleCap;
    }

    /**
     * @dev Allows users to buy presale tokens.
     * @param amount The number of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable presaleOpen {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * presalePrice, "Incorrect ETH value sent");
        require(totalSold + amount <= presaleCap, "Purchase exceeds presale cap");

        totalSold += amount;
        balances[msg.sender] += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their purchased tokens after presale ends.
     */
    function claimTokens() external claimEnabled {
        uint256 userBalance = balances[msg.sender];
        require(userBalance > 0, "No tokens to claim");

        balances[msg.sender] = 0; // Reset balance before transfer to prevent reentrancy
        require(
            IERC20(tokenAddress).transfer(msg.sender, userBalance),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, userBalance);
    }

    /**
     * @dev Allows the owner to withdraw collected funds.
     * @param recipient The address to receive the funds.
     */
    function withdrawFunds(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");

        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = recipient.call{value: balance}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(recipient, balance);
    }

    /**
     * @dev Enables or disables the claiming of tokens.
     * @param enabled Boolean value to enable or disable claims.
     */
    function setClaimEnabled(bool enabled) external onlyOwner {
        isClaimEnabled = enabled;
    }

    /**
     * @dev Updates the presale token price.
     * @param newPrice The new price per token in wei.
     */
    function updatePresalePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        presalePrice = newPrice;
    }

    /**
     * @dev Updates the presale cap.
     * @param newCap The new cap for presale tokens.
     */
    function updatePresaleCap(uint256 newCap) external onlyOwner {
        require(newCap >= totalSold, "New cap must be greater than or equal to sold tokens");
        presaleCap = newCap;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code addresses common presale-related issues, including user balance tracking, token claiming, and withdrawal of funds. It also incorporates security best practices like preventing reentrancy and handling edge cases effectively.
