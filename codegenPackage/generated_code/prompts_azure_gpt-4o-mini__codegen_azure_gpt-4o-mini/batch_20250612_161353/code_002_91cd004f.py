"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: Can you provide an example of integrating ERC20 and ERC721 assets with the Data Ownership Protocol for a decentralized application?
Generated: DETERMINISTIC_91cd004f7b06f208
Batch ID: 20250612_161353
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

// Importing the ERC20 and ERC721 interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Data Ownership Protocol
interface IDataOwnershipProtocol {
    function registerAsset(address owner, string memory assetId) external;
    function transferOwnership(string memory assetId, address newOwner) external;
}

// Main contract integrating ERC20 and ERC721 with the Data Ownership Protocol
contract AssetManager is Ownable {
    // State variables
    IDataOwnershipProtocol public dataOwnershipProtocol;
    mapping(address => mapping(uint256 => bool)) public erc721Assets; // Track ERC721 ownership
    mapping(address => uint256) public erc20Balances; // Track ERC20 balances

    // Events for logging
    event ERC20Deposited(address indexed user, uint256 amount);
    event ERC721Registered(address indexed user, address indexed nftAddress, uint256 tokenId);
    event OwnershipTransferred(string assetId, address indexed newOwner);

    // Constructor to set the Data Ownership Protocol address
    constructor(address _dataOwnershipProtocol) {
        dataOwnershipProtocol = IDataOwnershipProtocol(_dataOwnershipProtocol);
    }

    // Function to deposit ERC20 tokens
    function depositERC20(address tokenAddress, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer ERC20 tokens from user to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);
        erc20Balances[msg.sender] += amount;

        emit ERC20Deposited(msg.sender, amount);
    }

    // Function to register an ERC721 asset
    function registerERC721(address nftAddress, uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(IERC721(nftAddress).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        
        // Register the asset in the Data Ownership Protocol
        string memory assetId = string(abi.encodePacked(nftAddress, tokenId));
        dataOwnershipProtocol.registerAsset(msg.sender, assetId);
        
        // Mark the ERC721 asset as registered
        erc721Assets[nftAddress][tokenId] = true;

        emit ERC721Registered(msg.sender, nftAddress, tokenId);
    }

    // Function to transfer ownership of an asset
    function transferAssetOwnership(string memory assetId, address newOwner) external {
        // Transfer ownership in the Data Ownership Protocol
        dataOwnershipProtocol.transferOwnership(assetId, newOwner);
        
        emit OwnershipTransferred(assetId, newOwner);
    }

    // Function to withdraw ERC20 tokens
    function withdrawERC20(address tokenAddress, uint256 amount) external {
        require(erc20Balances[msg.sender] >= amount, "Insufficient balance");
        
        // Update the balance before transferring to prevent reentrancy
        erc20Balances[msg.sender] -= amount;
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to check ERC20 balance
    function getERC20Balance() external view returns (uint256) {
        return erc20Balances[msg.sender];
    }

    // Function to check if an ERC721 asset is registered
    function isERC721Registered(address nftAddress, uint256 tokenId) external view returns (bool) {
        return erc721Assets[nftAddress][tokenId];
    }
}
```
