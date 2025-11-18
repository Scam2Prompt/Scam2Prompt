"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: Implement a feature in a dApp that allows users to mint their custom NPC PFPs on the Base network, ensuring uniqueness and compliance with the ERC11 standard.
Generated: DETERMINISTIC_725efa2de83aa601
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready, well-documented code for implementing the requested feature. It adheres to the ERC-721 (commonly referred to as NFT standard) as ERC-11 does not exist. This implementation uses Solidity for Ethereum-compatible blockchains, including Base.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin ERC721 implementation and other utilities
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NPC PFP Minting Contract
/// @notice This contract allows users to mint unique NPC PFPs on the Base network.
/// @dev The contract ensures uniqueness and compliance with ERC721 standards.
contract NPCPFP is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Tracks token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping for storing the hash of minted metadata to ensure uniqueness
    mapping(bytes32 => bool) private _mintedMetadataHashes;

    /// @dev Emitted when a new NPC PFP is minted.
    /// @param recipient Address of the PFP recipient.
    /// @param tokenId Unique token ID of the minted PFP.
    event NPCPFPMinted(address indexed recipient, uint256 indexed tokenId);

    /// @param name The name of the NFT collection.
    /// @param symbol The symbol of the NFT collection.
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mints a new NPC PFP.
    /// @dev Ensures the metadata URI is unique.
    /// @param metadataURI A URI pointing to the metadata of the NPC PFP.
    function mintNPCPFP(string memory metadataURI) external {
        // Ensure the metadata URI hash is unique
        bytes32 metadataHash = keccak256(abi.encodePacked(metadataURI));
        require(!_mintedMetadataHashes[metadataHash], "Metadata URI must be unique");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the token and set the metadata URI
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, metadataURI);

        // Mark the hash as minted
        _mintedMetadataHashes[metadataHash] = true;

        // Emit the minting event
        emit NPCPFPMinted(msg.sender, newTokenId);
    }

    /// @notice Retrieves the total number of minted NPC PFPs.
    /// @return Total number of NPC PFPs minted.
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /// @notice Withdraws Ether from the contract (if applicable).
    /// @dev Only the owner can call this function.
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Allows the contract to receive Ether.
    receive() external payable {}

    fallback() external payable {}
}
```

### Key Points:
- **Uniqueness:** The `mintNPCPFP` method ensures no two NFTs share the same metadata URI by storing and checking a hash of the URI.
- **Security:** The contract uses `Ownable` for admin-only functionality like `withdraw`.
- **Compliance:** The contract follows ERC721 standards with extensions like `ERC721URIStorage` for metadata handling.

You can deploy this contract on Base or any Ethereum-compatible blockchain.
