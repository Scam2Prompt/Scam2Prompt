"""
Generated Code Metadata:
========================
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a token sale that includes a presale cap of 1000 ETH and a conversion rate of 1 ETH to 99,500 BCKR.
Generated: DETERMINISTIC_f38f440d9d85d7fb
Batch ID: 20250612_160940
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

// Importing the OpenZeppelin ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenSale contract for managing the presale of BCKR tokens
contract TokenSale is Ownable {
    // State variables
    IERC20 public token; // The token being sold
    uint256 public constant PRESALE_CAP = 1000 ether; // Presale cap in ETH
    uint256 public constant RATE = 99500; // Conversion rate: 1 ETH = 99,500 BCKR
    uint256 public totalRaised; // Total ETH raised in the presale
    bool public presaleActive; // Flag to indicate if presale is active

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStatusChanged(bool isActive);

    // Constructor to initialize the token sale contract
    constructor(IERC20 _token) {
        token = _token;
        presaleActive = false; // Presale is initially inactive
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        presaleActive = true;
        emit PresaleStatusChanged(true);
    }

    // Function to stop the presale
    function stopPresale() external onlyOwner {
        presaleActive = false;
        emit PresaleStatusChanged(false);
    }

    // Function to purchase tokens during the presale
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap reached");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value * RATE;

        // Update the total amount raised
        totalRaised += msg.value;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokensToPurchase, "Not enough tokens available");
        token.transfer(msg.sender, tokensToPurchase);

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to withdraw funds raised from the presale
    function withdrawFunds() external onlyOwner {
        require(totalRaised > 0, "No funds to withdraw");
        uint256 amount = address(this).balance;

        // Transfer the raised ETH to the owner
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Transfer failed");

        totalRaised = 0; // Reset total raised after withdrawal
    }

    // Function to withdraw unsold tokens after the presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 unsoldTokens = token.balanceOf(address(this));

        // Transfer unsold tokens to the owner
        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to accept ETH
    receive() external payable {
        buyTokens(); // Allow direct ETH transfers to buy tokens
    }
}
```
