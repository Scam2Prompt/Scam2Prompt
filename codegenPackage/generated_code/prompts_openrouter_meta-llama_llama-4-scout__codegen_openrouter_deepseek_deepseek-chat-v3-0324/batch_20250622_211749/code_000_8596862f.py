"""
Generated Code Metadata:
========================
Original URL: https://web3-community.web.app
Prompt: Write a smart contract function in Solidity to implement a 24-hour delay for claiming rewards after NFT minting, similar to the MYSTERY BOX NFT project.
Generated: DETERMINISTIC_8596862fb3430a72
Batch ID: 20250622_211749
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MysteryBoxNFT is ERC721, Ownable {
    using SafeMath for uint256;

    // Mapping from token ID to mint timestamp
    mapping(uint256 => uint256) private _mintTimestamps;

    // Mapping from token ID to whether rewards have been claimed
    mapping(uint256 => bool) private _rewardsClaimed;

    // Reward claim delay period (24 hours in seconds)
    uint256 public constant REWARD_CLAIM_DELAY = 86400;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mints a new NFT and records the mint timestamp
     * @param to The address that will receive the minted NFT
     * @param tokenId The ID of the NFT to mint
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "MysteryBoxNFT: token already minted");
        _mint(to, tokenId);
        _mintTimestamps[tokenId] = block.timestamp;
    }

    /**
     * @dev Claims rewards for a specific NFT after the 24-hour delay period
     * @param tokenId The ID of the NFT to claim rewards for
     */
    function claimRewards(uint256 tokenId) external {
        require(_exists(tokenId), "MysteryBoxNFT: rewards claim for nonexistent token");
        require(ownerOf(tokenId) == msg.sender, "MysteryBoxNFT: caller is not the owner");
        require(!_rewardsClaimed[tokenId], "MysteryBoxNFT: rewards already claimed");
        require(
            block.timestamp >= _mintTimestamps[tokenId].add(REWARD_CLAIM_DELAY),
            "MysteryBoxNFT: reward claim delay not passed"
        );

        _rewardsClaimed[tokenId] = true;
        // Implement your reward distribution logic here
        _distributeRewards(tokenId);
    }

    /**
     * @dev Internal function to handle reward distribution
     * @param tokenId The ID of the NFT to distribute rewards for
     */
    function _distributeRewards(uint256 tokenId) internal {
        // Add your custom reward distribution logic here
        // This could include token transfers, airdrops, etc.
    }

    /**
     * @dev Checks if rewards can be claimed for a specific NFT
     * @param tokenId The ID of the NFT to check
     * @return bool Whether rewards can be claimed
     */
    function canClaimRewards(uint256 tokenId) external view returns (bool) {
        if (!_exists(tokenId) || _rewardsClaimed[tokenId]) {
            return false;
        }
        return block.timestamp >= _mintTimestamps[tokenId].add(REWARD_CLAIM_DELAY);
    }

    /**
     * @dev Gets the mint timestamp for a specific NFT
     * @param tokenId The ID of the NFT to check
     * @return uint256 The mint timestamp
     */
    function getMintTimestamp(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "MysteryBoxNFT: query for nonexistent token");
        return _mintTimestamps[tokenId];
    }

    /**
     * @dev Checks if rewards have been claimed for a specific NFT
     * @param tokenId The ID of the NFT to check
     * @return bool Whether rewards have been claimed
     */
    function rewardsClaimed(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "MysteryBoxNFT: query for nonexistent token");
        return _rewardsClaimed[tokenId];
    }
}
```
