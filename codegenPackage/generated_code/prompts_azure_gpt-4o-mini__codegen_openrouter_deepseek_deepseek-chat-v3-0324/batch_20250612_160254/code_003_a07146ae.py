"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Develop a Solidity function to mint a PLR NFT that represents ownership of a digital product with private label rights, ensuring it includes cryptographic protection.
Generated: DETERMINISTIC_a07146ae79e33dea
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PLRNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using ECDSA for bytes32;

    Counters.Counter private _tokenIdCounter;

    // Struct to store product metadata
    struct Product {
        string name;
        string description;
        string ipfsHash;
        uint256 price;
        bool isActive;
    }

    // Mapping from token ID to Product
    mapping(uint256 => Product) private _products;

    // Mapping from IPFS hash to token ID to prevent duplicates
    mapping(string => bool) private _ipfsHashes;

    // Event emitted when a new PLR NFT is minted
    event PLRNFTMinted(
        uint256 indexed tokenId,
        address indexed owner,
        string name,
        string ipfsHash
    );

    constructor() ERC721("PrivateLabelRightsNFT", "PLRNFT") {}

    /**
     * @dev Mints a new PLR NFT with cryptographic protection
     * @param name Name of the digital product
     * @param description Description of the digital product
     * @param ipfsHash IPFS hash of the digital product content
     * @param price Price of the digital product in wei
     * @param signature Cryptographic signature to verify authenticity
     */
    function mintPLRNFT(
        string memory name,
        string memory description,
        string memory ipfsHash,
        uint256 price,
        bytes memory signature
    ) external payable {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(bytes(ipfsHash).length > 0, "IPFS hash cannot be empty");
        require(msg.value >= price, "Insufficient payment");
        require(!_ipfsHashes[ipfsHash], "IPFS hash already exists");

        // Verify the cryptographic signature
        bytes32 messageHash = keccak256(
            abi.encodePacked(name, description, ipfsHash, price, msg.sender)
        );
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        address signer = ethSignedMessageHash.recover(signature);
        require(signer == owner(), "Invalid signature");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Store product metadata
        _products[tokenId] = Product({
            name: name,
            description: description,
            ipfsHash: ipfsHash,
            price: price,
            isActive: true
        });

        _ipfsHashes[ipfsHash] = true;

        emit PLRNFTMinted(tokenId, msg.sender, name, ipfsHash);
    }

    /**
     * @dev Returns the product details for a given token ID
     * @param tokenId The NFT token ID
     */
    function getProductDetails(uint256 tokenId)
        external
        view
        returns (
            string memory name,
            string memory description,
            string memory ipfsHash,
            uint256 price,
            bool isActive
        )
    {
        require(_exists(tokenId), "Token does not exist");
        Product memory product = _products[tokenId];
        return (
            product.name,
            product.description,
            product.ipfsHash,
            product.price,
            product.isActive
        );
    }

    /**
     * @dev Withdraw contract balance to owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Toggle product active status (only owner)
     * @param tokenId The NFT token ID
     * @param isActive New status
     */
    function setProductStatus(uint256 tokenId, bool isActive) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _products[tokenId].isActive = isActive;
    }
}
```
