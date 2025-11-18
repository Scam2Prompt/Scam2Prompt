"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Generate code for an NFT smart contract that supports composable interchain NFTs, as described in Any Inu's roadmap, ensuring compatibility with Cosmos EVM chains.
Generated: DETERMINISTIC_f631fa84a7779f86
Batch ID: 20250612_152439
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

// Importing necessary libraries for ERC-721 and EIP-2535 (Composable NFTs)
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFT contract supporting composable functionality and Cosmos EVM chains compatibility
contract ComposableInterchainNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Token ID tracker
    Counters.Counter private _tokenIdCounter;

    // Mapping to store metadata URIs for each NFT
    mapping(uint256 => string) private _tokenMetadata;

    // Event for cross-chain transfer
    event InterchainNFTTransfer(address indexed from, address indexed to, uint256 tokenId, string destinationChain);

    // Constructor initializing the contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with specified metadata URI.
     * @param to Address of the recipient.
     * @param metadataURI URI pointing to the NFT metadata.
     */
    function mint(address to, string memory metadataURI) external onlyOwner {
        // Increment token counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT
        _safeMint(to, tokenId);

        // Store the metadata URI
        _tokenMetadata[tokenId] = metadataURI;
    }

    /**
     * @dev Get the metadata URI of a token.
     * @param tokenId ID of the token.
     * @return Metadata URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721: URI query for nonexistent token");
        return _tokenMetadata[tokenId];
    }

    /**
     * @dev Transfer the NFT to another address on a different chain.
     * @param to Address of the recipient on the destination chain.
     * @param tokenId ID of the token to be transferred.
     * @param destinationChain Name of the destination chain.
     */
    function interchainTransfer(
        address to,
        uint256 tokenId,
        string memory destinationChain
    ) external {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner nor approved");

        // Emit an interchain transfer event for tracking
        emit InterchainNFTTransfer(_msgSender(), to, tokenId, destinationChain);

        // Burn the NFT locally as it will exist only on the destination chain
        _burn(tokenId);
    }

    /**
     * @dev Receive an NFT that was transferred from another chain.
     * @param to Address of the recipient on this chain.
     * @param metadataURI Metadata URI of the received NFT.
     */
    function receiveInterchainNFT(address to, string memory metadataURI) external onlyOwner {
        // Increment token counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT to the recipient on this chain
        _safeMint(to, tokenId);

        // Store the metadata URI
        _tokenMetadata[tokenId] = metadataURI;
    }

    /**
     * @dev Internal hook that ensures cleanup of token metadata on burn.
     * @param tokenId ID of the token being burned.
     */
    function _burn(uint256 tokenId) internal override {
        super._burn(tokenId);
        if (bytes(_tokenMetadata[tokenId]).length != 0) {
            delete _tokenMetadata[tokenId];
        }
    }
}
```
