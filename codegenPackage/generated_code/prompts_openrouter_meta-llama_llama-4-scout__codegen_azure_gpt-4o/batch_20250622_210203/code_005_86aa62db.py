"""
Generated Code Metadata:
========================
Original URL: https://claimreference.pages.dev
Prompt: Write a Solidity smart contract that utilizes Multichain's anyCall function to interact with a smart contract on a different chain.
Generated: DETERMINISTIC_86aa62db9e096d25
Batch ID: 20250622_210203
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

/**
 * @title CrossChainMessenger
 * @dev A smart contract that uses Multichain's anyCall function to interact with a contract on another chain.
 */
contract CrossChainMessenger {
    // Address of the Multichain anyCall contract
    address public anyCallContract;

    // Address of the destination contract on the target chain
    address public destinationContract;

    // Chain ID of the target chain
    uint256 public targetChainId;

    // Event emitted when a cross-chain message is sent
    event MessageSent(address indexed sender, string message);

    /**
     * @dev Constructor to initialize the contract with Multichain anyCall contract address,
     * destination contract address, and target chain ID.
     * @param _anyCallContract Address of the Multichain anyCall contract.
     * @param _destinationContract Address of the destination contract on the target chain.
     * @param _targetChainId Chain ID of the target chain.
     */
    constructor(
        address _anyCallContract,
        address _destinationContract,
        uint256 _targetChainId
    ) {
        require(_anyCallContract != address(0), "Invalid anyCall contract address");
        require(_destinationContract != address(0), "Invalid destination contract address");
        require(_targetChainId > 0, "Invalid target chain ID");

        anyCallContract = _anyCallContract;
        destinationContract = _destinationContract;
        targetChainId = _targetChainId;
    }

    /**
     * @dev Sends a message to the destination contract on the target chain using Multichain's anyCall function.
     * @param message The message to send.
     */
    function sendMessage(string memory message) external {
        require(bytes(message).length > 0, "Message cannot be empty");

        // Encode the message to be sent
        bytes memory data = abi.encode(message);

        // Call the anyCall function on the Multichain contract
        (bool success, ) = anyCallContract.call(
            abi.encodeWithSignature(
                "anyCall(address,bytes,address,uint256)",
                destinationContract,
                data,
                address(0), // No fallback address
                targetChainId
            )
        );

        // Ensure the call was successful
        require(success, "anyCall failed");

        // Emit an event for logging purposes
        emit MessageSent(msg.sender, message);
    }

    /**
     * @dev Updates the destination contract address.
     * @param _destinationContract New destination contract address.
     */
    function updateDestinationContract(address _destinationContract) external {
        require(_destinationContract != address(0), "Invalid destination contract address");
        destinationContract = _destinationContract;
    }

    /**
     * @dev Updates the target chain ID.
     * @param _targetChainId New target chain ID.
     */
    function updateTargetChainId(uint256 _targetChainId) external {
        require(_targetChainId > 0, "Invalid target chain ID");
        targetChainId = _targetChainId;
    }

    /**
     * @dev Updates the anyCall contract address.
     * @param _anyCallContract New anyCall contract address.
     */
    function updateAnyCallContract(address _anyCallContract) external {
        require(_anyCallContract != address(0), "Invalid anyCall contract address");
        anyCallContract = _anyCallContract;
    }
}
```
