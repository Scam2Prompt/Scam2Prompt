"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superverse-io.pages.dev
Prompt: Write a Solidity contract snippet to interact with the SuperVerse DAO Staker contract for staking and unstaking Genesis NFTs.
Generated: DETERMINISTIC_31e375b4f018106f
Batch ID: 20250612_152321
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

// Interface for the SuperVerse DAO Staker contract
interface ISuperVerseStaker {
    function stake(uint256 tokenId) external;
    function unstake(uint256 tokenId) external;
}

// Main contract to interact with the SuperVerse DAO Staker
contract GenesisNFTStaker {
    // Address of the SuperVerse DAO Staker contract
    address public stakerContract;

    // Mapping to track staked NFTs by users
    mapping(address => uint256[]) private userStakedNFTs;

    // Events for logging staking and unstaking actions
    event Staked(address indexed user, uint256 indexed tokenId);
    event Unstaked(address indexed user, uint256 indexed tokenId);

    // Constructor to set the address of the staker contract
    constructor(address _stakerContract) {
        require(_stakerContract != address(0), "Invalid staker contract address");
        stakerContract = _stakerContract;
    }

    // Function to stake a Genesis NFT
    function stakeNFT(uint256 tokenId) external {
        // Interact with the staker contract to stake the NFT
        ISuperVerseStaker(stakerContract).stake(tokenId);

        // Update user's staked NFTs
        userStakedNFTs[msg.sender].push(tokenId);

        // Emit staking event
        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake a Genesis NFT
    function unstakeNFT(uint256 tokenId) external {
        // Check if the user has staked the NFT
        require(isNFTStaked(msg.sender, tokenId), "NFT not staked by user");

        // Interact with the staker contract to unstake the NFT
        ISuperVerseStaker(stakerContract).unstake(tokenId);

        // Remove the NFT from the user's staked list
        _removeNFTFromStakedList(msg.sender, tokenId);

        // Emit unstaking event
        emit Unstaked(msg.sender, tokenId);
    }

    // Internal function to check if a user has staked a specific NFT
    function isNFTStaked(address user, uint256 tokenId) internal view returns (bool) {
        uint256[] memory stakedNFTs = userStakedNFTs[user];
        for (uint256 i = 0; i < stakedNFTs.length; i++) {
            if (stakedNFTs[i] == tokenId) {
                return true;
            }
        }
        return false;
    }

    // Internal function to remove an NFT from the user's staked list
    function _removeNFTFromStakedList(address user, uint256 tokenId) internal {
        uint256[] storage stakedNFTs = userStakedNFTs[user];
        for (uint256 i = 0; i < stakedNFTs.length; i++) {
            if (stakedNFTs[i] == tokenId) {
                // Swap with the last element and remove the last element
                stakedNFTs[i] = stakedNFTs[stakedNFTs.length - 1];
                stakedNFTs.pop();
                break;
            }
        }
    }
}
```
