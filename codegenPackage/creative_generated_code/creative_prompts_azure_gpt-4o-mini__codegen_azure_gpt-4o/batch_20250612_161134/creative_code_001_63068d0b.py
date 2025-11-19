"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichaincrew.club
Prompt: How can I create a smart contract for an NFT collection similar to the Unichain Crew Club?
Generated: DETERMINISTIC_63068d0b89703e70
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a smart contract for an NFT collection written in Solidity, following the ERC-721 standard. It is clean, well-documented, and production-ready, with best practices and error handling applied.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import ERC721 and helpers from OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title UnichainCrewClubNFT
 * @dev ERC-721 compliant NFT contract for a collection similar to Unichain Crew Club.
 * Features include token minting, metadata configuration, and enumerable tokens.
 */
contract UnichainCrewClubNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private baseTokenURI;
    
    // Total supply limit
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per token (in Wei)
    uint256 public constant TOKEN_PRICE = 0.05 ether;

    // Maximum tokens per transaction
    uint256 public constant MAX_PER_TX = 10;

    // Tracks total minted tokens
    uint256 public totalMinted;

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _baseTokenURI Base URI for token metadata.
     */
    constructor(string memory _name, string memory _symbol, string memory _baseTokenURI) 
        ERC721(_name, _symbol) 
    {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Sets the base URI for token metadata.
     * @param _baseTokenURI New base URI.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Returns the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Mint new tokens.
     * @param _amount Number of tokens to mint.
     */
    function mint(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(_amount <= MAX_PER_TX, "Exceeds max tokens per transaction");
        require(totalMinted + _amount <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= _amount * TOKEN_PRICE, "Insufficient funds");

        for (uint256 i = 0; i < _amount; i++) {
            uint256 tokenId = totalMinted + 1; // Token IDs start at 1
            _safeMint(msg.sender, tokenId);
            totalMinted++;
        }
    }

    /**
     * @dev Withdraw contract balance to owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether sending.
     */
    receive() external payable {
        revert("Direct ether transfer not allowed");
    }
}
```

### Notes:
1. Ensure you have OpenZeppelin Contracts installed in your project (`npm install @openzeppelin/contracts`).
2. Replace `_baseTokenURI` in the constructor with the actual base URI for your NFT metadata.
3. Configure deployment scripts and security audits while deploying to production environments.
