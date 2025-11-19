"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blvckparis-nft.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to mint Blvck Genesis NFTs with a price of 0.05 ETH, including a fee structure.
Generated: DETERMINISTIC_7b3efb2da81e6182
Batch ID: 20250612_135717
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
 * @title BlvckGenesisNFT
 * @dev A smart contract for minting Blvck Genesis NFTs with a fee structure.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BlvckGenesisNFT is ERC721Enumerable, Ownable {
    // Price of each NFT
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Address to collect minting fees
    address payable public feeAddress;

    // Current token ID tracker
    uint256 private _currentTokenId;

    /**
     * @dev Constructor to initialize the contract with relevant parameters.
     * @param name Name of the NFT collection.
     * @param symbol Symbol for the NFT collection.
     * @param _feeAddress Address to collect minting fees.
     */
    constructor(
        string memory name,
        string memory symbol,
        address payable _feeAddress
    ) ERC721(name, symbol) {
        require(_feeAddress != address(0), "Fee address cannot be zero");
        feeAddress = _feeAddress;
    }

    /**
     * @dev Mint a new Blvck Genesis NFT.
     */
    function mint() external payable {
        // Ensure the correct mint price is paid
        require(msg.value == MINT_PRICE, "Incorrect ETH amount sent");

        // Ensure the maximum supply has not been reached
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        // Increment the token ID tracker
        _currentTokenId++;

        // Mint the NFT to the sender's address
        _safeMint(msg.sender, _currentTokenId);

        // Forward the minting fee to the fee address
        (bool success, ) = feeAddress.call{value: msg.value}("");
        require(success, "Fee transfer failed");
    }

    /**
     * @dev Update the fee address. Only the owner can call this.
     * @param _feeAddress New fee address.
     */
    function updateFeeAddress(address payable _feeAddress) external onlyOwner {
        require(_feeAddress != address(0), "Fee address cannot be zero");
        feeAddress = _feeAddress;
    }

    /**
     * @dev Withdraw any funds accidentally sent to the contract. Only the owner can call this.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdraw failed");
    }
}
```
