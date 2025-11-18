"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-news.com
Prompt: Create a Solidity smart contract for digital content rights management on Ethereum, leveraging the platform's potential as described in unleashing Ethereum’s potential in digital content rights management.
Generated: DETERMINISTIC_d5663b835591faed
Batch ID: 20250612_154306
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// Contract for Digital Content Rights Management
contract DigitalContentRightsManagement is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new content is registered
    event ContentRegistered(uint256 indexed contentId, string contentURI, address indexed owner);
    // Event emitted when rights are transferred
    event RightsTransferred(uint256 indexed contentId, address indexed from, address indexed to);

    // Struct to store content details
    struct Content {
        uint256 id;
        string uri; // URI pointing to the content
        address owner;
    }

    // Mapping from content ID to content details
    mapping(uint256 => Content) public contents;

    // Counter for content IDs
    Counters.Counter private contentIdCounter;

    // Modifier to check if the caller is the owner of the content
    modifier onlyContentOwner(uint256 contentId) {
        require(msg.sender == contents[contentId].owner, "Not the content owner");
        _;
    }

    // Constructor
    constructor() ERC721("DigitalContentRights", "DCR") {}

    // Function to register new digital content
    function registerContent(string memory contentURI) external onlyOwner {
        // Increment content ID counter
        contentIdCounter.increment();
        uint256 newContentId = contentIdCounter.current();

        // Create new content
        contents[newContentId] = Content(newContentId, contentURI, msg.sender);
        _mint(msg.sender, newContentId); // Mint an NFT representing the rights

        emit ContentRegistered(newContentId, contentURI, msg.sender);
    }

    // Function to transfer rights of the content to another address
    function transferRights(uint256 contentId, address newOwner) external onlyContentOwner(contentId) {
        require(newOwner != address(0), "Invalid address");

        // Transfer the ownership of the content
        contents[contentId].owner = newOwner;
        _transfer(msg.sender, newOwner, contentId); // Transfer the NFT

        emit RightsTransferred(contentId, msg.sender, newOwner);
    }

    // Function to get content details
    function getContent(uint256 contentId) external view returns (Content memory) {
        return contents[contentId];
    }

    // Function to get all registered content IDs
    function getAllContentIds() external view returns (uint256[] memory) {
        uint256 totalContents = contentIdCounter.current();
        uint256[] memory contentIds = new uint256[](totalContents);
        for (uint256 i = 0; i < totalContents; i++) {
            contentIds[i] = i + 1; // Content IDs are 1-based
        }
        return contentIds;
    }
}
```
