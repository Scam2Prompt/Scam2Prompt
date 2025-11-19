"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-whitelist.web.app
Prompt: Provide an example of how to create a smart contract for minting mystery boxes that incorporates a limited mint rights feature for $BTC holders.
Generated: DETERMINISTIC_0d086c2918162e1a
Batch ID: 20250612_160940
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

// Importing OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

// Contract for minting mystery boxes
contract MysteryBox is ERC721Enumerable, Ownable {
    // State variables
    mapping(address => uint256) public mintRights; // Maps $BTC holders to their mint rights
    uint256 public constant MAX_BOXES = 1000; // Maximum number of mystery boxes
    uint256 public boxPrice; // Price of each mystery box
    string private baseURI; // Base URI for the metadata

    // Event emitted when a mystery box is minted
    event MysteryBoxMinted(address indexed recipient, uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, uint256 _boxPrice, string memory _baseURI) 
        ERC721(name, symbol) {
        boxPrice = _boxPrice;
        baseURI = _baseURI;
    }

    // Function to mint a mystery box
    function mintMysteryBox() external payable {
        require(msg.value == boxPrice, "Incorrect Ether sent");
        require(totalSupply() < MAX_BOXES, "Maximum boxes minted");
        require(mintRights[msg.sender] > 0, "No mint rights");

        // Decrease mint rights for the caller
        mintRights[msg.sender]--;

        // Mint the mystery box to the caller
        uint256 tokenId = totalSupply() + 1;
        _mint(msg.sender, tokenId);

        emit MysteryBoxMinted(msg.sender, tokenId);
    }

    // Function to set mint rights for BTC holders
    function setMintRights(address[] calldata holders, uint256[] calldata rights) external onlyOwner {
        require(holders.length == rights.length, "Array lengths must match");
        
        for (uint256 i = 0; i < holders.length; i++) {
            mintRights[holders[i]] = rights[i];
        }
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Override base URI for token metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    // Function to update the price of mystery boxes
    function updateBoxPrice(uint256 newPrice) external onlyOwner {
        boxPrice = newPrice;
    }

    // Function to get remaining mint rights for an address
    function getMintRights(address holder) external view returns (uint256) {
        return mintRights[holder];
    }
}
```
