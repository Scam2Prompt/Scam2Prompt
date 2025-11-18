"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-9dc.pages.dev
Prompt: Write a smart contract in Solidity that facilitates the minting of Pepe 2.0 NFTs, including functionality for users to claim free tokens as described on the Pepe 2.0 website.
Generated: DETERMINISTIC_6fb47c30f7aebeaf
Batch ID: 20250612_151605
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
 * @title Pepe2NFT
 * @dev A smart contract that facilitates minting of Pepe 2.0 NFTs, including free claim functionality.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Pepe2NFT is ERC721Enumerable, Ownable {
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of tokens
    uint256 public constant CLAIM_LIMIT = 1; // Free claim limit per wallet
    uint256 public tokenPrice = 0.05 ether; // Price per NFT for minting
    uint256 public nextTokenId = 1; // Tracks the next token ID to be minted

    mapping(address => uint256) public claimedTokens; // Tracks free claims per wallet

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
     */
    constructor() ERC721("Pepe2NFT", "PEPE2") {}

    /**
     * @dev Allows users to claim a free NFT if they haven't claimed already.
     * @notice Users can only claim one free NFT per wallet.
     */
    function claimFreeNFT() external {
        require(claimedTokens[msg.sender] < CLAIM_LIMIT, "Already claimed free NFT");
        require(nextTokenId <= MAX_SUPPLY, "Max supply reached");

        claimedTokens[msg.sender] += 1;
        _safeMint(msg.sender, nextTokenId);
        nextTokenId++;
    }

    /**
     * @dev Allows users to mint NFTs by paying the token price.
     * @param quantity Number of NFTs the user wants to mint.
     */
    function mintNFT(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than zero");
        require(nextTokenId + quantity - 1 <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value == tokenPrice * quantity, "Incorrect Ether sent");

        for (uint256 i = 0; i < quantity; i++) {
            _safeMint(msg.sender, nextTokenId);
            nextTokenId++;
        }
    }

    /**
     * @dev Allows the owner to set a new token price.
     * @param newPrice The new price per NFT in wei.
     */
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        tokenPrice = newPrice;
    }

    /**
     * @dev Allows the owner to withdraw the contract's balance.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
