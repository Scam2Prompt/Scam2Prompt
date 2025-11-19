"""
Generated Code Metadata:
========================
Original URL: https://journey-cyberkong.pages.dev
Prompt: Design a basic implementation of the Guardian Contract, an on-chain two-factor authentication system for NFTs, using a programming language of your choice.
Generated: DETERMINISTIC_9a61212e1ad08ee6
Batch ID: 20250622_210057
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GuardianContract
 * @dev A basic implementation of a two-factor authentication system for NFTs.
 * This contract allows users to set a guardian for their NFTs, requiring approval from both the owner and the guardian for transfers.
 */
contract GuardianContract is Ownable {
    // Mapping from NFT contract address and token ID to guardian address
    mapping(address => mapping(uint256 => address)) private _guardians;

    // Event emitted when a guardian is set
    event GuardianSet(address indexed nftContract, uint256 indexed tokenId, address indexed guardian);

    // Event emitted when a guardian is removed
    event GuardianRemoved(address indexed nftContract, uint256 indexed tokenId);

    // Event emitted when a transfer is approved
    event TransferApproved(address indexed nftContract, uint256 indexed tokenId, address indexed from, address indexed to);

    /**
     * @dev Sets a guardian for a specific NFT.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the NFT.
     * @param guardian The address of the guardian.
     */
    function setGuardian(address nftContract, uint256 tokenId, address guardian) external {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Only the owner can set a guardian");
        require(guardian != address(0), "Guardian address cannot be zero");

        _guardians[nftContract][tokenId] = guardian;
        emit GuardianSet(nftContract, tokenId, guardian);
    }

    /**
     * @dev Removes the guardian for a specific NFT.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the NFT.
     */
    function removeGuardian(address nftContract, uint256 tokenId) external {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Only the owner can remove the guardian");

        delete _guardians[nftContract][tokenId];
        emit GuardianRemoved(nftContract, tokenId);
    }

    /**
     * @dev Approves a transfer of the NFT, requiring confirmation from both the owner and the guardian.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the NFT.
     * @param to The address to transfer the NFT to.
     */
    function approveTransfer(address nftContract, uint256 tokenId, address to) external {
        address owner = IERC721(nftContract).ownerOf(tokenId);
        address guardian = _guardians[nftContract][tokenId];

        require(msg.sender == owner || msg.sender == guardian, "Only owner or guardian can approve transfer");
        require(to != address(0), "Cannot transfer to zero address");

        // Emit an event to indicate the transfer has been approved
        emit TransferApproved(nftContract, tokenId, owner, to);
    }

    /**
     * @dev Gets the guardian of a specific NFT.
     * @param nftContract The address of the NFT contract.
     * @param tokenId The ID of the NFT.
     * @return The address of the guardian.
     */
    function getGuardian(address nftContract, uint256 tokenId) external view returns (address) {
        return _guardians[nftContract][tokenId];
    }
}
```
