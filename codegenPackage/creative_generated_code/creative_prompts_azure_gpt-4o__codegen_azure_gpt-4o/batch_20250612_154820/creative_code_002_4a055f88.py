"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-orbiter.net
Prompt: Generate Solidity code for a non-custodial smart contract that facilitates secure asset transfers across Ethereum Layer 2 networks, inspired by Orbiter Finance's bridging mechanics.
Generated: DETERMINISTIC_4a055f8816890482
Batch ID: 20250612_154820
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

/**
 * @title NonCustodialBridge
 * @notice Facilitates secure asset transfers across Ethereum Layer 2 networks
 * @dev This contract is inspired by Orbiter Finance's bridging mechanics. It operates completely non-custodially.
 */
contract NonCustodialBridge {
    // Event emitted when a transfer is initiated
    event TransferInitiated(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 timestamp,
        string targetNetwork
    );

    // Event emitted when a transfer is completed
    event TransferCompleted(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 timestamp
    );

    // Struct representing a transfer request
    struct TransferRequest {
        address sender;
        address recipient;
        uint256 amount;
        string targetNetwork;
        bool completed;
    }

    // Mapping to store all transfer requests
    mapping(bytes32 => TransferRequest) public transferRequests;

    /**
     * @dev Initiates a transfer request to another Layer 2 network.
     * @param recipient Address of the recipient on the target network.
     * @param amount Amount of Ether to transfer.
     * @param targetNetwork Identifier of the target Layer 2 network (e.g., "Arbitrum", "Optimism").
     */
    function initiateTransfer(
        address recipient,
        uint256 amount,
        string memory targetNetwork
    ) public payable {
        require(msg.value == amount, "Amount mismatch with sent Ether");
        require(recipient != address(0), "Invalid recipient address");
        require(bytes(targetNetwork).length > 0, "Target network must be specified");

        // Generate a unique hash for the transfer request
        bytes32 transferId = keccak256(
            abi.encodePacked(msg.sender, recipient, amount, targetNetwork, block.timestamp)
        );
        require(transferRequests[transferId].amount == 0, "Transfer already exists");

        // Create and store the transfer request
        transferRequests[transferId] = TransferRequest({
            sender: msg.sender,
            recipient: recipient,
            amount: amount,
            targetNetwork: targetNetwork,
            completed: false
        });

        emit TransferInitiated(msg.sender, recipient, amount, block.timestamp, targetNetwork);
    }

    /**
     * @dev Completes a transfer request on the source network.
     * @param transferId Identifier of the transfer request.
     */
    function completeTransfer(bytes32 transferId) public {
        TransferRequest storage request = transferRequests[transferId];
        require(request.amount > 0, "Transfer does not exist");
        require(!request.completed, "Transfer already completed");
        require(request.recipient == msg.sender, "Only recipient can complete the transfer");

        // Mark transfer as completed
        request.completed = true;

        // Transfer the Ether to the recipient
        payable(request.recipient).transfer(request.amount);

        emit TransferCompleted(request.sender, request.recipient, request.amount, block.timestamp);
    }

    /**
     * @dev Fallback function to handle plain Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    fallback() external payable {
        revert("Fallback function called");
    }
}
```
