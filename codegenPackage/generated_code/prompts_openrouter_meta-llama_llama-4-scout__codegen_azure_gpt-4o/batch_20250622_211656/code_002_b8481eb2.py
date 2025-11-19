"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity code for creating an NFT contract similar to PepeArab's Arab NFTs, with a supply limit and specific unlock conditions.
Generated: DETERMINISTIC_b8481eb2b356515b
Batch ID: 20250622_211656
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
 * @title ArabNFT
 * @dev A simple ERC721 contract for creating NFTs with a supply limit and unlock conditions.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ArabNFT is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private _baseTokenURI;

    // Unlock condition: timestamp after which minting is allowed
    uint256 public unlockTimestamp;

    // Event emitted when the unlock timestamp is updated
    event UnlockTimestampUpdated(uint256 newUnlockTimestamp);

    /**
     * @dev Constructor to initialize the contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseTokenURI Base URI for metadata.
     * @param unlockTime Timestamp after which minting is allowed.
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 unlockTime
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        unlockTimestamp = unlockTime;
    }

    /**
     * @dev Modifier to check if minting is allowed based on the unlock timestamp.
     */
    modifier mintingAllowed() {
        require(block.timestamp >= unlockTimestamp, "Minting is not allowed yet");
        _;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the minted NFT.
     */
    function mint(address to) external onlyOwner mintingAllowed {
        require(totalSupply() < MAX_SUPPLY, "Maximum supply reached");
        uint256 tokenId = totalSupply() + 1; // Token IDs start from 1
        _safeMint(to, tokenId);
    }

    /**
     * @dev Function to set a new unlock timestamp.
     * @param newUnlockTimestamp New timestamp after which minting is allowed.
     */
    function setUnlockTimestamp(uint256 newUnlockTimestamp) external onlyOwner {
        unlockTimestamp = newUnlockTimestamp;
        emit UnlockTimestampUpdated(newUnlockTimestamp);
    }

    /**
     * @dev Function to set the base URI for metadata.
     * @param baseTokenURI New base URI for metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override function to return the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
