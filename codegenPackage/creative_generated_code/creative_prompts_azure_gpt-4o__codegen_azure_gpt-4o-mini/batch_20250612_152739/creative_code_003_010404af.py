"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acidmonkeysdrop.pages.dev
Prompt: Create a smart contract in Solidity to manage eligibility and claiming of Acid Labs NFTs based on wallet connections.
Generated: DETERMINISTIC_010404afa90d8c91
Batch ID: 20250612_152739
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

/**
 * @title AcidLabsNFTManager
 * @dev Smart contract to manage eligibility and claiming of Acid Labs NFTs
 */
contract AcidLabsNFTManager is Ownable {
    // Mapping to track eligible wallets
    mapping(address => bool) public eligibleWallets;
    
    // Reference to the NFT contract
    IERC721 public acidLabsNFT;

    // Event to emit when a wallet is marked eligible
    event WalletEligibilityUpdated(address indexed wallet, bool indexed isEligible);
    
    // Event to emit when an NFT is claimed
    event NFTClaimed(address indexed wallet, uint256 tokenId);

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _nftAddress Address of the Acid Labs NFT contract.
     */
    constructor(address _nftAddress) {
        require(_nftAddress != address(0), "NFT address cannot be zero");
        acidLabsNFT = IERC721(_nftAddress);
    }

    /**
     * @dev Function to mark a wallet as eligible or ineligible.
     * @param wallet The address of the wallet to update eligibility for.
     * @param isEligible Boolean indicating eligibility status.
     */
    function setWalletEligibility(address wallet, bool isEligible) external onlyOwner {
        eligibleWallets[wallet] = isEligible;
        emit WalletEligibilityUpdated(wallet, isEligible);
    }

    /**
     * @dev Function to claim an NFT if eligible.
     * @param tokenId The ID of the NFT to claim.
     */
    function claimNFT(uint256 tokenId) external {
        require(eligibleWallets[msg.sender], "Wallet not eligible to claim NFT");
        require(acidLabsNFT.ownerOf(tokenId) == address(this), "NFT not owned by contract");

        // Transfer the NFT to the caller
        acidLabsNFT.transferFrom(address(this), msg.sender, tokenId);
        
        emit NFTClaimed(msg.sender, tokenId);
    }

    /**
     * @dev Function to withdraw any accidentally sent ERC20 tokens.
     * @param tokenAddress The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= amount, "Insufficient token balance");

        token.transfer(owner(), amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
