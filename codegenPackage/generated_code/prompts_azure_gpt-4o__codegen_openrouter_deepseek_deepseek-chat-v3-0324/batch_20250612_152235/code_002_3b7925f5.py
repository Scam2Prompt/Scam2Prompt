"""
Generated Code Metadata:
========================
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: Generate code to validate off-chain bridge inputs using EigenLayer's light node bridge mechanism and handle slashing in case of incorrect inputs.
Generated: DETERMINISTIC_3b7925f51e7ae145
Batch ID: 20250612_152235
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

interface IEigenLayerLightNode {
    function verifyStateCommitment(
        bytes32 stateRoot,
        bytes32[] calldata proof,
        bytes32 leaf
    ) external view returns (bool);
}

contract BridgeValidator is Ownable {
    IEigenLayerLightNode public lightNode;
    uint256 public slashAmount;
    mapping(address => bool) public isOperator;
    mapping(bytes32 => bool) public processedMessages;

    event MessageProcessed(bytes32 indexed messageHash);
    event OperatorSlashed(address indexed operator, uint256 amount);
    event OperatorAdded(address indexed operator);
    event OperatorRemoved(address indexed operator);

    constructor(address _lightNode, uint256 _slashAmount) {
        require(_lightNode != address(0), "Invalid light node address");
        lightNode = IEigenLayerLightNode(_lightNode);
        slashAmount = _slashAmount;
    }

    modifier onlyOperator() {
        require(isOperator[msg.sender], "Not an operator");
        _;
    }

    function addOperator(address _operator) external onlyOwner {
        require(_operator != address(0), "Invalid operator address");
        require(!isOperator[_operator], "Already an operator");
        isOperator[_operator] = true;
        emit OperatorAdded(_operator);
    }

    function removeOperator(address _operator) external onlyOwner {
        require(isOperator[_operator], "Not an operator");
        isOperator[_operator] = false;
        emit OperatorRemoved(_operator);
    }

    function updateSlashAmount(uint256 _slashAmount) external onlyOwner {
        slashAmount = _slashAmount;
    }

    function validateAndProcessMessage(
        bytes32 messageHash,
        bytes32 stateRoot,
        bytes32[] calldata proof
    ) external onlyOperator {
        require(!processedMessages[messageHash], "Message already processed");
        require(
            lightNode.verifyStateCommitment(stateRoot, proof, messageHash),
            "Invalid state commitment proof"
        );

        processedMessages[messageHash] = true;
        emit MessageProcessed(messageHash);
    }

    function slashOperator(address _operator, bytes32 invalidMessageHash) external {
        require(isOperator[_operator], "Not an operator");
        require(processedMessages[invalidMessageHash], "Message not processed");

        // In a real implementation, this would interact with EigenLayer's slashing mechanism
        // For demonstration, we just emit an event and mark the operator as slashed
        isOperator[_operator] = false;
        emit OperatorSlashed(_operator, slashAmount);
    }

    function isMessageProcessed(bytes32 messageHash) external view returns (bool) {
        return processedMessages[messageHash];
    }
}
```
