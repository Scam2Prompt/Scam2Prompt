"""
Generated Code Metadata:
========================
Original URL: https://dappdroppage.pages.dev
Prompt: Write a simple smart contract in Solidity that could be used for a dApp drop scenario, incorporating unique features that might have been discussed on a dApp drop page.
Generated: DETERMINISTIC_6a1cfcb6129a81d0
Batch ID: 20250612_163934
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title dAppDropNFT
 * @dev A smart contract for distributing NFTs in a dApp drop scenario with:
 * - Whitelist via Merkle Proof
 * - Limited supply
 * - Claim tracking
 * - Admin minting capabilities
 */
contract dAppDropNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 1000;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Merkle root for whitelist verification
    bytes32 public merkleRoot;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Event emitted when a new NFT is minted
    event Minted(address indexed recipient, uint256 tokenId);

    /**
     * @dev Constructor initializes the NFT contract
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseURI_ Base URI for token metadata
     * @param merkleRoot_ Merkle root for whitelist verification
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseURI_,
        bytes32 merkleRoot_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseURI_;
        merkleRoot = merkleRoot_;
    }

    /**
     * @dev Allows whitelisted users to claim their NFT
     * @param merkleProof Proof to verify whitelist status
     */
    function claim(bytes32[] calldata merkleProof) external {
        require(totalSupply() < MAX_SUPPLY, "dAppDropNFT: Max supply reached");
        require(!hasClaimed[msg.sender], "dAppDropNFT: Already claimed");

        // Verify merkle proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "dAppDropNFT: Invalid proof"
        );

        // Mint NFT
        _mintNFT(msg.sender);
        hasClaimed[msg.sender] = true;
    }

    /**
     * @dev Admin function to mint NFTs
     * @param to Address to receive the NFT
     */
    function adminMint(address to) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "dAppDropNFT: Max supply reached");
        _mintNFT(to);
    }

    /**
     * @dev Internal function to mint NFTs
     * @param to Address to receive the NFT
     */
    function _mintNFT(address to) internal {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        emit Minted(to, tokenId);
    }

    /**
     * @dev Returns the total supply minted so far
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Sets the base URI for token metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets the merkle root for whitelist verification
     * @param newMerkleRoot New merkle root
     */
    function setMerkleRoot(bytes32 newMerkleRoot) external onlyOwner {
        merkleRoot = newMerkleRoot;
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
