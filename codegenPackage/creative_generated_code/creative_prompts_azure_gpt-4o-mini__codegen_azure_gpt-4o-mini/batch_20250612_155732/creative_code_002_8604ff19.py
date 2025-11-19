"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksyn-airdrop-4.nfts2.me
Prompt: Can you provide a code snippet for a smart contract that includes features to prevent intellectual property rights infringement in NFTs?
Generated: DETERMINISTIC_8604ff19cc217d72
Batch ID: 20250612_155732
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

// Import OpenZeppelin's ERC721 implementation for NFT standard
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Intellectual Property NFT Contract
/// @notice This contract allows minting of NFTs with intellectual property protections.
contract IntellectualPropertyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for unique token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Mapping to store the details of intellectual property
    struct IPDetails {
        string title;  // Title of the intellectual property
        string description;  // Description of the intellectual property
        address creator;  // Address of the creator
        bool isActive;  // Indicates if the IP is active
    }
    
    // Mapping from token ID to IP details
    mapping(uint256 => IPDetails) private _ipDetails;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string title, address indexed creator);

    // Error definitions
    error IPNotActive();
    error NotTokenOwner();
    
    /// @dev Constructor to initialize the contract with a name and symbol
    constructor() ERC721("IntellectualPropertyNFT", "IPNFT") {}

    /// @notice Mint a new NFT with intellectual property details
    /// @param title Title of the intellectual property
    /// @param description Description of the intellectual property
    function mintNFT(string memory title, string memory description) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        // Store IP details
        _ipDetails[tokenId] = IPDetails({
            title: title,
            description: description,
            creator: msg.sender,
            isActive: true
        });

        emit NFTCreated(tokenId, title, msg.sender);
        _tokenIdCounter.increment();
    }

    /// @notice Retrieve details of an NFT by its token ID
    /// @param tokenId The ID of the token to retrieve
    /// @return title The title of the intellectual property
    /// @return description The description of the intellectual property
    /// @return creator The creator's address of the intellectual property
    /// @return isActive The active status of the intellectual property
    function getIPDetails(uint256 tokenId) external view returns (string memory title, string memory description, address creator, bool isActive) {
        require(_exists(tokenId), "Token does not exist");
        
        IPDetails memory ipDetail = _ipDetails[tokenId];
        return (ipDetail.title, ipDetail.description, ipDetail.creator, ipDetail.isActive);
    }

    /// @notice Deactivate the intellectual property associated with an NFT
    /// @param tokenId The ID of the token to deactivate
    function deactivateIP(uint256 tokenId) external {
        if (msg.sender != ownerOf(tokenId)) revert NotTokenOwner();
        _ipDetails[tokenId].isActive = false;
    }

    /// @dev Override the transfer function to prevent transfer of inactive IP NFTs
    /// @param from The current owner of the token
    /// @param to The new owner of the token
    /// @param tokenId The token ID to transfer
    function _transfer(address from, address to, uint256 tokenId) internal override {
        if (!_ipDetails[tokenId].isActive) revert IPNotActive();
        super._transfer(from, to, tokenId);
    }
}
```
