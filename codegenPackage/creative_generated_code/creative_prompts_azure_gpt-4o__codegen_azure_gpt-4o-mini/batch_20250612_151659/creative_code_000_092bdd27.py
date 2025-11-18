"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Write a smart contract in Solidity for minting NFTs similar to the Prime Ape Planet collection, ensuring compatibility with the Ethereum blockchain and incorporating metadata for 3D models.
Generated: DETERMINISTIC_092bdd27189b3ffe
Batch ID: 20250612_151659
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

// Importing the OpenZeppelin ERC721 implementation and Ownable contract for ownership control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title PrimeApePlanetNFT
// @dev A contract for minting NFTs with metadata for 3D models
contract PrimeApePlanetNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for the metadata of the NFTs
    string private _baseTokenURI;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // @dev Function to mint a new NFT
    // @param to The address that will own the minted NFT
    // @param metadataURI The URI that points to the metadata for the NFT
    function mintNFT(address to, string memory metadataURI) external onlyOwner {
        require(to != address(0), "Recipient address cannot be zero.");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty.");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(to, tokenId);
        _tokenURIs[tokenId] = metadataURI;

        emit Minted(tokenId, to, metadataURI);
    }

    // @dev Function to get the metadata URI of a specific NFT
    // @param tokenId The ID of the NFT
    // @return The metadata URI of the specified NFT
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist.");
        return string(abi.encodePacked(_baseTokenURI, _tokenURIs[tokenId]));
    }

    // @dev Function to set a new base URI for the metadata
    // @param newBaseTokenURI The new base URI
    function setBaseTokenURI(string memory newBaseTokenURI) external onlyOwner {
        _baseTokenURI = newBaseTokenURI;
    }

    // @dev Function to withdraw Ether from the contract (if applicable)
    // @param recipient The address to receive the withdrawn Ether
    function withdraw(address payable recipient) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero.");
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw.");
        
        (bool success, ) = recipient.call{value: balance}("");
        require(success, "Transfer failed.");
    }

    // @dev Receive function to accept Ether
    receive() external payable {}
}
```
