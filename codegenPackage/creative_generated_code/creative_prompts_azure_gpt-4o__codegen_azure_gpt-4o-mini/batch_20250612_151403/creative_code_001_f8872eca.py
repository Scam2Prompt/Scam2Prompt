"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Generate a smart contract in Solidity for minting NFTs that represent racing dogs in the Alphadogs blockchain game.
Generated: DETERMINISTIC_f8872ecac24b65f1
Batch ID: 20250612_151403
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

// Importing the ERC721 interface and the extension for metadata
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Alphadogs racing dogs NFT
contract AlphadogsNFT is ERC721URIStorage, Ownable {
    // Counter for the token IDs
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event DogMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("AlphadogsNFT", "ADOG") {
        _tokenIdCounter = 1; // Start token IDs from 1
    }

    // Function to mint a new racing dog NFT
    // @param recipient Address of the new owner of the NFT
    // @param tokenURI Metadata URI for the NFT
    function mintDog(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "Invalid address: recipient cannot be the zero address");
        require(bytes(tokenURI).length > 0, "Invalid tokenURI: it cannot be empty");

        uint256 newTokenId = _tokenIdCounter; // Get the current token ID
        _tokenIdCounter++; // Increment the token ID counter for the next mint

        // Mint the new NFT and assign it to the recipient
        _mint(recipient, newTokenId);
        
        // Set the tokenURI for the new token
        _setTokenURI(newTokenId, tokenURI);

        // Emit the DogMinted event
        emit DogMinted(recipient, newTokenId, tokenURI);
    }

    // Function to get the current token ID counter for external use
    // @return Current token ID counter
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter;
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        // Transfer balance to the owner
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("No ether accepted"); // Reject any ether sent to the contract
    }
}
```
