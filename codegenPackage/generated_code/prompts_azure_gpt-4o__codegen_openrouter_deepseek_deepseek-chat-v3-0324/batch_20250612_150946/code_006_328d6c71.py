"""
Generated Code Metadata:
========================
Original URL: https://bankless.pages.dev
Prompt: Create a smart contract in Solidity that verifies if a Base, Introduced NFT is eligible for $BASED token redemption and checks if the NFT is still in the same wallet after redemption.
Generated: DETERMINISTIC_328d6c71809eea99
Batch ID: 20250612_150946
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

contract BasedTokenRedemption is Ownable {
    IERC721 public nftContract;
    IERC20 public basedToken;
    
    // Mapping to track redeemed NFTs
    mapping(uint256 => bool) public isRedeemed;
    
    // Event emitted when NFT is redeemed
    event NFTRedeemed(address indexed user, uint256 tokenId, uint256 amount);
    
    /**
     * @dev Constructor to initialize the contract
     * @param _nftContract Address of the NFT contract
     * @param _basedToken Address of the $BASED token contract
     */
    constructor(address _nftContract, address _basedToken) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_basedToken != address(0), "Invalid token contract address");
        
        nftContract = IERC721(_nftContract);
        basedToken = IERC20(_basedToken);
    }
    
    /**
     * @dev Check if NFT is eligible for redemption
     * @param tokenId The NFT token ID to check
     * @return bool True if eligible, false otherwise
     */
    function isEligibleForRedemption(uint256 tokenId) public view returns (bool) {
        // Check if NFT exists and hasn't been redeemed yet
        try nftContract.ownerOf(tokenId) returns (address owner) {
            return !isRedeemed[tokenId] && owner != address(0);
        } catch {
            return false;
        }
    }
    
    /**
     * @dev Redeem NFT for $BASED tokens
     * @param tokenId The NFT token ID to redeem
     * @param amount The amount of $BASED tokens to redeem
     */
    function redeemNFT(uint256 tokenId, uint256 amount) external {
        require(isEligibleForRedemption(tokenId), "NFT not eligible for redemption");
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not NFT owner");
        require(amount > 0, "Amount must be greater than 0");
        
        // Mark NFT as redeemed
        isRedeemed[tokenId] = true;
        
        // Transfer $BASED tokens to the caller
        require(basedToken.transfer(msg.sender, amount), "Token transfer failed");
        
        emit NFTRedeemed(msg.sender, tokenId, amount);
    }
    
    /**
     * @dev Verify if NFT is still in the same wallet after redemption
     * @param tokenId The NFT token ID to verify
     * @param expectedOwner The expected owner address
     * @return bool True if still owned by expected owner, false otherwise
     */
    function verifyOwnershipAfterRedemption(uint256 tokenId, address expectedOwner) external view returns (bool) {
        try nftContract.ownerOf(tokenId) returns (address owner) {
            return owner == expectedOwner;
        } catch {
            return false;
        }
    }
    
    /**
     * @dev Withdraw any accidentally sent ERC20 tokens
     * @param token Address of the token contract
     * @param amount Amount to withdraw
     */
    function withdrawERC20(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(IERC20(token).transfer(owner(), amount), "Withdrawal failed");
    }
}
```
