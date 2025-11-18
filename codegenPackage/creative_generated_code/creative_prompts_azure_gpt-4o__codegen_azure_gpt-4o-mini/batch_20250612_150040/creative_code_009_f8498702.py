"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappsnodes.pages.dev
Prompt: Create a script to integrate NFT staking functionality into a Dapp using the Smart Dapps Chain platform's features.
Generated: DETERMINISTIC_f8498702b1a8c851
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Staking contract
interface IStaking {
    function stake(uint256 tokenId) external;
    function unstake(uint256 tokenId) external;
    function rewardsOf(address owner) external view returns (uint256);
}

// NFT Staking Contract
contract NFTStaking is IStaking, Ownable {
    // Mapping of token owners to their staked status
    mapping(uint256 => address) private _stakedOwners;
    // Mapping to track staking timestamps for reward calculations
    mapping(uint256 => uint256) private _stakingStartTime;
    
    // The ERC721 NFT contract
    IERC721 public nftContract;

    // Event emitted when an NFT is staked
    event Staked(address owner, uint256 tokenId);
    // Event emitted when an NFT is unstaked
    event Unstaked(address owner, uint256 tokenId);
    
    // Constructor to set the NFT contract address
    constructor(address nftAddress) {
        nftContract = IERC721(nftAddress);
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external override {
        // Check if the caller is the owner of the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this token");
        require(_stakedOwners[tokenId] == address(0), "Token already staked");

        // Transfer the NFT to the staking contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Update the mappings to track staking
        _stakedOwners[tokenId] = msg.sender;
        _stakingStartTime[tokenId] = block.timestamp;

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external override {
        require(_stakedOwners[tokenId] == msg.sender, "You do not own this staked token");

        // Clear the staking data
        delete _stakedOwners[tokenId];
        delete _stakingStartTime[tokenId];

        // Transfer the NFT back to the owner
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    // Function to calculate rewards based on time staked
    function rewardsOf(address owner) external view override returns (uint256) {
        uint256 totalRewards = 0;

        // Loop through all tokens - to be optimized in a real-world scenario
        for (uint256 i = 0; i < 10000; i++) { // Assuming a max of 10,000 NFTs
            if (_stakedOwners[i] == owner) {
                totalRewards += (block.timestamp - _stakingStartTime[i]) / 1 days; // 1 reward per day
            }
        }

        return totalRewards;
    }
}
```
