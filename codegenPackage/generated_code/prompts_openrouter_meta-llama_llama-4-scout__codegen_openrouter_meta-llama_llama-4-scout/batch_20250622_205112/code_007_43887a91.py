"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Write a code snippet for sending messages across blockchains using LayerZero's OAppSender and OAppReceiver contracts.
Generated: DETERMINISTIC_43887a91c17f1ce3
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('hardhat');
const { LayerZero } = require('@layerzerolabs/lz-contracts');

// Define OAppSender contract
async function deployOAppSender() {
  // Deploy OAppSender contract
  const OAppSender = await ethers.getContractFactory('OAppSender');
  const oAppSender = await OAppSender.deploy();

  // Wait for deployment to complete
  await oAppSender.deployed();

  return oAppSender;
}

// Define OAppReceiver contract
async function deployOAppReceiver() {
  // Deploy OAppReceiver contract
  const OAppReceiver = await ethers.getContractFactory('OAppReceiver');
  const oAppReceiver = await OAppReceiver.deploy();

  // Wait for deployment to complete
  await oAppReceiver.deployed();

  return oAppReceiver;
}

// Define function to send message across blockchains
async function sendMessageAcrossBlockchains(
  oAppSender,
  oAppReceiverAddress,
  dstChainId,
  message
) {
  try {
    // Get LayerZero endpoint
    const endpoint = await oAppSender.endpoint();

    // Send message
    const tx = await oAppSender.send(
      dstChainId,
      oAppReceiverAddress,
      ethers.utils.arrayify(message)
    );

    // Wait for transaction to complete
    await tx.wait();

    console.log(`Message sent: ${message}`);
  } catch (error) {
    console.error('Error sending message:', error);
  }
}

// Define main function
async function main() {
  // Deploy OAppSender and OAppReceiver contracts
  const oAppSender = await deployOAppSender();
  const oAppReceiver = await deployOAppReceiver();

  // Set OAppReceiver address
  const oAppReceiverAddress = oAppReceiver.address;

  // Define destination chain ID
  const dstChainId = 2; // Replace with actual destination chain ID

  // Define message to send
  const message = 'Hello, world!';

  // Send message across blockchains
  await sendMessageAcrossBlockchains(
    oAppSender,
    oAppReceiverAddress,
    dstChainId,
    message
  );
}

// Run main function
main().catch((error) => {
  console.error('Error:', error);
  process.exitCode = 1;
});
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@layerzerolabs/lz-contracts/contracts/OAppSender.sol";
import "@layerzerolabs/lz-contracts/contracts/OAppReceiver.sol";

// Define OAppSender contract
contract OAppSender is OAppSender {
  // Define constructor
  constructor(address _endpoint) OAppSender(_endpoint) {}

  // Define send function
  function send(
    uint256 _dstChainId,
    address _oappReceiver,
    bytes calldata _payload
  ) external payable {
    // Send message
    _send(_dstChainId, _oappReceiver, _payload, payable(msg.sender));
  }
}

// Define OAppReceiver contract
contract OAppReceiver is OAppReceiver {
  // Define constructor
  constructor() {}

  // Define execute function
  function execute(
    uint256 _srcChainId,
    address _srcAddress,
    bytes calldata _payload
  ) external {
    // Execute message
    _execute(_srcChainId, _srcAddress, _payload);
  }
}
```
