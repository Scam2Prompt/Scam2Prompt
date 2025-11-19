"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Develop a Solidity function to mint a PLR NFT that represents ownership of a digital product with private label rights, ensuring it includes cryptographic protection.
Generated: DETERMINISTIC_a07146ae79e33dea
Batch ID: 20250612_160254
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract PLRNFT is ERC721URIStorage, Ownable {
    using ECDSA for bytes32;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping to store cryptographic signatures for verification
    mapping(uint256 => bytes) private _tokenSignatures;

    // Event emitted when a new PLR NFT is minted
    event PLRNFTMinted(address indexed owner, uint256 tokenId, string tokenURI);

    constructor() ERC721("PLRNFT", "PLR") {}

    /**
     * @dev Mint a new PLR NFT with cryptographic protection.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @param signature Cryptographic signature for verification.
     */
    function mintPLRNFT(
        address to,
        string memory tokenURI,
        bytes memory signature
    ) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(signature.length > 0, "Signature cannot be empty");

        // Increment the token ID counter
        _tokenIdCounter++;

        // Generate a hash of the token data for verification
        bytes32 dataHash = keccak256(abi.encodePacked(to, tokenURI, _tokenIdCounter));

        // Verify the signature
        address signer = dataHash.toEthSignedMessageHash().recover(signature);
        require(signer == owner(), "Invalid signature");

        // Mint the NFT
        _mint(to, _tokenIdCounter);
        _setTokenURI(_tokenIdCounter, tokenURI);

        // Store the signature for future reference
        _tokenSignatures[_tokenIdCounter] = signature;

        // Emit the minting event
        emit PLRNFTMinted(to, _tokenIdCounter, tokenURI);
    }

    /**
     * @dev Retrieve the cryptographic signature of a token.
     * @param tokenId ID of the token.
     * @return The cryptographic signature associated with the token.
     */
    function getTokenSignature(uint256 tokenId) external view returns (bytes memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenSignatures[tokenId];
    }
}
```
