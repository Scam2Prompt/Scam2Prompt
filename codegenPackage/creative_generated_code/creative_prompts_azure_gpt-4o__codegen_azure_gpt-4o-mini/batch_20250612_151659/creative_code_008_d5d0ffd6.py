"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Create a Solidity contract snippet that includes a whitelist (WL) mechanism for Ember NFT minting, ensuring only "Lit List" members can participate in the Fire Sale.
Generated: DETERMINISTIC_d5d0ffd66d5a5a00
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title EmberNFT
 * @dev ERC721 contract for Ember NFTs with a whitelist mechanism for minting during the Fire Sale.
 */
contract EmberNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to keep track of whitelist members
    mapping(address => bool) private _whitelist;

    // Event to emit when a user is added to the whitelist
    event AddedToWhitelist(address indexed user);
    
    // Event to emit when a user is removed from the whitelist
    event RemovedFromWhitelist(address indexed user);

    // Modifier to check if the caller is on the whitelist
    modifier onlyWhitelisted() {
        require(_whitelist[msg.sender], "Not whitelisted for the Fire Sale");
        _;
    }

    constructor() ERC721("EmberNFT", "EMB") {}

    /**
     * @dev Function to mint a new NFT. Only whitelisted members can call this function.
     */
    function mint() external onlyWhitelisted {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Function to add a user to the whitelist.
     * @param user The address to be added to the whitelist.
     */
    function addToWhitelist(address user) external onlyOwner {
        require(user != address(0), "Cannot add zero address to whitelist");
        require(!_whitelist[user], "User already whitelisted");
        
        _whitelist[user] = true;
        emit AddedToWhitelist(user);
    }

    /**
     * @dev Function to remove a user from the whitelist.
     * @param user The address to be removed from the whitelist.
     */
    function removeFromWhitelist(address user) external onlyOwner {
        require(_whitelist[user], "User not whitelisted");
        
        delete _whitelist[user];
        emit RemovedFromWhitelist(user);
    }

    /**
     * @dev Function to check if an address is whitelisted.
     * @param user The address to check.
     * @return True if the user is whitelisted, false otherwise.
     */
    function isWhitelisted(address user) external view returns (bool) {
        return _whitelist[user];
    }
}
```
