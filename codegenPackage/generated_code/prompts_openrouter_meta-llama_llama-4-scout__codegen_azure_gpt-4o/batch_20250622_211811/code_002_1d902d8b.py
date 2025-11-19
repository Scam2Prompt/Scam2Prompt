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

Below is a high-level implementation of a cross-chain NFT marketplace using zkBridge and LayerZero. The code is written in Solidity for Ethereum-compatible blockchains. Note that this is a simplified version and should be further refined for production use.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import LayerZero and zkBridge interfaces
import "@layerzerolabs/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@zkbridge/contracts/interfaces/IZkBridge.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CrossChainNFTMarketplace is Ownable {
    // LayerZero endpoint for cross-chain communication
    ILayerZeroEndpoint public layerZeroEndpoint;

    // zkBridge interface for zero-knowledge proof-based bridging
    IZkBridge public zkBridge;

    // Struct to store NFT listing details
    struct NFTListing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping to store NFT listings
    mapping(uint256 => NFTListing) public listings;

    // Counter for listing IDs
    uint256 public listingCounter;

    // Events
    event NFTListed(uint256 listingId, address seller, address nftContract, uint256 tokenId, uint256 price);
    event NFTPurchased(uint256 listingId, address buyer);
    event NFTTransferredCrossChain(uint256 listingId, address buyer, uint16 destinationChainId);

    // Constructor to initialize LayerZero and zkBridge
    constructor(address _layerZeroEndpoint, address _zkBridge) {
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
        zkBridge = IZkBridge(_zkBridge);
    }

    /**
     * @dev List an NFT for sale.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     * @param price Sale price in wei.
     */
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(IERC721(nftContract).isApprovedForAll(msg.sender, address(this)), "Marketplace is not approved to transfer the NFT");

        listingCounter++;
        listings[listingCounter] = NFTListing({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit NFTListed(listingCounter, msg.sender, nftContract, tokenId, price);
    }

    /**
     * @dev Purchase an NFT.
     * @param listingId ID of the listing to purchase.
     */
    function purchaseNFT(uint256 listingId) external payable {
        NFTListing storage listing = listings[listingId];
        require(listing.isActive, "Listing is not active");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer NFT to the buyer
        IERC721(listing.nftContract).safeTransferFrom(listing.seller, msg.sender, listing.tokenId);

        // Mark listing as inactive
        listing.isActive = false;

        emit NFTPurchased(listingId, msg.sender);
    }

    /**
     * @dev Transfer an NFT cross-chain using LayerZero and zkBridge.
     * @param listingId ID of the listing to transfer.
     * @param destinationChainId ID of the destination chain.
     * @param destinationAddress Address of the recipient on the destination chain.
     */
    function transferNFTCrossChain(uint256 listingId, uint16 destinationChainId, bytes memory destinationAddress) external payable {
        NFTListing storage listing = listings[listingId];
        require(listing.isActive, "Listing is not active");
        require(IERC721(listing.nftContract).ownerOf(listing.tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Mark listing as inactive
        listing.isActive = false;

        // Encode payload for cross-chain transfer
        bytes memory payload = abi.encode(listing.nftContract, listing.tokenId, destinationAddress);

        // Call LayerZero to send the payload
        layerZeroEndpoint.send{value: msg.value}(
            destinationChainId,
            destinationAddress,
            payload,
            payable(msg.sender),
            address(0),
            bytes("")
        );

        emit NFTTransferredCrossChain(listingId, msg.sender, destinationChainId);
    }

    /**
     * @dev Receive cross-chain NFT transfer (to be called by LayerZero/zkBridge).
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     * @param recipient Address of the recipient.
     */
    function receiveNFTCrossChain(address nftContract, uint256 tokenId, address recipient) external {
        // Verify the sender is LayerZero or zkBridge
        require(msg.sender == address(layerZeroEndpoint) || msg.sender == address(zkBridge), "Unauthorized sender");

        // Transfer NFT to the recipient
        IERC721(nftContract).safeTransferFrom(address(this), recipient, tokenId);
    }

    /**
     * @dev Withdraw contract balance (for owner).
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

### Notes:
- This code assumes the existence of LayerZero and zkBridge contracts/interfaces.
- Security measures like reentrancy guards, gas optimizations, and additional validations should be added for production readiness.
- The `receiveNFTCrossChain` function is simplified and would need proper verification of zkBridge proofs in a real-world implementation.
