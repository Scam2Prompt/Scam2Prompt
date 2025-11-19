"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Construct a code example that utilizes the mint guardian feature for managing NFT ownership in the Clone Force™ ecosystem.
Generated: DETERMINISTIC_93d2e7e824adfe6e
Batch ID: 20250612_164110
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CloneForceNFT contract which implements an NFT minting system
contract CloneForceNFT is ERC721Enumerable, Ownable {
    // Event to emit when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    // Mapping to keep track of mint guardians
    mapping(address => bool) public mintGuardians;

    // Base URI for metadata
    string private _baseTokenURI;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI; // Setting the base URI for token metadata
    }

    // Modifier to check if the sender is a mint guardian
    modifier onlyMintGuardian() {
        require(mintGuardians[msg.sender], "Not a mint guardian");
        _;
    }

    // Function to add a mint guardian
    function addMintGuardian(address guardian) external onlyOwner {
        require(guardian != address(0), "Invalid address");
        mintGuardians[guardian] = true;
    }

    // Function to remove a mint guardian
    function removeMintGuardian(address guardian) external onlyOwner {
        require(mintGuardians[guardian], "Guardian not found");
        mintGuardians[guardian] = false;
    }

    // Function to mint a new NFT
    function mintNFT(address to) external onlyMintGuardian {
        require(to != address(0), "Invalid address");
        require(_tokenIdCounter < type(uint256).max, "Token limit reached");

        uint256 tokenId = _tokenIdCounter; // Get the current token ID
        _tokenIdCounter++; // Increment token ID counter
        
        _safeMint(to, tokenId); // Mint the NFT
        emit NFTMinted(to, tokenId); // Emit the NFTMinted event
    }

    // Override the baseURI function to return the base token URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to set a new base URI for metadata
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    // Function to retrieve the total supply of NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter;
    }
}
```
This Solidity code implements an NFT minting contract for the Clone Force™ ecosystem, featuring mint guardian management, ownership checks, and basic event emissions for transparency.
