"""
Generated Code Metadata:
========================
Original URL: https://bigtime-ai.pages.dev
Prompt: Design a smart contract for a blockchain-based game that utilizes NFTs and a cryptocurrency like $BIGTIME for in-game transactions.
Generated: DETERMINISTIC_f29f9d152872c74a
Batch ID: 20250622_205842
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

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for a blockchain-based game utilizing NFTs and $BIGTIME for transactions
contract GameNFT is ERC721, Ownable {
    // State variables
    uint256 public nextTokenId; // Counter for the next token ID
    IERC20 public bigTimeToken; // Reference to the $BIGTIME token contract

    // Mapping from token ID to the owner of the NFT
    mapping(uint256 => address) public tokenOwners;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with the token name, symbol, and $BIGTIME token address
    constructor(string memory name, string memory symbol, address _bigTimeToken) 
        ERC721(name, symbol) 
    {
        bigTimeToken = IERC20(_bigTimeToken);
    }

    // Function to mint a new NFT
    function mintNFT() external {
        // Define the cost of minting an NFT in $BIGTIME
        uint256 mintingCost = 100 * 10 ** 18; // Example cost: 100 $BIGTIME

        // Check if the sender has enough $BIGTIME tokens
        require(bigTimeToken.balanceOf(msg.sender) >= mintingCost, "Insufficient $BIGTIME balance");

        // Transfer the minting cost from the sender to the contract owner
        require(bigTimeToken.transferFrom(msg.sender, owner(), mintingCost), "Transfer failed");

        // Mint the NFT
        uint256 tokenId = nextTokenId;
        _mint(msg.sender, tokenId);
        tokenOwners[tokenId] = msg.sender; // Track the owner of the token
        nextTokenId++;

        // Emit the Minted event
        emit Minted(msg.sender, tokenId);
    }

    // Function to get the owner of a specific token ID
    function getTokenOwner(uint256 tokenId) external view returns (address) {
        return tokenOwners[tokenId];
    }

    // Function to withdraw $BIGTIME tokens from the contract (only owner)
    function withdrawTokens() external onlyOwner {
        uint256 balance = bigTimeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(bigTimeToken.transfer(owner(), balance), "Transfer failed");
    }

    // Function to set a new $BIGTIME token address (only owner)
    function setBigTimeToken(address _bigTimeToken) external onlyOwner {
        bigTimeToken = IERC20(_bigTimeToken);
    }
}
```
