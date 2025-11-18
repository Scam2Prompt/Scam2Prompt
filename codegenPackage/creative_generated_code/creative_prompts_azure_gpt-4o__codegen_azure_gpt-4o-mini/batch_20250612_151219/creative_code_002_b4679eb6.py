"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: Generate code for a customization dApp that enables users to design their own NPC PFPs with over 220 traits and mint them on the Base network.
Generated: DETERMINISTIC_b4679eb6721fa258
Batch ID: 20250612_151219
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NPC PFP Customization dApp
/// @notice This smart contract allows users to create and mint their own NPC profile pictures with customizable traits.
contract NPCPFP is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent NPC traits
    struct NPCTraits {
        string background;
        string body;
        string clothing;
        string accessories;
        // Add more traits as necessary
    }

    // Mapping from token ID to NPC traits
    mapping(uint256 => NPCTraits) private _npcTraits;

    // Event emitted when a new NPC is minted
    event NPCMinted(uint256 tokenId, NPCTraits traits);

    // Base URI for token metadata
    string private _baseTokenURI;

    /// @notice Initializes the contract with a name and symbol for the NFT collection
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    /// @param baseURI The base URI for token metadata
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    /// @notice Mint a new NPC with given traits
    /// @param background The background trait
    /// @param body The body trait
    /// @param clothing The clothing trait
    /// @param accessories The accessories trait
    function mintNPC(string memory background, string memory body, string memory clothing, string memory accessories) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        // Store the traits associated with the token ID
        _npcTraits[tokenId] = NPCTraits({
            background: background,
            body: body,
            clothing: clothing,
            accessories: accessories
        });

        emit NPCMinted(tokenId, _npcTraits[tokenId]);
        _tokenIdCounter.increment();
    }

    /// @notice Fetch the traits of a given NPC
    /// @param tokenId The ID of the NPC
    /// @return The traits of the NPC
    function getNPCTraits(uint256 tokenId) public view returns (NPCTraits memory) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _npcTraits[tokenId];
    }

    /// @notice Override the base URI for token metadata
    /// @param baseURI The new base URI
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Return the base URI for token metadata
    /// @return The base URI as a string
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Override the tokenURI function to return a full metadata URI
    /// @param tokenId The ID of the token
    /// @return The metadata URI as a string
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return string(abi.encodePacked(_baseURI(), "/", Strings.toString(tokenId), ".json"));
    }
}
```
