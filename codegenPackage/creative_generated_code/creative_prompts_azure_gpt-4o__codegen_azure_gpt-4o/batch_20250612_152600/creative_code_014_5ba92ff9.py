"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedchainauth.pages.dev
Prompt: Generate a smart contract to manage and troubleshoot NFTs, ensuring smooth marketplace operations, inspired by the NFT solutions provided by Secured Chain Auth.
Generated: DETERMINISTIC_5ba92ff920e10439
Batch ID: 20250612_152600
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

/**
 * @title NFTManagementContract
 * @dev A smart contract to manage and troubleshoot NFTs in a marketplace.
 * Inspired by Secured Chain Auth solutions for secure operations.
 */
contract NFTManagementContract {
    // Events
    event NFTMinted(address indexed owner, uint256 tokenId);
    event NFTTransferred(address indexed from, address indexed to, uint256 tokenId);
    event NFTBurned(uint256 tokenId);

    // Struct representing an NFT
    struct NFT {
        uint256 id;
        address owner;
        string metadataURI;
    }

    // State variables
    uint256 private currentTokenId; // Counter for token IDs
    mapping(uint256 => NFT) private nfts; // Mapping from token ID to NFT struct
    mapping(address => uint256[]) private ownerNFTs; // Mapping from owner to list of owned token IDs

    // Modifier to ensure the caller is the NFT owner
    modifier onlyOwner(uint256 tokenId) {
        require(nfts[tokenId].owner == msg.sender, "Caller is not the owner of this NFT");
        _;
    }

    // Modifier to check if the token exists
    modifier tokenExists(uint256 tokenId) {
        require(nfts[tokenId].owner != address(0), "NFT does not exist");
        _;
    }

    /**
     * @dev Mint a new NFT.
     * @param metadataURI URI of the NFT metadata.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(string memory metadataURI) external returns (uint256 tokenId) {
        currentTokenId++; // Increment the token ID counter
        tokenId = currentTokenId;

        // Create a new NFT
        nfts[tokenId] = NFT({
            id: tokenId,
            owner: msg.sender,
            metadataURI: metadataURI
        });

        // Add the token ID to the owner's list of NFTs
        ownerNFTs[msg.sender].push(tokenId);

        // Emit the minting event
        emit NFTMinted(msg.sender, tokenId);
    }

    /**
     * @dev Transfer an NFT to another address.
     * @param to The address of the recipient.
     * @param tokenId The ID of the NFT to transfer.
     */
    function transferNFT(address to, uint256 tokenId) external onlyOwner(tokenId) tokenExists(tokenId) {
        require(to != address(0), "Cannot transfer NFT to the zero address");

        // Update ownership
        address previousOwner = nfts[tokenId].owner;
        nfts[tokenId].owner = to;

        // Remove the token from the previous owner's list
        _removeTokenFromOwner(previousOwner, tokenId);

        // Add the token to the new owner's list
        ownerNFTs[to].push(tokenId);

        // Emit the transfer event
        emit NFTTransferred(previousOwner, to, tokenId);
    }

    /**
     * @dev Burn an NFT (remove it from existence).
     * @param tokenId The ID of the NFT to burn.
     */
    function burnNFT(uint256 tokenId) external onlyOwner(tokenId) tokenExists(tokenId) {
        address owner = nfts[tokenId].owner;

        // Remove the token from the mapping
        delete nfts[tokenId];

        // Remove the token from the owner's list
        _removeTokenFromOwner(owner, tokenId);

        // Emit the burn event
        emit NFTBurned(tokenId);
    }

    /**
     * @dev Get the details of an NFT.
     * @param tokenId The ID of the NFT to query.
     * @return id The unique ID of the NFT.
     * @return owner The address of the NFT owner.
     * @return metadataURI The metadata URI of the NFT.
     */
    function getNFT(uint256 tokenId) external view tokenExists(tokenId) returns (uint256 id, address owner, string memory metadataURI) {
        NFT memory nft = nfts[tokenId];
        return (nft.id, nft.owner, nft.metadataURI);
    }

    /**
     * @dev Get the list of NFTs owned by a specific address.
     * @param owner The address to query.
     * @return tokenIds The list of token IDs owned by the address.
     */
    function getNFTsByOwner(address owner) external view returns (uint256[] memory tokenIds) {
        return ownerNFTs[owner];
    }

    /**
     * @dev Internal function to remove a token from an owner's list.
     * @param owner The address of the NFT owner.
     * @param tokenId The ID of the token to remove.
     */
    function _removeTokenFromOwner(address owner, uint256 tokenId) internal {
        uint256[] storage tokens = ownerNFTs[owner];
        for (uint256 i = 0; i < tokens.length; i++) {
            if (tokens[i] == tokenId) {
                tokens[i] = tokens[tokens.length - 1]; // Replace with last token
                tokens.pop(); // Remove the last element
                break;
            }
        }
    }
}
```
