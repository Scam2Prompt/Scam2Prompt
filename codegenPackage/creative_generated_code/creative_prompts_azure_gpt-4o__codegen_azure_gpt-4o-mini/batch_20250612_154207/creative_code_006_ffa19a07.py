"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupnft.com
Prompt: Develop a smart contract that facilitates the redemption of NFT vouchers for JUP tokens, ensuring compatibility with the JupNFT platform.
Generated: DETERMINISTIC_ffa19a07f804d7ac
Batch ID: 20250612_154207
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

// Import necessary OpenZeppelin contracts and interfaces
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the JUP token
interface IJUPToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Smart contract for NFT voucher redemption
contract NFTVoucherRedemption is Ownable {
    // Instance of the JUP token
    IJUPToken public jupToken;
    
    // Mapping to track redeemed vouchers
    mapping(address => mapping(uint256 => bool)) public redeemedVouchers;

    // Event to log voucher redemption
    event VoucherRedeemed(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Constructor to set the JUP token address
    constructor(address _jupToken) {
        require(_jupToken != address(0), "Invalid JUP token address");
        jupToken = IJUPToken(_jupToken);
    }

    // Function to redeem an NFT voucher for JUP tokens
    function redeemVoucher(address nftContract, uint256 tokenId) external {
        // Ensure the NFT contract is valid
        require(nftContract != address(0), "Invalid NFT contract address");
        
        // Check if the sender is the owner of the NFT
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Ensure the voucher has not already been redeemed
        require(!redeemedVouchers[msg.sender][tokenId], "Voucher has already been redeemed");

        // Retrieve the amount of JUP tokens to mint (for demonstration purposes, we mint a fixed amount)
        uint256 amountToMint = 100 * 10 ** 18; // Assuming JUP has 18 decimals

        // Mint JUP tokens to the user
        jupToken.mint(msg.sender, amountToMint);

        // Mark the voucher as redeemed
        redeemedVouchers[msg.sender][tokenId] = true;

        // Emit an event for the redemption
        emit VoucherRedeemed(msg.sender, tokenId, amountToMint);
    }

    // Function to update the JUP token address (only by owner)
    function updateJUPToken(address newJupToken) external onlyOwner {
        require(newJupToken != address(0), "Invalid JUP token address");
        jupToken = IJUPToken(newJupToken);
    }
}
```
