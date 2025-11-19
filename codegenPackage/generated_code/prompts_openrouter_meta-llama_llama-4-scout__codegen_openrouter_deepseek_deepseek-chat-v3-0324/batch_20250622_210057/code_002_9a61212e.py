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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title GuardianContract
 * @dev Implements two-factor authentication for NFT transfers
 */
contract GuardianContract is ERC721, Ownable {
    using ECDSA for bytes32;

    // Struct to store guardian information
    struct Guardian {
        address guardianAddress;
        uint256 activationTimestamp;
        bool isActive;
    }

    // Mapping from token ID to guardian
    mapping(uint256 => Guardian) private _guardians;

    // Time delay before guardian can be changed (in seconds)
    uint256 public constant GUARDIAN_CHANGE_DELAY = 86400; // 24 hours

    // Events
    event GuardianSet(uint256 indexed tokenId, address indexed guardian);
    event GuardianRemoved(uint256 indexed tokenId);
    event TransferWithGuardianApproval(
        uint256 indexed tokenId,
        address indexed from,
        address indexed to
    );

    /**
     * @dev Constructor
     * @param name_ Name of the NFT
     * @param symbol_ Symbol of the NFT
     */
    constructor(string memory name_, string memory symbol_) ERC721(name_, symbol_) {}

    /**
     * @dev Sets a guardian for a specific token
     * @param tokenId The token ID to set guardian for
     * @param guardianAddress The address of the guardian
     */
    function setGuardian(uint256 tokenId, address guardianAddress) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not owner or approved");
        require(guardianAddress != address(0), "Invalid guardian address");
        require(guardianAddress != ownerOf(tokenId), "Owner cannot be guardian");

        _guardians[tokenId] = Guardian({
            guardianAddress: guardianAddress,
            activationTimestamp: block.timestamp,
            isActive: true
        });

        emit GuardianSet(tokenId, guardianAddress);
    }

    /**
     * @dev Removes guardian for a specific token
     * @param tokenId The token ID to remove guardian from
     */
    function removeGuardian(uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not owner or approved");
        require(_guardians[tokenId].isActive, "No active guardian");

        delete _guardians[tokenId];
        emit GuardianRemoved(tokenId);
    }

    /**
     * @dev Transfers token with guardian approval
     * @param from Current owner of the token
     * @param to Address to receive the token
     * @param tokenId Token ID to transfer
     * @param guardianSignature Signature from the guardian approving the transfer
     */
    function transferWithGuardianApproval(
        address from,
        address to,
        uint256 tokenId,
        bytes memory guardianSignature
    ) external {
        require(_exists(tokenId), "Token does not exist");
        require(_guardians[tokenId].isActive, "No active guardian");

        // Verify guardian signature
        bytes32 messageHash = keccak256(abi.encodePacked(from, to, tokenId));
        address signer = messageHash.toEthSignedMessageHash().recover(guardianSignature);
        require(signer == _guardians[tokenId].guardianAddress, "Invalid guardian signature");

        // Transfer the token
        _transfer(from, to, tokenId);
        emit TransferWithGuardianApproval(tokenId, from, to);
    }

    /**
     * @dev Override ERC721 transfer functions to require guardian approval
     */
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public virtual override {
        if (_guardians[tokenId].isActive) {
            revert("Guardian approval required - use transferWithGuardianApproval");
        }
        super.transferFrom(from, to, tokenId);
    }

    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes memory data
    ) public virtual override {
        if (_guardians[tokenId].isActive) {
            revert("Guardian approval required - use transferWithGuardianApproval");
        }
        super.safeTransferFrom(from, to, tokenId, data);
    }

    /**
     * @dev Gets guardian information for a token
     * @param tokenId The token ID to query
     * @return guardianAddress The guardian's address
     * @return activationTimestamp When the guardian was activated
     * @return isActive Whether the guardian is active
     */
    function getGuardian(uint256 tokenId)
        external
        view
        returns (
            address guardianAddress,
            uint256 activationTimestamp,
            bool isActive
        )
    {
        Guardian memory guardian = _guardians[tokenId];
        return (guardian.guardianAddress, guardian.activationTimestamp, guardian.isActive);
    }

    /**
     * @dev Checks if guardian change is allowed (after delay period)
     * @param tokenId The token ID to check
     * @return bool True if guardian can be changed
     */
    function canChangeGuardian(uint256 tokenId) external view returns (bool) {
        Guardian memory guardian = _guardians[tokenId];
        return
            guardian.isActive &&
            block.timestamp >= guardian.activationTimestamp + GUARDIAN_CHANGE_DELAY;
    }
}
```
