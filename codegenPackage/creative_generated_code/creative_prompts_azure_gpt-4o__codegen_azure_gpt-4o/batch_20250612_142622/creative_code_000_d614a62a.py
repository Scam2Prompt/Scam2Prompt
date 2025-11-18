"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Write a smart contract in Solidity for minting NFTs with a 10k supply, a maximum of 10 per transaction, and 50 per wallet, similar to the "Fuck OpenSea" collection's minting rules.
Generated: DETERMINISTIC_d614a62a5b1e0f84
Batch ID: 20250612_142622
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMinting is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Maximum NFTs that can be minted per transaction
    uint256 public constant MAX_PER_TX = 10;

    // Maximum NFTs that can be minted per wallet
    uint256 public constant MAX_PER_WALLET = 50;

    // Price per NFT (adjust if needed)
    uint256 public constant NFT_PRICE = 0.05 ether;

    // Base URI for metadata
    string private baseTokenURI;

    constructor(string memory _baseTokenURI) ERC721("MyNFTCollection", "MNFT") {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Mint NFTs to the sender's wallet.
     * @param _amount Number of NFTs to mint.
     */
    function mint(uint256 _amount) external payable {
        // Ensure minting does not exceed the maximum supply
        require(totalSupply() + _amount <= MAX_SUPPLY, "Minting exceeds max supply");

        // Ensure the sender does not exceed the wallet limit
        require(balanceOf(msg.sender) + _amount <= MAX_PER_WALLET, "Exceeds max NFTs per wallet");

        // Ensure the transaction does not exceed the max per transaction
        require(_amount > 0 && _amount <= MAX_PER_TX, "Invalid number of NFTs per transaction");

        // Verify sufficient payment
        require(msg.value >= NFT_PRICE * _amount, "Insufficient funds");

        // Mint NFTs to the sender
        for (uint256 i = 0; i < _amount; i++) {
            _safeMint(msg.sender, totalSupply() + 1);
        }
    }

    /**
     * @dev Set the base URI for metadata.
     * @param _baseTokenURI New base URI.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override baseURI function from ERC721.
     * @return Base URI for token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Withdraw contract balance to owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
