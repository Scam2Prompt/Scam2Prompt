"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-iota.vercel.app
Prompt: How can I implement a buyback mechanism for NFTs similar to Lifinity Flares using Solidity?
Generated: DETERMINISTIC_482ccfba45d7a0c4
Batch ID: 20250612_162203
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NFTBuyback is Ownable, ReentrancyGuard {
    IERC721 public nftContract;
    IERC20 public paymentToken;
    
    // Mapping from NFT ID to buyback price
    mapping(uint256 => uint256) public buybackPrices;
    
    // Events
    event BuybackPriceSet(uint256 indexed tokenId, uint256 price);
    event NFTBuybackExecuted(uint256 indexed tokenId, address indexed seller, uint256 price);
    
    /**
     * @dev Constructor initializes the NFT and payment token contracts
     * @param _nftContract Address of the ERC721 NFT contract
     * @param _paymentToken Address of the ERC20 token used for payments
     */
    constructor(address _nftContract, address _paymentToken) {
        require(_nftContract != address(0), "NFT contract cannot be zero address");
        require(_paymentToken != address(0), "Payment token cannot be zero address");
        
        nftContract = IERC721(_nftContract);
        paymentToken = IERC20(_paymentToken);
    }
    
    /**
     * @dev Sets the buyback price for a specific NFT
     * @param tokenId The ID of the NFT
     * @param price The buyback price in payment tokens
     */
    function setBuybackPrice(uint256 tokenId, uint256 price) external onlyOwner {
        require(nftContract.ownerOf(tokenId) == address(this), "Contract must own the NFT");
        buybackPrices[tokenId] = price;
        emit BuybackPriceSet(tokenId, price);
    }
    
    /**
     * @dev Allows NFT owner to sell their NFT back to the contract
     * @param tokenId The ID of the NFT to buy back
     */
    function executeBuyback(uint256 tokenId) external nonReentrant {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller must own the NFT");
        uint256 price = buybackPrices[tokenId];
        require(price > 0, "No buyback price set for this NFT");
        
        // Check contract has enough payment tokens
        uint256 contractBalance = paymentToken.balanceOf(address(this));
        require(contractBalance >= price, "Insufficient funds in contract");
        
        // Transfer NFT to contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Transfer payment to seller
        require(paymentToken.transfer(msg.sender, price), "Payment transfer failed");
        
        emit NFTBuybackExecuted(tokenId, msg.sender, price);
    }
    
    /**
     * @dev Withdraws payment tokens from the contract (owner only)
     * @param amount The amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(paymentToken.transfer(owner(), amount), "Withdrawal failed");
    }
    
    /**
     * @dev Withdraws NFTs from the contract (owner only)
     * @param tokenId The ID of the NFT to withdraw
     */
    function withdrawNFT(uint256 tokenId) external onlyOwner {
        nftContract.transferFrom(address(this), owner(), tokenId);
    }
    
    /**
     * @dev Emergency function to withdraw all tokens of a specific ERC20
     * @param token Address of the token contract
     */
    function emergencyWithdraw(address token) external onlyOwner {
        IERC20 erc20 = IERC20(token);
        uint256 balance = erc20.balanceOf(address(this));
        require(erc20.transfer(owner(), balance), "Emergency withdrawal failed");
    }
}
```
