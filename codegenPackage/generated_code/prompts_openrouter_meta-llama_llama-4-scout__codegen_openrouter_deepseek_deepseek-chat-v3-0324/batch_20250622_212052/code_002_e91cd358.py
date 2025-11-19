"""
Generated Code Metadata:
========================
Original URL: https://dvhuh.pages.dev
Prompt: Generate code to enable NFT minting, transferring, and receiving on a blockchain platform using a mobile wallet or extension.
Generated: DETERMINISTIC_e91cd358c20d33ab
Batch ID: 20250622_212052
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMinter is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping from token ID to creator address
    mapping(uint256 => address) private _creators;

    // Event emitted when a new NFT is minted
    event Minted(address indexed minter, uint256 indexed tokenId, string tokenURI);

    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mints a new NFT and assigns it to the specified address
     * @param to The address that will own the minted NFT
     * @param tokenURI The URI pointing to the NFT metadata
     */
    function mintNFT(address to, string memory tokenURI) public returns (uint256) {
        require(bytes(tokenURI).length > 0, "NFTMinter: tokenURI cannot be empty");
        
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        
        _safeMint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        _creators[newTokenId] = msg.sender;

        emit Minted(msg.sender, newTokenId, tokenURI);
        return newTokenId;
    }

    /**
     * @dev Transfers NFT from one address to another
     * @param from The current owner of the NFT
     * @param to The address to receive the NFT
     * @param tokenId The ID of the NFT to transfer
     */
    function transferNFT(address from, address to, uint256 tokenId) public {
        require(_exists(tokenId), "NFTMinter: NFT does not exist");
        require(_isApprovedOrOwner(msg.sender, tokenId), "NFTMinter: transfer caller is not owner nor approved");
        
        _transfer(from, to, tokenId);
    }

    /**
     * @dev Returns the creator of a specific NFT
     * @param tokenId The ID of the NFT
     */
    function getCreator(uint256 tokenId) public view returns (address) {
        require(_exists(tokenId), "NFTMinter: NFT does not exist");
        return _creators[tokenId];
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burns a specific NFT
     * @param tokenId The ID of the NFT to be burned
     */
    function burn(uint256 tokenId) public {
        require(_isApprovedOrOwner(msg.sender, tokenId), "NFTMinter: caller is not owner nor approved");
        _burn(tokenId);
    }

    /**
     * @dev Returns the URI for a given token ID
     * @param tokenId The ID of the token to query
     */
    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }

    /**
     * @dev Hook that is called before any token transfer
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Destroys `tokenId` and clears storage
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }
}
```

```javascript
// Frontend interaction using ethers.js
import { ethers } from 'ethers';
import NFTMinterABI from './NFTMinterABI.json';

const NFTMinterAddress = "0x..."; // Contract address

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Initialize contract instance
const nftMinter = new ethers.Contract(NFTMinterAddress, NFTMinterABI, signer);

// Mint NFT function
async function mintNFT(toAddress, tokenURI) {
    try {
        const tx = await nftMinter.mintNFT(toAddress, tokenURI);
        await tx.wait();
        console.log("NFT minted successfully");
    } catch (error) {
        console.error("Error minting NFT:", error);
    }
}

// Transfer NFT function
async function transferNFT(fromAddress, toAddress, tokenId) {
    try {
        const tx = await nftMinter.transferNFT(fromAddress, toAddress, tokenId);
        await tx.wait();
        console.log("NFT transferred successfully");
    } catch (error) {
        console.error("Error transferring NFT:", error);
    }
}

// Get NFT owner function
async function getNFTOwner(tokenId) {
    try {
        const owner = await nftMinter.ownerOf(tokenId);
        return owner;
    } catch (error) {
        console.error("Error getting NFT owner:", error);
        return null;
    }
}

// Get NFT metadata URI function
async function getNFTURI(tokenId) {
    try {
        const uri = await nftMinter.tokenURI(tokenId);
        return uri;
    } catch (error) {
        console.error("Error getting NFT URI:", error);
        return null;
    }
}
```
