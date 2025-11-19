"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: How can I use Chainlink's Cross-Chain Interoperability Protocol (CCIP) to move data between different blockchains?
Generated: DETERMINISTIC_73c224e20f4b57d9
Batch ID: 20250612_160853
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

// Import Chainlink CCIP interface for cross-chain operations
import "@chainlink/contracts/src/v0.8/interfaces/CCIP.sol";

// Contract that demonstrates the use of Chainlink CCIP for cross-chain data transfer
contract CrossChainDataTransfer {
    
    // CCIP interface instance
    CCIP public ccip;

    // Event to emit the data transfer status
    event DataSent(address indexed recipient, string data);
    event DataReceived(address indexed sender, string data);

    // Constructor to initialize the CCIP interface
    constructor(address _ccipAddress) {
        // Set the CCIP interface address
        ccip = CCIP(_ccipAddress);
    }

    /**
     * @dev Sends data to a specified recipient on a different blockchain.
     * @param recipient The address of the recipient on the target blockchain.
     * @param data The data to send.
     */
    function sendData(address recipient, string memory data) external {
        // Prepare the data payload
        bytes memory payload = abi.encode(data);

        // Attempt to send data using CCIP
        try ccip.send(recipient, payload) {
            emit DataSent(recipient, data);
        } catch {
            revert("Failed to send data via CCIP.");
        }
    }

    /**
     * @dev Callback function that is called when data is received from another blockchain.
     * @param sender The address of the sender on the source blockchain.
     * @param data The received data.
     */
    function onDataReceived(address sender, bytes memory data) external {
        // Decode the received data
        string memory receivedData = abi.decode(data, (string));

        // Emit the event for data reception
        emit DataReceived(sender, receivedData);
    }
}
```

Note: Ensure that you replace `@chainlink/contracts/src/v0.8/interfaces/CCIP.sol` with the correct path to the Chainlink contracts library in your project, and deploy the contract to a network that supports Chainlink CCIP.
