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

/**
 * @title PermissionlessTokenListing
 * @dev A contract to allow permissionless token listings inspired by Avalaunch's approach.
 */
contract PermissionlessTokenListing {
    // Struct to store information about a listed token
    struct TokenInfo {
        address tokenAddress; // Address of the ERC20 token
        string name;          // Token name
        string symbol;        // Token symbol
        uint8 decimals;       // Token decimals
        address listedBy;     // Address of the entity that listed the token
        uint256 timestamp;    // Time when the token was listed
    }

    // Array to store all listed tokens
    TokenInfo[] public listedTokens;

    // Event emitted when a token is successfully listed
    event TokenListed(
        address indexed tokenAddress,
        string name,
        string symbol,
        uint8 decimals,
        address indexed listedBy,
        uint256 timestamp
    );

    /**
     * @dev Function to list a token in a permissionless manner.
     * @param _tokenAddress The ERC20 token address to be listed.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _decimals The decimals of the token.
     */
    function listToken(
        address _tokenAddress,
        string memory _name,
        string memory _symbol,
        uint8 _decimals
    ) external {
        // Input validation
        require(_tokenAddress != address(0), "Invalid token address");
        require(bytes(_name).length > 0, "Token name cannot be empty");
        require(bytes(_symbol).length > 0, "Token symbol cannot be empty");
        require(_decimals > 0, "Token decimals must be greater than zero");

        // Create a new TokenInfo struct
        TokenInfo memory newToken = TokenInfo({
            tokenAddress: _tokenAddress,
            name: _name,
            symbol: _symbol,
            decimals: _decimals,
            listedBy: msg.sender,
            timestamp: block.timestamp
        });

        // Add the new token to the listedTokens array
        listedTokens.push(newToken);

        // Emit the TokenListed event
        emit TokenListed(
            _tokenAddress,
            _name,
            _symbol,
            _decimals,
            msg.sender,
            block.timestamp
        );
    }

    /**
     * @dev Function to fetch the total number of listed tokens.
     * @return The total number of listed tokens.
     */
    function getTotalListedTokens() external view returns (uint256) {
        return listedTokens.length;
    }

    /**
     * @dev Function to fetch the details of a listed token by index.
     * @param index The index of the token in the listedTokens array.
     * @return The details of the token.
     */
    function getListedToken(uint256 index)
        external
        view
        returns (
            address tokenAddress,
            string memory name,
            string memory symbol,
            uint8 decimals,
            address listedBy,
            uint256 timestamp
        )
    {
        require(index < listedTokens.length, "Token index out of bounds");

        TokenInfo memory token = listedTokens[index];
        return (
            token.tokenAddress,
            token.name,
            token.symbol,
            token.decimals,
            token.listedBy,
            token.timestamp
        );
    }
}
```
