"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.fulviomenegozzo.com
Prompt: Create a smart contract in Solidity that limits NFT purchases to a maximum of 5 per wallet and includes functionality for setting a total price in ETH, based on the features of the Memeland pre-sale.
Generated: DETERMINISTIC_72f691b0efb09ad1
Batch ID: 20250612_151624
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
 * @title MemelandNFT
 * @dev A smart contract that allows the purchase of NFTs with a limit of 5 NFTs per wallet during the pre-sale.
 */
contract MemelandNFT is ERC721Enumerable, Ownable {
    // State variables
    uint256 public constant MAX_NFTS_PER_WALLET = 5; // Maximum NFTs allowed per wallet
    uint256 public totalPrice; // Total price for one NFT in wei
    mapping(address => uint256) public walletMintCount; // Track number of NFTs purchased per wallet
    bool public saleActive; // Status of the sale

    // Events
    event SaleStatusChanged(bool active);
    event NFTMinted(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param _totalPrice Initial price for the NFT in ETH.
     */
    constructor(uint256 _totalPrice) ERC721("MemelandNFT", "MLND") {
        totalPrice = _totalPrice * 1 ether; // Set price in wei
        saleActive = false; // Sale is inactive initially
    }

    /**
     * @dev Function to start or stop the sale.
     * @param _active Boolean to indicate the sale status.
     */
    function setSaleStatus(bool _active) external onlyOwner {
        saleActive = _active;
        emit SaleStatusChanged(_active);
    }

    /**
     * @dev Function to mint NFTs.
     * @param numberOfNfts Number of NFTs to mint.
     */
    function mint(uint256 numberOfNfts) external payable {
        require(saleActive, "Sale is not active");
        require(numberOfNfts > 0 && numberOfNfts <= MAX_NFTS_PER_WALLET, "Invalid number of NFTs");
        require(walletMintCount[msg.sender] + numberOfNfts <= MAX_NFTS_PER_WALLET, "Exceeds max NFTs per wallet");
        require(msg.value >= totalPrice * numberOfNfts, "Insufficient ETH sent");

        walletMintCount[msg.sender] += numberOfNfts;

        // Mint the NFTs
        for (uint256 i = 0; i < numberOfNfts; i++) {
            _mint(msg.sender, totalSupply() + 1); // Mint a new NFT
        }

        emit NFTMinted(msg.sender, numberOfNfts);
    }

    /**
     * @dev Function to withdraw funds from the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to set a new price for the NFT.
     * @param newPrice New price in ETH.
     */
    function setPrice(uint256 newPrice) external onlyOwner {
        totalPrice = newPrice * 1 ether; // Update price in wei
    }

    /**
     * @dev Function to get the current price of the NFT.
     * @return Current price in wei.
     */
    function getCurrentPrice() external view returns (uint256) {
        return totalPrice;
    }
}
```
