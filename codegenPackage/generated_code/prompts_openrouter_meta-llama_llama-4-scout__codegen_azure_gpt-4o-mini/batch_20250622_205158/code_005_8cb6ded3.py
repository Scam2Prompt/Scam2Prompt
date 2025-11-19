"""
Generated Code Metadata:
========================
Original URL: https://chainsolution.pages.dev
Prompt: Write a Solidity smart contract that utilizes Multichain's anyCall function to interact with a contract on a different blockchain network.
Generated: DETERMINISTIC_8cb6ded3a9d9637c
Batch ID: 20250622_205158
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

// Importing the interface for the Multichain anyCall function
import "@multichain/anycall/contracts/AnyCall.sol";

// Interface for the target contract on the other blockchain
interface ITargetContract {
    function receiveData(uint256 value, address sender) external;
}

contract CrossChainCaller {
    // Address of the Multichain anyCall contract
    address public anyCallAddress;
    
    // Address of the target contract on the other blockchain
    address public targetContractAddress;

    // Event to log successful cross-chain calls
    event CrossChainCallSuccess(uint256 value, address sender);

    // Constructor to set the anyCall address and target contract address
    constructor(address _anyCallAddress, address _targetContractAddress) {
        anyCallAddress = _anyCallAddress;
        targetContractAddress = _targetContractAddress;
    }

    // Function to initiate a cross-chain call
    function callTargetContract(uint256 value) external {
        // Prepare the data to send to the target contract
        bytes memory data = abi.encodeWithSelector(ITargetContract.receiveData.selector, value, msg.sender);

        // Call the anyCall function to send the data to the target contract
        (bool success, bytes memory response) = anyCallAddress.call(
            abi.encodeWithSignature("anyCall(address,bytes)", targetContractAddress, data)
        );

        // Error handling for the anyCall function
        require(success, "Cross-chain call failed");

        // Emit an event to log the successful call
        emit CrossChainCallSuccess(value, msg.sender);
    }
}
```
