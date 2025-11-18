"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synchronizedwallet.pages.dev
Prompt: Implement a solution for minting and transferring NFTs, referencing the "NFTs minting/transfer" functionality described in the Decentralized Dapps documentation.
Generated: DETERMINISTIC_502da43be06c2782
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, well-documented, production-ready implementation in Solidity for an ERC-721 NFT contract. This contract allows minting and transferring NFTs.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC721 implementation, which is a standard for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NFTMintingTransfer
/// @dev A contract for minting and transferring NFTs, following the ERC-721 standard.
contract NFTMintingTransfer is ERC721, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Mapping to store metadata URIs for tokens
    mapping(uint256 => string) private _tokenURIs;

    /// @notice Constructor for the NFT contract
    /// @param name - Name of the NFT collection
    /// @param symbol - Symbol for the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new NFT
    /// @dev Only the contract owner can mint an NFT
    /// @param to - Address to receive the NFT
    /// @param tokenURI - Metadata URI for the NFT
    /// @return tokenId - ID of the newly minted NFT
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Set the metadata URI for the NFT
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit an event (optional)
        emit Minted(to, _currentTokenId, tokenURI);

        return _currentTokenId;
    }

    /// @notice Transfer an NFT from one address to another
    /// @dev Uses the safeTransferFrom function from the ERC721 standard
    /// @param from - Address transferring the NFT
    /// @param to - Address receiving the NFT
    /// @param tokenId - ID of the NFT to transfer
    function transferNFT(address from, address to, uint256 tokenId) external {
        // Ensure the caller is authorized to transfer the token
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Safely transfer the NFT
        _safeTransfer(from, to, tokenId, "");
    }

    /// @notice Get the metadata URI of an NFT
    /// @param tokenId - ID of the NFT
    /// @return Metadata URI of the NFT
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /// @dev Internal function to set the metadata URI for a token
    /// @param tokenId - ID of the token
    /// @param uri - Metadata URI to set
    function _setTokenURI(uint256 tokenId, string memory uri) internal {
        _tokenURIs[tokenId] = uri;
    }

    // Event emitted when an NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId, string tokenURI);
}
```

**Dependencies:**
- This code requires OpenZeppelin Contracts, which can be installed via npm:
```
npm install @openzeppelin/contracts
```

**Deployment:**
- Deploy the contract using a Solidity-compatible framework like Hardhat or Truffle, and ensure it is deployed on a blockchain network compatible with the Ethereum Virtual Machine (EVM).
