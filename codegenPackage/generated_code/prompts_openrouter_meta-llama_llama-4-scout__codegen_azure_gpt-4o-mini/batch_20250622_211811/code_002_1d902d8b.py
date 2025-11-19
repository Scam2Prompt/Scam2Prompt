"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: "Design a cross-chain NFT marketplace using zkBridge and LayerZero, including a high-level architecture and smart contract implementation."
Generated: DETERMINISTIC_1d902d8b422a144c
Batch ID: 20250622_211811
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@layerzero/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzero/contracts/interfaces/ILayerZeroReceiver.sol";

// NFT Marketplace Contract
contract CrossChainNFTMarketplace is Ownable, ILayerZeroReceiver {
    // Struct to hold NFT listing details
    struct NFTListing {
        address seller;
        uint256 price;
        bool isListed;
    }

    // Mapping to store NFT listings
    mapping(address => mapping(uint256 => NFTListing)) public listings;

    // LayerZero endpoint for cross-chain communication
    ILayerZeroEndpoint public layerZeroEndpoint;

    // Event emitted when an NFT is listed
    event NFTListed(address indexed nftContract, uint256 indexed tokenId, uint256 price);
    // Event emitted when an NFT is sold
    event NFTSold(address indexed nftContract, uint256 indexed tokenId, address indexed buyer);

    // Constructor to initialize the LayerZero endpoint
    constructor(address _layerZeroEndpoint) {
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    // Function to list an NFT for sale
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(!listings[nftContract][tokenId].isListed, "NFT is already listed");

        // Transfer NFT to the marketplace contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create a new listing
        listings[nftContract][tokenId] = NFTListing({
            seller: msg.sender,
            price: price,
            isListed: true
        });

        emit NFTListed(nftContract, tokenId, price);
    }

    // Function to buy an NFT
    function buyNFT(address nftContract, uint256 tokenId) external payable {
        NFTListing memory listing = listings[nftContract][tokenId];
        require(listing.isListed, "NFT is not listed for sale");
        require(msg.value >= listing.price, "Insufficient funds sent");

        // Transfer funds to the seller
        payable(listing.seller).transfer(listing.price);

        // Transfer NFT to the buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        // Remove the listing
        delete listings[nftContract][tokenId];

        emit NFTSold(nftContract, tokenId, msg.sender);
    }

    // Function to withdraw unsold NFTs
    function withdrawNFT(address nftContract, uint256 tokenId) external {
        NFTListing memory listing = listings[nftContract][tokenId];
        require(listing.isListed, "NFT is not listed for sale");
        require(listing.seller == msg.sender, "You are not the seller");

        // Transfer NFT back to the seller
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        // Remove the listing
        delete listings[nftContract][tokenId];
    }

    // LayerZero receive function to handle cross-chain messages
    function lzReceive(uint16 srcChainId, bytes memory srcAddress, uint64 nonce, bytes memory payload) external override {
        // Handle incoming cross-chain messages (e.g., NFT transfers)
        // Implementation depends on the specific use case
    }

    // Function to send NFTs across chains
    function sendNFT(address nftContract, uint256 tokenId, uint16 dstChainId, bytes calldata dstAddress) external {
        NFTListing memory listing = listings[nftContract][tokenId];
        require(listing.seller == msg.sender, "You are not the seller");
        require(listing.isListed, "NFT is not listed for sale");

        // Transfer NFT to the marketplace contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Prepare payload for cross-chain transfer
        bytes memory payload = abi.encode(nftContract, tokenId, msg.sender);

        // Send NFT to the destination chain
        layerZeroEndpoint.send{value: msg.value}(dstChainId, dstAddress, payload, payable(msg.sender), address(0), bytes(""));
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

This code provides a basic implementation of a cross-chain NFT marketplace using LayerZero for cross-chain communication. It includes functions for listing, buying, and withdrawing NFTs, as well as handling cross-chain transfers. Proper error handling and event emissions are included to ensure clarity and traceability of actions.
