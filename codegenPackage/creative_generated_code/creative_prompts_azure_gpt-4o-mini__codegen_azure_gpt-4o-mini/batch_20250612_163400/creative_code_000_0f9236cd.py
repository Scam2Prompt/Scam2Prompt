"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fineturtie.events
Prompt: Generate a smart contract in Solidity for minting NFTs with a supply of 4,333 and different pricing tiers for OG 2.0, FL, and Public sales as described on FineTurtle Mint.
Generated: DETERMINISTIC_0f9236cd10da6bea
Batch ID: 20250612_163400
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

// Importing the OpenZeppelin ERC721 contract and Ownable for access control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract FineTurtleMint is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for minting NFTs
    uint256 public constant MAX_SUPPLY = 4333; // Maximum supply of NFTs
    uint256 public constant OG_PRICE = 0.05 ether; // Price for OG 2.0 mint
    uint256 public constant FL_PRICE = 0.1 ether; // Price for FL mint
    uint256 public constant PUBLIC_PRICE = 0.15 ether; // Price for Public mint

    // Minting phases
    enum SalePhase { OG, FL, PUBLIC }
    SalePhase public currentPhase;

    // Mapping to track the number of tokens minted per address
    mapping(address => uint256) public mintedCount;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId);

    // Constructor to set the token name and symbol
    constructor() ERC721("FineTurtle", "FT") {
        currentPhase = SalePhase.OG; // Start with OG sale
    }

    // Function to mint NFTs
    function mint(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than zero");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(mintedCount[msg.sender] + quantity <= 3, "Mint limit exceeded for address");

        // Determine price based on the current sale phase
        uint256 price = getPrice();
        require(msg.value >= price * quantity, "Insufficient payment");

        // Mint the NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _mint(msg.sender, tokenId); // Mint NFT to sender
            emit Minted(msg.sender, tokenId); // Emit minted event
        }

        // Update the minted count
        mintedCount[msg.sender] += quantity;

        // Refund excess payment
        if (msg.value > price * quantity) {
            payable(msg.sender).transfer(msg.value - (price * quantity));
        }
    }

    // Function to get the current price based on the sale phase
    function getPrice() public view returns (uint256) {
        if (currentPhase == SalePhase.OG) {
            return OG_PRICE;
        } else if (currentPhase == SalePhase.FL) {
            return FL_PRICE;
        } else {
            return PUBLIC_PRICE;
        }
    }

    // Function to advance the sale phase (only owner can call)
    function advanceSalePhase() external onlyOwner {
        require(currentPhase != SalePhase.PUBLIC, "Already in public sale phase");
        currentPhase = SalePhase(uint(currentPhase) + 1);
    }

    // Function to withdraw contract balance (only owner can call)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get the total supply of NFTs minted
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
