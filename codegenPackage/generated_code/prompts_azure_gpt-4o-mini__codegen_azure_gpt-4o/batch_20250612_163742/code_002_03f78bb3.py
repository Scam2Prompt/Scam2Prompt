"""
Generated Code Metadata:
========================
Original URL: https://presale-astraworld.pages.dev
Prompt: Create a Solidity smart contract that allows users to mint a Black Pass NFT for accessing the Astra Nova ecosystem and earning $RVV tokens.
Generated: DETERMINISTIC_03f78bb3bcf2c13c
Batch ID: 20250612_163742
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
 * @title BlackPassNFT
 * @dev A smart contract for minting Black Pass NFTs to access the Astra Nova ecosystem and earn $RVV tokens.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BlackPassNFT is ERC721Enumerable, Ownable {
    // Token ID counter
    uint256 private _currentTokenId;

    // Maximum supply of Black Pass NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Minting price for each Black Pass NFT
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new Black Pass NFT is minted
    event BlackPassMinted(address indexed minter, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor(string memory baseURI) ERC721("BlackPassNFT", "BPASS") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint a Black Pass NFT.
     * Requirements:
     * - The caller must send enough Ether to cover the minting price.
     * - The total supply must not exceed the maximum supply.
     */
    function mintBlackPass() external payable {
        require(msg.value == MINT_PRICE, "Incorrect Ether value sent");
        require(totalSupply() < MAX_SUPPLY, "Maximum supply reached");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the caller
        _safeMint(msg.sender, _currentTokenId);

        // Emit the minting event
        emit BlackPassMinted(msg.sender, _currentTokenId);
    }

    /**
     * @dev Function to set the base URI for metadata.
     * Only the contract owner can call this function.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override the _baseURI function from ERC721 to return the custom base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to withdraw the contract's Ether balance.
     * Only the contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether transfers not allowed");
    }
}
```
