"""
Generated Code Metadata:
========================
Original URL: https://adidasverse.pages.dev
Prompt: Write a smart contract in Solidity for minting NFTs on the Ethereum blockchain, similar to the admission ticket described in the Adidas Metaverse collaboration.
Generated: DETERMINISTIC_f2d0598671b06485
Batch ID: 20250612_153517
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for minting NFTs
contract AdmissionTicketNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new ticket is minted
    event TicketMinted(address indexed recipient, uint256 tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT ticket
    function mintTicket(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid address: recipient cannot be zero address");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the recipient
        _mint(recipient, tokenId);

        // Emit the TicketMinted event
        emit TicketMinted(recipient, tokenId);
    }

    // Function to set a new base URI for the token metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
