"""
Generated Code Metadata:
========================
Original URL: https://abc-abracadabra.web.app
Prompt: Generate a smart contract code for an NFT collection with a free public price and no royalties, inspired by the ABC - Abracadabra white list.
Generated: DETERMINISTIC_9bfb81033511531e
Batch ID: 20250622_204900
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
 * @title NFTCollection
 * @dev A smart contract for an NFT collection with free minting and no royalties.
 * Inspired by the ABC - Abracadabra whitelist concept.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollection is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Mapping to track whitelist addresses
    mapping(address => bool) public whitelist;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint an NFT. Free for everyone.
     */
    function mint() external {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(whitelist[msg.sender], "Address not whitelisted");

        // Mint the NFT to the sender
        _safeMint(msg.sender, totalSupply() + 1);
    }

    /**
     * @dev Function to add addresses to the whitelist.
     * Only callable by the owner of the contract.
     * @param addresses Array of addresses to whitelist.
     */
    function addToWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = true;
        }
    }

    /**
     * @dev Function to remove addresses from the whitelist.
     * Only callable by the owner of the contract.
     * @param addresses Array of addresses to remove from the whitelist.
     */
    function removeFromWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = false;
        }
    }

    /**
     * @dev Function to set the base URI for metadata.
     * Only callable by the owner of the contract.
     * @param baseURI The base URI to set.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Internal function to return the base URI for metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Override the ERC721 _transfer function to disable royalties.
     * This ensures no fees are deducted during transfers.
     * @param from Address transferring the NFT.
     * @param to Address receiving the NFT.
     * @param tokenId ID of the NFT being transferred.
     */
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);
        // No additional logic for royalties
    }
}
```
