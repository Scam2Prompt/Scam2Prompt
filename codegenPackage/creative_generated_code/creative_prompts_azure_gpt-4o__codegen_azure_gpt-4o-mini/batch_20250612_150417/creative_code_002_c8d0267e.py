"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earodrame.finance
Prompt: Create a smart contract that interacts with the LayerEdge Network to anchor aggregated zk proofs to an L1 blockchain for immutable integrity.
Generated: DETERMINISTIC_c8d0267e931aafd8
Batch ID: 20250612_150417
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

// Importing required libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for LayerEdge Network interaction
interface ILayerEdge {
    function anchorProof(bytes32 proofHash) external returns (bool);
}

/**
 * @title ZKProofAnchor
 * @dev This contract anchors aggregated zero-knowledge proofs to an L1 blockchain.
 */
contract ZKProofAnchor is Ownable {
    using SafeMath for uint256;

    // Address of the LayerEdge network contract
    ILayerEdge public layerEdgeContract;

    // Event emitted when a ZK proof is anchored
    event ProofAnchored(bytes32 indexed proofHash, address indexed anchoredBy);

    /**
     * @dev Constructor to set the LayerEdge contract address.
     * @param _layerEdgeAddress Address of the LayerEdge contract.
     */
    constructor(address _layerEdgeAddress) {
        require(_layerEdgeAddress != address(0), "Invalid LayerEdge address");
        layerEdgeContract = ILayerEdge(_layerEdgeAddress);
    }

    /**
     * @dev Function to anchor a zero-knowledge proof.
     * @param proofHash The hash of the aggregated zk proof to be anchored.
     * @return success A boolean indicating success or failure.
     */
    function anchorZKProof(bytes32 proofHash) external onlyOwner returns (bool success) {
        // Ensure the proof hash is not zero
        require(proofHash != bytes32(0), "Invalid proof hash");

        // Call LayerEdge contract to anchor the proof
        success = layerEdgeContract.anchorProof(proofHash);
        require(success, "Failed to anchor proof");

        // Emit event upon successful anchoring
        emit ProofAnchored(proofHash, msg.sender);
    }

    /**
     * @dev Function to update the LayerEdge contract address.
     * @param newLayerEdgeAddress The new LayerEdge contract address.
     */
    function updateLayerEdgeAddress(address newLayerEdgeAddress) external onlyOwner {
        require(newLayerEdgeAddress != address(0), "Invalid LayerEdge address");
        layerEdgeContract = ILayerEdge(newLayerEdgeAddress);
    }
}
```
