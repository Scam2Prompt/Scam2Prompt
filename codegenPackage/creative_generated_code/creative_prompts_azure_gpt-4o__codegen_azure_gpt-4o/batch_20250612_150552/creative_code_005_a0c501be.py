"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://llamanft.pages.dev
Prompt: Develop a Solidity smart contract for issuing NFTs with unique designs, ensuring security and testing mechanisms before public launch, as detailed in the Cyber Lama project.
Generated: DETERMINISTIC_a0c501be1b43abbb
Batch ID: 20250612_150552
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

// Import the ERC721 standard and utilities from OpenZeppelin library
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Cyber Lama NFT Contract for issuing NFTs with unique designs
contract CyberLamaNFT is ERC721URIStorage, Ownable {
    // Variable to track the current token ID
    uint256 private _currentTokenId;

    // Mapping to ensure each design URI is unique
    mapping(string => bool) private _designURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("CyberLamaNFT", "CLNFT") {}

    /**
     * @dev Mint a new NFT with a unique design URI.
     * @param to The address that will own the minted NFT.
     * @param tokenURI The URI containing metadata of the NFT's design.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        // Ensure the design URI is unique
        require(!_designURIs[tokenURI], "Design URI already exists");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT and assign it to the 'to' address
        _safeMint(to, _currentTokenId);

        // Set the token URI for the newly minted NFT
        _setTokenURI(_currentTokenId, tokenURI);

        // Mark the design URI as used
        _designURIs[tokenURI] = true;

        // Emit the NFTMinted event
        emit NFTMinted(to, _currentTokenId, tokenURI);
    }

    /**
     * @dev Retrieve the current token ID count.
     * @return The current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Check if a design URI has already been used.
     * @param tokenURI The URI to check.
     * @return True if the URI has been used, false otherwise.
     */
    function isDesignURIUsed(string memory tokenURI) external view returns (bool) {
        return _designURIs[tokenURI];
    }
}
```
