"""
Generated Code Metadata:
========================
Original URL: https://web3-dapp.pages.dev
Prompt: Explain how to implement the anyCall feature in a smart contract for cross-chain transactions using Multichain.
Generated: DETERMINISTIC_0af1a15af530a9ec
Batch ID: 20250612_163500
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

// Importing the Multichain interface for cross-chain functionality
import "@multichain/multichain-sdk/contracts/IMultichain.sol";

contract CrossChainAnyCall {
    // Address of the Multichain contract
    IMultichain public multichain;

    // Event to log cross-chain calls
    event CrossChainCallExecuted(
        address indexed from,
        address indexed to,
        uint256 value,
        bytes data,
        uint256 chainId
    );

    // Constructor to set the Multichain contract address
    constructor(address _multichainAddress) {
        require(_multichainAddress != address(0), "Invalid Multichain address");
        multichain = IMultichain(_multichainAddress);
    }

    // Function to execute a cross-chain call
    function anyCall(
        address to,
        uint256 value,
        bytes calldata data,
        uint256 chainId
    ) external payable {
        // Ensure the value sent matches the value parameter
        require(msg.value == value, "Value mismatch");

        // Emit an event for logging purposes
        emit CrossChainCallExecuted(msg.sender, to, value, data, chainId);

        // Call the Multichain contract to execute the cross-chain transaction
        (bool success, ) = address(multichain).call{value: value}(
            abi.encodeWithSignature("anyCall(address,uint256,bytes,uint256)", to, value, data, chainId)
        );

        // Error handling for the cross-chain call
        require(success, "Cross-chain call failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw Ether from the contract
    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }
}
```
