"""
Generated Code Metadata:
========================
Original URL: https://abc-abracadabra.web.app
Prompt: Explain how to implement a "0% royalties" policy in an NFT smart contract, referencing the ABC - Abracadabra project as an example.
Generated: DETERMINISTIC_98cea4028e7fbebd
Batch ID: 20250612_151415
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

// Importing OpenZeppelin's ERC721 implementation for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the NFT with a 0% royalties policy
contract ZeroRoyaltiesNFT is ERC721, Ownable {
    // Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Counter for tracking the next token ID
    uint256 private _nextTokenId;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Constructor to initialize the NFT contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _nextTokenId = 1; // Start token IDs from 1
    }

    // Function to mint a new NFT
    function mint(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _nextTokenId; // Get the current token ID
        _mint(msg.sender, tokenId); // Mint the NFT to the owner's address
        _setTokenURI(tokenId, tokenURI); // Set the token's metadata URI

        emit Minted(tokenId, msg.sender, tokenURI); // Emit the minting event
        _nextTokenId++; // Increment the token ID for the next mint
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist"); // Ensure the token exists
        _tokenURIs[tokenId] = tokenURI; // Set the token URI
    }

    // Function to retrieve the token URI for a given token ID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Ensure the token exists
        return _tokenURIs[tokenId]; // Return the token URI
    }

    // Function to withdraw any Ether from the contract (if applicable)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get the contract's balance
        require(balance > 0, "No funds to withdraw"); // Ensure there are funds to withdraw
        payable(owner()).transfer(balance); // Transfer the balance to the owner
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
