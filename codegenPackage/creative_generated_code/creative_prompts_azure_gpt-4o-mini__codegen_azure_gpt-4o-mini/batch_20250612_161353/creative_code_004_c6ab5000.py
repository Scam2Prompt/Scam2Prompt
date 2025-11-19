"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phoenixai-art.pages.dev
Prompt: Create a sample smart contract for the PXAI token, ensuring it includes features for buy-back and burn mechanisms as mentioned in the Phoenix AI tokenomics section.
Generated: DETERMINISTIC_c6ab5000ca69276e
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PXAIToken
 * @dev This contract implements the PXAI token with buy-back and burn mechanisms.
 */
contract PXAIToken is ERC20, Ownable {
    // Events
    event BuyBack(address indexed buyer, uint256 amount);
    event TokensBurned(address indexed burner, uint256 amount);
    
    // Buy-back percentage in basis points (e.g., 500 = 5%)
    uint256 public buyBackPercentage = 500; 
    // Total supply cap
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** decimals();

    // Constructor that initializes the token with a name and symbol
    constructor() ERC20("PXAI Token", "PXAI") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    // Function to buy back tokens and burn them
    function buyBack(uint256 amount) external payable onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "ETH value must be greater than zero");

        // Calculate the amount of tokens to buy back
        uint256 tokensToBuyBack = (msg.value * buyBackPercentage) / 10_000;
        require(tokensToBuyBack <= balanceOf(address(this)), "Insufficient tokens in contract");

        // Transfer ETH to the contract
        (bool success,) = address(this).call{ value: msg.value }("");
        require(success, "Failed to send Ether");

        // Transfer tokens from the contract to the owner and burn them
        _transfer(address(this), owner(), tokensToBuyBack);
        _burn(owner(), tokensToBuyBack);

        emit BuyBack(msg.sender, tokensToBuyBack);
        emit TokensBurned(owner(), tokensToBuyBack);
    }

    // Function to mint new tokens (only owner can call)
    function mintTokens(uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Cannot exceed max supply");
        _mint(msg.sender, amount);
    }

    // Function to set the buy-back percentage (only owner can call)
    function setBuyBackPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Percentage must be in basis points (max 10000)");
        buyBackPercentage = newPercentage;
    }

    // Function to withdraw Ether from the contract (only owner can call)
    function withdrawEther() external onlyOwner {
        (bool success,) = owner().call{ value: address(this).balance }("");
        require(success, "Failed to withdraw Ether");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
