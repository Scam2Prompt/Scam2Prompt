"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notocoin.pages.dev
Prompt: Implement a smart contract in Solidity that could hypothetically handle the future listing of Notcoin on a cryptocurrency exchange, based on the potential scenarios discussed in the NotCoin whitepaper.
Generated: DETERMINISTIC_299998d2affb5db1
Batch ID: 20250612_151027
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title NotcoinExchangeContract
 * @dev This contract manages the potential scenarios for the listing of Notcoin on a cryptocurrency exchange.
 */
contract NotcoinExchangeContract is Ownable {
    // Events
    event TokenListed(address indexed tokenAddress);
    event TokenDelisted(address indexed tokenAddress);
    event ListingFailed(address indexed tokenAddress, string reason);
    
    // Mapping to track if a token is listed
    mapping(address => bool) private listedTokens;
    
    // Array to store listed tokens
    address[] private tokenList;

    // Modifier to check if a token is already listed
    modifier onlyListedToken(address tokenAddress) {
        require(listedTokens[tokenAddress], "Token is not listed.");
        _;
    }

    // Modifier to check if a token is not listed
    modifier onlyUnlistedToken(address tokenAddress) {
        require(!listedTokens[tokenAddress], "Token is already listed.");
        _;
    }

    /**
     * @dev Lists a new token on the exchange.
     * @param tokenAddress The address of the token to be listed.
     */
    function listToken(address tokenAddress) external onlyOwner onlyUnlistedToken(tokenAddress) {
        // Ensure the provided address is a valid ERC20 token
        IERC20 token = IERC20(tokenAddress);
        require(token.totalSupply() > 0, "Invalid token address");

        // Add token to the mapping and array
        listedTokens[tokenAddress] = true;
        tokenList.push(tokenAddress);

        emit TokenListed(tokenAddress);
    }

    /**
     * @dev Delists an existing token from the exchange.
     * @param tokenAddress The address of the token to be delisted.
     */
    function delistToken(address tokenAddress) external onlyOwner onlyListedToken(tokenAddress) {
        // Remove token from the mapping
        listedTokens[tokenAddress] = false;

        // Remove token from the array (simple removal - may require optimization for large arrays)
        for (uint256 i = 0; i < tokenList.length; i++) {
            if (tokenList[i] == tokenAddress) {
                tokenList[i] = tokenList[tokenList.length - 1];
                tokenList.pop();
                break;
            }
        }

        emit TokenDelisted(tokenAddress);
    }

    /**
     * @dev Checks if a token is listed.
     * @param tokenAddress The address of the token to check.
     * @return bool Whether the token is listed or not.
     */
    function isTokenListed(address tokenAddress) external view returns (bool) {
        return listedTokens[tokenAddress];
    }

    /**
     * @dev Retrieves the list of all listed tokens.
     * @return address[] List of addresses of listed tokens.
     */
    function getListedTokens() external view returns (address[] memory) {
        return tokenList;
    }
}
```
