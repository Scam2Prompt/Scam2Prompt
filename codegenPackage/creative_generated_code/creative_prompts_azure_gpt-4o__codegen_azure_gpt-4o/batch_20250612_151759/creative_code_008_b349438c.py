"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multismartchain.web.app
Prompt: Create a Solidity contract to manage and troubleshoot NFTs, ensuring smooth functionality in the NFT marketplace as per MultiSmartChain's services.
Generated: DETERMINISTIC_b349438c12759ee8
Batch ID: 20250612_151759
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
 * @title NFT Marketplace Manager
 * @dev This contract manages NFTs and facilitates smooth functionality in a marketplace.
 */
contract NFTMarketplaceManager {
    
    // Struct to represent an NFT
    struct NFT {
        uint256 id;
        address owner;
        string metadataURI;
        bool isListed;
        uint256 price;
    }
    
    // Mapping to store NFTs by their ID
    mapping(uint256 => NFT) public nfts;
    
    // Mapping to check ownership of address
    mapping(address => uint256[]) public ownedNFTs;

    // Current NFT ID tracker
    uint256 public nextNFTId;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed id, address indexed owner, string metadataURI);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed id, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed id, address indexed seller, address indexed buyer, uint256 price);

    // Modifier to check NFT ownership
    modifier onlyOwner(uint256 _id) {
        require(nfts[_id].owner == msg.sender, "You are not the owner of this NFT");
        _;
    }

    // Modifier to check if NFT exists
    modifier nftExists(uint256 _id) {
        require(nfts[_id].id != 0, "NFT does not exist");
        _;
    }

    /**
     * @dev Function to create a new NFT
     * @param _metadataURI URI pointing to the NFT metadata
     */
    function createNFT(string memory _metadataURI) external {
        nextNFTId++;
        nfts[nextNFTId] = NFT({
            id: nextNFTId,
            owner: msg.sender,
            metadataURI: _metadataURI,
            isListed: false,
            price: 0
        });

        ownedNFTs[msg.sender].push(nextNFTId);
        emit NFTCreated(nextNFTId, msg.sender, _metadataURI);
    }

    /**
     * @dev Function to list an NFT for sale
     * @param _id ID of the NFT to list
     * @param _price Sale price for the NFT
     */
    function listNFT(uint256 _id, uint256 _price) external onlyOwner(_id) nftExists(_id) {
        require(_price > 0, "Price must be greater than zero");
        nfts[_id].isListed = true;
        nfts[_id].price = _price;

        emit NFTListed(_id, _price);
    }

    /**
     * @dev Function to buy a listed NFT
     * @param _id ID of the NFT to purchase
     */
    function buyNFT(uint256 _id) external payable nftExists(_id) {
        NFT storage nft = nfts[_id];
        require(nft.isListed, "NFT is not listed for sale");
        require(msg.value == nft.price, "Incorrect payment amount");

        address previousOwner = nft.owner;
        nft.owner = msg.sender;
        nft.isListed = false;
        nft.price = 0;

        // Transfer funds to the seller
        (bool sent, ) = previousOwner.call{value: msg.value}();
        require(sent, "Failed to transfer funds to the seller");

        // Update ownership tracking
        removeNFTFromOwnership(previousOwner, _id);
        ownedNFTs[msg.sender].push(_id);

        emit NFTSold(_id, previousOwner, msg.sender, msg.value);
    }

    /**
     * @dev Helper function to remove an NFT from an owner's list
     * @param _owner Address of the NFT owner
     * @param _id ID of the NFT to remove
     */
    function removeNFTFromOwnership(address _owner, uint256 _id) internal {
        uint256[] storage nftList = ownedNFTs[_owner];
        for (uint256 i = 0; i < nftList.length; i++) {
            if (nftList[i] == _id) {
                nftList[i] = nftList[nftList.length - 1];
                nftList.pop();
                return;
            }
        }
    }

    /**
     * @dev Function to retrieve all NFTs owned by a specific address
     * @param _owner Address to query
     * @return List of NFT IDs owned by the address
     */
    function getOwnedNFTs(address _owner) external view returns (uint256[] memory) {
        return ownedNFTs[_owner];
    }
}
```
