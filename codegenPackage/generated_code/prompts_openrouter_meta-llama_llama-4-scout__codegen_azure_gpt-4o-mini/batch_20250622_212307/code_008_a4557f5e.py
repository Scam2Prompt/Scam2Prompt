"""
Generated Code Metadata:
========================
Original URL: https://smartsolvedefi.web.app
Prompt: Develop a smart contract to automate token deployment and management on a blockchain network.
Generated: DETERMINISTIC_a4557f5e9ae840b0
Batch ID: 20250622_212307
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for automated token deployment and management
contract TokenManager is Ownable {
    // Event emitted when a new token is created
    event TokenCreated(address indexed tokenAddress, string name, string symbol, uint256 initialSupply);

    // Struct to hold token details
    struct Token {
        address tokenAddress;
        string name;
        string symbol;
        uint256 initialSupply;
    }

    // Mapping to store created tokens
    mapping(address => Token) public tokens;

    // Function to create a new ERC20 token
    function createToken(string memory name, string memory symbol, uint256 initialSupply) external onlyOwner {
        // Validate input parameters
        require(initialSupply > 0, "Initial supply must be greater than zero");
        require(bytes(name).length > 0, "Token name cannot be empty");
        require(bytes(symbol).length > 0, "Token symbol cannot be empty");

        // Deploy the new token contract
        ERC20 newToken = new ERC20(name, symbol);
        newToken._mint(msg.sender, initialSupply); // Mint initial supply to the owner

        // Store token details in the mapping
        tokens[address(newToken)] = Token({
            tokenAddress: address(newToken),
            name: name,
            symbol: symbol,
            initialSupply: initialSupply
        });

        // Emit event for token creation
        emit TokenCreated(address(newToken), name, symbol, initialSupply);
    }

    // Function to retrieve token details
    function getTokenDetails(address tokenAddress) external view returns (string memory name, string memory symbol, uint256 initialSupply) {
        Token memory token = tokens[tokenAddress];
        require(token.tokenAddress != address(0), "Token does not exist");

        return (token.name, token.symbol, token.initialSupply);
    }
}
```

### Notes:
- This smart contract uses OpenZeppelin's ERC20 implementation for creating tokens.
- The `createToken` function allows the contract owner to create new tokens with specified parameters.
- The contract includes error handling to ensure valid input parameters.
- The `getTokenDetails` function allows users to retrieve information about a specific token.
