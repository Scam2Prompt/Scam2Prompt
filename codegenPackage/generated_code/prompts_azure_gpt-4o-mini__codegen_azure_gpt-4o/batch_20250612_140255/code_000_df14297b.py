"""
Generated Code Metadata:
========================
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Generate code to create a smart contract for an NFT collection, ensuring it includes features to prevent intellectual property rights infringement.
Generated: DETERMINISTIC_df14297b22666c66
Batch ID: 20250612_140255
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
 * @title NFTCollection
 * @dev A smart contract for creating an NFT collection with intellectual property rights protection.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollection is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Mapping to store intellectual property rights (IPR) agreements
    mapping(uint256 => string) private _iprAgreements;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, address owner, string tokenURI, string iprAgreement);

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with intellectual property rights agreement.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @param iprAgreement Intellectual property rights agreement (e.g., license terms).
     */
    function mintNFT(
        address to,
        string memory tokenURI,
        string memory iprAgreement
    ) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(bytes(iprAgreement).length > 0, "IPR agreement cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Store the intellectual property rights agreement
        _iprAgreements[_currentTokenId] = iprAgreement;

        // Emit the NFTMinted event
        emit NFTMinted(_currentTokenId, to, tokenURI, iprAgreement);
    }

    /**
     * @dev Get the intellectual property rights agreement for a specific token ID.
     * @param tokenId ID of the token.
     * @return The intellectual property rights agreement.
     */
    function getIPRAgreement(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _iprAgreements[tokenId];
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to prevent transfers if necessary.
     * This can be extended to enforce specific rules related to intellectual property rights.
     * @param from Address transferring the token.
     * @param to Address receiving the token.
     * @param tokenId ID of the token being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Add custom logic here if needed to enforce IPR rules
    }
}
```
