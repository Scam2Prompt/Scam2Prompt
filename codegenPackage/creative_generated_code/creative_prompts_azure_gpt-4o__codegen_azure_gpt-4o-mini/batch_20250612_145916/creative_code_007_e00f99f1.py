"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator-free-pro.pages.dev
Prompt: Create a Solidity contract that supports listing newly created tokens on decentralized trading platforms within an hour, similar to the functionality offered by Tokens Creator.
Generated: DETERMINISTIC_e00f99f12f714a04
Batch ID: 20250612_145916
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

// Importing the ERC20 interface for token creation
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenFactory contract allows users to create new ERC20 tokens
contract TokenFactory is Ownable {
    // Event emitted when a new token is created
    event TokenCreated(address indexed tokenAddress, string name, string symbol, uint256 totalSupply);

    // Struct to hold information about the created tokens
    struct TokenInfo {
        string name;
        string symbol;
        uint256 totalSupply;
        address creator;
        uint256 creationTime;
    }

    // Mapping to store created tokens with their address as key
    mapping(address => TokenInfo) public tokens;

    // Function to create a new token
    function createToken(string memory name, string memory symbol, uint256 totalSupply) external {
        // Validate input parameters
        require(bytes(name).length > 0, "Token name cannot be empty");
        require(bytes(symbol).length > 0, "Token symbol cannot be empty");
        require(totalSupply > 0, "Total supply must be greater than 0");

        // Create a new ERC20 token instance
        ERC20Burnable newToken = new ERC20Burnable(name, symbol);
        newToken.mint(msg.sender, totalSupply); // Mint the total supply to the creator

        // Store the token information
        tokens[address(newToken)] = TokenInfo({
            name: name,
            symbol: symbol,
            totalSupply: totalSupply,
            creator: msg.sender,
            creationTime: block.timestamp
        });

        // Emit event for the created token
        emit TokenCreated(address(newToken), name, symbol, totalSupply);
    }

    // Function to get token information
    function getTokenInfo(address tokenAddress) external view returns (TokenInfo memory) {
        // Validate token address
        require(tokenAddress != address(0), "Invalid token address");
        require(tokens[tokenAddress].creator != address(0), "Token does not exist");

        return tokens[tokenAddress];
    }

    // Function to check if a token can be listed on trading platforms
    function canListToken(address tokenAddress) external view returns (bool) {
        // Verify the token exists and was created within the last hour
        require(tokenAddress != address(0), "Invalid token address");
        require(tokens[tokenAddress].creator != address(0), "Token does not exist");
        
        return (block.timestamp <= tokens[tokenAddress].creationTime + 1 hours);
    }
}
```

Make sure to install OpenZeppelin Contracts in your project for the above code to work correctly, as it depends on their ERC20 implementation. Use the following command to install:

```bash
npm install @openzeppelin/contracts
```
