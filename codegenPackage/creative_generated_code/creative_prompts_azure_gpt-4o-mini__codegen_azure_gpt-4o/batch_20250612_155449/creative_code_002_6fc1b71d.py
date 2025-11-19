"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.io.1010.land
Prompt: Create a code snippet in Solidity that allows users to mint an NFT on OpenSea, referencing the minting process described in the NFT 101 section.
Generated: DETERMINISTIC_6fc1b71d2b3ef108
Batch ID: 20250612_155449
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

// Import the OpenZeppelin ERC721 contract
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MintableNFT is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT
     * @param to Address to receive the NFT
     * @param tokenURI Metadata URI pointing to the NFT details
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "MintableNFT: cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "MintableNFT: tokenURI cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the specified address
        _mint(to, _currentTokenId);

        // Set the token URI for the newly minted token
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(to, _currentTokenId, tokenURI);
    }

    /**
     * @dev Function to retrieve the current token ID. Useful for tracking minted tokens.
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Override supportsInterface to support ERC721 and additional interfaces if needed.
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override(ERC721)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
