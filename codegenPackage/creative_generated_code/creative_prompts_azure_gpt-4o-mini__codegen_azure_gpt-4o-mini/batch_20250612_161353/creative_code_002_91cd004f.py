"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: Can you provide an example of integrating ERC20 and ERC721 assets with the Data Ownership Protocol for a decentralized application?
Generated: DETERMINISTIC_91cd004f7b06f208
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

// Importing the required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Data Ownership Protocol
interface IDataOwnership {
    function registerDataOwnership(address owner, uint256 tokenId) external;
    function transferOwnership(address from, address to, uint256 tokenId) external;
}

// Example contract integrating ERC20 and ERC721 with a Data Ownership Protocol
contract AssetIntegration is Ownable {
    // State variables for ERC20 and ERC721 token contracts
    IERC20 public erc20Token;
    IERC721 public erc721Token;
    IDataOwnership public dataOwnershipProtocol;

    // Event to emit when ownership is registered
    event OwnershipRegistered(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize token contracts and data ownership protocol
    constructor(address _erc20Token, address _erc721Token, address _dataOwnershipProtocol) {
        erc20Token = IERC20(_erc20Token);
        erc721Token = IERC721(_erc721Token);
        dataOwnershipProtocol = IDataOwnership(_dataOwnershipProtocol);
    }

    // Function to register asset ownership in the Data Ownership Protocol
    function registerOwnership(uint256 tokenId) external {
        // Ensure the caller is the owner of the ERC721 token
        require(erc721Token.ownerOf(tokenId) == msg.sender, "Not the token owner");
        
        // Register ownership with the Data Ownership Protocol
        dataOwnershipProtocol.registerDataOwnership(msg.sender, tokenId);
        
        // Emit an event for ownership registration
        emit OwnershipRegistered(msg.sender, tokenId);
    }

    // Function to transfer ERC20 tokens
    function transferERC20(address to, uint256 amount) external {
        // Ensure the transfer amount is greater than 0
        require(amount > 0, "Transfer amount must be greater than 0");
        
        // Transfer ERC20 tokens from the caller to the specified address
        bool success = erc20Token.transferFrom(msg.sender, to, amount);
        require(success, "ERC20 transfer failed");
    }

    // Function to transfer ERC721 token and notify Data Ownership Protocol
    function transferERC721(address to, uint256 tokenId) external {
        // Ensure the caller is the owner of the ERC721 token
        require(erc721Token.ownerOf(tokenId) == msg.sender, "Not the token owner");

        // Transfer the ERC721 token
        erc721Token.safeTransferFrom(msg.sender, to, tokenId);
        
        // Notify the Data Ownership Protocol about the transfer
        dataOwnershipProtocol.transferOwnership(msg.sender, to, tokenId);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
