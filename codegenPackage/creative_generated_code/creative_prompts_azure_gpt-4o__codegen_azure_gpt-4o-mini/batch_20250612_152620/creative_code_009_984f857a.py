"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Write a Solidity contract to implement a fractional NFT system where investors can earn equity-based rewards, similar to InQubeta’s NFT marketplace model.
Generated: DETERMINISTIC_984f857a726de99f
Batch ID: 20250612_152620
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

/// @title Fractional NFT Contract
/// @author Your Name
/// @notice This contract allows fractional ownership of NFTs and rewards investors based on their equity shares.
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FractionalNFT is Ownable {
    // Struct to represent a fractional NFT
    struct FractionalNFTInfo {
        address nftContract;         // Address of the NFT contract
        uint256 nftTokenId;         // Token ID of the NFT
        uint256 totalShares;        // Total number of shares
        uint256 totalValue;         // Total value of the NFT
        mapping(address => uint256) shares; // Mapping of investor addresses to their shares
        uint256 rewardPool;         // Total rewards pooled for distribution
    }

    // Mapping to store fractional NFT information
    mapping(uint256 => FractionalNFTInfo) public fractionalNFTs;
    uint256 public nextNFTId; // Counter for unique NFT IDs

    // Event emitted when a new fractional NFT is created
    event FractionalNFTCreated(uint256 indexed nftId, address indexed nftContract, uint256 indexed nftTokenId, uint256 totalShares, uint256 totalValue);
    // Event emitted when shares are purchased
    event SharesPurchased(uint256 indexed nftId, address indexed investor, uint256 sharesAmount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(uint256 indexed nftId, address indexed investor, uint256 rewardAmount);

    /// @notice Create a new fractional NFT
    /// @param _nftContract The address of the NFT contract
    /// @param _nftTokenId The token ID of the NFT
    /// @param _totalShares The total number of shares to be created
    /// @param _totalValue The total value of the NFT
    function createFractionalNFT(
        address _nftContract,
        uint256 _nftTokenId,
        uint256 _totalShares,
        uint256 _totalValue
    ) external onlyOwner {
        require(_totalShares > 0, "Total shares must be greater than zero");
        require(_totalValue > 0, "Total value must be greater than zero");

        // Creating new fractional NFT
        FractionalNFTInfo storage fractionalNFT = fractionalNFTs[nextNFTId];
        fractionalNFT.nftContract = _nftContract;
        fractionalNFT.nftTokenId = _nftTokenId;
        fractionalNFT.totalShares = _totalShares;
        fractionalNFT.totalValue = _totalValue;

        emit FractionalNFTCreated(nextNFTId, _nftContract, _nftTokenId, _totalShares, _totalValue);
        nextNFTId++;
    }

    /// @notice Purchase shares in a fractional NFT
    /// @param _nftId The ID of the fractional NFT
    /// @param _sharesAmount The number of shares to purchase
    function purchaseShares(uint256 _nftId, uint256 _sharesAmount) external payable {
        FractionalNFTInfo storage fractionalNFT = fractionalNFTs[_nftId];
        
        require(_sharesAmount > 0, "Shares amount must be greater than zero");
        require(fractionalNFT.shares[msg.sender] + _sharesAmount <= fractionalNFT.totalShares, "Exceeds total shares");

        // Calculate cost per share
        uint256 sharePrice = fractionalNFT.totalValue / fractionalNFT.totalShares;
        require(msg.value >= sharePrice * _sharesAmount, "Insufficient payment");

        // Assign shares to the investor
        fractionalNFT.shares[msg.sender] += _sharesAmount;

        // Add received funds to the reward pool
        fractionalNFT.rewardPool += msg.value;

        emit SharesPurchased(_nftId, msg.sender, _sharesAmount);
    }

    /// @notice Claim rewards based on shares owned
    /// @param _nftId The ID of the fractional NFT
    function claimRewards(uint256 _nftId) external {
        FractionalNFTInfo storage fractionalNFT = fractionalNFTs[_nftId];
        
        uint256 sharesOwned = fractionalNFT.shares[msg.sender];
        require(sharesOwned > 0, "No shares owned");

        // Calculate the reward amount for the investor
        uint256 rewardAmount = (fractionalNFT.rewardPool * sharesOwned) / fractionalNFT.totalShares;
        require(rewardAmount > 0, "No rewards available");

        // Reset the reward pool for the investor
        fractionalNFT.rewardPool -= rewardAmount;

        // Transfer the reward to the investor
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(_nftId, msg.sender, rewardAmount);
    }

    /// @notice Withdraw funds from the contract (for owner)
    /// @param amount The amount to withdraw
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdraw failed");
    }

    /// @notice Fallback function to receive ETH
    receive() external payable {}
}
```
