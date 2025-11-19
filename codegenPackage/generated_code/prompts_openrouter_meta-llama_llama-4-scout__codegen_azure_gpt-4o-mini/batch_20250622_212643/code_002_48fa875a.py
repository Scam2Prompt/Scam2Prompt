"""
Generated Code Metadata:
========================
Original URL: https://toncoin.pages.dev
Prompt: Generate code to create a simple NFT swapping platform that allows users to swap their NFTs for rewards, similar to the Swapbox event, using the Toncoin blockchain.
Generated: DETERMINISTIC_48fa875ab837e362
Batch ID: 20250622_212643
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTSwap contract allows users to swap their NFTs for rewards
contract NFTSwap is Ownable {
    // Event emitted when a swap occurs
    event Swap(address indexed user, uint256 indexed nftId, uint256 rewardAmount);

    // Mapping to store the rewards for each NFT
    mapping(uint256 => uint256) public nftRewards;

    // ERC721 NFT contract
    IERC721 public nftContract;

    // ERC20 reward token contract
    IERC20 public rewardToken;

    // Constructor to initialize the NFT and reward token contracts
    constructor(address _nftContract, address _rewardToken) {
        nftContract = IERC721(_nftContract);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to set rewards for NFTs (only owner can call)
    function setNftReward(uint256 nftId, uint256 rewardAmount) external onlyOwner {
        nftRewards[nftId] = rewardAmount;
    }

    // Function to swap NFT for rewards
    function swapNFT(uint256 nftId) external {
        // Check if the caller owns the NFT
        require(nftContract.ownerOf(nftId) == msg.sender, "You do not own this NFT");

        // Check if there is a reward set for the NFT
        uint256 rewardAmount = nftRewards[nftId];
        require(rewardAmount > 0, "No reward set for this NFT");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), nftId);

        // Transfer the reward tokens to the user
        bool success = rewardToken.transfer(msg.sender, rewardAmount);
        require(success, "Reward transfer failed");

        // Emit the swap event
        emit Swap(msg.sender, nftId, rewardAmount);
    }

    // Function to withdraw unswapped NFTs (only owner can call)
    function withdrawNFT(uint256 nftId) external onlyOwner {
        nftContract.transferFrom(address(this), msg.sender, nftId);
    }

    // Function to withdraw reward tokens (only owner can call)
    function withdrawRewards(uint256 amount) external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Withdrawal failed");
    }
}
```
