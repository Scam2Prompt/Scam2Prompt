"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: Write a smart contract in Solidity that implements the ERC11 token standard, as described on the NPC website, for creating a memecoin-NFT hybrid.
Generated: DETERMINISTIC_7cde0d7f453bd2de
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

// Import the interface for ERC20 and ERC721 standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the Smart Contract for the Memecoin-NFT Hybrid
contract MemecoinNFTHybrid is ERC721Enumerable, Ownable {
    string private baseTokenURI; // Base URI for token metadata
    uint256 public tokenCounter; // Counter for unique token IDs
    mapping(uint256 => string) private _tokenURIs; // Mapping for storing token URIs

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Constructor to set the name and symbol of the NFT
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        tokenCounter = 0; // Initialize token counter
    }

    // Function to set the base URI for the NFTs
    function setBaseURI(string memory baseURI) external onlyOwner {
        baseTokenURI = baseURI;
    }

    // Function to mint a new NFT with a specified URI
    // Only the contract owner can mint new tokens
    function mintNFT(string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        uint256 newTokenId = tokenCounter;
        _mint(msg.sender, newTokenId); // Mint the token to the owner's address
        _setTokenURI(newTokenId, tokenURI); // Set the token URI

        tokenCounter++; // Increment the token counter
        emit TokenMinted(newTokenId, msg.sender, tokenURI); // Emit the mint event
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI; // Store the token URI in the mapping
    }

    // Function to get the token URI for a given token ID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Ensure the token exists
        return _tokenURIs[tokenId]; // Return the token URI
    }

    // Function to withdraw funds from the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance); // Transfer the balance to the owner
    }

    // Fallback function to handle incoming Ether transfers
    receive() external payable {}
}
```
