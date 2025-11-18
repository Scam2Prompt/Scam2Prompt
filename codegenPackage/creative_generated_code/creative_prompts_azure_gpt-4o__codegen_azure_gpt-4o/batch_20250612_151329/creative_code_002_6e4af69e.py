"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-two.vercel.app
Prompt: Develop a smart contract in Solidity that supports limited edition NFT drops (e.g., 10 editions for "The Decay"), as outlined in the content.
Generated: DETERMINISTIC_6e4af69ea84a28e9
Batch ID: 20250612_151329
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
 * @title LimitedEditionNFT
 * @dev A smart contract for creating limited edition NFT drops.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LimitedEditionNFT is ERC721Enumerable, Ownable {
    // Event for minting a new limited edition NFT
    event MintLimitedEdition(address indexed to, uint256 indexed tokenId, string indexed editionName);

    // Struct to store information about each limited edition drop
    struct Edition {
        string name;
        uint256 maxSupply;
        uint256 currentSupply;
    }

    // Mapping to store editions data
    mapping(string => Edition) private editions;

    // Base URI for NFT metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize contract with name and symbol of the NFT collection.
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseURI_ Base URI for NFT metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseURI_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseURI_;
    }

    /**
     * @dev Function to create a new limited edition drop.
     * @param editionName Name of the edition
     * @param maxSupply Maximum supply for the edition
     */
    function createEdition(string memory editionName, uint256 maxSupply) external onlyOwner {
        require(maxSupply > 0, "Max supply must be greater than zero");
        require(editions[editionName].maxSupply == 0, "Edition already exists");

        editions[editionName] = Edition({
            name: editionName,
            maxSupply: maxSupply,
            currentSupply: 0
        });
    }

    /**
     * @dev Function to mint an NFT from a specific edition.
     * @param to Address to mint the NFT to
     * @param editionName Name of the edition to mint from
     */
    function mint(address to, string memory editionName) external onlyOwner {
        Edition storage edition = editions[editionName];
        require(edition.maxSupply > 0, "Edition does not exist");
        require(edition.currentSupply < edition.maxSupply, "Edition sold out");

        // Increment the current supply of the edition
        edition.currentSupply += 1;

        // Mint the NFT
        uint256 tokenId = totalSupply() + 1; // Token ID starts from 1
        _safeMint(to, tokenId);

        // Emit event
        emit MintLimitedEdition(to, tokenId, editionName);
    }

    /**
     * @dev Function to retrieve metadata base URI.
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for NFT metadata.
     * @param baseURI_ New base URI
     */
    function setBaseURI(string memory baseURI_) external onlyOwner {
        _baseTokenURI = baseURI_;
    }

    /**
     * @dev Function to get details of an edition.
     * @param editionName Name of the edition
     * @return Edition details (name, maxSupply, currentSupply)
     */
    function getEditionDetails(string memory editionName)
        external
        view
        returns (string memory, uint256, uint256)
    {
        Edition memory edition = editions[editionName];
        require(edition.maxSupply > 0, "Edition does not exist");

        return (edition.name, edition.maxSupply, edition.currentSupply);
    }
}
```
