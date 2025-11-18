"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dioneprotocol-app.pages.dev
Prompt: Write a Solidity contract for an NFT collection inspired by celestial narratives, similar to the Elysium88 collection on Odyssey Chain. Include features for storyline integration and staking boosts.
Generated: DETERMINISTIC_bdc5055f62a252d6
Batch ID: 20250612_153527
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
 * @title CelestialNFTCollection
 * @notice A smart contract for an NFT collection inspired by celestial narratives.
 *         Includes storyline integration and staking boost functionality.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CelestialNFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Token ID tracker
    Counters.Counter private _tokenIdCounter;

    // Structure to hold storyline data
    struct Storyline {
        string title;       // Title of the narrative
        string description; // Description or story
    }

    // Mapping to associate token IDs with their storyline details
    mapping(uint256 => Storyline) private _storylines;

    // Mapping to track staking boosts for token IDs
    mapping(uint256 => uint256) private _stakingBoosts;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to set the collection name and symbol, and initial base URI.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseURI Base URI for token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override baseURI function from ERC721 to return custom base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mint a new NFT and associate it with a storyline.
     * @param to Address to mint the NFT to.
     * @param title Title of the narrative.
     * @param description Description of the narrative.
     */
    function mint(address to, string memory title, string memory description) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the token
        _mint(to, tokenId);

        // Store the storyline details
        _storylines[tokenId] = Storyline(title, description);
    }

    /**
     * @dev Retrieve the storyline details for a specific token ID.
     * @param tokenId ID of the token.
     * @return title Title of the narrative.
     * @return description Description of the narrative.
     */
    function getStoryline(uint256 tokenId) external view returns (string memory title, string memory description) {
        require(_exists(tokenId), "Token does not exist");
        Storyline memory storyline = _storylines[tokenId];
        return (storyline.title, storyline.description);
    }

    /**
     * @dev Set staking boost for a token ID.
     * @param tokenId ID of the token.
     * @param boostAmount Amount of staking boost to set.
     */
    function setStakingBoost(uint256 tokenId, uint256 boostAmount) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _stakingBoosts[tokenId] = boostAmount;
    }

    /**
     * @dev Get the staking boost for a specific token ID.
     * @param tokenId ID of the token.
     * @return boostAmount Staking boost amount associated with the token.
     */
    function getStakingBoost(uint256 tokenId) external view returns (uint256 boostAmount) {
        require(_exists(tokenId), "Token does not exist");
        return _stakingBoosts[tokenId];
    }

    /**
     * @dev Update the base token URI.
     * @param baseURI New base URI for token metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
}
```
