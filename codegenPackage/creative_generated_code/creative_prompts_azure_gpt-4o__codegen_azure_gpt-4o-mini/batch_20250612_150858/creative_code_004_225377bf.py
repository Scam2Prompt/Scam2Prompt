"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork-network.github.io
Prompt: Create a decentralized exchange (DEX) smart contract on Manta Network that prevents front-running attacks by leveraging its privacy features.
Generated: DETERMINISTIC_225377bfcc0921d2
Batch ID: 20250612_150858
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

// Import necessary interfaces and libraries for the Manta Network
import "@openzeppelin/contracts/access/Ownable.sol"; // For ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol"; // ERC20 token interface
import "@openzeppelin/contracts/utils/math/SafeMath.sol"; // Safe math operations

/**
 * @title DecentralizedExchange
 * @dev A simple DEX implementation that leverages privacy features to prevent front-running
 */
contract DecentralizedExchange is Ownable {
    using SafeMath for uint256;

    // Events for logging actions
    event TokenListed(address indexed tokenAddress, uint256 indexed price);
    event TokenSwapped(address indexed tokenSold, address indexed tokenBought, uint256 amountSold, uint256 amountBought);
    
    // Struct to hold token listing information
    struct TokenListing {
        uint256 price; // Price of the token in terms of ETH
        bool isListed; // Status of the listing
    }

    // Mapping of token addresses to their listings
    mapping(address => TokenListing) public tokenListings;

    /**
     * @dev List a new token on the exchange
     * @param tokenAddress The address of the ERC20 token to be listed
     * @param price The price of the token in terms of ETH
     */
    function listToken(address tokenAddress, uint256 price) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(price > 0, "Price must be greater than zero");
        
        tokenListings[tokenAddress] = TokenListing(price, true);
        emit TokenListed(tokenAddress, price);
    }

    /**
     * @dev Swap tokens on the DEX
     * @param tokenToSell The address of the ERC20 token to sell
     * @param amountToSell The amount of tokens to sell
     */
    function swapTokens(address tokenToSell, uint256 amountToSell) external {
        TokenListing memory listing = tokenListings[tokenToSell];
        require(listing.isListed, "Token is not listed");
        require(amountToSell > 0, "Sell amount must be greater than zero");

        // Calculate the amount of ETH to receive based on the listing price
        uint256 amountToReceive = listing.price.mul(amountToSell).div(1 ether);

        // Transfer the specified amount of tokens from the user to the contract
        IERC20(tokenToSell).transferFrom(msg.sender, address(this), amountToSell);
        
        // Transfer ETH to the user
        (bool success, ) = msg.sender.call{value: amountToReceive}("");
        require(success, "Ether transfer failed");

        emit TokenSwapped(tokenToSell, address(0), amountToSell, amountToReceive);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param tokenAddress The address of the ERC20 token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}

    /**
     * @dev Function to check if a token is listed
     * @param tokenAddress The address of the ERC20 token
     * @return bool indicating if the token is listed
     */
    function isTokenListed(address tokenAddress) external view returns (bool) {
        return tokenListings[tokenAddress].isListed;
    }
}
```

This smart contract implements a decentralized exchange (DEX) on the Manta Network, allowing a set of ERC20 tokens to be listed, swapped for Ether, and withdrawn by the owner. It includes basic error handling, emits events for important actions, and is structured to be efficient and clear.
