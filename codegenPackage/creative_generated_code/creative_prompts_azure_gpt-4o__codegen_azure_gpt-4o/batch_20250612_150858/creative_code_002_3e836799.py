"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneyglobalse.web.app
Prompt: Generate a smart contract in Solidity for minting NFTs with metadata fields for Disney, Pixar, and Star Wars™-themed digital pins.
Generated: DETERMINISTIC_3e8367995b395941
Batch ID: 20250612_150858
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
 * @title NFTMintingContract
 * @dev A smart contract for minting NFTs with metadata fields for Disney, Pixar, and Star Wars-themed digital pins.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, address indexed owner, string theme, string metadataURI);

    // Valid themes for the NFTs
    enum Theme {
        Disney,
        Pixar,
        StarWars
    }

    constructor() ERC721("DigitalPinNFT", "DPNFT") {}

    /**
     * @dev Mint a new NFT with a metadata URI and a theme.
     * @param to Address that will own the minted NFT.
     * @param metadataURI URI that points to the metadata for the NFT.
     * @param theme Theme of the NFT (Disney, Pixar, or Star Wars).
     */
    function mintNFT(address to, string memory metadataURI, Theme theme) external onlyOwner {
        require(to != address(0), "Minting to the zero address is not allowed");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Set the URI for the token's metadata
        _setTokenURI(_currentTokenId, metadataURI);

        // Emit the minting event
        emit NFTMinted(_currentTokenId, to, getThemeString(theme), metadataURI);
    }

    /**
     * @dev Get the token ID of the next NFT to be minted.
     * @return uint256 The next token ID.
     */
    function getNextTokenId() external view returns (uint256) {
        return _currentTokenId + 1;
    }

    /**
     * @dev Convert the Theme enum to a string.
     * @param theme Theme enum value.
     * @return string The string representation of the theme.
     */
    function getThemeString(Theme theme) internal pure returns (string memory) {
        if (theme == Theme.Disney) {
            return "Disney";
        } else if (theme == Theme.Pixar) {
            return "Pixar";
        } else if (theme == Theme.StarWars) {
            return "Star Wars";
        }
        return "Unknown Theme";
    }

    /**
     * @dev Override the _beforeTokenTransfer function to add custom logic
     * (Optional for more advanced features like royalties or restrictions).
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Additional custom logic can be added here if needed
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("ETH transfers are not allowed");
    }
}
```
