"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neondrainer.web.app
Prompt: Create a Solidity contract that allows users to trade fractional NFTs based on the Wen token model described on the website.
Generated: DETERMINISTIC_0cbee94c8bc7d417
Batch ID: 20250612_162508
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

// Importing OpenZeppelin Contracts for ERC721 and SafeMath
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FractionalNFT is a contract that allows users to trade fractional NFTs
contract FractionalNFT is ERC721Holder, Ownable {
    using SafeMath for uint256;

    // Structure to hold details about the fractional NFT
    struct FractionalNFTDetail {
        uint256 totalShares;    // Total shares of the fractional NFT
        uint256 sharePrice;     // Price per share
        address nftContract;     // Address of the NFT contract
        uint256 tokenId;        // ID of the NFT token
    }

    // Mapping from token ID to its fractional details
    mapping(uint256 => FractionalNFTDetail) public fractionalNFTs;

    // Event emitted when a new fractional NFT is created
    event FractionalNFTCreated(uint256 indexed tokenId, uint256 totalShares, uint256 sharePrice, address indexed nftContract);
    
    // Event emitted when shares are purchased
    event SharesPurchased(uint256 indexed tokenId, address indexed buyer, uint256 sharesPurchased);

    // Function to create a new fractional NFT
    function createFractionalNFT(
        address _nftContract,
        uint256 _tokenId,
        uint256 _totalShares,
        uint256 _sharePrice
    ) external onlyOwner {
        // Validate inputs
        require(_totalShares > 0, "Total shares must be greater than zero");
        require(_sharePrice > 0, "Share price must be greater than zero");

        // Transfer the NFT to this contract
        IERC721(_nftContract).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Store the fractional NFT details
        fractionalNFTs[_tokenId] = FractionalNFTDetail({
            totalShares: _totalShares,
            sharePrice: _sharePrice,
            nftContract: _nftContract,
            tokenId: _tokenId
        });

        emit FractionalNFTCreated(_tokenId, _totalShares, _sharePrice, _nftContract);
    }

    // Function to purchase shares of a fractional NFT
    function purchaseShares(uint256 _tokenId, uint256 _shares) external payable {
        FractionalNFTDetail storage fractionalNFT = fractionalNFTs[_tokenId];

        // Ensure fractional NFT exists
        require(fractionalNFT.totalShares > 0, "Fractional NFT does not exist");
        require(_shares > 0, "Shares must be greater than zero");
        require(_shares <= fractionalNFT.totalShares, "Insufficient shares available");
        require(msg.value == _shares.mul(fractionalNFT.sharePrice), "Incorrect Ether sent for purchase");

        // Deduct purchased shares from total shares
        fractionalNFT.totalShares = fractionalNFT.totalShares.sub(_shares);

        // Emit event for shares purchased
        emit SharesPurchased(_tokenId, msg.sender, _shares);
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw the NFT from the contract after all shares are sold
    function withdrawNFT(uint256 _tokenId) external onlyOwner {
        FractionalNFTDetail storage fractionalNFT = fractionalNFTs[_tokenId];

        // Ensure all shares are sold
        require(fractionalNFT.totalShares == 0, "All shares must be sold before withdraw");

        // Transfer the NFT back to the owner
        IERC721(fractionalNFT.nftContract).safeTransferFrom(address(this), msg.sender, fractionalNFT.tokenId);

        // Delete the fractional details from storage
        delete fractionalNFTs[_tokenId];
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
