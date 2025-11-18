"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pira.pages.dev
Prompt: Write a Solidity function to implement permissionless token listings, inspired by Avalaunch's emphasis on permissionless project launches.
Generated: DETERMINISTIC_aa05293536e348e5
Batch ID: 20250612_151415
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PermissionlessTokenListing
 * @dev This contract allows projects to list their tokens without prior approval
 * while ensuring that only valid ERC20 tokens can be listed.
 */
contract PermissionlessTokenListing is Ownable {
    
    // Event emitted when a new token is listed
    event TokenListed(address indexed tokenAddress, address indexed owner);
    
    // Mapping to track listed tokens
    mapping(address => bool) public listedTokens;

    /**
     * @dev Modifier to check if the token is a valid ERC20 token
     * @param tokenAddress The address of the token to check
     */
    modifier onlyValidToken(address tokenAddress) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(IERC20(tokenAddress).totalSupply() > 0, "Token is not valid");
        _;
    }

    /**
     * @dev List a new token for trading.
     * @param tokenAddress The address of the ERC20 token to list.
     * Emits a TokenListed event.
     */
    function listToken(address tokenAddress) external onlyValidToken(tokenAddress) {
        require(!listedTokens[tokenAddress], "Token is already listed");

        // Mark the token as listed
        listedTokens[tokenAddress] = true;

        // Emit event for the token listing
        emit TokenListed(tokenAddress, msg.sender);
    }

    /**
     * @dev Unlist a token if the caller is the owner.
     * @param tokenAddress The address of the ERC20 token to unlist.
     */
    function unlistToken(address tokenAddress) external onlyOwner {
        require(listedTokens[tokenAddress], "Token is not listed");
        
        // Unlist the token
        listedTokens[tokenAddress] = false;
    }

    /**
     * @dev Check if a token is listed.
     * @param tokenAddress The address of the token to check.
     * @return true if the token is listed, false otherwise.
     */
    function isTokenListed(address tokenAddress) external view returns (bool) {
        return listedTokens[tokenAddress];
    }
}
```
