"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defi.pages.dev
Prompt: Generate a Solidity smart contract for the Narcos Land play-to-own game, including NFT minting, land ownership mechanics, and strategic gameplay features described on the Pablo website.
Generated: DETERMINISTIC_c9045bed209bac59
Batch ID: 20250612_153401
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

// Importing OpenZeppelin contracts for safe ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NarcosLand contract for minting NFTs representing land ownership
contract NarcosLand is ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // State variable to keep track of the next token ID
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to land attributes (could be expanded later)
    struct Land {
        string name;
        string location;
        uint256 size; // Size in acres
        address owner; // Current owner
    }

    mapping(uint256 => Land) public lands;

    // Event emitted when land is minted
    event LandMinted(uint256 indexed tokenId, string name, string location, uint256 size, address owner);

    // Constructor to initialize the smart contract
    constructor() ERC721("NarcosLand", "NLAND") {}

    // Function to mint new land NFTs
    function mintLand(string memory name, string memory location, uint256 size, string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment token ID for the next minting

        // Create and store the land attributes
        lands[tokenId] = Land({
            name: name,
            location: location,
            size: size,
            owner: msg.sender
        });

        // Mint the NFT and set its URI
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Emit event for the minted land
        emit LandMinted(tokenId, name, location, size, msg.sender);
    }

    // Function to transfer land ownership
    function transferLand(uint256 tokenId, address newOwner) external {
        // Ensure the caller is the owner of the land
        require(ownerOf(tokenId) == msg.sender, "You do not own this land");
        require(newOwner != address(0), "Invalid new owner address");

        // Transfer ownership
        _transfer(msg.sender, newOwner, tokenId);

        // Update the land's owner in the mapping
        lands[tokenId].owner = newOwner;
    }

    // Function to get land details
    function getLandDetails(uint256 tokenId) external view returns (string memory, string memory, uint256, address) {
        require(_exists(tokenId), "Land does not exist"); // Check if the land exists
        Land memory land = lands[tokenId]; // Retrieve land details

        // Return land attributes
        return (land.name, land.location, land.size, land.owner);
    }

    // Function to burn a land NFT (only callable by the owner)
    function burnLand(uint256 tokenId) external onlyOwner {
        // Ensure the land exists
        require(_exists(tokenId), "Land does not exist");

        // Burn the NFT
        _burn(tokenId);

        // Remove land details from the mapping
        delete lands[tokenId];
    }
}
```
