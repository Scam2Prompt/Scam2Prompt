"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitesrock.fi
Prompt: Write a smart contract using Solidity that integrates with WhiteRock's audited contracts to facilitate secure and transparent trading of tokenized real-world assets (RWAs).
Generated: DETERMINISTIC_533e9eb618f53157
Batch ID: 20250612_154603
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
 * @title Tokenized Real-World Asset Trading Smart Contract
 * @author [Your Name]
 * @notice This contract facilitates secure and transparent trading of tokenized real-world assets (RWAs)
 * @dev Integrates with WhiteRock's audited contracts
 */
interface IWhiteRockAsset {
    function transferFrom(address from, address to, uint256 tokenId) external returns (bool);
    function ownerOf(uint256 tokenId) external view returns (address);
    function approve(address to, uint256 tokenId) external;
}

contract RWAExchange {
    // Address of the WhiteRock's asset contract
    address public whiteRockAssetContract;

    // Events
    event TradeProposed(uint256 indexed tradeId, address indexed proposer, uint256 tokenId, uint256 price);
    event TradeAccepted(uint256 indexed tradeId, address indexed accepter, uint256 tokenId, uint256 price);
    event TradeCancelled(uint256 indexed tradeId, address indexed proposer);

    // Struct to represent a trade
    struct Trade {
        address proposer;
        uint256 tokenId;
        uint256 price; // Price in wei
        bool isActive;
    }

    // Mapping of trade IDs to Trade details
    mapping(uint256 => Trade) public trades;

    // Counter for trade IDs
    uint256 private tradeCounter;

    // Modifier to check if the caller is the owner of the token
    modifier onlyTokenOwner(uint256 tokenId) {
        require(IWhiteRockAsset(whiteRockAssetContract).ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        _;
    }

    // Modifier to check if the trade is active
    modifier tradeIsActive(uint256 tradeId) {
        require(trades[tradeId].isActive, "Trade is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the WhiteRock asset contract address
     * @param _whiteRockAssetContract Address of the WhiteRock asset contract
     */
    constructor(address _whiteRockAssetContract) {
        require(_whiteRockAssetContract != address(0), "Invalid contract address");
        whiteRockAssetContract = _whiteRockAssetContract;
    }

    /**
     * @notice Proposes a trade for a tokenized asset
     * @dev The proposer must be the owner of the token
     * @param tokenId ID of the token to trade
     * @param price Price in wei for the token
     */
    function proposeTrade(uint256 tokenId, uint256 price) external onlyTokenOwner(tokenId) {
        require(price > 0, "Price must be greater than zero");

        // Approve the contract to transfer the token on behalf of the owner
        IWhiteRockAsset(whiteRockAssetContract).approve(address(this), tokenId);

        // Create trade
        trades[tradeCounter] = Trade({
            proposer: msg.sender,
            tokenId: tokenId,
            price: price,
            isActive: true
        });

        emit TradeProposed(tradeCounter, msg.sender, tokenId, price);
        tradeCounter++;
    }

    /**
     * @notice Accepts a trade and transfers the token to the buyer
     * @param tradeId ID of the trade to accept
     */
    function acceptTrade(uint256 tradeId) external payable tradeIsActive(tradeId) {
        Trade memory trade = trades[tradeId];

        require(msg.value == trade.price, "Incorrect payment amount");

        // Transfer payment to the proposer
        payable(trade.proposer).transfer(msg.value);

        // Transfer token to the buyer
        require(IWhiteRockAsset(whiteRockAssetContract).transferFrom(trade.proposer, msg.sender, trade.tokenId), "Token transfer failed");

        // Deactivate the trade
        trades[tradeId].isActive = false;

        emit TradeAccepted(tradeId, msg.sender, trade.tokenId, trade.price);
    }

    /**
     * @notice Cancels an active trade
     * @dev Only the proposer of the trade can cancel it
     * @param tradeId ID of the trade to cancel
     */
    function cancelTrade(uint256 tradeId) external tradeIsActive(tradeId) {
        Trade memory trade = trades[tradeId];

        require(msg.sender == trade.proposer, "Only proposer can cancel the trade");

        // Deactivate the trade
        trades[tradeId].isActive = false;

        emit TradeCancelled(tradeId, msg.sender);
    }

    /**
     * @notice Gets the details of a trade
     * @param tradeId ID of the trade
     * @return Trade details including proposer, tokenId, price, and isActive flag
     */
    function getTradeDetails(uint256 tradeId) external view returns (Trade memory) {
        return trades[tradeId];
    }
}
```
