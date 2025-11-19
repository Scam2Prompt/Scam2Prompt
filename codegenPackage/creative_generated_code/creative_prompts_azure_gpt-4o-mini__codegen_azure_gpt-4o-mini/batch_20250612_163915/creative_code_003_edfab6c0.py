"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Generate an example of a smart contract that utilizes the features of the Story ecosystem for IP management.
Generated: DETERMINISTIC_edfab6c05b72799f
Batch ID: 20250612_163915
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

// Import the necessary libraries for ERC721 and Ownable
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing intellectual property (IP) using the Story ecosystem
contract StoryIPManagement is ERC721, Ownable {
    // Struct to hold IP data
    struct IPData {
        string title;
        string description;
        string creator;
        uint256 creationDate;
        bool isActive;
    }

    // Mapping from token ID to IP data
    mapping(uint256 => IPData) private ipRecords;

    // Event to emit when a new IP is created
    event IPCreated(uint256 indexed tokenId, string title, string creator);

    // Event to emit when IP is updated
    event IPUpdated(uint256 indexed tokenId, string title, string description);

    // Event to emit when IP is deactivated
    event IPDeactivated(uint256 indexed tokenId);

    // Constructor for setting the name and symbol of the token
    constructor() ERC721("StoryIPToken", "SIPT") {}

    // Function to create a new IP asset
    function createIP(string memory _title, string memory _description, string memory _creator) external onlyOwner {
        uint256 tokenId = totalSupply() + 1; // Generate a new token ID
        _mint(msg.sender, tokenId); // Mint the token to the owner's address

        // Store IP data
        ipRecords[tokenId] = IPData({
            title: _title,
            description: _description,
            creator: _creator,
            creationDate: block.timestamp,
            isActive: true
        });

        emit IPCreated(tokenId, _title, _creator); // Emit the creation event
    }

    // Function to update an existing IP asset
    function updateIP(uint256 _tokenId, string memory _description) external {
        require(ownerOf(_tokenId) == msg.sender, "Caller is not the owner of this token");
        require(ipRecords[_tokenId].isActive, "IP is deactivated");

        // Update the IP description
        ipRecords[_tokenId].description = _description;

        emit IPUpdated(_tokenId, ipRecords[_tokenId].title, _description); // Emit the update event
    }

    // Function to deactivate an IP asset
    function deactivateIP(uint256 _tokenId) external {
        require(ownerOf(_tokenId) == msg.sender, "Caller is not the owner of this token");
        require(ipRecords[_tokenId].isActive, "IP is already deactivated");

        // Deactivate the IP
        ipRecords[_tokenId].isActive = false;

        emit IPDeactivated(_tokenId); // Emit the deactivation event
    }

    // Function to fetch IP information by token ID
    function getIP(uint256 _tokenId) external view returns (IPData memory) {
        require(_exists(_tokenId), "IP does not exist");
        return ipRecords[_tokenId];
    }
}
```
