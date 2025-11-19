"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Develop a smart contract in Solidity that incorporates rarity traits for NFTs, similar to the KevinLand approach of generating NFTs from dozens of traits.
Generated: DETERMINISTIC_55743b0871d548d0
Batch ID: 20250612_152827
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
 * @title NFT contract with rarity traits
 */
contract NFTRarityTraits is SafeERC721, Ownable {
    // Mapping of NFT traits
    mapping (address => mapping (uint256 => NFT)) public nftTraits;

    // Mapping of trait rarities
    mapping (string => uint256) public traitRarities;

    // Mapping of trait supply
    mapping (string => uint256) public traitSupply;

    // Event emitted when an NFT is created
    event NewNFT(address indexed owner, uint256 indexed tokenId);

    // Event emitted when a trait is added
    event NewTrait(string traitName, uint256 rarity);

    // Struct representing an NFT
    struct NFT {
        uint256 id;
        address owner;
        string[] traits;
    }

    // Mapping of NFTs
    mapping (uint256 => NFT) public nfts;

    // Total supply of NFTs
    uint256 public totalSupply;

    // Mapping of approved addresses
    mapping (address => bool) public approvedAddresses;

    /**
     * @dev Constructor
     */
    constructor() public {
        // Initialize total supply
        totalSupply = 0;
    }

    /**
     * @dev Add a new trait
     * @param traitName Name of the trait
     * @param rarity Rarity of the trait (1-100)
     */
    function addTrait(string memory traitName, uint256 rarity) public onlyOwner {
        require(rarity >= 1 && rarity <= 100, "Rarity must be between 1 and 100");
        traitRarities[traitName] = rarity;
        emit NewTrait(traitName, rarity);
    }

    /**
     * @dev Create a new NFT
     * @param traits Array of trait names
     */
    function createNFT(string[] memory traits) public {
        // Generate a random NFT id
        uint256 tokenId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))) % (2**256);

        // Check if NFT id already exists
        while (nfts[tokenId].id != 0) {
            tokenId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp))) % (2**256);
        }

        // Create a new NFT
        NFT memory nft;
        nft.id = tokenId;
        nft.owner = msg.sender;
        nft.traits = traits;

        // Update NFT mappings
        nfts[tokenId] = nft;
        nftTraits[msg.sender][tokenId] = nft;

        // Update total supply
        totalSupply++;

        // Emit event
        emit NewNFT(msg.sender, tokenId);

        // Transfer NFT to owner
        _mint(msg.sender, tokenId);
    }

    /**
     * @dev Get the rarity of an NFT
     * @param tokenId ID of the NFT
     * @return Rarity of the NFT
     */
    function getNFTRarity(uint256 tokenId) public view returns (uint256) {
        NFT memory nft = nfts[tokenId];
        require(nft.id != 0, "NFT does not exist");

        uint256 rarity = 0;
        for (uint256 i = 0; i < nft.traits.length; i++) {
            string memory trait = nft.traits[i];
            rarity += traitRarities[trait];
        }
        return rarity / nft.traits.length;
    }

    /**
     * @dev Get the traits of an NFT
     * @param tokenId ID of the NFT
     * @return Traits of the NFT
     */
    function getNFTraits(uint256 tokenId) public view returns (string[] memory) {
        NFT memory nft = nfts[tokenId];
        require(nft.id != 0, "NFT does not exist");
        return nft.traits;
    }

    /**
     * @dev Check if an address is approved
     * @param addr Address to check
     * @return Whether the address is approved
     */
    function isApproved(address addr) public view returns (bool) {
        return approvedAddresses[addr];
    }

    /**
     * @dev Approve an address
     * @param addr Address to approve
     */
    function approveAddress(address addr) public onlyOwner {
        approvedAddresses[addr] = true;
    }

    /**
     * @dev Revoke approval for an address
     * @param addr Address to revoke
     */
    function revokeApproval(address addr) public onlyOwner {
        approvedAddresses[addr] = false;
    }

    /**
     * @dev Transfer an NFT
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param tokenId ID of the NFT
     */
    function transfer(address from, address to, uint256 tokenId) public {
        require(msg.sender == from || isApproved(msg.sender), "Only owner or approved addresses can transfer");
        _transfer(from, to, tokenId);
    }
}
```
