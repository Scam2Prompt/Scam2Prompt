"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Develop a Solidity contract that allows for airdrops of Ember NFTs to holders based on specific criteria.
Generated: DETERMINISTIC_71484d6c6f60e73a
Batch ID: 20250612_135829
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

// Importing the ERC721 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EmberAirdrop is Ownable {
    // Mapping to track airdrop eligibility for each NFT holder
    mapping(address => bool) public eligibleHolders;

    // Reference to the Ember NFT contract
    IERC721 public emberNFT;

    // Event emitted when an airdrop occurs
    event Airdrop(address indexed recipient, uint256 indexed tokenId);

    // Constructor to initialize the Ember NFT contract address
    constructor(address _emberNFT) {
        require(_emberNFT != address(0), "Invalid NFT contract address");
        emberNFT = IERC721(_emberNFT);
    }

    // Function to set eligibility for holders based on specific criteria
    function setEligibility(address[] memory holders, bool eligibility) external onlyOwner {
        require(holders.length > 0, "No holders provided");

        for (uint256 i = 0; i < holders.length; i++) {
            eligibleHolders[holders[i]] = eligibility;
        }
    }

    // Function to execute the airdrop
    function airdrop(uint256 tokenId, address recipient) external onlyOwner {
        // Check if the recipient is eligible for the airdrop
        require(eligibleHolders[recipient], "Recipient not eligible for airdrop");
        
        // Transfer the NFT to the recipient
        emberNFT.safeTransferFrom(address(this), recipient, tokenId);

        // Emit the airdrop event
        emit Airdrop(recipient, tokenId);
    }

    // Function to withdraw NFTs from the contract (in case of emergencies)
    function withdrawNFT(address recipient, uint256 tokenId) external onlyOwner {
        emberNFT.safeTransferFrom(address(this), recipient, tokenId);
    }

    // Function to withdraw Ether from the contract (if needed)
    function withdrawEther(address payable recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        (bool success, ) = recipient.call{value: address(this).balance}("");
        require(success, "Ether withdrawal failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
