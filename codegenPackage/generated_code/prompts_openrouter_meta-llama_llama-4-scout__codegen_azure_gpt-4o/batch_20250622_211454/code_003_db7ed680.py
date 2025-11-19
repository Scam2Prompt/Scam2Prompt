"""
Generated Code Metadata:
========================
Original URL: https://rewardtevara.xyz
Prompt: "Design a simple smart contract using Solidity to create and manage Soulbound NFTs on a ZK Stack powered platform like Tevara."
Generated: DETERMINISTIC_db7ed680172c44ec
Batch ID: 20250622_211454
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

/**
 * @title SoulboundNFT
 * @dev A smart contract for creating and managing Soulbound NFTs.
 * Soulbound NFTs are non-transferable and tied to a specific wallet.
 * This contract is designed to work on a ZK Stack powered platform like Tevara.
 */
contract SoulboundNFT {
    // Event emitted when a new Soulbound NFT is minted
    event SoulboundNFTMinted(address indexed recipient, uint256 tokenId);

    // Event emitted when metadata of a Soulbound NFT is updated
    event MetadataUpdated(uint256 indexed tokenId, string newMetadata);

    // Struct to represent a Soulbound NFT
    struct NFT {
        string metadata; // Metadata associated with the NFT
        bool exists;     // Flag to check if the NFT exists
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) private _nfts;

    // Mapping from wallet address to token ID
    mapping(address => uint256) private _ownerToTokenId;

    // Counter for generating unique token IDs
    uint256 private _tokenIdCounter;

    // Modifier to ensure the caller owns the NFT
    modifier onlyOwner(uint256 tokenId) {
        require(_ownerToTokenId[msg.sender] == tokenId, "Caller does not own this NFT");
        _;
    }

    /**
     * @dev Mint a new Soulbound NFT.
     * @param recipient The address of the wallet to bind the NFT to.
     * @param metadata The metadata associated with the NFT.
     */
    function mint(address recipient, string memory metadata) external {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(_ownerToTokenId[recipient] == 0, "Recipient already owns a Soulbound NFT");

        // Increment the token ID counter
        _tokenIdCounter++;

        // Create the new NFT
        _nfts[_tokenIdCounter] = NFT(metadata, true);

        // Bind the NFT to the recipient's wallet
        _ownerToTokenId[recipient] = _tokenIdCounter;

        // Emit the minting event
        emit SoulboundNFTMinted(recipient, _tokenIdCounter);
    }

    /**
     * @dev Update the metadata of a Soulbound NFT.
     * @param tokenId The ID of the NFT to update.
     * @param newMetadata The new metadata to associate with the NFT.
     */
    function updateMetadata(uint256 tokenId, string memory newMetadata) external onlyOwner(tokenId) {
        require(_nfts[tokenId].exists, "NFT does not exist");

        // Update the metadata
        _nfts[tokenId].metadata = newMetadata;

        // Emit the metadata update event
        emit MetadataUpdated(tokenId, newMetadata);
    }

    /**
     * @dev Get the details of a Soulbound NFT.
     * @param tokenId The ID of the NFT to retrieve.
     * @return metadata The metadata associated with the NFT.
     * @return owner The owner of the NFT.
     */
    function getNFTDetails(uint256 tokenId) external view returns (string memory metadata, address owner) {
        require(_nfts[tokenId].exists, "NFT does not exist");

        // Find the owner of the NFT
        address nftOwner = address(0);
        for (address addr = address(0); addr <= address(type(uint160).max); addr++) {
            if (_ownerToTokenId[addr] == tokenId) {
                nftOwner = addr;
                break;
            }
        }

        return (_nfts[tokenId].metadata, nftOwner);
    }

    /**
     * @dev Get the token ID associated with a wallet address.
     * @param wallet The wallet address to query.
     * @return tokenId The token ID associated with the wallet.
     */
    function getTokenIdByWallet(address wallet) external view returns (uint256 tokenId) {
        return _ownerToTokenId[wallet];
    }
}
```
