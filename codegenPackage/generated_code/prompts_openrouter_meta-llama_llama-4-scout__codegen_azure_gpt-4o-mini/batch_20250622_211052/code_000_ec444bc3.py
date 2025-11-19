"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Write a smart contract for a blockchain-based marketplace for software engineers that enables the creation and trading of NFTs.
Generated: DETERMINISTIC_ec444bc34c5383d9
Batch ID: 20250622_211052
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title Software Marketplace NFT Contract
// @dev This contract allows software engineers to create and trade NFTs representing their software projects.
contract SoftwareMarketplaceNFT is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to project details
    struct Project {
        string name;
        string description;
        string ipfsHash; // IPFS hash for project files
        address creator;
    }

    mapping(uint256 => Project) private _projects;

    // Event emitted when a new project NFT is created
    event ProjectCreated(uint256 indexed tokenId, string name, address indexed creator);

    // Event emitted when a project NFT is transferred
    event ProjectTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("SoftwareMarketplaceNFT", "SMNFT") {}

    // @dev Creates a new project NFT
    // @param name The name of the software project
    // @param description A brief description of the project
    // @param ipfsHash The IPFS hash of the project files
    function createProject(string memory name, string memory description, string memory ipfsHash) external {
        require(bytes(name).length > 0, "Project name cannot be empty");
        require(bytes(description).length > 0, "Project description cannot be empty");
        require(bytes(ipfsHash).length > 0, "IPFS hash cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _mint(msg.sender, tokenId);
        _projects[tokenId] = Project(name, description, ipfsHash, msg.sender);

        emit ProjectCreated(tokenId, name, msg.sender);
    }

    // @dev Retrieves project details by token ID
    // @param tokenId The ID of the token
    // @return The project details
    function getProject(uint256 tokenId) external view returns (Project memory) {
        require(_exists(tokenId), "Project does not exist");
        return _projects[tokenId];
    }

    // @dev Overrides the transfer function to emit a custom event
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);
        emit ProjectTransferred(tokenId, from, to);
    }

    // @dev Allows the owner to burn a project NFT
    // @param tokenId The ID of the token to burn
    function burnProject(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Project does not exist");
        _burn(tokenId);
        delete _projects[tokenId]; // Remove project details after burning
    }
}
```
