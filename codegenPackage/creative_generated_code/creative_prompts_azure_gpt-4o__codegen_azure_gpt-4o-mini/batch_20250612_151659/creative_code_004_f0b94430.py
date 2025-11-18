"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Write a function in Solidity to limit the number of Ember NFTs a user can mint during the Fire Sale (1 per user) and Public Sale (2 per transaction).
Generated: DETERMINISTIC_f0b9443064092001
Batch ID: 20250612_151659
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EmberNFT is ERC721, Ownable {
    // Mapping to track the number of NFTs minted by each address
    mapping(address => uint256) public userMintCount;

    // Constants for the maximum limits during sales
    uint256 public constant FIRE_SALE_LIMIT = 1; // Limit for Fire Sale
    uint256 public constant PUBLIC_SALE_LIMIT = 2; // Limit for Public Sale

    // Sale states
    enum SaleState { NotStarted, FireSale, PublicSale }
    SaleState public currentSaleState;

    // Event to emit when a mint occurs
    event Mint(address indexed user, uint256 tokenId);

    // Token ID counter
    uint256 private _tokenIdCounter;

    constructor() ERC721("EmberNFT", "EMB") {
        currentSaleState = SaleState.NotStarted; // Initial state
    }

    // Function to start the Fire Sale
    function startFireSale() external onlyOwner {
        currentSaleState = SaleState.FireSale;
    }

    // Function to start the Public Sale
    function startPublicSale() external onlyOwner {
        currentSaleState = SaleState.PublicSale;
    }
    
    // Function to end the current sale
    function endSale() external onlyOwner {
        currentSaleState = SaleState.NotStarted;
    }

    // Function to mint new NFTs
    function mint() external {
        require(currentSaleState != SaleState.NotStarted, "Sale not active");

        // Determine the limit based on the current sale state
        uint256 limit = currentSaleState == SaleState.FireSale ? FIRE_SALE_LIMIT : PUBLIC_SALE_LIMIT;
        
        // Check if user has exceeded their minting limit
        require(userMintCount[msg.sender] < limit, "Minting limit reached for this sale");

        // Increment user's mint count and mint the NFT
        userMintCount[msg.sender]++;
        uint256 newTokenId = _tokenIdCounter++;
        _mint(msg.sender, newTokenId);

        // Emit mint event
        emit Mint(msg.sender, newTokenId);
    }

    // Function to get the current mint count of a user
    function getUserMintCount(address user) external view returns (uint256) {
        return userMintCount[user];
    }
}
```
