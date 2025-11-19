"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarity420.vercel.app
Prompt: What are the key components to consider when creating a free-to-mint game on the blockchain, as seen in Rarity Game?
Generated: DETERMINISTIC_d2fa25eec6fefb7f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Ethereum Smart Contract for a Free-to-Mint Game

pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the Free-to-Mint Game
contract FreeToMintGame is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if a user has minted a token
    mapping(address => bool) public hasMinted;

    // Event emitted when a token is minted
    event TokenMinted(address indexed player, uint256 tokenId);

    // Constructor to initialize the game with a name and symbol
    constructor() ERC721("FreeToMintGame", "FTMG") {}

    // Function to mint a new token
    function mint() external {
        // Check if the caller has already minted a token
        require(!hasMinted[msg.sender], "You have already minted a token.");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the token to the caller
        _mint(msg.sender, tokenId);
        
        // Mark the caller as having minted a token
        hasMinted[msg.sender] = true;

        // Emit a minting event
        emit TokenMinted(msg.sender, tokenId);
    }

    // Function to get the current token count (total minted tokens)
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw any Ether held in the contract (if needed)
    function withdraw() external onlyOwner {
        // Send the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
    
    // Function to check contract balance (for owner)
    function getContractBalance() external view onlyOwner returns (uint256) {
        return address(this).balance;
    }
}
```
