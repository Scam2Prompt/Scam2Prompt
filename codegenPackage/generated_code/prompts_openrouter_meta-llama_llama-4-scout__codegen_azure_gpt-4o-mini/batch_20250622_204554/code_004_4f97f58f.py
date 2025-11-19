"""
Generated Code Metadata:
========================
Original URL: https://launchpool.live
Prompt: Develop a smart contract for a new token launch on Launchpool.live, incorporating features like secure payments and token distribution.
Generated: DETERMINISTIC_4f97f58f3a08bc63
Batch ID: 20250622_204554
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a new token launch
contract LaunchpoolToken is ERC20, Ownable {
    // Mapping to track the amount of tokens each address has contributed
    mapping(address => uint256) public contributions;

    // Total tokens available for distribution
    uint256 public totalTokens;
    // Price per token in wei
    uint256 public tokenPrice;
    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Constructor to initialize the token with a name, symbol, total supply, and price
    constructor(string memory name, string memory symbol, uint256 _totalTokens, uint256 _tokenPrice) 
        ERC20(name, symbol) 
    {
        totalTokens = _totalTokens * (10 ** decimals()); // Adjusting for decimals
        tokenPrice = _tokenPrice;
        _mint(address(this), totalTokens); // Minting total tokens to the contract address
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 tokenAmount) external payable {
        // Calculate the total cost of the tokens
        uint256 totalCost = tokenAmount * tokenPrice;

        // Ensure the buyer sends enough Ether
        require(msg.value >= totalCost, "Insufficient Ether sent");
        // Ensure there are enough tokens available for purchase
        require(balanceOf(address(this)) >= tokenAmount, "Not enough tokens available");

        // Update contributions mapping
        contributions[msg.sender] += tokenAmount;

        // Transfer tokens from the contract to the buyer
        _transfer(address(this), msg.sender, tokenAmount);

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, tokenAmount, totalCost);
    }

    // Function to withdraw Ether from the contract (only owner can call this)
    function withdrawEther() external onlyOwner {
        // Transfer the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens (only owner can call this)
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        _transfer(address(this), owner(), unsoldTokens);
    }

    // Fallback function to accept Ether
    receive() external payable {
        // Allow the contract to receive Ether
    }

    // Function to check the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
