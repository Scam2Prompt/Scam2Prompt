"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oddfellowsnft.com
Prompt: Write a code snippet to mint an NFT that represents membership in the Secret Society of Odd Fellows.
Generated: DETERMINISTIC_44dbd80c463d7393
Batch ID: 20250612_160625
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

// Import OpenZeppelin's ERC721 library
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the NFT representing membership in the Secret Society of Odd Fellows
contract SecretSocietyMembership is ERC721Enumerable, Ownable {
    // Event to emit when a new NFT is minted
    event MembershipMinted(address indexed member, uint256 tokenId);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping to check if an address already has a membership
    mapping(address => bool) private _hasMembership;

    // Base URI for the NFT metadata
    string private _baseTokenURI;

    // Constructor to set the name and symbol of the NFT
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT for membership
    function mintMembership() external {
        require(!_hasMembership[msg.sender], "Already a member");
        
        // Increment the token ID counter and assign it to the new member
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the NFT to the sender
        _mint(msg.sender, newTokenId);

        // Mark the address as having membership
        _hasMembership[msg.sender] = true;

        // Emit the membership mint event
        emit MembershipMinted(msg.sender, newTokenId);
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base token URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to check if an address has a membership
    function hasMembership(address member) external view returns (bool) {
        return _hasMembership[member];
    }
}
```
