"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Design a Farcaster frame that utilizes Moxie Protocol's bonding curves for fan token pricing.
Generated: DETERMINISTIC_3db51b1d22c41a65
Batch ID: 20250622_211215
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Moxie Protocol's bonding curve
interface IMoxieBondingCurve {
    function buy(uint256 amount) external payable returns (uint256);
    function sell(uint256 amount) external returns (uint256);
    function getPrice(uint256 amount) external view returns (uint256);
}

// FanToken contract that utilizes Moxie Protocol's bonding curves
contract FanToken is ERC20, Ownable {
    // Instance of the Moxie Protocol's bonding curve
    IMoxieBondingCurve public bondingCurve;

    // Event emitted when tokens are bought
    event TokensBought(address indexed buyer, uint256 amount, uint256 cost);
    
    // Event emitted when tokens are sold
    event TokensSold(address indexed seller, uint256 amount, uint256 revenue);

    // Constructor to initialize the token and bonding curve
    constructor(string memory name, string memory symbol, address _bondingCurve) 
        ERC20(name, symbol) 
    {
        require(_bondingCurve != address(0), "Invalid bonding curve address");
        bondingCurve = IMoxieBondingCurve(_bondingCurve);
    }

    // Function to buy fan tokens using Ether
    function buyTokens(uint256 amount) external payable {
        // Calculate the price for the requested amount of tokens
        uint256 price = bondingCurve.getPrice(amount);
        require(msg.value >= price, "Insufficient Ether sent");

        // Buy tokens from the bonding curve
        uint256 tokensBought = bondingCurve.buy{value: msg.value}(amount);
        
        // Mint the bought tokens to the buyer
        _mint(msg.sender, tokensBought);

        // Emit the TokensBought event
        emit TokensBought(msg.sender, tokensBought, price);
    }

    // Function to sell fan tokens back to the bonding curve
    function sellTokens(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Approve the bonding curve to spend the tokens
        _approve(msg.sender, address(bondingCurve), amount);

        // Sell tokens to the bonding curve
        uint256 revenue = bondingCurve.sell(amount);
        
        // Burn the sold tokens
        _burn(msg.sender, amount);

        // Emit the TokensSold event
        emit TokensSold(msg.sender, amount, revenue);
        
        // Transfer the revenue to the seller
        payable(msg.sender).transfer(revenue);
    }

    // Function to withdraw any Ether from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
