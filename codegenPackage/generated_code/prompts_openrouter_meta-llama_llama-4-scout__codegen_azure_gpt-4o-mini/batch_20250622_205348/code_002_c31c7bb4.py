"""
Generated Code Metadata:
========================
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Generate a smart contract in Solidity for an NFT project similar to Prime Ape Planet, including functionalities for minting, exclusive events, and charity donations.
Generated: DETERMINISTIC_c31c7bb43bcaaa8e
Batch ID: 20250622_205348
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract PrimeApePlanetNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    using Address for address payable;

    // State variables
    Counters.Counter private _tokenIdCounter;
    string private _baseTokenURI;
    uint256 public mintPrice;
    uint256 public charityPercentage; // Percentage of mint price to donate
    address payable public charityAddress;

    // Events
    event Minted(address indexed owner, uint256 indexed tokenId);
    event CharityDonation(uint256 amount, address indexed charityAddress);

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI, uint256 _mintPrice, uint256 _charityPercentage, address payable _charityAddress) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
        mintPrice = _mintPrice;
        charityPercentage = _charityPercentage;
        charityAddress = _charityAddress;
    }

    // Function to mint a new NFT
    function mint() external payable {
        require(msg.value >= mintPrice, "Insufficient funds to mint NFT");
        
        // Calculate charity donation
        uint256 charityAmount = (msg.value * charityPercentage) / 100;
        uint256 ownerAmount = msg.value - charityAmount;

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Transfer charity funds
        if (charityAmount > 0) {
            charityAddress.sendValue(charityAmount);
            emit CharityDonation(charityAmount, charityAddress);
        }

        // Transfer remaining funds to the owner
        payable(owner()).sendValue(ownerAmount);

        emit Minted(msg.sender, tokenId);
    }

    // Function to set a new base URI for the token metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw funds from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).sendValue(balance);
    }

    // Function to update charity address
    function updateCharityAddress(address payable newCharityAddress) external onlyOwner {
        require(newCharityAddress != address(0), "Invalid address");
        charityAddress = newCharityAddress;
    }

    // Function to update charity percentage
    function updateCharityPercentage(uint256 newCharityPercentage) external onlyOwner {
        require(newCharityPercentage <= 100, "Percentage must be between 0 and 100");
        charityPercentage = newCharityPercentage;
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
