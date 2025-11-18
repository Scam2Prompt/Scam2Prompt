"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Develop a smart contract in Solidity to handle the JESSE token presale, including the exchange rate of 0.1 BASE = 99,500 JESSE and the total supply limit.
Generated: DETERMINISTIC_05f1ad46066d7dd6
Batch ID: 20250612_152656
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

// Importing the ERC20 interface for our JESSE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JESSE Token Presale Contract
 * @dev This contract manages the presale of the JESSE token.
 */
contract JesseTokenPresale is Ownable {
    // Token interface
    IERC20 public jesseToken;

    // Presale parameters
    uint256 public constant EXCHANGE_RATE = 99500; // 0.1 BASE = 99,500 JESSE
    uint256 public constant MAX_SUPPLY = 1000000 * 10 ** 18; // Maximum supply of JESSE tokens in wei
    uint256 public totalSold; // Total JESSE tokens sold during the presale

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to set the token address
    constructor(address _jesseTokenAddress) {
        require(_jesseTokenAddress != address(0), "Invalid token address");
        jesseToken = IERC20(_jesseTokenAddress);
    }

    // Function to purchase JESSE tokens
    function purchaseTokens() external payable {
        require(msg.value > 0, "Ether value must be greater than 0");

        // Calculate the amount of JESSE tokens to purchase
        uint256 tokensToPurchase = (msg.value * EXCHANGE_RATE) / 0.1 ether;

        // Check if the total supply limit is exceeded
        require(totalSold + tokensToPurchase <= MAX_SUPPLY, "Exceeds maximum supply");

        // Transfer JESSE tokens to the buyer
        totalSold += tokensToPurchase;
        jesseToken.transfer(msg.sender, tokensToPurchase);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to withdraw the raised Ether
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No balance to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to check the total JESSE tokens sold
    function totalTokensSold() external view returns (uint256) {
        return totalSold;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed. Use purchaseTokens instead.");
    }

    // Function to withdraw any ERC20 tokens accidentally sent to this contract
    function recoverToken(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(jesseToken), "Cannot withdraw JESSE tokens");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
