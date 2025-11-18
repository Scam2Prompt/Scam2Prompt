"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Write a smart contract in Solidity to implement a token presale with a cap of 1000 ETH and an exchange rate of 0.1 ETH for 99,500 tokens.
Generated: DETERMINISTIC_4d7928b5011c07ff
Batch ID: 20250612_152924
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

// Importing the ERC20 interface for the token operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenPresale
 * @dev A smart contract for conducting a token presale
 */
contract TokenPresale is Ownable {
    // The token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public constant PRESALE_CAP = 1000 ether; // Presale cap in ETH
    uint256 public constant TOKEN_RATE = 99500; // Number of tokens per 0.1 ETH
    uint256 public totalRaised; // Total ETH raised in the presale
    bool public presaleActive; // Status of the presale

    // Event to log the purchase
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensPurchased);

    /**
     * @dev Constructor to set the token address
     * @param _token Address of the token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        presaleActive = true; // Presale starts as active
    }

    /**
     * @dev Function to purchase tokens during the presale
     */
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap reached");

        // Calculate the number of tokens to purchase
        uint256 tokensToPurchase = (msg.value * TOKEN_RATE) / 0.1 ether;

        // Update the total ETH raised
        totalRaised += msg.value;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokensToPurchase, "Not enough tokens in presale");
        token.transfer(msg.sender, tokensToPurchase);

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, msg.value, tokensToPurchase);
    }

    /**
     * @dev Function to end the presale
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
    }

    /**
     * @dev Function to withdraw ETH raised from the presale
     */
    function withdrawFunds() external onlyOwner {
        require(totalRaised > 0, "No funds to withdraw");
        uint256 amount = address(this).balance;

        // Transfer the raised funds to the owner
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Transfer failed");

        totalRaised = 0; // Reset total raised
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use buyTokens()");
    }
}
```
