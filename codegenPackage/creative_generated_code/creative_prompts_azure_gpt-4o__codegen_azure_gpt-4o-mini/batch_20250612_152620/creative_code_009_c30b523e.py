"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepewifhat.pages.dev
Prompt: Create a function in Solidity to verify if a wallet has enough BNB balance to mint a PEPE WIF HAT NFT and execute the minting process.
Generated: DETERMINISTIC_c30b523e555a9714
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PepeWifHatNFT is ERC721, Ownable {
    uint256 public constant MINT_PRICE = 0.1 ether; // Set the price for minting an NFT
    uint256 public nextTokenId;
    
    // Event to emit when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    constructor() ERC721("Pepe Wif Hat", "PEPEHAT") {}

    /**
     * @dev Function to mint a new Pepe Wif Hat NFT.
     * Requires that the sender has enough BNB to cover the minting price.
     */
    function mintNFT() external payable {
        // Check if the sender has sent enough BNB to mint
        require(msg.value >= MINT_PRICE, "Insufficient BNB to mint NFT");
        
        // Mint the NFT and assign it to the sender
        _safeMint(msg.sender, nextTokenId);
        
        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, nextTokenId);

        // Increment the token ID for the next mint
        nextTokenId++;
    }

    /**
     * @dev Function to withdraw the contract's balance to the owner.
     * Only the contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        
        // Ensure there is a balance to withdraw
        require(balance > 0, "No balance to withdraw");
        
        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed.");
    }

    /**
     * @dev Function to check the BNB balance of the sender.
     * @return bool indicating if the sender has enough BNB for minting.
     */
    function hasEnoughBalance() external view returns (bool) {
        return msg.sender.balance >= MINT_PRICE;
    }
}
```
