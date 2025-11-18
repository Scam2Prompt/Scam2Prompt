"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monkeypagelab.com
Prompt: Develop a smart contract that supports the minting of NFTs containing webpage data, compatible with the Monkey Page Lab platform.
Generated: DETERMINISTIC_b4d85ce192cec640
Batch ID: 20250612_151659
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
 * @title MonkeyPageNFT
 * @dev A smart contract for minting NFTs containing webpage data.
 * Compatible with the Monkey Page Lab platform.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MonkeyPageNFT is ERC721URIStorage, Ownable {
    // Counter for tracking token IDs
    uint256 private _currentTokenId;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId, string tokenURI);

    /**
     * @dev Constructor initializes the contract with a name and symbol.
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param recipient Address to receive the NFT.
     * @param tokenURI URI pointing to the webpage data or metadata.
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the recipient
        _safeMint(recipient, _currentTokenId);

        // Set the token URI containing webpage data
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(recipient, _currentTokenId, tokenURI);
    }

    /**
     * @dev Function to retrieve the current token ID.
     * @return The current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Function to withdraw contract balance (if applicable).
     * @param recipient Address to receive the withdrawn funds.
     */
    function withdrawBalance(address payable recipient) external onlyOwner {
        require(address(this).balance > 0, "No balance to withdraw");
        recipient.transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
