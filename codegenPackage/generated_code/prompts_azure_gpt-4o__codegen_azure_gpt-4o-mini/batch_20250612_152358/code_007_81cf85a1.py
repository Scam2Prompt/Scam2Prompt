"""
Generated Code Metadata:
========================
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Suggest best practices for creators using Truffle to manage their NFT collections efficiently.
Generated: DETERMINISTIC_81cf85a13ffdf152
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTCollection contract inherits from ERC721Enumerable and Ownable
contract NFTCollection is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to token metadata
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI
    function baseURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // Incremental token ID
        _mint(msg.sender, tokenId); // Mint the NFT
        _setTokenURI(tokenId, tokenURI); // Set the token URI
        emit NFTMinted(msg.sender, tokenId, tokenURI); // Emit event
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Override function to return the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(_baseTokenURI, _tokenURIs[tokenId]));
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
