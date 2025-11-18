"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-community.web.app
Prompt: Generate a Solidity smart contract that includes a function for free minting of NFTs and a reward system with randomized prize values.
Generated: DETERMINISTIC_6a2b69711f286a43
Batch ID: 20250612_145931
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract FreeMintNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Mapping to store reward values for each token
    mapping(uint256 => uint256) private _rewardValues;

    // Event emitted when a new NFT is minted
    event Minted(address indexed recipient, uint256 tokenId, uint256 rewardValue);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("FreeMintNFT", "FMNFT") {}

    // Function to mint a new NFT for free
    function mintNFT() external {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);

        // Assign a random reward value to the minted NFT
        uint256 rewardValue = _randomReward();
        _rewardValues[tokenId] = rewardValue;

        // Emit the Minted event
        emit Minted(msg.sender, tokenId, rewardValue);
    }

    // Internal function to generate a random reward value
    function _randomReward() internal view returns (uint256) {
        // Returns a random value based on block properties (not secure for production)
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % 100 + 1;
    }

    // Function to get the reward value for a specific token
    function getRewardValue(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _rewardValues[tokenId];
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view override returns (bool) {
        return super._exists(tokenId);
    }
}
```
