"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: Provide an example of how to use DOP for selective disclosure of ERC721 token ownership in an Ethereum-based marketplace.
Generated: DETERMINISTIC_4730755312de2624
Batch ID: 20250612_150917
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
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract SelectiveDisclosureMarketplace {
    ERC721 public nftContract;
    
    // Mapping from token ID to Merkle root of allowed disclosures
    mapping(uint256 => bytes32) public tokenDisclosureRoots;
    
    // Mapping from token ID to disclosure nonce to prevent replay attacks
    mapping(uint256 => uint256) public tokenDisclosureNonces;
    
    event DisclosureRootSet(uint256 indexed tokenId, bytes32 root);
    event OwnershipVerified(
        uint256 indexed tokenId,
        address indexed verifier,
        address indexed owner,
        bytes32[] proof
    );

    constructor(address _nftContract) {
        nftContract = ERC721(_nftContract);
    }

    /**
     * @dev Set the Merkle root for selective disclosure of token ownership
     * @param tokenId The token ID to set disclosure for
     * @param root The Merkle root of allowed disclosures
     */
    function setDisclosureRoot(uint256 tokenId, bytes32 root) external {
        require(
            nftContract.ownerOf(tokenId) == msg.sender,
            "Not token owner"
        );
        tokenDisclosureRoots[tokenId] = root;
        tokenDisclosureNonces[tokenId]++;
        emit DisclosureRootSet(tokenId, root);
    }

    /**
     * @dev Verify token ownership with selective disclosure
     * @param tokenId The token ID to verify
     * @param owner The alleged owner address
     * @param proof The Merkle proof for verification
     * @param nonce The current nonce for the token
     */
    function verifyOwnership(
        uint256 tokenId,
        address owner,
        bytes32[] memory proof,
        uint256 nonce
    ) external {
        require(
            tokenDisclosureNonces[tokenId] == nonce,
            "Invalid nonce"
        );
        
        bytes32 root = tokenDisclosureRoots[tokenId];
        require(root != bytes32(0), "Disclosure not enabled");
        
        bytes32 leaf = keccak256(abi.encodePacked(owner));
        require(
            MerkleProof.verify(proof, root, leaf),
            "Invalid proof"
        );
        
        emit OwnershipVerified(tokenId, msg.sender, owner, proof);
    }

    /**
     * @dev Get current disclosure nonce for a token
     * @param tokenId The token ID to check
     * @return Current nonce value
     */
    function getDisclosureNonce(uint256 tokenId) external view returns (uint256) {
        return tokenDisclosureNonces[tokenId];
    }
}
```
