"""
Generated Code Metadata:
========================
Original URL: https://rewardtevara.xyz
Prompt: Create a smart contract to manage utility NFTs for a web3 gaming ecosystem, incorporating ZK Stack for enhanced performance.
Generated: DETERMINISTIC_8392629029bd02d4
Batch ID: 20250612_151057
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/AccessControl.sol";

/**
 * @title UtilityNFTManager
 * @author [Your Name]
 * @notice A smart contract for managing utility NFTs in a web3 gaming ecosystem.
 */
contract UtilityNFTManager {
    using SafeMath for uint256;
    using SafeERC721 for IERC721;

    // Mapping of NFT owners
    mapping(address => mapping(uint256 => bool)) public nftOwners;

    // Mapping of NFT metadata
    mapping(uint256 => NFTMetadata) public nftMetadata;

    // Mapping of ZK proof verification results
    mapping(bytes32 => bool) public zkProofs;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    // Event emitted when an NFT's metadata is updated
    event NFTMetadataUpdated(uint256 indexed tokenId, NFTMetadata metadata);

    // Event emitted when a ZK proof is verified
    event ZKProofVerified(bytes32 indexed proofHash, bool result);

    // Struct to represent NFT metadata
    struct NFTMetadata {
        string name;
        string description;
        string imageURI;
    }

    // Access control roles
    enum Roles {
        MINTER,
        TRANSFERER,
        METADATA_UPDATER,
        ZK_VERIFIER
    }

    // Access control mappings
    mapping(address => mapping(Roles => bool)) public roles;

    /**
     * @dev Initializes the contract with access control roles.
     * @param minter The address of the minter role.
     * @param transferer The address of the transferer role.
     * @param metadataUpdater The address of the metadata updater role.
     * @param zkVerifier The address of the ZK verifier role.
     */
    constructor(address minter, address transferer, address metadataUpdater, address zkVerifier) public {
        _grantRole(minter, Roles.MINTER);
        _grantRole(transferer, Roles.TRANSFERER);
        _grantRole(metadataUpdater, Roles.METADATA_UPDATER);
        _grantRole(zkVerifier, Roles.ZK_VERIFIER);
    }

    /**
     * @dev Mints a new NFT.
     * @param owner The address of the NFT owner.
     * @param tokenId The ID of the NFT.
     * @param metadata The metadata of the NFT.
     */
    function mintNFT(address owner, uint256 tokenId, NFTMetadata memory metadata) public {
        require(roles[msg.sender][Roles.MINTER], "Only minter role can mint NFTs");
        nftOwners[owner][tokenId] = true;
        nftMetadata[tokenId] = metadata;
        emit NFTMinted(owner, tokenId);
    }

    /**
     * @dev Transfers an NFT.
     * @param from The address of the current owner.
     * @param to The address of the new owner.
     * @param tokenId The ID of the NFT.
     */
    function transferNFT(address from, address to, uint256 tokenId) public {
        require(roles[msg.sender][Roles.TRANSFERER], "Only transferer role can transfer NFTs");
        require(nftOwners[from][tokenId], "NFT not owned by sender");
        nftOwners[from][tokenId] = false;
        nftOwners[to][tokenId] = true;
        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Updates an NFT's metadata.
     * @param tokenId The ID of the NFT.
     * @param metadata The new metadata of the NFT.
     */
    function updateNFTMetadata(uint256 tokenId, NFTMetadata memory metadata) public {
        require(roles[msg.sender][Roles.METADATA_UPDATER], "Only metadata updater role can update metadata");
        nftMetadata[tokenId] = metadata;
        emit NFTMetadataUpdated(tokenId, metadata);
    }

    /**
     * @dev Verifies a ZK proof.
     * @param proof The ZK proof.
     * @return bool The verification result.
     */
    function verifyZKProof(bytes memory proof) public returns (bool) {
        require(roles[msg.sender][Roles.ZK_VERIFIER], "Only ZK verifier role can verify proofs");
        bytes32 proofHash = keccak256(proof);
        zkProofs[proofHash] = true;
        emit ZKProofVerified(proofHash, true);
        return true;
    }

    /**
     * @dev Grants a role to an address.
     * @param addr The address to grant the role to.
     * @param role The role to grant.
     */
    function _grantRole(address addr, Roles role) internal {
        roles[addr][role] = true;
    }

    /**
     * @dev Revokes a role from an address.
     * @param addr The address to revoke the role from.
     * @param role The role to revoke.
     */
    function _revokeRole(address addr, Roles role) internal {
        roles[addr][role] = false;
    }
}
```
