"""
Generated Code Metadata:
========================
Original URL: https://zerion-bridge.vercel.app
Prompt: Generate an example of a smart contract that utilizes zkSync Bridge for Ethereum to zkSync transfers.
Generated: DETERMINISTIC_8b19fcce9316b640
Batch ID: 20250622_211435
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

// Importing the necessary interfaces for zkSync Bridge
import "@zksync/contracts/interfaces/IZkSync.sol";

contract ZkSyncBridgeExample {
    // Address of the zkSync contract
    IZkSync public zkSync;

    // Event emitted when funds are transferred to zkSync
    event FundsTransferred(address indexed sender, uint256 amount, uint256 indexed nonce);

    // Constructor to initialize the zkSync contract address
    constructor(address _zkSyncAddress) {
        require(_zkSyncAddress != address(0), "Invalid zkSync address");
        zkSync = IZkSync(_zkSyncAddress);
    }

    // Function to transfer Ether to zkSync
    function transferToZkSync() external payable {
        require(msg.value > 0, "Amount must be greater than zero");

        // Generate a nonce for the transaction
        uint256 nonce = zkSync.getNonce(msg.sender);

        // Transfer funds to zkSync
        (bool success, ) = address(zkSync).call{value: msg.value}(
            abi.encodeWithSignature("deposit(address,uint256,uint256)", msg.sender, msg.value, nonce)
        );

        // Check if the transfer was successful
        require(success, "Transfer to zkSync failed");

        // Emit an event for the transfer
        emit FundsTransferred(msg.sender, msg.value, nonce);
    }

    // Function to withdraw funds from zkSync back to Ethereum
    function withdrawFromZkSync(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Call the withdraw function on zkSync
        (bool success, ) = address(zkSync).call(
            abi.encodeWithSignature("withdraw(address,uint256)", msg.sender, amount)
        );

        // Check if the withdrawal was successful
        require(success, "Withdrawal from zkSync failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to check the balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
