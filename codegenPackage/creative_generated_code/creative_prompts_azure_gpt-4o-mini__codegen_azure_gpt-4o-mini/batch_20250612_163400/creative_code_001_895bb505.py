"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fineturtie.events
Prompt: How can I implement a minting function for a limited NFT supply of 4,333 with specific ETH prices for different user categories based on the FineTurtle Mint specifications?
Generated: DETERMINISTIC_895bb5053d8f9955
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract FineTurtleMint is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Total supply limit
    uint256 public constant MAX_SUPPLY = 4333;

    // Price tiers for different user categories
    enum UserCategory { Regular, Whitelisted, VIP }
    mapping(UserCategory => uint256) public categoryPrices;

    // Mapping to track whether an address is whitelisted
    mapping(address => bool) public whitelistedAddresses;

    // Event to emit when a mint occurs
    event Mint(address indexed to, uint256 tokenId);

    constructor() ERC721("FineTurtle", "FTNFT") {
        // Setting the prices for different user categories
        categoryPrices[UserCategory.Regular] = 0.05 ether;
        categoryPrices[UserCategory.Whitelisted] = 0.03 ether;
        categoryPrices[UserCategory.VIP] = 0.01 ether;
    }

    /**
     * @dev Allows users to mint an NFT based on their category.
     * @param category The category of the user (Regular, Whitelisted, VIP)
     */
    function mint(UserCategory category) external payable {
        // Verify that the NFT supply limit has not been reached
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        // Check if the sent value matches the price for the user's category
        require(msg.value == categoryPrices[category], "Incorrect ETH amount sent");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Emit the mint event
        emit Mint(msg.sender, tokenId);
    }

    /**
     * @dev Allows the owner to whitelist an address.
     * @param addr The address to whitelist
     */
    function whitelistAddress(address addr) external onlyOwner {
        whitelistedAddresses[addr] = true;
    }

    /**
     * @dev Allows the owner to remove an address from the whitelist.
     * @param addr The address to remove from whitelist
     */
    function removeWhitelistedAddress(address addr) external onlyOwner {
        whitelistedAddresses[addr] = false;
    }

    /**
     * @dev Withdraw contract balance to owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}

    /**
     * @dev Function to get current price for a specific category
     * @param category The category of the user
     * @return The price for the specified user category
     */
    function getPrice(UserCategory category) external view returns (uint256) {
        return categoryPrices[category];
    }
}
```
