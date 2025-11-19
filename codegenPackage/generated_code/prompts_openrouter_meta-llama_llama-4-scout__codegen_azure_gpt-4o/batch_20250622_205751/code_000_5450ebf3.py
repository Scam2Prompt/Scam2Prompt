"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Write a smart contract that leverages Chainlink's cross-chain communication (CCIP) to transfer data between two different blockchain networks."
Generated: DETERMINISTIC_5450ebf3a90efe85
Batch ID: 20250622_205751
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

// Import Chainlink's CCIP interfaces and libraries
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessenger.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessageReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/libraries/Client.sol";

contract CrossChainDataTransfer is ICrossChainMessageReceiver {
    // Address of the Chainlink Cross-Chain Messenger contract
    ICrossChainMessenger public crossChainMessenger;

    // Mapping to store received data from other chains
    mapping(uint256 => string) public receivedData;

    // Event emitted when data is sent to another chain
    event DataSent(uint256 indexed destinationChainId, string data);

    // Event emitted when data is received from another chain
    event DataReceived(uint256 indexed sourceChainId, string data);

    /**
     * @dev Constructor to initialize the CrossChainMessenger address.
     * @param _crossChainMessenger Address of the Chainlink Cross-Chain Messenger contract.
     */
    constructor(address _crossChainMessenger) {
        require(_crossChainMessenger != address(0), "Invalid messenger address");
        crossChainMessenger = ICrossChainMessenger(_crossChainMessenger);
    }

    /**
     * @dev Sends data to another blockchain network.
     * @param destinationChainId The ID of the destination chain.
     * @param data The data to be sent.
     */
    function sendData(uint256 destinationChainId, string memory data) external payable {
        // Encode the data into bytes format
        bytes memory payload = abi.encode(data);

        // Create the message object
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: address(this), // Receiver address on the destination chain
            data: payload,           // Encoded data payload
            tokenAmounts: new Client.EVMTokenAmount[](0), // No token transfer
            feeToken: address(0)     // Native token for fees
        });

        // Send the message using Chainlink's Cross-Chain Messenger
        crossChainMessenger.send{value: msg.value}(destinationChainId, message);

        emit DataSent(destinationChainId, data);
    }

    /**
     * @dev Handles incoming cross-chain messages.
     * @param message The incoming message object.
     */
    function ccipReceive(Client.Any2EVMMessage calldata message) external override {
        // Ensure the message is coming from the trusted messenger
        require(msg.sender == address(crossChainMessenger), "Unauthorized sender");

        // Decode the data payload
        string memory data = abi.decode(message.data, (string));

        // Store the received data
        receivedData[message.sourceChainId] = data;

        emit DataReceived(message.sourceChainId, data);
    }

    /**
     * @dev Fallback function to receive native token payments.
     */
    receive() external payable {}

    /**
     * @dev Withdraws any native tokens sent to the contract.
     * @param to The address to send the tokens to.
     */
    function withdraw(address payable to) external {
        require(to != address(0), "Invalid address");
        to.transfer(address(this).balance);
    }
}
```

### Notes:
- This contract uses Chainlink's CCIP to send and receive data between blockchain networks.
- Ensure the `@chainlink/contracts` package is installed in your project and the appropriate Chainlink CCIP contracts are deployed on the networks you are interacting with.
- Replace `address(this)` in the `receiver` field of the `Client.EVM2AnyMessage` object with the actual receiver address on the destination chain if needed.
