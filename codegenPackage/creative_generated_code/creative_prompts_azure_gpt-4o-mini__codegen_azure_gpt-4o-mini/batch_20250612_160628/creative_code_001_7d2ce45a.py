"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: Write a code snippet to integrate ERC20 and ERC721 tokens with the Data Ownership Protocol for private transactions.
Generated: DETERMINISTIC_7d2ce45aabb54303
Batch ID: 20250612_160628
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

// Importing necessary interfaces for ERC20 and ERC721 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

// Interface for the Data Ownership Protocol
interface IDataOwnershipProtocol {
    function registerOwnership(address owner, uint256 tokenId) external;
    function transferOwnership(address from, address to, uint256 tokenId) external;
}

// Main contract for integrating ERC20 and ERC721 tokens
contract TokenIntegration {

    // State variables for ERC20 and ERC721 token contracts
    IERC20 public erc20Token;
    IERC721 public erc721Token;
    IDataOwnershipProtocol public dataOwnershipProtocol;

    // Event to log the data ownership registration
    event DataOwnershipRegistered(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with the token addresses
    constructor(address _erc20Token, address _erc721Token, address _dataOwnershipProtocol) {
        // Set the ERC20 token contract
        erc20Token = IERC20(_erc20Token);
        // Set the ERC721 token contract
        erc721Token = IERC721(_erc721Token);
        // Set the Data Ownership Protocol contract
        dataOwnershipProtocol = IDataOwnershipProtocol(_dataOwnershipProtocol);
    }

    // Function to register ownership of an ERC721 token with the Data Ownership Protocol
    function registerOwnership(uint256 tokenId) external {
        // Ensure the caller owns the token
        require(erc721Token.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");

        // Call the Data Ownership Protocol to register the ownership
        dataOwnershipProtocol.registerOwnership(msg.sender, tokenId);

        // Emit an event indicating successful registration
        emit DataOwnershipRegistered(msg.sender, tokenId);
    }

    // Function to transfer ownership of an ERC721 token
    function transferOwnership(address to, uint256 tokenId) external {
        // Ensure the caller owns the token
        require(erc721Token.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the token");

        // Transfer the token
        erc721Token.transferFrom(msg.sender, to, tokenId);

        // Call the Data Ownership Protocol to transfer ownership
        dataOwnershipProtocol.transferOwnership(msg.sender, to, tokenId);
    }

    // Function to withdraw ERC20 tokens to the caller's address
    function withdrawERC20(uint256 amount) external {
        // Ensure the caller has enough ERC20 tokens
        require(erc20Token.balanceOf(address(this)) >= amount, "Insufficient ERC20 balance");

        // Transfer the tokens to the caller
        require(erc20Token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
