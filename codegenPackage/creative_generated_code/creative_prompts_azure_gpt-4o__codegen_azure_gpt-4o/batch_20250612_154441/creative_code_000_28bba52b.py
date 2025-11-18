"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract in Solidity that integrates a minting platform for NFTs, similar to the MintStone and Relic minting system described on Clone Force™.
Generated: DETERMINISTIC_28bba52bdab6d5b6
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title NFTMintingPlatform
 * @dev A smart contract for minting NFTs with customizable features.
 *      Supports owner-controlled minting and integrated metadata storage.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingPlatform is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Minting fee (in wei)
    uint256 public mintingFee;

    // Events
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor to initialize the contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol for the NFT collection.
     * @param initialMintingFee The initial fee for minting an NFT.
     */
    constructor(string memory name, string memory symbol, uint256 initialMintingFee) ERC721(name, symbol) {
        require(initialMintingFee >= 0, "Minting fee must be non-negative");
        mintingFee = initialMintingFee;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address that will own the minted NFT.
     * @param tokenURI The metadata URI for the NFT.
     * Requirements:
     * - Caller must send enough ETH to cover the minting fee.
     */
    function mintNFT(address to, string memory tokenURI) external payable {
        require(msg.value >= mintingFee, "Insufficient ETH sent for minting");

        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(to, _currentTokenId, tokenURI);
    }

    /**
     * @dev Allows the owner to set a new minting fee.
     * @param newFee The new minting fee in wei.
     * Requirements:
     * - Only the contract owner can call this function.
     */
    function setMintingFee(uint256 newFee) external onlyOwner {
        require(newFee >= 0, "Minting fee must be non-negative");
        mintingFee = newFee;
    }

    /**
     * @dev Allows the owner to withdraw the accumulated funds.
     * Requirements:
     * - Only the contract owner can call this function.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Returns the current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
