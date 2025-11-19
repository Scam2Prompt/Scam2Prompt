"""
Generated Code Metadata:
========================
Original URL: https://dop-io.web.app
Prompt: Write a smart contract example using the Data Ownership Protocol (DOP) to selectively disclose ERC20 token holdings while maintaining privacy for other assets.
Generated: DETERMINISTIC_4c2e3163ef95d776
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title SelectiveDisclosureERC20
 * @dev A smart contract implementing the Data Ownership Protocol (DOP) for selective disclosure
 * of ERC20 token holdings while maintaining privacy for other assets.
 */
contract SelectiveDisclosureERC20 {
    // Merkle root of all token balances (address => token => balance)
    bytes32 public merkleRoot;
    
    // Mapping to track which disclosures have been used to prevent replay attacks
    mapping(bytes32 => bool) public usedDisclosures;

    // Event emitted when a user discloses their token balance
    event BalanceDisclosed(
        address indexed account,
        address indexed token,
        uint256 balance,
        bytes32 disclosureId
    );

    /**
     * @dev Sets the initial merkle root
     * @param _merkleRoot The root of the merkle tree containing all token balances
     */
    constructor(bytes32 _merkleRoot) {
        merkleRoot = _merkleRoot;
    }

    /**
     * @dev Updates the merkle root (only callable by owner in production)
     * @param _newMerkleRoot The new merkle root
     */
    function updateMerkleRoot(bytes32 _newMerkleRoot) external {
        // In production, add onlyOwner modifier
        merkleRoot = _newMerkleRoot;
    }

    /**
     * @dev Discloses a specific ERC20 token balance while keeping others private
     * @param token The ERC20 token address to disclose
     * @param balance The balance to disclose
     * @param proof The merkle proof verifying the balance
     * @param disclosureId A unique identifier for this disclosure to prevent replay
     */
    function discloseBalance(
        address token,
        uint256 balance,
        bytes32[] calldata proof,
        bytes32 disclosureId
    ) external {
        require(!usedDisclosures[disclosureId], "Disclosure already used");
        
        // Verify the proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, token, balance));
        require(
            MerkleProof.verify(proof, merkleRoot, leaf),
            "Invalid merkle proof"
        );

        // Mark this disclosure as used
        usedDisclosures[disclosureId] = true;

        // Emit the disclosure event
        emit BalanceDisclosed(msg.sender, token, balance, disclosureId);
    }

    /**
     * @dev Verifies a disclosed balance without emitting an event
     * @param account The account whose balance is being verified
     * @param token The ERC20 token address
     * @param balance The balance to verify
     * @param proof The merkle proof verifying the balance
     * @return bool True if the proof is valid
     */
    function verifyDisclosedBalance(
        address account,
        address token,
        uint256 balance,
        bytes32[] calldata proof
    ) external view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(account, token, balance));
        return MerkleProof.verify(proof, merkleRoot, leaf);
    }
}
```
