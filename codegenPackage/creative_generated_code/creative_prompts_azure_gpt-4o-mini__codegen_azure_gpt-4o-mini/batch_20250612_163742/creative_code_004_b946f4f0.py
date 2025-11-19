"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiedan.vip
Prompt: Explain how to implement a buy/sell function for the $TIEDAN token using a smart contract in Solidity.
Generated: DETERMINISTIC_b946f4f078160ff7
Batch ID: 20250612_163742
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for secure token management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Declaring the TokenExchange contract which allows buying and selling of the $TIEDAN token
contract TokenExchange is Ownable {
    // The $TIEDAN token interface
    IERC20 public tiedanToken;

    // Event emitted when tokens are bought
    event TokensBought(address indexed buyer, uint256 amountSpent, uint256 tokensPurchased);

    // Event emitted when tokens are sold
    event TokensSold(address indexed seller, uint256 tokensSold, uint256 amountReceived);

    // Price of the $TIEDAN token in Wei (1 Ether = 10^18 Wei)
    uint256 public tokenPrice;

    // Constructor to initialize the token address and price
    constructor(IERC20 _tiedanToken, uint256 _tokenPrice) {
        tiedanToken = _tiedanToken;
        tokenPrice = _tokenPrice;
    }

    // Function to buy $TIEDAN tokens
    function buyTokens(uint256 _amount) external payable {
        // Calculate the cost to buy the specified amount of tokens
        uint256 cost = _amount * tokenPrice;

        // Require that the amount sent is equal to the cost
        require(msg.value >= cost, "Insufficient Ether sent");

        // Transfer $TIEDAN tokens to the buyer
        require(tiedanToken.balanceOf(address(this)) >= _amount, "Not enough tokens available");
        tiedanToken.transfer(msg.sender, _amount);

        // Emit the TokensBought event
        emit TokensBought(msg.sender, msg.value, _amount);
    }

    // Function to sell $TIEDAN tokens
    function sellTokens(uint256 _amount) external {
        // Require that the seller has enough tokens to sell
        require(tiedanToken.balanceOf(msg.sender) >= _amount, "Insufficient tokens");

        // Calculate the revenue from selling the specified amount of tokens
        uint256 revenue = _amount * tokenPrice;

        // Transfer $TIEDAN tokens from the seller to the contract
        tiedanToken.transferFrom(msg.sender, address(this), _amount);

        // Transfer Ether to the seller
        payable(msg.sender).transfer(revenue);

        // Emit the TokensSold event
        emit TokensSold(msg.sender, _amount, revenue);
    }

    // Function to update the token price (only owner can call)
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        tokenPrice = _newPrice;
    }

    // Function to withdraw Ether from the contract (only owner can call)
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw $TIEDAN tokens from the contract (only owner can call)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(tiedanToken.balanceOf(address(this)) >= _amount, "Not enough tokens in contract");
        tiedanToken.transfer(owner(), _amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
