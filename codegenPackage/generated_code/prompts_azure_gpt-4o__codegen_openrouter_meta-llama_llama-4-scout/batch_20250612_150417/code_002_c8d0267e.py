"""
Generated Code Metadata:
========================
Original URL: https://earodrame.finance
Prompt: Create a smart contract that interacts with the LayerEdge Network to anchor aggregated zk proofs to an L1 blockchain for immutable integrity.
Generated: DETERMINISTIC_c8d0267e931aafd8
Batch ID: 20250612_150417
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title LayerEdgeNetworkAnchor
 * @author [Your Name]
 * @notice A smart contract that interacts with the LayerEdge Network to anchor aggregated zk proofs to an L1 blockchain for immutable integrity.
 */
contract LayerEdgeNetworkAnchor {
    using SafeMath for uint256;

    // Mapping of aggregated zk proof hashes to their corresponding block numbers
    mapping(bytes32 => uint256) public proofHashes;

    // Event emitted when a new aggregated zk proof is anchored
    event ProofAnchored(bytes32 indexed proofHash, uint256 blockNumber);

    // Event emitted when a proof hash is already anchored
    event ProofAlreadyAnchored(bytes32 indexed proofHash);

    // Only the owner can anchor new proofs
    address public owner;

    /**
     * @dev Constructor
     */
    constructor() public {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Anchor an aggregated zk proof to the L1 blockchain
     * @param proofHash The hash of the aggregated zk proof
     */
    function anchorProof(bytes32 proofHash) public onlyOwner {
        // Check if the proof hash is already anchored
        require(proofHashes[proofHash] == 0, "Proof hash is already anchored");

        // Anchor the proof hash to the current block number
        proofHashes[proofHash] = block.number;

        // Emit the ProofAnchored event
        emit ProofAnchored(proofHash, block.number);
    }

    /**
     * @dev Check if a proof hash is anchored
     * @param proofHash The hash of the aggregated zk proof
     * @return bool True if the proof hash is anchored, false otherwise
     */
    function isProofAnchored(bytes32 proofHash) public view returns (bool) {
        return proofHashes[proofHash] != 0;
    }

    /**
     * @dev Get the block number of an anchored proof hash
     * @param proofHash The hash of the aggregated zk proof
     * @return uint256 The block number of the anchored proof hash
     */
    function getAnchoredBlockNumber(bytes32 proofHash) public view returns (uint256) {
        return proofHashes[proofHash];
    }

    /**
     * @dev Update the owner of the contract
     * @param newOwner The new owner address
     */
    function updateOwner(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
