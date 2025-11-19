"""
Generated Code Metadata:
========================
Original URL: https://proposal-playmemoria.com
Prompt: Develop a simple smart contract for NFT staking on a blockchain platform like Avalanche.
Generated: DETERMINISTIC_5af5427ce52abcf4
Batch ID: 20250622_212051
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

// Importing the ERC721 interface for NFT interactions
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the staking contract
interface IStaking {
    function stake(uint256 tokenId) external;
    function unstake(uint256 tokenId) external;
}

// NFTStaking contract for staking ERC721 tokens
contract NFTStaking is Ownable {
    // Mapping to track staked NFTs
    mapping(uint256 => address) public stakedBy;
    // Mapping to track the staking status of NFTs
    mapping(uint256 => bool) public isStaked;

    // Event emitted when an NFT is staked
    event Staked(address indexed owner, uint256 indexed tokenId);
    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed owner, uint256 indexed tokenId);

    // Reference to the ERC721 contract
    IERC721 public nftContract;

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        // Ensure the NFT is not already staked
        require(!isStaked[tokenId], "NFT is already staked");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        // Update the staking status
        stakedBy[tokenId] = msg.sender;
        isStaked[tokenId] = true;

        // Emit the Staked event
        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external {
        // Ensure the NFT is staked
        require(isStaked[tokenId], "NFT is not staked");
        // Ensure the caller is the owner of the staked NFT
        require(stakedBy[tokenId] == msg.sender, "You are not the owner of this NFT");

        // Update the staking status
        isStaked[tokenId] = false;
        delete stakedBy[tokenId];

        // Transfer the NFT back to the owner
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, tokenId);
    }

    // Function to check if an NFT is staked
    function isNFTStaked(uint256 tokenId) external view returns (bool) {
        return isStaked[tokenId];
    }

    // Function to get the owner of a staked NFT
    function ownerOfStakedNFT(uint256 tokenId) external view returns (address) {
        require(isStaked[tokenId], "NFT is not staked");
        return stakedBy[tokenId];
    }
}
```
