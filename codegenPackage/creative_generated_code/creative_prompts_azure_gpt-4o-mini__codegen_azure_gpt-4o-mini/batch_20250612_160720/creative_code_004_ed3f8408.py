"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-nakamigos.vercel.app
Prompt: Explain how to set up a limited sale for NFTs, including a maximum purchase limit of 1 set for 0.1 ETH, as outlined on the Openpen page.
Generated: DETERMINISTIC_ed3f8408f7f56109
Batch ID: 20250612_160720
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

/**
 * @title LimitedSaleNFT
 * @dev A contract for selling NFTs with limited sale conditions.
 */
contract LimitedSaleNFT is ERC721Enumerable, Ownable {
    // Address of the recipient of funds
    address payable private recipient;

    // Maximum purchase limit per address
    uint256 public constant MAX_PURCHASE_LIMIT = 1;

    // Price of each NFT
    uint256 public constant NFT_PRICE = 0.1 ether;

    // Mapping to track number of NFTs purchased by each address
    mapping(address => uint256) public purchases;

    // Counter for NFT IDs
    uint256 private nextTokenId;

    // Event to emit when an NFT is successfully purchased
    event NFTPurchased(address indexed buyer, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param _recipient Address to receive funds from sales.
     */
    constructor(address payable _recipient) ERC721("LimitedSaleNFT", "LSNFT") {
        require(_recipient != address(0), "Recipient address cannot be zero");
        recipient = _recipient;
    }

    /**
     * @dev Function to purchase an NFT.
     * Limits the purchase to 1 NFT per address and requires the correct ETH payment.
     */
    function purchaseNFT() external payable {
        require(msg.value == NFT_PRICE, "Incorrect ETH amount sent");
        require(purchases[msg.sender] < MAX_PURCHASE_LIMIT, "Purchase limit reached");

        // Update purchase count for the buyer
        purchases[msg.sender]++;

        // Mint the new NFT
        uint256 tokenId = nextTokenId;
        _safeMint(msg.sender, tokenId);
        nextTokenId++;

        // Emit event for purchase
        emit NFTPurchased(msg.sender, tokenId);

        // Transfer funds to the recipient
        recipient.transfer(msg.value);
    }

    /**
     * @dev Function to withdraw any funds accidentally sent to the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        recipient.transfer(balance);
    }

    /**
     * @dev Function to get the total number of NFTs minted.
     * @return The total number of NFTs minted.
     */
    function totalSupply() external view returns (uint256) {
        return nextTokenId;
    }
}
```
