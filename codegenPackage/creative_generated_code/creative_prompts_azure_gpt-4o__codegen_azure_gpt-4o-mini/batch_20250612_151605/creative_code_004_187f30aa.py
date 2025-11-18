"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmpeppe.web.app
Prompt: Write code to mint Player Card NFTs inspired by legendary soccer players and Pepe artwork, ensuring a maximum supply of 420 NFTs.
Generated: DETERMINISTIC_187f30aaefb3ca41
Batch ID: 20250612_151605
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

// Import OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to mint Player Card NFTs
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 420;
    
    // Base URI for metadata
    string private baseURI;

    // Mapping from token ID to a boolean indicating if it's minted
    mapping(uint256 => bool) private minted;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    // Constructor to initialize the NFT with a name and symbol
    constructor(string memory _name, string memory _symbol, string memory _baseURI) 
        ERC721(_name, _symbol) 
    {
        baseURI = _baseURI;
    }

    // Function to mint an NFT
    function mintNFT() external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = totalSupply(); // Get the next token ID
        minted[tokenId] = true; // Mark this token ID as minted

        _safeMint(msg.sender, tokenId); // Mint the NFT to the caller
        emit NFTMinted(msg.sender, tokenId); // Emit event
    }

    // Function to retrieve the base URI for metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    // Function to update the base URI (only callable by owner)
    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
