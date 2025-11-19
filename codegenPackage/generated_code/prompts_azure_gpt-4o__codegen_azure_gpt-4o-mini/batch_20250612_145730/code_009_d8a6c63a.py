"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity contract to handle the presale process for $PEAB tokens, including wallet connection, token swapping, and staking functionality.
Generated: DETERMINISTIC_d8a6c63a63315603
Batch ID: 20250612_145730
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Presale contract for $PEAB tokens
contract PEABPresale is Ownable, ReentrancyGuard {
    // State variables
    IERC20 public peabToken; // The PEAB token contract
    uint256 public presalePrice; // Price of one PEAB token in wei
    uint256 public totalTokensForSale; // Total tokens available for presale
    uint256 public tokensSold; // Total tokens sold during presale
    mapping(address => uint256) public contributions; // Track contributions of each address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _peabToken, uint256 _presalePrice, uint256 _totalTokensForSale) {
        require(address(_peabToken) != address(0), "Invalid token address");
        require(_presalePrice > 0, "Price must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens must be greater than zero");

        peabToken = _peabToken;
        presalePrice = _presalePrice;
        totalTokensForSale = _totalTokensForSale;
    }

    // Function to purchase tokens during presale
    function buyTokens(uint256 tokenAmount) external payable nonReentrant {
        require(tokenAmount > 0, "Must purchase at least one token");
        require(tokensSold + tokenAmount <= totalTokensForSale, "Not enough tokens available");
        require(msg.value == tokenAmount * presalePrice, "Incorrect Ether value sent");

        contributions[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        // Transfer PEAB tokens to the buyer
        require(peabToken.transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalTokensForSale - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        require(peabToken.transfer(owner(), unsoldTokens), "Token transfer failed");
        emit TokensWithdrawn(owner(), unsoldTokens);
    }

    // Function to get the current presale status
    function getPresaleStatus() external view returns (uint256, uint256, uint256) {
        return (presalePrice, totalTokensForSale, tokensSold);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
