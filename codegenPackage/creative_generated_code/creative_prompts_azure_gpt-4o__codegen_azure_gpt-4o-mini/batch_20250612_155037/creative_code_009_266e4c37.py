"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Create a Solidity contract that utilizes Hyperlane's permissionless interoperability feature to enable communication between multiple chains without requiring explicit permissions.
Generated: DETERMINISTIC_266e4c372593a4db
Batch ID: 20250612_155037
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

// Importing Hyperlane core contracts for interoperability
import "@hyperlane-xyz/core/contracts/interstate/interstate.sol";
import "@hyperlane-xyz/core/contracts/interstate/InterchainGasPaymaster.sol";

// Contract to demonstrate permissionless interoperability using Hyperlane
contract InteroperableContract is InterstateMessenger, InterchainGasPaymaster {
    // Mapping to store inter-chain data
    mapping(uint256 => string) public dataStore;

    // Event emitted when data is sent between chains
    event DataSent(uint256 indexed destinationChainId, string data);

    // Constructor to set the messenger and gas paymaster address
    constructor(address _messenger, address _gasPaymaster) 
        InterstateMessenger(_messenger) 
        InterchainGasPaymaster(_gasPaymaster) 
    {}

    // Function to send data to a different chain
    function sendData(uint256 destinationChainId, string memory data) public {
        // Emit event for tracking
        emit DataSent(destinationChainId, data);

        // Call the send function from the InterstateMessenger
        // Here we assume that the data is properly encoded
        bytes memory payload = abi.encode(data);
        send(destinationChainId, payload);
    }

    // Function to receive data from another chain
    function receiveData(bytes memory payload) external {
        // Decode the received data
        string memory receivedData = abi.decode(payload, (string));

        // Store the received data (for demonstration)
        uint256 currentChainId = getChainId();
        dataStore[currentChainId] = receivedData;

        // Optionally, emit an event for tracking received data
        emit DataReceived(currentChainId, receivedData);
    }

    // Event emitted when data is received from another chain
    event DataReceived(uint256 indexed sourceChainId, string data);

    // Function to get the current chain ID
    function getChainId() public view returns (uint256) {
        // Return the current chain ID
        return block.chainid;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    // Function to withdraw any accidentally sent Ether
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
