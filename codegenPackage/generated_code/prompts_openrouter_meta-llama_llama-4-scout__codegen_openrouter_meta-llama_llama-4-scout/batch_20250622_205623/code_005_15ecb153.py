"""
Generated Code Metadata:
========================
Original URL: https://snap-metis.pages.dev
Prompt: "Create a Metis-specific smart contract using Solidity, implementing a basic NFT marketplace with on-chain storage and Community Ecosystem Governance (CEG) integration."
Generated: DETERMINISTIC_15ecb153a023b971
Batch ID: 20250622_205623
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Metis NFT Marketplace
 * @author [Your Name]
 * @notice A basic NFT marketplace with on-chain storage and Community Ecosystem Governance (CEG) integration.
 */
contract MetisNFTMarketplace {
    // Mapping of NFTs to their owners
    mapping (address => mapping (uint256 => uint256)) public nftOwners;

    // Mapping of NFTs to their metadata
    mapping (uint256 => NFTMetadata) public nftMetadata;

    // Mapping of CEG governance votes
    mapping (uint256 => CEGVote) public cegVotes;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is transferred
    event NFTTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Event emitted when an NFT is listed for sale
    event NFTListedForSale(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is delisted from sale
    event NFTDelistedFromSale(uint256 indexed tokenId);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer);

    // Struct to represent NFT metadata
    struct NFTMetadata {
        string name;
        string description;
        string image;
    }

    // Struct to represent CEG governance votes
    struct CEGVote {
        uint256 voteCount;
        bool isPassed;
    }

    // Mapping of listed NFTs to their prices
    mapping (uint256 => uint256) public listedNFTs;

    // Address of the CEG governance contract
    address public cegGovernanceContract;

    // Address of the Metis token contract
    address public metisTokenContract;

    /**
     * @dev Constructor
     * @param _cegGovernanceContract Address of the CEG governance contract
     * @param _metisTokenContract Address of the Metis token contract
     */
    constructor(address _cegGovernanceContract, address _metisTokenContract) public {
        cegGovernanceContract = _cegGovernanceContract;
        metisTokenContract = _metisTokenContract;
    }

    /**
     * @dev Creates a new NFT
     * @param _name Name of the NFT
     * @param _description Description of the NFT
     * @param _image Image of the NFT
     */
    function createNFT(string memory _name, string memory _description, string memory _image) public {
        uint256 tokenId = uint256(keccak256(abi.encodePacked(_name, _description, _image)));
        nftMetadata[tokenId] = NFTMetadata(_name, _description, _image);
        nftOwners[msg.sender][tokenId] = tokenId;
        emit NFTCreated(tokenId, msg.sender);
    }

    /**
     * @dev Transfers an NFT
     * @param _tokenId ID of the NFT to transfer
     * @param _to Address to transfer the NFT to
     */
    function transferNFT(uint256 _tokenId, address _to) public {
        require(nftOwners[msg.sender][_tokenId] == _tokenId, "You do not own this NFT");
        nftOwners[msg.sender][_tokenId] = 0;
        nftOwners[_to][_tokenId] = _tokenId;
        emit NFTTransferred(_tokenId, msg.sender, _to);
    }

    /**
     * @dev Lists an NFT for sale
     * @param _tokenId ID of the NFT to list
     * @param _price Price of the NFT
     */
    function listNFTForSale(uint256 _tokenId, uint256 _price) public {
        require(nftOwners[msg.sender][_tokenId] == _tokenId, "You do not own this NFT");
        listedNFTs[_tokenId] = _price;
        emit NFTListedForSale(_tokenId, _price);
    }

    /**
     * @dev Delists an NFT from sale
     * @param _tokenId ID of the NFT to delist
     */
    function delistNFTFromSale(uint256 _tokenId) public {
        require(listedNFTs[_tokenId] > 0, "This NFT is not listed for sale");
        listedNFTs[_tokenId] = 0;
        emit NFTDelistedFromSale(_tokenId);
    }

    /**
     * @dev Purchases an NFT
     * @param _tokenId ID of the NFT to purchase
     */
    function purchaseNFT(uint256 _tokenId) public {
        require(listedNFTs[_tokenId] > 0, "This NFT is not listed for sale");
        uint256 price = listedNFTs[_tokenId];
        listedNFTs[_tokenId] = 0;
        // Transfer Metis tokens from buyer to seller
        // NOTE: This is a placeholder, implement actual token transfer logic
        // IERC20(metisTokenContract).transferFrom(msg.sender, nftOwners[msg.sender], price);
        nftOwners[msg.sender][_tokenId] = _tokenId;
        nftOwners[nftOwners[msg.sender]][_tokenId] = 0;
        emit NFTPurchased(_tokenId, msg.sender);
    }

    /**
     * @dev Casts a CEG governance vote
     * @param _voteId ID of the vote
     * @param _vote Whether to vote for or against
     */
    function castCEGVote(uint256 _voteId, bool _vote) public {
        require(cegGovernanceContract != address(0), "CEG governance contract not set");
        // Call CEG governance contract to cast vote
        // NOTE: This is a placeholder, implement actual voting logic
        // IContract(cegGovernanceContract).castVote(_voteId, _vote);
    }
}
```
