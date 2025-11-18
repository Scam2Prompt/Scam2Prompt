"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba-3.web.app
Prompt: Write a smart contract in Solidity for an ICO token sale similar to Shiba 3.0, including features like a fixed total supply and the ability to purchase tokens with Ethereum.
Generated: DETERMINISTIC_c4f6f5cb37d220ad
Batch ID: 20250612_151354
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

// Importing the OpenZeppelin ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ICO Token contract
contract ICOToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 private constant _totalSupply = 1_000_000_000 * 10**18; // 1 Billion Tokens with 18 decimals
    // Token price in wei (1 token = 0.001 ETH)
    uint256 public tokenPrice = 0.001 ether;

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to mint total supply of tokens to the owner
    constructor() ERC20("ICO Token", "ICOT") {
        _mint(msg.sender, _totalSupply);
    }

    // Function to purchase tokens
    function buyTokens(uint256 tokenAmount) external payable {
        // Calculate the required Ether for the number of tokens requested
        uint256 cost = tokenAmount * tokenPrice;

        // Ensure the sender has sent enough Ether
        require(msg.value >= cost, "Insufficient Ether sent for the purchase");

        // Ensure the contract has enough tokens available for purchase
        require(balanceOf(owner()) >= tokenAmount, "Not enough tokens available");

        // Transfer tokens to the buyer
        _transfer(owner(), msg.sender, tokenAmount);

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, tokenAmount);
        
        // If there is excess Ether, refund the difference
        if (msg.value > cost) {
            (bool sent, ) = msg.sender.call{value: msg.value - cost}("");
            require(sent, "Failed to send Ether back to sender");
        }
    }

    // Function to withdraw Ether from the contract (only owner can call)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        (bool sent, ) = owner().call{value: balance}("");
        require(sent, "Failed to withdraw Ether");
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to check the contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
