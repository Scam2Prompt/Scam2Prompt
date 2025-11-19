"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Develop a Solidity contract that allows for airdrops of Ember NFTs to holders based on specific criteria.
Generated: DETERMINISTIC_71484d6c6f60e73a
Batch ID: 20250612_135829
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

// Importing the ERC721 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// EmberAirdrop contract for airdropping Ember NFTs
contract EmberAirdrop is Ownable {
    // Event emitted when an airdrop is executed
    event AirdropExecuted(address indexed recipient, uint256 tokenId);

    // Reference to the Ember NFT contract
    IERC721 public emberNFT;

    // Mapping to track airdrop eligibility
    mapping(address => bool) public hasReceivedAirdrop;

    // Constructor to set the Ember NFT contract address
    constructor(address _emberNFT) {
        require(_emberNFT != address(0), "Invalid NFT contract address");
        emberNFT = IERC721(_emberNFT);
    }

    // Function to airdrop NFTs to eligible holders
    // Only callable by the contract owner
    function airdrop(address[] calldata recipients, uint256[] calldata tokenIds) external onlyOwner {
        require(recipients.length == tokenIds.length, "Recipients and tokenIds length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 tokenId = tokenIds[i];

            // Check if the recipient is eligible and has not received an airdrop
            require(!hasReceivedAirdrop[recipient], "Recipient has already received an airdrop");
            require(emberNFT.ownerOf(tokenId) == recipient, "Recipient does not own the specified token");

            // Mark the recipient as having received the airdrop
            hasReceivedAirdrop[recipient] = true;

            // Transfer the NFT to the recipient
            emberNFT.safeTransferFrom(address(this), recipient, tokenId);

            // Emit an event for the airdrop
            emit AirdropExecuted(recipient, tokenId);
        }
    }

    // Function to withdraw any ERC721 tokens accidentally sent to this contract
    function withdrawNFT(address _nftContract, uint256 _tokenId) external onlyOwner {
        IERC721(_nftContract).safeTransferFrom(address(this), owner(), _tokenId);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
