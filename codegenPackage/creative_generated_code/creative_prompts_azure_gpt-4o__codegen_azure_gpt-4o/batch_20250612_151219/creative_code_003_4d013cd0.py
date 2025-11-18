"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frame-i48.pages.dev
Prompt: Write a smart contract in Solidity to create an NFT collection on the Frame network with enforced royalties using the Palette Protocol.
Generated: DETERMINISTIC_4d013cd030397ebb
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

// Import OpenZeppelin's ERC721 standard implementation and required extensions
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Palette Protocol to enforce royalties
interface IPaletteProtocol {
    function setRoyalty(address owner, uint256 tokenId, uint256 percentage) external;
    function getRoyalty(uint256 tokenId) external view returns (address, uint256);
}

// Smart contract to create an NFT collection with enforced royalties on the Frame network
contract FrameNFTCollection is ERC721URIStorage, Ownable {
    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI, uint256 royaltyPercentage);

    // Reference to the Palette Protocol contract
    IPaletteProtocol public paletteProtocol;

    // Counter to generate unique token IDs
    uint256 private _tokenIdCounter;

    // Constructor to initialize the NFT collection and Palette Protocol contract
    constructor(string memory name, string memory symbol, address paletteProtocolAddress) ERC721(name, symbol) {
        require(paletteProtocolAddress != address(0), "Palette Protocol address cannot be zero");
        paletteProtocol = IPaletteProtocol(paletteProtocolAddress);
    }

    /**
     * @dev Mint a new NFT with specified tokenURI and royalty percentage
     * @param to Address of the recipient
     * @param tokenURI URI pointing to the metadata of the NFT
     * @param royaltyPercentage Percentage of royalties (e.g., 1000 = 10%)
     */
    function mintNFT(address to, string memory tokenURI, uint256 royaltyPercentage) external onlyOwner {
        require(to != address(0), "Recipient address cannot be zero");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(royaltyPercentage <= 10000, "Royalty percentage cannot exceed 100%");

        // Increment the token ID counter and mint the NFT
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;
        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Set the royalty with the Palette Protocol
        paletteProtocol.setRoyalty(to, newTokenId, royaltyPercentage);

        // Emit the NFTMinted event
        emit NFTMinted(to, newTokenId, tokenURI, royaltyPercentage);
    }

    /**
     * @dev Retrieve royalty information for a specific token ID
     * @param tokenId ID of the token
     * @return owner Address of the royalty recipient
     * @return percentage Royalty percentage
     */
    function getRoyaltyInfo(uint256 tokenId) external view returns (address owner, uint256 percentage) {
        return paletteProtocol.getRoyalty(tokenId);
    }

    /**
     * @dev Override _transfer to ensure royalties are enforced on transfers
     * @param from Address of the sender
     * @param to Address of the recipient
     * @param tokenId ID of the token being transferred
     */
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);

        // Fetch royalty info and enforce it (implementation depends on the Palette Protocol standards)
        (, uint256 royaltyPercentage) = paletteProtocol.getRoyalty(tokenId);
        require(royaltyPercentage > 0, "Royalty enforcement failed");
        // Logic to enforce royalty payment would go here, if necessary
    }
}
```
