"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Write a smart contract code for minting NFTs with specific traits, similar to KevinLands, which has 10k unique NFTs generated from dozens of different traits.
Generated: DETERMINISTIC_a3278a534325ceec
Batch ID: 20250622_210348
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

/**
 * @title NFTMintingContract
 * @dev A smart contract for minting NFTs with specific traits.
 *      This contract supports the generation of unique NFTs with traits similar to KevinLands.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private _baseTokenURI;

    // Struct to define traits for an NFT
    struct Traits {
        string background;
        string body;
        string accessory;
        string headgear;
    }

    // Mapping from token ID to traits
    mapping(uint256 => Traits) private _tokenTraits;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner, Traits traits);

    // Constructor to initialize the contract
    constructor(string memory baseURI) ERC721("KevinLandsNFT", "KLNFT") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT with specific traits.
     * @param background The background trait of the NFT.
     * @param body The body trait of the NFT.
     * @param accessory The accessory trait of the NFT.
     * @param headgear The headgear trait of the NFT.
     */
    function mintNFT(
        string memory background,
        string memory body,
        string memory accessory,
        string memory headgear
    ) external {
        // Ensure the maximum supply is not exceeded
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        // Generate a new token ID
        uint256 tokenId = totalSupply() + 1;

        // Assign traits to the new NFT
        _tokenTraits[tokenId] = Traits(background, body, accessory, headgear);

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);

        // Emit the minting event
        emit NFTMinted(tokenId, msg.sender, _tokenTraits[tokenId]);
    }

    /**
     * @dev Get the traits of a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return Traits of the NFT.
     */
    function getTraits(uint256 tokenId) external view returns (Traits memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        return _tokenTraits[tokenId];
    }

    /**
     * @dev Set the base URI for metadata.
     * @param baseURI The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override the base URI function from ERC721.
     * @return Base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to enforce additional rules if needed.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Additional rules can be added here if necessary
    }
}
```
