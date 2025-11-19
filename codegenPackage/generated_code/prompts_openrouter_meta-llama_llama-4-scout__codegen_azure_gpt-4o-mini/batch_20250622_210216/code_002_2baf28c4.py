"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-ai.web.app
Prompt: Develop a basic smart contract in Solidity for managing $SCOTTY token sales on a decentralized exchange (DEX).
Generated: DETERMINISTIC_2baf28c403ba984e
Batch ID: 20250622_210216
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

// Importing OpenZeppelin's ERC20 implementation for the $SCOTTY token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for the $SCOTTY token
contract ScottyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token details
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals
    uint256 public tokenPrice; // Price of one token in wei

    // Event emitted when tokens are bought
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Constructor to initialize the token and set the initial price
    constructor(uint256 _tokenPrice) ERC20("ScottyToken", "$SCOTTY") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
        tokenPrice = _tokenPrice; // Set the token price
    }

    // Function to buy tokens
    function buyTokens(uint256 _amount) external payable {
        // Calculate the total cost of the tokens
        uint256 totalCost = _amount.mul(tokenPrice);
        
        // Ensure the buyer sends enough Ether
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Ensure the contract has enough tokens to sell
        require(balanceOf(owner()) >= _amount, "Not enough tokens available");

        // Transfer tokens from the owner to the buyer
        _transfer(owner(), msg.sender, _amount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount, totalCost);

        // Refund any excess Ether sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to update the token price (only owner can call)
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        tokenPrice = _newPrice;
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
