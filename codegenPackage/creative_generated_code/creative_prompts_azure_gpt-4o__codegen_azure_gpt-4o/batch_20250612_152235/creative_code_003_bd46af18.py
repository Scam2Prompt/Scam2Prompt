"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blum-8sr.pages.dev
Prompt: Create a smart contract that supports trading ordinals and NFTs using Blum's self-custody wallet integration.
Generated: DETERMINISTIC_bd46af18a7109f1a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a production-ready smart contract written in Solidity for Ethereum, allowing the trading of NFTs and ordinals, integrated with self-custody wallets like Blum's.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title NFTOrdinalTrading
 * @dev A smart contract for trading NFTs and ordinals with self-custody wallet integration.
 */
contract NFTOrdinalTrading {
    // Struct to represent a trade listing
    struct Trade {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    // Mapping of trade IDs to Trade structs
    mapping(uint256 => Trade) public trades;

    // Unique trade ID tracker
    uint256 private tradeCounter;

    // Blum wallet integration address (for example purposes)
    address public immutable blumWallet;

    // Events
    event TradeCreated(uint256 indexed tradeId, address indexed seller, address indexed nftContract, uint256 tokenId, uint256 price);
    event TradeCancelled(uint256 indexed tradeId);
    event TradeExecuted(uint256 indexed tradeId, address indexed buyer);

    // Constructor to set the Blum wallet address
    constructor(address _blumWallet) {
        require(_blumWallet != address(0), "Wallet address cannot be zero");
        blumWallet = _blumWallet;
    }

    /**
     * @dev Create a trade listing for an NFT or ordinal.
     * @param nftContract Address of the NFT contract.
     * @param tokenId ID of the NFT token.
     * @param price Price in wei for the NFT/ordinal.
     */
    function createTrade(address nftContract, uint256 tokenId, uint256 price) external {
        require(nftContract != address(0), "Invalid NFT contract address");
        require(price > 0, "Price must be greater than zero");

        // Transfer NFT ownership from seller to the contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Create a new trade entry
        trades[tradeCounter] = Trade({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit TradeCreated(tradeCounter, msg.sender, nftContract, tokenId, price);

        // Increment trade counter for next listing
        tradeCounter++;
    }

    /**
     * @dev Cancel an active trade listing.
     * @param tradeId ID of the trade to cancel.
     */
    function cancelTrade(uint256 tradeId) external {
        Trade storage trade = trades[tradeId];

        require(trade.isActive, "Trade is not active");
        require(trade.seller == msg.sender, "Only the seller can cancel the trade");

        // Return NFT/ordinal back to the seller
        IERC721(trade.nftContract).transferFrom(address(this), trade.seller, trade.tokenId);

        // Mark the trade as inactive
        trade.isActive = false;

        emit TradeCancelled(tradeId);
    }

    /**
     * @dev Execute a trade and purchase the NFT/ordinal.
     * @param tradeId ID of the trade to execute.
     */
    function executeTrade(uint256 tradeId) external payable {
        Trade storage trade = trades[tradeId];

        require(trade.isActive, "Trade is not active");
        require(msg.value == trade.price, "Incorrect price sent");

        // Transfer funds to the seller
        payable(trade.seller).transfer(msg.value);

        // Transfer NFT/ordinal to the buyer
        IERC721(trade.nftContract).transferFrom(address(this), msg.sender, trade.tokenId);

        // Mark the trade as inactive
        trade.isActive = false;

        emit TradeExecuted(tradeId, msg.sender);
    }

    /**
     * @dev Fallback function to receive ETH (for future extensions like royalties).
     */
    receive() external payable {
        // Accept ETH deposits
    }

    /**
     * @dev Utility function to withdraw ETH from the contract. Restricted to the Blum wallet.
     */
    function withdraw() external {
        require(msg.sender == blumWallet, "Only Blum wallet can withdraw");

        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        payable(blumWallet).transfer(balance);
    }
}

// Interface for ERC721 token standard
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```

### Key Features:
- Supports NFT trading with listing, cancellation, and execution functionality.
- Integration with Blum self-custody wallets through the `blumWallet` address.
- Proper error handling and event emission for transparency.
- Includes an emergency `withdraw()` function for the wallet administrator.
