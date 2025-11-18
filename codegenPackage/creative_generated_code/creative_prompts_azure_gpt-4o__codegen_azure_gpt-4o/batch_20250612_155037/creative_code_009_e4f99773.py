"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeflarre.com
Prompt: Generate a smart contract that demonstrates cross-chain NFT purchases on stakeflarre using tokens from another blockchain, leveraging both the FTSO and Data Connector protocols.
Generated: DETERMINISTIC_e4f997733d2b6dfb
Batch ID: 20250612_155037
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
 * @title CrossChainNFTPurchase
 * @dev Smart contract to demonstrate cross-chain NFT purchases on StakeFlare using tokens from another blockchain.
 *      Utilizes Flare Time Series Oracle (FTSO) for price data and Data Connector protocol for cross-chain transactions.
 */
contract CrossChainNFTPurchase {
    // Struct to represent available NFTs for purchase
    struct NFT {
        uint256 id;
        address owner;
        uint256 price; // Price in the foreign blockchain's token (e.g., USDT)
    }

    mapping(uint256 => NFT) public nfts; // Mapping of NFT ID to NFT details
    uint256 public nextNFTId; // Counter for assigning NFT IDs

    address public ftso; // Address of Flare Time Series Oracle
    address public dataConnector; // Address of the Data Connector protocol

    event NFTListed(uint256 indexed nftId, address indexed owner, uint256 price);
    event NFTSold(uint256 indexed nftId, address indexed buyer, uint256 price);

    /**
     * @dev Constructor to initialize the contract.
     * @param _ftso Address of the Flare Time Series Oracle contract.
     * @param _dataConnector Address of the Data Connector protocol contract.
     */
    constructor(address _ftso, address _dataConnector) {
        require(_ftso != address(0), "FTSO address cannot be zero");
        require(_dataConnector != address(0), "Data Connector address cannot be zero");

        ftso = _ftso;
        dataConnector = _dataConnector;
    }

    /**
     * @dev Function to list an NFT for sale.
     * @param _price Price of the NFT in foreign blockchain tokens.
     */
    function listNFT(uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        nfts[nextNFTId] = NFT({
            id: nextNFTId,
            owner: msg.sender,
            price: _price
        });

        emit NFTListed(nextNFTId, msg.sender, _price);
        nextNFTId++;
    }

    /**
     * @dev Function to purchase an NFT using tokens from a foreign blockchain.
     * @param _nftId ID of the NFT to purchase.
     * @param _foreignTxHash Transaction hash from the foreign blockchain confirming token transfer.
     */
    function purchaseNFT(uint256 _nftId, bytes32 _foreignTxHash) external {
        NFT storage nft = nfts[_nftId];
        require(nft.owner != address(0), "NFT does not exist");
        require(nft.owner != msg.sender, "Cannot purchase your own NFT");

        // Verify the token transfer on the foreign blockchain using the Data Connector protocol.
        bool txVerified = IDataConnector(dataConnector).verifyTransaction(
            _foreignTxHash, msg.sender, nft.price
        );
        require(txVerified, "Foreign blockchain transaction not verified");

        // Simulate price conversion using FTSO
        uint256 priceInNativeTokens = IFTSO(ftso).convertPrice(nft.price);
        require(priceInNativeTokens > 0, "Invalid price conversion");

        // Transfer ownership of the NFT
        address previousOwner = nft.owner;
        nft.owner = msg.sender;

        emit NFTSold(_nftId, msg.sender, nft.price);

        // Handle payment to the previous owner (in the form of native tokens)
        // This would typically involve another contract or external call.
        payable(previousOwner).transfer(priceInNativeTokens);
    }
}

interface IDataConnector {
    function verifyTransaction(
        bytes32 txHash,
        address buyer,
        uint256 amount
    ) external view returns (bool);
}

interface IFTSO {
    function convertPrice(uint256 foreignPrice) external view returns (uint256);
}
```
