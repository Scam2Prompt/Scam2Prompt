"""
Generated Code Metadata:
========================
Original URL: https://reg-bemorebasedxyz.pages.dev
Prompt: Generate a smart contract for minting tokens on the BASE chain using Transient innovations, with a pricing structure of 0.0042069 ETH or free.
Generated: DETERMINISTIC_e2d56fbc9f41a2de
Batch ID: 20250622_211011
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

// Importing OpenZeppelin's ERC721 implementation for token standards
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for minting tokens on the BASE chain
contract TokenMinting is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public constant MINT_PRICE = 0.0042069 ether; // Price for minting a token
    mapping(address => bool) public hasMinted; // Track if an address has minted a token

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 tokenId);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC721("TransientToken", "TTK") {}

    // Function to mint a new token
    function mintToken() external payable {
        // Check if the user has already minted a token
        require(!hasMinted[msg.sender], "You have already minted a token.");

        // Check if the payment is correct or if the minting is free
        require(msg.value == MINT_PRICE || msg.value == 0, "Incorrect payment amount.");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the token to the sender's address
        _mint(msg.sender, tokenId);
        hasMinted[msg.sender] = true; // Mark the sender as having minted

        // Emit the token minted event
        emit TokenMinted(msg.sender, tokenId);
    }

    // Function to withdraw the contract's balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get the contract's balance
        require(balance > 0, "No funds to withdraw."); // Ensure there are funds to withdraw

        // Transfer the balance to the owner's address
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed."); // Ensure the transfer was successful
    }

    // Function to receive Ether. This is necessary to accept payments.
    receive() external payable {}
}
```
