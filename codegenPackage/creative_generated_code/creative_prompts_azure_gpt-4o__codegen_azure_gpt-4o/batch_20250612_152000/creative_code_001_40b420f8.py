"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Generate Solidity code for deploying a smart contract on Metis Layer 2 that integrates decentralized storage and supports low gas fees.
Generated: DETERMINISTIC_40b420f8dd28dfbf
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Importing OpenZeppelin's Ownable and ERC721 for basic token functionalities.
// These can be replaced with other standards or custom implementations as needed.
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// Interface for interacting with a decentralized storage (e.g., IPFS, Filecoin, or any other service).
interface IDecentralizedStorage {
    function uploadFile(string calldata fileHash) external returns (bool);
    function retrieveFile(string calldata fileHash) external view returns (string memory);
}

// This contract integrates ERC721 functionality with decentralized storage
// and is optimized for low gas fees on Metis Layer 2.
contract DecentralizedStorageNFT is ERC721, Ownable {
    // Event emitted when a file is stored on decentralized storage.
    event FileStored(address indexed sender, string fileHash, uint256 tokenId);

    // Address of the decentralized storage contract.
    IDecentralizedStorage public storageService;

    // Mapping of token IDs to their associated file hashes (stored off-chain).
    mapping(uint256 => string) private tokenFileHashes;

    // Counter for generating unique token IDs.
    uint256 private _tokenIdCounter;

    // Constructor to initialize token name, symbol, and decentralized storage contract.
    constructor(address _storageServiceAddress) ERC721("DecentralizedStorageNFT", "DSNFT") {
        require(_storageServiceAddress != address(0), "Storage service address cannot be zero.");
        storageService = IDecentralizedStorage(_storageServiceAddress);
    }

    // Function to mint a new NFT and store its associated file hash in decentralized storage.
    function mintNFT(string calldata fileHash) external {
        require(bytes(fileHash).length > 0, "File hash cannot be empty.");

        // Increment the token ID counter.
        uint256 newTokenId = ++_tokenIdCounter;

        // Store the file hash in the mapping and upload it to the decentralized storage.
        tokenFileHashes[newTokenId] = fileHash;
        bool success = storageService.uploadFile(fileHash);
        require(success, "Failed to upload file to decentralized storage.");

        // Mint the NFT to the sender.
        _safeMint(msg.sender, newTokenId);

        emit FileStored(msg.sender, fileHash, newTokenId);
    }

    // Function to retrieve the file hash associated with a token ID.
    function getFileHash(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token ID does not exist.");
        return tokenFileHashes[tokenId];
    }

    // Function to update the decentralized storage service (only owner).
    function updateStorageService(address newStorageService) external onlyOwner {
        require(newStorageService != address(0), "New storage service address cannot be zero.");
        storageService = IDecentralizedStorage(newStorageService);
    }
}
```

Make sure to deploy the `IDecentralizedStorage` contract (or integrate with an existing one) before deploying this smart contract.
