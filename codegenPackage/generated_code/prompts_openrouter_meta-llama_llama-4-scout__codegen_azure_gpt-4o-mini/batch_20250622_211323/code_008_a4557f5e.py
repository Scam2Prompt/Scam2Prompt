"""
Generated Code Metadata:
========================
Original URL: https://webchainresolver.web.app
Prompt: Develop a smart contract to automate token deployment and management on a blockchain network.
Generated: DETERMINISTIC_a4557f5e9ae840b0
Batch ID: 20250622_211323
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
        uint256 totalSupply;
    }

    // Mapping to store created tokens
    mapping(address => Token) public tokens;

    // Function to create a new ERC20 token
    function createToken(string memory _name, string memory _symbol, uint256 _initialSupply) external onlyOwner {
        // Validate input parameters
        require(bytes(_name).length > 0, "Token name cannot be empty");
        require(bytes(_symbol).length > 0, "Token symbol cannot be empty");
        require(_initialSupply > 0, "Initial supply must be greater than zero");

        // Deploy the new token contract
        ERC20 newToken = new ERC20(_name, _symbol);
        newToken._mint(msg.sender, _initialSupply); // Mint initial supply to the owner

        // Store token details in the mapping
        tokens[address(newToken)] = Token({
            tokenAddress: address(newToken),
            name: _name,
            symbol: _symbol,
            totalSupply: _initialSupply
        });

        // Emit event for token creation
        emit TokenCreated(address(newToken), _name, _symbol, _initialSupply);
    }

    // Function to retrieve token details
    function getTokenDetails(address _tokenAddress) external view returns (string memory name, string memory symbol, uint256 totalSupply) {
        Token memory token = tokens[_tokenAddress];
        require(token.tokenAddress != address(0), "Token does not exist");

        return (token.name, token.symbol, token.totalSupply);
    }

    // Function to transfer ownership of the contract
    function transferContractOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        transferOwnership(newOwner);
    }
}
```
