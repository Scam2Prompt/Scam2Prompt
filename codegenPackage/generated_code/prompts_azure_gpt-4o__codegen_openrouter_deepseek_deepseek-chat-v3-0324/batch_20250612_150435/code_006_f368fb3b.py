"""
Generated Code Metadata:
========================
Original URL: https://btconbase-ai.pages.dev
Prompt: Develop a decentralized application (dApp) that leverages Bitcoin on Base branding and assets under the CC0 license for community-driven projects.
Generated: DETERMINISTIC_f368fb3bba5da57c
Batch ID: 20250612_150435
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title BitcoinOnBaseCommunity
 * @dev A decentralized application (dApp) for community-driven projects leveraging Bitcoin on Base branding
 * @notice This contract allows minting of CC0-licensed NFTs representing community projects
 */
contract BitcoinOnBaseCommunity is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Event emitted when a new project is minted
    event ProjectMinted(address indexed recipient, uint256 tokenId, string projectName);

    /**
     * @dev Constructor sets the name and symbol of the NFT collection
     * @param baseURI The base URI for token metadata
     */
    constructor(string memory baseURI) ERC721("BitcoinOnBase Community Projects", "BOBCP") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new community project NFT
     * @param recipient The address receiving the NFT
     * @param projectName The name of the community project
     */
    function mintProject(address recipient, string memory projectName) external {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(recipient, tokenId);
        emit ProjectMinted(recipient, tokenId, projectName);
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The token ID to query
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, tokenId.toString(), ".json"))
            : "";
    }

    /**
     * @dev Returns the total supply of tokens minted so far
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

```javascript
// Frontend interaction script (using ethers.js)
import { ethers } from 'ethers';
import BitcoinOnBaseCommunityABI from './BitcoinOnBaseCommunityABI.json';

const contractAddress = "0x..."; // Replace with deployed contract address
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const contract = new ethers.Contract(contractAddress, BitcoinOnBaseCommunityABI, signer);

async function mintProject(projectName) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Call the mint function
        const tx = await contract.mintProject(await signer.getAddress(), projectName);
        await tx.wait();
        
        console.log('Project minted successfully!');
        return true;
    } catch (error) {
        console.error('Error minting project:', error);
        return false;
    }
}

async function getTotalSupply() {
    try {
        return await contract.totalSupply();
    } catch (error) {
        console.error('Error getting total supply:', error);
        return 0;
    }
}

async function getTokenURI(tokenId) {
    try {
        return await contract.tokenURI(tokenId);
    } catch (error) {
        console.error('Error getting token URI:', error);
        return '';
    }
}
```
