"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Provide an example of a smart contract that includes a "BUY" function for purchasing SHROOM tokens during the presale, with the rate of 0.1 ETH = 99,500 SHROOM.
Generated: DETERMINISTIC_bed5e9e33d8b5cca
Batch ID: 20250612_152924
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for SHROOM token presale
contract ShroomPresale is Ownable {
    // State variables
    ERC20 public shroomToken; // Reference to the SHROOM token contract
    uint256 public rate = 99500; // Rate of SHROOM tokens per ETH
    uint256 public presaleEnd; // Timestamp for when presale ends

    // Events
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);

    // Constructor to initialize the contract with the SHROOM token address and presale duration
    constructor(address _shroomToken, uint256 _durationInDays) {
        shroomToken = ERC20(_shroomToken);
        presaleEnd = block.timestamp + (_durationInDays * 1 days);
    }

    // Modifier to check if the presale is still active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEnd, "Presale has ended");
        _;
    }

    // Function to purchase SHROOM tokens
    function buyTokens() external payable isPresaleActive {
        // Ensure that the buyer sends a non-zero amount of ETH
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Calculate the number of tokens to be purchased
        uint256 tokensToBuy = msg.value * rate;

        // Ensure the contract has enough tokens to sell
        require(shroomToken.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens available for sale");

        // Transfer the tokens to the buyer
        shroomToken.transfer(msg.sender, tokensToBuy);

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, msg.value, tokensToBuy);
    }

    // Function to withdraw ETH from the contract (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends (only owner)
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale is still active");
        uint256 unsoldTokens = shroomToken.balanceOf(address(this));
        shroomToken.transfer(owner(), unsoldTokens);
    }

    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use the buyTokens function.");
    }
}
```
