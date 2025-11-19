"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t1-32y.pages.dev
Prompt: How can I implement a minting function for a traditional NFT collection with a whitelist and a public mint price of 0.01 ETH, based on the details from Blaze?
Generated: DETERMINISTIC_5af10d8215e5e696
Batch ID: 20250612_162404
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract WhitelistNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public constant MINT_PRICE = 0.01 ether; // Public mint price
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs
    mapping(address => bool) public whitelisted; // Track whitelisted addresses

    // Events
    event Minted(address indexed user, uint256 tokenId);

    // Constructor
    constructor() ERC721("WhitelistNFT", "WNFT") {}

    // Modifier to check if the user is whitelisted
    modifier onlyWhitelisted() {
        require(whitelisted[msg.sender], "You are not whitelisted");
        _;
    }

    // Function to add addresses to the whitelist
    function addToWhitelist(address _address) external onlyOwner {
        require(!whitelisted[_address], "Address is already whitelisted");
        whitelisted[_address] = true;
    }

    // Function to remove addresses from the whitelist
    function removeFromWhitelist(address _address) external onlyOwner {
        require(whitelisted[_address], "Address is not whitelisted");
        whitelisted[_address] = false;
    }

    // Mint function for whitelisted users
    function mint() external payable onlyWhitelisted {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(msg.value >= MINT_PRICE, "Insufficient ETH sent");

        uint256 tokenId = _tokenIdCounter.current(); // Get current token ID
        _tokenIdCounter.increment(); // Increment token ID counter
        _safeMint(msg.sender, tokenId); // Mint the token to the user

        emit Minted(msg.sender, tokenId); // Emit mint event
    }

    // Function to withdraw funds from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = msg.sender.call{value: balance}(""); // Transfer balance
        require(success, "Transfer failed"); // Ensure transfer succeeded
    }

    // Function to check contract balance (for owner's use)
    function contractBalance() external view onlyOwner returns (uint256) {
        return address(this).balance; // Return contract balance
    }
}
```
