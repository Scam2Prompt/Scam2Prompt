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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AlphaSphereMarketplace
 * @dev A marketplace for listing NFTs with fixed-price and auction-based sales methods.
 */
contract AlphaSphereMarketplace is Ownable, ERC721Holder {
    using SafeMath for uint256;

    // Enumeration for sale types
    enum SaleType { FixedPrice, Auction }

    // Struct to hold sale details
    struct Sale {
        address seller;
        SaleType saleType;
        uint256 price; // Fixed price or starting bid for auction
        uint256 auctionEndTime; // End time for auction
        bool isActive;
    }

    // Mapping of token ID to sale details
    mapping(uint256 => Sale) public sales;

    event Listed(uint256 indexed tokenId, address indexed seller, SaleType saleType, uint256 price);
    event SaleCancelled(uint256 indexed tokenId, address indexed seller);
    event Sold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event AuctionEnded(uint256 indexed tokenId, address indexed winner, uint256 price);

    /**
     * @dev Lists an NFT for sale.
     * @param _tokenId The ID of the NFT to list.
     * @param _saleType The type of sale (fixed price or auction).
     * @param _price The price for fixed price or starting bid for auction.
     * @param _auctionDuration The duration of the auction in seconds (only for auction type).
     */
    function listNFT(
        uint256 _tokenId,
        SaleType _saleType,
        uint256 _price,
        uint256 _auctionDuration
    ) external {
        require(_price > 0, "Price must be greater than zero");
        require(IERC721(msg.sender).ownerOf(_tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(sales[_tokenId].isActive == false, "NFT already listed for sale");

        // Transfer NFT to the contract
        IERC721(msg.sender).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Set sale details
        if (_saleType == SaleType.Auction) {
            require(_auctionDuration > 0, "Auction duration must be greater than zero");
            sales[_tokenId] = Sale(msg.sender, _saleType, _price, block.timestamp.add(_auctionDuration), true);
        } else {
            sales[_tokenId] = Sale(msg.sender, _saleType, _price, 0, true);
        }

        emit Listed(_tokenId, msg.sender, _saleType, _price);
    }

    /**
     * @dev Cancels the sale of an NFT.
     * @param _tokenId The ID of the NFT to cancel.
     */
    function cancelSale(uint256 _tokenId) external {
        Sale memory sale = sales[_tokenId];
        require(sale.isActive == true, "NFT is not listed for sale");
        require(sale.seller == msg.sender, "Caller is not the seller");

        // Mark sale as inactive
        sales[_tokenId].isActive = false;

        // Transfer NFT back to the seller
        IERC721(address(this)).safeTransferFrom(address(this), msg.sender, _tokenId);

        emit SaleCancelled(_tokenId, msg.sender);
    }

    /**
     * @dev Buys an NFT at a fixed price.
     * @param _tokenId The ID of the NFT to buy.
     */
    function buyNFT(uint256 _tokenId) external payable {
        Sale memory sale = sales[_tokenId];
        require(sale.isActive == true, "NFT is not for sale");
        require(sale.saleType == SaleType.FixedPrice, "NFT is not listed for fixed price");
        require(msg.value == sale.price, "Incorrect price sent");

        // Mark sale as inactive
        sales[_tokenId].isActive = false;

        // Transfer NFT to buyer
        IERC721(address(this)).safeTransferFrom(address(this), msg.sender, _tokenId);
        
        // Transfer funds to the seller
        payable(sale.seller).transfer(msg.value);

        emit Sold(_tokenId, msg.sender, sale.seller, sale.price);
    }

    /**
     * @dev Bids on an NFT in auction.
     * @param _tokenId The ID of the NFT to bid on.
     */
    function bidNFT(uint256 _tokenId) external payable {
        Sale memory sale = sales[_tokenId];
        require(sale.isActive == true, "NFT is not for auction");
        require(sale.saleType == SaleType.Auction, "NFT is not listed for auction");
        require(block.timestamp < sale.auctionEndTime, "Auction has ended");
        require(msg.value > sale.price, "Bid must be higher than current price");

        // Refund the previous bidder
        if (sale.price > 0) {
            payable(sale.seller).transfer(sale.price); // Refund the previous bid
        }

        // Update the sale details
        sales[_tokenId].price = msg.value; // Update to the new bid

        emit AuctionEnded(_tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Ends the auction and transfers the NFT to the highest bidder.
     * @param _tokenId The ID of the NFT.
     */
    function endAuction(uint256 _tokenId) external {
        Sale memory sale = sales[_tokenId];
        require(sale.isActive == true, "NFT auction is not active");
        require(sale.saleType == SaleType.Auction, "NFT is not up for auction");
        require(block.timestamp >= sale.auctionEndTime, "Auction has not ended yet");

        // Mark sale as inactive
        sales[_tokenId].isActive = false;

        // Transfer NFT to the highest bidder
        IERC721(address(this)).safeTransferFrom(address(this), msg.sender, _tokenId);

        // Transfer funds to the seller
        payable(sale.seller).transfer(sale.price);

        emit AuctionEnded(_tokenId, msg.sender, sale.price);
    }
}
```
