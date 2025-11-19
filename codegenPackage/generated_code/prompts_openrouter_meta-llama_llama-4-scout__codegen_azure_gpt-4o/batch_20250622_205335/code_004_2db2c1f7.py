"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Design a simple smart contract for a digital being project like Zero Beings, incorporating OpenSea's verified contract standards.
Generated: DETERMINISTIC_2db2c1f7eb5bb852
Batch ID: 20250622_205335
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

// Importing OpenZeppelin libraries for ERC721 and Ownable standards
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a digital being project
contract DigitalBeings is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new token is minted
    event DigitalBeingCreated(uint256 indexed tokenId, address indexed owner, string tokenURI);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new digital being.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the token.
     */
    function mintDigitalBeing(address to, string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the token to the specified address
        _safeMint(to, _currentTokenId);

        // Set the token URI for the minted token
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the event for the new token creation
        emit DigitalBeingCreated(_currentTokenId, to, tokenURI);
    }

    /**
     * @dev Override the base URI function to return the custom base URI.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @param baseTokenURI New base URI string.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to retrieve the current token ID counter.
     * @return Current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Function to withdraw contract balance (if any) to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether (if needed for future use cases).
     */
    receive() external payable {}
}
```
