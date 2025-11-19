"""
Generated Code Metadata:
========================
Original URL: https://swiftcoinlive.web.app
Prompt: Implement a whitelist system for early access to minting on a decentralized platform, using blockchain-based authentication.
Generated: DETERMINISTIC_d3cacdb6312f48f9
Batch ID: 20250622_212712
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract WhitelistMinter is Ownable {
    bytes32 public merkleRoot;
    mapping(address => bool) public hasMinted;
    bool public mintingEnabled;

    event Minted(address indexed minter);
    event MerkleRootUpdated(bytes32 newMerkleRoot);
    event MintingToggled(bool enabled);

    constructor(bytes32 _merkleRoot) {
        merkleRoot = _merkleRoot;
        mintingEnabled = false;
    }

    /**
     * @dev Update the merkle root for whitelist verification
     * @param _merkleRoot The new merkle root to set
     */
    function updateMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
        emit MerkleRootUpdated(_merkleRoot);
    }

    /**
     * @dev Toggle minting on/off
     * @param _enabled Boolean indicating whether minting should be enabled
     */
    function toggleMinting(bool _enabled) external onlyOwner {
        mintingEnabled = _enabled;
        emit MintingToggled(_enabled);
    }

    /**
     * @dev Mint function for whitelisted addresses
     * @param proof Merkle proof to verify whitelist status
     */
    function mint(bytes32[] calldata proof) external {
        require(mintingEnabled, "Minting is not enabled");
        require(!hasMinted[msg.sender], "Address has already minted");
        
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(proof, merkleRoot, leaf),
            "Invalid proof - not whitelisted"
        );

        hasMinted[msg.sender] = true;
        emit Minted(msg.sender);
        
        // Add your minting logic here
    }

    /**
     * @dev Check if an address is whitelisted
     * @param account Address to check
     * @param proof Merkle proof for the address
     * @return bool Whether the address is whitelisted
     */
    function isWhitelisted(address account, bytes32[] calldata proof) public view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(account));
        return MerkleProof.verify(proof, merkleRoot, leaf);
    }
}
```
