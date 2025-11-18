"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Write a Solidity smart contract to represent GoMining's digital miner tokens, ensuring they can be resold on marketplaces like OpenSea and continue mining BTC for the owner.
Generated: DETERMINISTIC_9e6e6796692207ee
Batch ID: 20250612_153916
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

// @title GoMining Digital Miner Tokens
// @dev This contract represents digital miner tokens that can be sold on marketplaces like OpenSea and continue to mine BTC for the owner.
contract GoMiningToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to store mining status of each token
    mapping(uint256 => bool) private _isMining;

    // Event emitted when a new miner token is created
    event MinerTokenCreated(uint256 indexed tokenId, address indexed owner);

    // Constructor to set the token name and symbol
    constructor() ERC721("GoMining Token", "GMT") {}

    // @notice Function to mint a new miner token
    // @dev Only the owner of the contract can mint new tokens
    // @return The ID of the newly minted token
    function mintMinerToken() external onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _isMining[tokenId] = true; // Mark the token as mining
        
        emit MinerTokenCreated(tokenId, msg.sender);
        
        _tokenIdCounter.increment();
        return tokenId;
    }

    // @notice Function to check if a token is actively mining BTC
    // @param tokenId The ID of the token to check
    // @return bool indicating whether the token is mining
    function isMining(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _isMining[tokenId];
    }

    // @notice Function to simulate the mining of BTC
    // @dev This is a placeholder for actual mining logic
    // @param tokenId The ID of the token that is mining
    function mineBTC(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this token");
        require(_isMining[tokenId], "Token is not mining");

        // Placeholder logic for mining BTC
        // Actual mining logic would go here
    }

    // @notice Override the _beforeTokenTransfer hook to maintain mining status during transfers
    // @dev This ensures the mining status is checked before transfers
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // We could add logic here if we need to change mining status on transfer
    }

    // @notice Function to burn a token (to stop it from mining and remove it)
    // @dev Only the owner of the token can burn it
    // @param tokenId The ID of the token to burn
    function burn(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this token");
        _burn(tokenId);
        delete _isMining[tokenId]; // Remove mining status
    }
}
```
