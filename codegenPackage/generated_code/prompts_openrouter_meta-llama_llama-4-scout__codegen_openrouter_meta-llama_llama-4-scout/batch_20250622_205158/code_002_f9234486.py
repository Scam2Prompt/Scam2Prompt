"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: "Design a smart contract using Solidity that interacts with the Rangers Protocol's NFT protocol, allowing users to create, transfer, and manage NFTs on the platform, and provide a detailed explanation of the contract's functionality."
Generated: DETERMINISTIC_f923448669e1bc61
Batch ID: 20250622_205158
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
 * @title Rangers NFT Contract
 * @author [Your Name]
 * @notice This contract interacts with the Rangers Protocol's NFT protocol,
 *         allowing users to create, transfer, and manage NFTs on the platform.
 */
contract RangersNFT {
    // Mapping of NFT owners
    mapping (address => mapping (uint256 => uint256)) public nftOwners;

    // Mapping of NFT metadata
    mapping (uint256 => NFTMetadata) public nftMetadata;

    // Rangers Protocol's NFT interface
    IRangersNFT public rangersNFT;

    // Event emitted when an NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an NFT is transferred
    event NFTTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Struct to hold NFT metadata
    struct NFTMetadata {
        string name;
        string description;
        string image;
    }

    /**
     * @dev Constructor
     * @param _rangersNFT Address of the Rangers Protocol's NFT contract
     */
    constructor(address _rangersNFT) public {
        require(_rangersNFT != address(0), "RangersNFT: Invalid Rangers NFT contract address");
        rangersNFT = IRangersNFT(_rangersNFT);
    }

    /**
     * @dev Creates a new NFT
     * @param _name Name of the NFT
     * @param _description Description of the NFT
     * @param _image Image URL of the NFT
     * @return uint256 ID of the newly created NFT
     */
    function createNFT(string memory _name, string memory _description, string memory _image) public returns (uint256) {
        // Check if the user has the required permissions to create an NFT
        require(rangersNFT.isValidUser(msg.sender), "RangersNFT: User is not authorized to create NFTs");

        // Generate a new token ID
        uint256 tokenId = rangersNFT.getNextTokenId();

        // Create the NFT metadata
        NFTMetadata memory metadata = NFTMetadata(_name, _description, _image);

        // Store the NFT metadata
        nftMetadata[tokenId] = metadata;

        // Transfer the NFT to the creator
        nftOwners[msg.sender][tokenId] = tokenId;

        // Emit the NFT created event
        emit NFTCreated(tokenId, msg.sender);

        return tokenId;
    }

    /**
     * @dev Transfers an NFT
     * @param _tokenId ID of the NFT to transfer
     * @param _to Address of the recipient
     */
    function transferNFT(uint256 _tokenId, address _to) public {
        // Check if the sender is the owner of the NFT
        require(nftOwners[msg.sender][_tokenId] == _tokenId, "RangersNFT: User is not the owner of the NFT");

        // Check if the recipient is a valid address
        require(_to != address(0), "RangersNFT: Invalid recipient address");

        // Transfer the NFT
        nftOwners[_to][_tokenId] = _tokenId;
        delete nftOwners[msg.sender][_tokenId];

        // Emit the NFT transferred event
        emit NFTTransferred(_tokenId, msg.sender, _to);
    }

    /**
     * @dev Gets the owner of an NFT
     * @param _tokenId ID of the NFT
     * @return address Owner of the NFT
     */
    function getNFTowner(uint256 _tokenId) public view returns (address) {
        for (address owner in nftOwners) {
            if (nftOwners[owner][_tokenId] == _tokenId) {
                return owner;
            }
        }
        return address(0);
    }
}

// Rangers Protocol's NFT interface
interface IRangersNFT {
    function isValidUser(address _user) external view returns (bool);
    function getNextTokenId() external view returns (uint256);
}
```
