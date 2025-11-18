"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethermall.pages.dev
Prompt: Write a smart contract that supports EtherMail's "Email-as-a-Wallet" concept, enabling users to send and receive tokens or NFTs directly through their email address.
Generated: DETERMINISTIC_9f3ed219989a5120
Batch ID: 20250612_154321
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract EmailWallet is Ownable {
    // Mapping from email addresses to wallet addresses
    mapping(string => address) private emailToAddress;

    // Event emitted when a new email is registered
    event EmailRegistered(string email, address walletAddress);

    // Event emitted when tokens are sent
    event TokensSent(string fromEmail, string toEmail, uint256 amount);

    // Event emitted when an NFT is sent
    event NFTSent(string fromEmail, string toEmail, uint256 tokenId);

    // Register an email address to the sender's wallet address
    function registerEmail(string calldata email) external {
        require(emailToAddress[email] == address(0), "Email already registered");
        
        emailToAddress[email] = msg.sender;
        emit EmailRegistered(email, msg.sender);
    }

    // Send ERC20 tokens to an email address
    function sendTokens(string calldata recipientEmail, address tokenAddress, uint256 amount) external {
        require(emailToAddress[recipientEmail] != address(0), "Recipient email not registered");
        
        address recipient = emailToAddress[recipientEmail];
        
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        token.transferFrom(msg.sender, recipient, amount);
        emit TokensSent(getEmailByAddress(msg.sender), recipientEmail, amount);
    }

    // Send an ERC721 token to an email address
    function sendNFT(string calldata recipientEmail, address nftAddress, uint256 tokenId) external {
        require(emailToAddress[recipientEmail] != address(0), "Recipient email not registered");
        
        address recipient = emailToAddress[recipientEmail];
        
        IERC721 nft = IERC721(nftAddress);
        require(nft.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        nft.safeTransferFrom(msg.sender, recipient, tokenId);
        emit NFTSent(getEmailByAddress(msg.sender), recipientEmail, tokenId);
    }

    // Retrieve email associated with a wallet address
    function getEmailByAddress(address walletAddress) public view returns (string memory) {
        for (string memory email in emailToAddress) {
            if (emailToAddress[email] == walletAddress) {
                return email;
            }
        }
        revert("Email not found for this address");
    }

    // Check if an email is registered
    function isEmailRegistered(string calldata email) external view returns (bool) {
        return emailToAddress[email] != address(0);
    }
}
```
