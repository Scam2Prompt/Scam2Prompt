"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asdasdwer23wrt23r23r23.pages.dev
Prompt: Develop a smart contract for distributing GRAPECOIN tokens based on wallet verification and NFT ownership.
Generated: DETERMINISTIC_6e55e36194f308ec
Batch ID: 20250612_153517
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GrapeCoinToken
 * @dev ERC20 Token with distribution based on wallet verification and NFT ownership
 */
contract GrapeCoinToken is ERC20, Ownable {
    // Address of the NFT contract to verify ownership
    IERC721 public nftContract;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     * @param _nftContract Address of the NFT contract used for verification.
     */
    constructor(address _nftContract) ERC20("GrapeCoin", "GRAPE") {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Function to distribute tokens to eligible NFT owners.
     * @param recipients Array of addresses to whom tokens will be distributed.
     * @param tokenId ID of the NFT that must be owned to receive tokens.
     * @param amount Amount of tokens to distribute to each eligible recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256 tokenId, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < recipients.length; i++) {
            // Ensure the recipient owns the specified NFT
            require(nftContract.ownerOf(tokenId) == recipients[i], "Recipient does not own the NFT");
        }

        // Mint and distribute tokens to each recipient
        for (uint256 i = 0; i < recipients.length; i++) {
            _mint(recipients[i], amount);
            emit TokensDistributed(recipients[i], amount);
        }
    }

    /**
     * @dev Function to change the NFT contract address.
     * @param _nftContract New NFT contract address.
     */
    function setNftContract(address _nftContract) external onlyOwner {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }
}
```
