"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominingtoken.web.app
Prompt: Develop a smart contract in Solidity to list a GoMining digital miner for resale on OpenSea, ensuring compliance with the 5% service charge policy.
Generated: DETERMINISTIC_4017dea237450879
Batch ID: 20250612_153925
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

// Import the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// A smart contract for listing a GoMining digital miner for resale
contract GoMiningMiner is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Events
    event MinerListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event MinerSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Counter for tracking the next token ID
    Counters.Counter private _tokenIdCounter;

    // Struct to hold miner details
    struct Miner {
        uint256 tokenId;
        uint256 price;
        address seller;
        bool isListed;
    }

    // Mapping from tokenId to Miner struct
    mapping(uint256 => Miner) public miners;

    // The service charge percentage
    uint256 public constant SERVICE_CHARGE_PERCENTAGE = 5;

    // Constructor to initialize the token
    constructor() ERC721("GoMiningMiner", "GMM") {}

    // Function to mint a new miner
    function mintMiner() external onlyOwner returns (uint256) {
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        _mint(msg.sender, newTokenId);

        // Initialize miner details
        miners[newTokenId] = Miner({
            tokenId: newTokenId,
            price: 0,
            seller: address(0),
            isListed: false
        });

        return newTokenId;
    }

    // Function to list a miner for sale
    function listMiner(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "Miner does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list the miner");
        require(price > 0, "Price must be greater than zero");

        miners[tokenId].price = price;
        miners[tokenId].seller = msg.sender;
        miners[tokenId].isListed = true;

        emit MinerListed(tokenId, msg.sender, price);
    }

    // Function to buy a listed miner
    function buyMiner(uint256 tokenId) external payable {
        require(miners[tokenId].isListed, "Miner is not listed for sale");
        require(msg.value >= miners[tokenId].price, "Insufficient funds to buy miner");

        // Calculate service charge
        uint256 serviceCharge = (miners[tokenId].price * SERVICE_CHARGE_PERCENTAGE) / 100;
        uint256 sellerAmount = miners[tokenId].price - serviceCharge;

        // Transfer payment to the seller
        payable(miners[tokenId].seller).transfer(sellerAmount);
        
        // Transfer miner ownership
        _transfer(miners[tokenId].seller, msg.sender, tokenId);

        // Reset miner details
        miners[tokenId].isListed = false;
        miners[tokenId].seller = address(0);
        miners[tokenId].price = 0;

        emit MinerSold(tokenId, msg.sender, miners[tokenId].price);
    }

    // Function to withdraw service charges (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to get miner details
    function getMinerDetails(uint256 tokenId) external view returns (Miner memory) {
        require(_exists(tokenId), "Miner does not exist");
        return miners[tokenId];
    }
}
```
