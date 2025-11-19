"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicgame.pages.dev
Prompt: Generate a sample code for a smart contract that allows players to trade in-game assets on the Sonic platform, focusing on secure user authentication.
Generated: DETERMINISTIC_c7a9301cf8ab6473
Batch ID: 20250612_160038
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";

/// @title Sonic Trading Platform
/// @author Your Name
/// @notice This contract allows players to securely trade in-game assets (ERC721 tokens)
contract SonicTrade is Ownable, ERC721Holder {
    using Counters for Counters.Counter;
    Counters.Counter private _tradeCounter;

    // Struct to represent a trade
    struct Trade {
        uint256 id;
        address seller;
        address buyer;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping from trade ID to trade details
    mapping(uint256 => Trade) private trades;

    // Event emitted when a trade is created
    event TradeCreated(uint256 tradeId, address indexed seller, address indexed nftContract, uint256 tokenId, uint256 price);
    
    // Event emitted when a trade is completed
    event TradeCompleted(uint256 tradeId, address indexed buyer);

    /// @notice Creates a new trade for an in-game asset
    /// @param nftContract Address of the ERC721 contract
    /// @param tokenId ID of the token to trade
    /// @param price Sale price of the asset
    /// @dev This function should be called by the seller
    function createTrade(address nftContract, uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        
        // Transfer the NFT to the contract for secure trading
        IERC721(nftContract).safeTransferFrom(msg.sender, address(this), tokenId);

        _tradeCounter.increment();
        uint256 tradeId = _tradeCounter.current();

        trades[tradeId] = Trade({
            id: tradeId,
            seller: msg.sender,
            buyer: address(0),
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit TradeCreated(tradeId, msg.sender, nftContract, tokenId, price);
    }

    /// @notice Completes a trade, transferring the NFT to the buyer
    /// @param tradeId ID of the trade to complete
    /// @dev The buyer must send the exact price to complete the trade
    function completeTrade(uint256 tradeId) external payable {
        Trade storage trade = trades[tradeId];
        
        require(trade.isActive, "Trade is not active");
        require(msg.value == trade.price, "Incorrect price sent");
        require(trade.seller != msg.sender, "Seller cannot be buyer");

        // Transfer the NFT to the buyer
        IERC721(trade.nftContract).safeTransferFrom(address(this), msg.sender, trade.tokenId);
        
        // Pay the seller
        payable(trade.seller).transfer(msg.value);

        // Mark trade as completed
        trade.isActive = false;
        trade.buyer = msg.sender;

        emit TradeCompleted(tradeId, msg.sender);
    }

    /// @notice Cancels an active trade and retrieves the NFT
    /// @param tradeId ID of the trade to cancel
    /// @dev This function should be called by the seller
    function cancelTrade(uint256 tradeId) external {
        Trade storage trade = trades[tradeId];
        
        require(trade.isActive, "Trade is not active");
        require(trade.seller == msg.sender, "Only seller can cancel");

        // Transfer the NFT back to the seller
        IERC721(trade.nftContract).safeTransferFrom(address(this), msg.sender, trade.tokenId);
        
        // Mark trade as inactive
        trade.isActive = false;
    }
}
```
