"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citizwentokyo.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates the minting of new identities and lands in the Neo Tokyo metaverse, adhering to the token cost specifications provided.
Generated: DETERMINISTIC_59686e4f4041df0c
Batch ID: 20250612_153400
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
 * @title NeoTokyoIdentityAndLand
 * @dev Smart contract for minting identities and lands in the Neo Tokyo metaverse.
 *      This contract uses ERC721 standards.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NeoTokyoIdentityAndLand is ERC721, Ownable {
    // Token counters for identities and lands
    uint256 public identityCounter;
    uint256 public landCounter;

    // Token costs
    uint256 public identityCost = 0.05 ether; // Cost for identity minting
    uint256 public landCost = 0.1 ether;     // Cost for land minting

    // Mapping to store metadata for identities and lands
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new identity is minted
    event IdentityMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    // Event emitted when a new land is minted
    event LandMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    constructor() ERC721("NeoTokyoIdentityAndLand", "NTIL") {}

    /**
     * @dev Mint a new identity token.
     * @param tokenURI The metadata URI for the identity token.
     */
    function mintIdentity(string memory tokenURI) external payable {
        require(msg.value >= identityCost, "Insufficient funds to mint identity");

        // Increment counter and mint token
        identityCounter++;
        uint256 tokenId = identityCounter;
        _safeMint(msg.sender, tokenId);

        // Set token URI and emit event
        _setTokenURI(tokenId, tokenURI);
        emit IdentityMinted(msg.sender, tokenId, tokenURI);
    }

    /**
     * @dev Mint a new land token.
     * @param tokenURI The metadata URI for the land token.
     */
    function mintLand(string memory tokenURI) external payable {
        require(msg.value >= landCost, "Insufficient funds to mint land");

        // Increment counter and mint token
        landCounter++;
        uint256 tokenId = identityCounter + landCounter; // Different ID range from identities
        _safeMint(msg.sender, tokenId);

        // Set token URI and emit event
        _setTokenURI(tokenId, tokenURI);
        emit LandMinted(msg.sender, tokenId, tokenURI);
    }

    /**
     * @dev Set a token URI for a given token ID.
     * @param tokenId The ID of the token.
     * @param tokenURI The metadata URI of the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Retrieve the token URI of a given token ID.
     * @param tokenId The ID of the token.
     * @return The metadata URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Update the minting cost for identities.
     * @param newCost The new cost in wei for identity minting.
     */
    function setIdentityCost(uint256 newCost) external onlyOwner {
        identityCost = newCost;
    }

    /**
     * @dev Update the minting cost for lands.
     * @param newCost The new cost in wei for land minting.
     */
    function setLandCost(uint256 newCost) external onlyOwner {
        landCost = newCost;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner()).transfer(balance);
    }
}
```
