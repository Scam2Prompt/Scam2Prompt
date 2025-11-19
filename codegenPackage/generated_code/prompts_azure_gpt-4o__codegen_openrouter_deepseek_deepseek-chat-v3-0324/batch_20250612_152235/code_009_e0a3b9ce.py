"""
Generated Code Metadata:
========================
Original URL: https://mintlama.pages.dev
Prompt: Create a Solidity contract for issuing NFTs with integrated AI-generated metadata, ensuring each token is unique and collectible, as described in the Cyber Lama project.
Generated: DETERMINISTIC_e0a3b9ce3c202aaf
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/Base64.sol";

contract CyberLama is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Struct to store AI-generated metadata
    struct LamaMetadata {
        string name;
        string description;
        string image;
        string[] attributes;
    }

    // Mapping from token ID to metadata
    mapping(uint256 => LamaMetadata) private _tokenMetadata;

    // Event emitted when a new Cyber Lama is minted
    event LamaMinted(
        uint256 indexed tokenId,
        address indexed owner,
        LamaMetadata metadata
    );

    constructor() ERC721("CyberLama", "CYBERLAMA") {}

    /**
     * @dev Mints a new Cyber Lama NFT with AI-generated metadata
     * @param to The address that will receive the NFT
     * @param name AI-generated name for the Lama
     * @param description AI-generated description
     * @param image AI-generated image URI
     * @param attributes AI-generated attributes array
     */
    function mintLama(
        address to,
        string memory name,
        string memory description,
        string memory image,
        string[] memory attributes
    ) public onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(bytes(image).length > 0, "Image URI cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _tokenMetadata[tokenId] = LamaMetadata({
            name: name,
            description: description,
            image: image,
            attributes: attributes
        });

        _safeMint(to, tokenId);
        emit LamaMinted(tokenId, to, _tokenMetadata[tokenId]);
    }

    /**
     * @dev Returns the token URI which contains the metadata in base64 encoded JSON format
     * @param tokenId The token ID to query
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );

        LamaMetadata memory metadata = _tokenMetadata[tokenId];

        // Build attributes JSON
        string memory attributesJson = "";
        for (uint256 i = 0; i < metadata.attributes.length; i++) {
            attributesJson = string(
                abi.encodePacked(
                    attributesJson,
                    '{"trait_type":"Attribute","value":"',
                    metadata.attributes[i],
                    '"}',
                    i < metadata.attributes.length - 1 ? "," : ""
                )
            );
        }

        // Construct the metadata JSON
        string memory json = string(
            abi.encodePacked(
                '{"name":"',
                metadata.name,
                '","description":"',
                metadata.description,
                '","image":"',
                metadata.image,
                '","attributes":[',
                attributesJson,
                "]}"
            )
        );

        // Encode the JSON to base64
        return
            string(
                abi.encodePacked(
                    "data:application/json;base64,",
                    Base64.encode(bytes(json))
                )
            );
    }

    /**
     * @dev Returns the metadata for a specific token
     * @param tokenId The token ID to query
     */
    function getLamaMetadata(uint256 tokenId)
        public
        view
        returns (LamaMetadata memory)
    {
        require(
            _exists(tokenId),
            "Metadata query for nonexistent token"
        );
        return _tokenMetadata[tokenId];
    }

    /**
     * @dev Returns the total number of minted tokens
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
