"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Generate a smart contract in Solidity for minting NFTs that represent racing dogs in the Alphadogs blockchain game.
Generated: DETERMINISTIC_f8872ecac24b65f1
Batch ID: 20250612_151403
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
 * @title AlphadogsNFT
 * @dev Smart contract for minting NFTs representing racing dogs in the Alphadogs blockchain game.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AlphadogsNFT is ERC721URIStorage, Ownable {
    // Counter to track token IDs
    uint256 private _currentTokenId;

    // Mapping to check if a racing dog ID is already minted
    mapping(uint256 => bool) private _mintedDogIds;

    // Event emitted when a new NFT is minted
    event DogMinted(address indexed owner, uint256 tokenId, string tokenURI);

    /**
     * @dev Constructor for the AlphadogsNFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new racing dog NFT.
     * @param to Address of the recipient.
     * @param dogId Unique ID representing the racing dog.
     * @param tokenURI URI containing metadata for the NFT.
     */
    function mintRacingDog(
        address to,
        uint256 dogId,
        string memory tokenURI
    ) external onlyOwner {
        require(!_mintedDogIds[dogId], "Dog ID has already been minted");
        require(to != address(0), "Invalid recipient address");

        // Increment token ID counter
        _currentTokenId += 1;

        // Mint the NFT with the new token ID
        _safeMint(to, _currentTokenId);

        // Set the token URI for the minted NFT
        _setTokenURI(_currentTokenId, tokenURI);

        // Mark the dog ID as minted
        _mintedDogIds[dogId] = true;

        // Emit event for minting
        emit DogMinted(to, _currentTokenId, tokenURI);
    }

    /**
     * @dev Returns the total number of tokens minted so far.
     */
    function totalMinted() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Check if a racing dog ID has been minted.
     * @param dogId Unique ID representing the racing dog.
     * @return True if the dog ID has been minted, false otherwise.
     */
    function isDogMinted(uint256 dogId) external view returns (bool) {
        return _mintedDogIds[dogId];
    }
}
```
