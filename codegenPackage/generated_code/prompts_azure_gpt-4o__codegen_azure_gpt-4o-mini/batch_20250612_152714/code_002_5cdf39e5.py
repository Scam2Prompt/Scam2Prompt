"""
Generated Code Metadata:
========================
Original URL: https://move-e87.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim tokens or NFTs after verifying their wallet address, similar to the MoveDrop Claim process.
Generated: DETERMINISTIC_5cdf39e54ddf374c
Batch ID: 20250612_152714
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MoveDropClaim
 * @dev A smart contract that allows users to claim tokens or NFTs after verifying their wallet address.
 */
contract MoveDropClaim is Ownable {
    // Mapping to track claimed addresses
    mapping(address => bool) private claimed;

    // ERC20 token to be claimed
    IERC20 public token;
    
    // ERC721 NFT to be claimed
    IERC721 public nft;

    // Event emitted when a claim is successful
    event Claimed(address indexed claimant, uint256 amount, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with the token and NFT addresses.
     * @param _tokenAddress The address of the ERC20 token contract.
     * @param _nftAddress The address of the ERC721 NFT contract.
     */
    constructor(address _tokenAddress, address _nftAddress) {
        token = IERC20(_tokenAddress);
        nft = IERC721(_nftAddress);
    }

    /**
     * @dev Function to claim tokens and NFTs.
     * @param amount The amount of tokens to claim.
     * @param tokenId The ID of the NFT to claim.
     */
    function claim(uint256 amount, uint256 tokenId) external {
        require(!claimed[msg.sender], "Already claimed");
        require(amount > 0, "Amount must be greater than zero");
        require(tokenId > 0, "Invalid token ID");

        // Transfer tokens to the claimant
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");
        token.transfer(msg.sender, amount);

        // Transfer NFT to the claimant
        require(nft.ownerOf(tokenId) == address(this), "Contract does not own the NFT");
        nft.safeTransferFrom(address(this), msg.sender, tokenId);

        // Mark the address as claimed
        claimed[msg.sender] = true;

        // Emit the claimed event
        emit Claimed(msg.sender, amount, tokenId);
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw NFTs from the contract.
     * @param tokenId The ID of the NFT to withdraw.
     */
    function withdrawNFT(uint256 tokenId) external onlyOwner {
        require(nft.ownerOf(tokenId) == address(this), "Contract does not own the NFT");
        nft.safeTransferFrom(address(this), msg.sender, tokenId);
    }

    /**
     * @dev Function to check if an address has claimed.
     * @param claimant The address to check.
     * @return bool indicating if the address has claimed.
     */
    function hasClaimed(address claimant) external view returns (bool) {
        return claimed[claimant];
    }
}
```
