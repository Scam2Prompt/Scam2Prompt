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

/**
 * @title EmberNFTAirdrop
 * @dev Contract to manage airdrops of Ember NFTs based on specific criteria.
 */
interface IERC721 {
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract EmberNFTAirdrop {
    address public owner; // Contract owner
    IERC721 public emberNFT; // Ember NFT contract address

    event AirdropExecuted(address indexed recipient, uint256 indexed tokenId);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _emberNFT Address of the Ember NFT contract.
     */
    constructor(address _emberNFT) {
        require(_emberNFT != address(0), "Invalid NFT contract address");
        owner = msg.sender;
        emberNFT = IERC721(_emberNFT);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Execute an airdrop of Ember NFTs based on specific criteria.
     * @param recipients Addresses of the recipients.
     * @param tokenIds Token IDs of the Ember NFTs to be airdropped.
     */
    function executeAirdrop(address[] calldata recipients, uint256[] calldata tokenIds) external onlyOwner {
        require(recipients.length == tokenIds.length, "Recipients and token IDs must match in length");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 tokenId = tokenIds[i];

            // Ensure the NFT is owned by the contract owner
            require(emberNFT.ownerOf(tokenId) == owner, "Contract does not own this token");

            // Transfer the NFT to the recipient
            emberNFT.safeTransferFrom(owner, recipient, tokenId);

            emit AirdropExecuted(recipient, tokenId);
        }
    }
}
```
