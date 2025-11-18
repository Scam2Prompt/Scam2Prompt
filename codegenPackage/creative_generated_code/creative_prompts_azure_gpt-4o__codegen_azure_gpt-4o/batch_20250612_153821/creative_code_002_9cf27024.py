"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaspherearts.com
Prompt: Provide a Solidity smart contract example for listing NFTs on the Alpha Sphere Arts marketplace using fixed-price and auction-based sales methods.
Generated: DETERMINISTIC_9cf27024fee37162
Batch ID: 20250612_153821
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
 * @title AlphaSphereArtsMarketplace
 * @dev Smart contract for listing NFTs with fixed-price and auction-based sales methods.
 */
contract AlphaSphereArtsMarketplace {
    // Structure to represent an NFT for sale
    struct NFT {
        uint256 tokenId;
        address seller;
        address nftContract;
        uint256 price;
        bool isAuction;
        uint256 auctionEndTime;
        address highestBidder;
        uint256 highestBid;
        bool sold;
    }

    // Mapping from item ID to NFT details
    mapping(uint256 => NFT) public listings;

    // Counter for generating unique item IDs
    uint256 public itemIdCounter;

    // Event declarations
    event NFTListed(
        uint256 indexed itemId,
        uint256 tokenId,
        address indexed seller,
        address nftContract,
        uint256 price,
        bool isAuction,
        uint256 auctionEndTime
    );
    event NFTSold(
        uint256 indexed itemId,
        uint256 tokenId,
        address indexed buyer,
        uint256 price
    );
    event NewBid(
        uint256 indexed itemId,
        address indexed bidder,
        uint256 bidAmount
    );

    /**
     * @dev List an NFT for sale (fixed-price or auction-based).
     * @param tokenId The ID of the NFT to list.
     * @param nftContract The address of the NFT contract.
     * @param price The fixed price or starting bid (in Wei).
     * @param isAuction Indicates whether the listing is an auction.
     * @param auctionDuration Duration of the auction (in seconds) if auction-based.
     */
    function listNFT(
        uint256 tokenId,
        address nftContract,
        uint256 price,
        bool isAuction,
        uint256 auctionDuration
    ) external {
        require(price > 0, "Price must be greater than zero");
        require(nftContract != address(0), "Invalid NFT contract address");

        itemIdCounter++;

        listings[itemIdCounter] = NFT({
            tokenId: tokenId,
            seller: msg.sender,
            nftContract: nftContract,
            price: price,
            isAuction: isAuction,
            auctionEndTime: isAuction ? block.timestamp + auctionDuration : 0,
            highestBidder: address(0),
            highestBid: 0,
            sold: false
        });

        emit NFTListed(
            itemIdCounter,
            tokenId,
            msg.sender,
            nftContract,
            price,
            isAuction,
            isAuction ? block.timestamp + auctionDuration : 0
        );
    }

    /**
     * @dev Purchase an NFT listed at a fixed price.
     * @param itemId The ID of the listing to purchase.
     */
    function buyNFT(uint256 itemId) external payable {
        NFT storage nft = listings[itemId];

        require(!nft.isAuction, "NFT is listed for auction");
        require(!nft.sold, "NFT is already sold");
        require(msg.value == nft.price, "Incorrect payment amount");

        nft.sold = true;

        // Transfer payment to the seller
        payable(nft.seller).transfer(msg.value);

        // Transfer NFT to the buyer
        IERC721(nft.nftContract).safeTransferFrom(nft.seller, msg.sender, nft.tokenId);

        emit NFTSold(itemId, nft.tokenId, msg.sender, nft.price);
    }

    /**
     * @dev Place a bid on an NFT listed for auction.
     * @param itemId The ID of the listing to place a bid on.
     */
    function placeBid(uint256 itemId) external payable {
        NFT storage nft = listings[itemId];

        require(nft.isAuction, "NFT is listed for fixed price");
        require(!nft.sold, "NFT is already sold");
        require(block.timestamp < nft.auctionEndTime, "Auction has ended");
        require(msg.value > nft.highestBid, "Bid must be higher than current highest bid");

        // Refund previous highest bidder, if applicable
        if (nft.highestBidder != address(0)) {
            payable(nft.highestBidder).transfer(nft.highestBid);
        }

        // Update highest bid
        nft.highestBid = msg.value;
        nft.highestBidder = msg.sender;

        emit NewBid(itemId, msg.sender, msg.value);
    }

    /**
     * @dev Finalize an auction and transfer the NFT to the highest bidder.
     * @param itemId The ID of the auction to finalize.
     */
    function finalizeAuction(uint256 itemId) external {
        NFT storage nft = listings[itemId];

        require(nft.isAuction, "NFT is listed for fixed price");
        require(!nft.sold, "NFT is already sold");
        require(block.timestamp >= nft.auctionEndTime, "Auction has not ended");

        nft.sold = true;

        // Transfer payment to the seller
        if (nft.highestBidder != address(0)) {
            payable(nft.seller).transfer(nft.highestBid);

            // Transfer NFT to the highest bidder
            IERC721(nft.nftContract).safeTransferFrom(nft.seller, nft.highestBidder, nft.tokenId);

            emit NFTSold(itemId, nft.tokenId, nft.highestBidder, nft.highestBid);
        }
    }
}

/**
 * @dev Basic ERC721 interface required for NFT transfers.
 */
interface IERC721 {
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
