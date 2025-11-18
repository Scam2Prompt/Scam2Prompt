"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Generate a Solidity contract that leverages Somnia's blockchain to mint and transfer NFTs with interoperability across metaverses.
Generated: DETERMINISTIC_d18a40187dad6c7d
Batch ID: 20250612_151301
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

// Importing OpenZeppelin ERC721 contract
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with other metaverses (placeholder)
interface IMetaverse {
    function transferNFT(address from, address to, uint256 tokenId) external returns (bool);
}

// Main NFT contract
contract SomniaNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    // Event emitted when an NFT is transferred to another metaverse
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId, address metaverse);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint new NFTs
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // New token ID
        _mint(to, tokenId); // Minting the NFT
        emit NFTMinted(to, tokenId); // Emitting mint event
    }

    // Function to set the base URI for metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to retrieve the base URI for metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to transfer NFTs to other metaverses
    function transferToMetaverse(address metaverse, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not owner nor approved");
        require(IMetaverse(metaverse).transferNFT(msg.sender, to, tokenId), "Transfer failed");
        
        // Burn the NFT locally after transferring to another metaverse
        _burn(tokenId);
        
        emit NFTTransferred(msg.sender, to, tokenId, metaverse); // Emitting transfer event
    }

    // Function to handle receiving Ether (if needed)
    receive() external payable {
        // Accept Ether payments
    }

    // Function to withdraw contract balance (if necessary)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
