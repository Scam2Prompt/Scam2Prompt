"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: Write a Solidity function to celebrate the 280th anniversary of Karaton Surakarta by minting commemorative NFTs tied to $MASA token transactions.
Generated: DETERMINISTIC_22a214f9450208a2
Batch ID: 20250612_145625
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for commemorative NFTs
contract KaratonSurakartaNFT is ERC721Enumerable, Ownable {
    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    // Mapping from token ID to the associated $MASA transaction amount
    mapping(uint256 => uint256) public tokenIdToMasaAmount;

    // Counter for the next token ID
    uint256 private _nextTokenId;

    // Reference to the $MASA token contract
    IERC20 public masaToken;

    // Constructor to initialize the contract
    constructor(address _masaTokenAddress) ERC721("Karaton Surakarta Commemorative NFT", "KSCNFT") {
        masaToken = IERC20(_masaTokenAddress);
    }

    // Function to mint a commemorative NFT
    function mintNFT(uint256 amount) external {
        // Check if the user has approved the contract to spend $MASA tokens
        require(masaToken.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance for $MASA tokens");

        // Transfer $MASA tokens from the user to the contract
        require(masaToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Mint the NFT
        uint256 tokenId = _nextTokenId++;
        _mint(msg.sender, tokenId);

        // Store the amount of $MASA associated with this token
        tokenIdToMasaAmount[tokenId] = amount;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to withdraw $MASA tokens from the contract
    function withdrawMasaTokens(uint256 amount) external onlyOwner {
        require(masaToken.balanceOf(address(this)) >= amount, "Insufficient $MASA balance in contract");
        require(masaToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to get the total amount of $MASA associated with a specific NFT
    function getMasaAmountForToken(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return tokenIdToMasaAmount[tokenId];
    }
}
```
