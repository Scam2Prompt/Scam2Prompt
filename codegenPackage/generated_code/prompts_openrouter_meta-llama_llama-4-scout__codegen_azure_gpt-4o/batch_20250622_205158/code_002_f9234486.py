"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: "Design a smart contract using Solidity that interacts with the Rangers Protocol's NFT protocol, allowing users to create, transfer, and manage NFTs on the platform, and provide a detailed explanation of the contract's functionality."
Generated: DETERMINISTIC_f923448669e1bc61
Batch ID: 20250622_205158
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

/**
 * @title RangersNFTManager
 * @dev A smart contract to create, transfer, and manage NFTs using Rangers Protocol's NFT standard.
 */
interface IRangersNFT {
    function mint(address to, uint256 tokenId, string memory tokenURI) external;
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
    function setTokenURI(uint256 tokenId, string memory tokenURI) external;
}

contract RangersNFTManager {
    // Address of the Rangers Protocol NFT contract
    address public rangersNFTContract;

    // Event emitted when a new NFT is created
    event NFTCreated(address indexed creator, uint256 indexed tokenId, string tokenURI);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the Rangers Protocol NFT contract address.
     * @param _rangersNFTContract Address of the Rangers Protocol NFT contract.
     */
    constructor(address _rangersNFTContract) {
        require(_rangersNFTContract != address(0), "Invalid Rangers NFT contract address");
        rangersNFTContract = _rangersNFTContract;
    }

    /**
     * @dev Function to create a new NFT.
     * @param to Address of the recipient who will own the NFT.
     * @param tokenId Unique identifier for the NFT.
     * @param tokenURI Metadata URI for the NFT.
     */
    function createNFT(address to, uint256 tokenId, string memory tokenURI) external {
        require(to != address(0), "Invalid recipient address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        IRangersNFT(rangersNFTContract).mint(to, tokenId, tokenURI);

        emit NFTCreated(msg.sender, tokenId, tokenURI);
    }

    /**
     * @dev Function to transfer an NFT to another address.
     * @param from Address of the current owner of the NFT.
     * @param to Address of the recipient.
     * @param tokenId Unique identifier for the NFT.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(to != address(0), "Invalid recipient address");
        require(IRangersNFT(rangersNFTContract).ownerOf(tokenId) == from, "Sender is not the owner of the NFT");

        IRangersNFT(rangersNFTContract).transferFrom(from, to, tokenId);

        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Function to update the metadata URI of an NFT.
     * @param tokenId Unique identifier for the NFT.
     * @param tokenURI New metadata URI for the NFT.
     */
    function updateTokenURI(uint256 tokenId, string memory tokenURI) external {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(IRangersNFT(rangersNFTContract).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");

        IRangersNFT(rangersNFTContract).setTokenURI(tokenId, tokenURI);
    }
}
```
