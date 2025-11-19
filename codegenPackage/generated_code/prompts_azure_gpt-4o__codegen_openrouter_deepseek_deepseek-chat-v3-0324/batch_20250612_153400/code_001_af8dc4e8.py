"""
Generated Code Metadata:
========================
Original URL: https://omnigenesis.vercel.app
Prompt: Generate code for deploying a decentralized application (dApp) that leverages Omni Network's high-performance blockchain architecture to enable cross-rollup communication.
Generated: DETERMINISTIC_af8dc4e8780d5dc7
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossRollupMessenger
 * @dev A contract for enabling cross-rollup communication on Omni Network
 */
contract CrossRollupMessenger is Ownable, ReentrancyGuard {
    // Event emitted when a message is sent to another rollup
    event MessageSent(
        uint256 indexed destinationChainId,
        address indexed recipient,
        bytes message,
        uint256 fee
    );

    // Event emitted when a message is received from another rollup
    event MessageReceived(
        uint256 indexed sourceChainId,
        address indexed sender,
        bytes message
    );

    // Mapping to store message fees
    mapping(uint256 => uint256) public chainFee;

    // Address of the Omni Network's bridge contract
    address public omniBridge;

    // Modifier to check if the caller is the Omni bridge
    modifier onlyBridge() {
        require(msg.sender == omniBridge, "Caller is not the Omni bridge");
        _;
    }

    /**
     * @dev Constructor
     * @param _omniBridge Address of the Omni Network's bridge contract
     */
    constructor(address _omniBridge) {
        require(_omniBridge != address(0), "Invalid bridge address");
        omniBridge = _omniBridge;
    }

    /**
     * @dev Set the fee for sending messages to a specific chain
     * @param chainId The destination chain ID
     * @param fee The fee amount in wei
     */
    function setChainFee(uint256 chainId, uint256 fee) external onlyOwner {
        chainFee[chainId] = fee;
    }

    /**
     * @dev Send a message to another rollup
     * @param destinationChainId The destination chain ID
     * @param recipient The address of the recipient on the destination chain
     * @param message The message data to send
     */
    function sendMessage(
        uint256 destinationChainId,
        address recipient,
        bytes calldata message
    ) external payable nonReentrant {
        uint256 fee = chainFee[destinationChainId];
        require(msg.value >= fee, "Insufficient fee");
        
        // Refund excess fee
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value - fee);
        }

        emit MessageSent(destinationChainId, recipient, message, fee);
    }

    /**
     * @dev Receive a message from another rollup (called by Omni bridge)
     * @param sourceChainId The source chain ID
     * @param sender The address of the sender on the source chain
     * @param message The message data received
     */
    function receiveMessage(
        uint256 sourceChainId,
        address sender,
        bytes calldata message
    ) external onlyBridge {
        emit MessageReceived(sourceChainId, sender, message);
    }

    /**
     * @dev Withdraw collected fees
     * @param amount The amount to withdraw
     */
    function withdrawFees(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Update the Omni bridge address
     * @param newBridge The new bridge address
     */
    function updateOmniBridge(address newBridge) external onlyOwner {
        require(newBridge != address(0), "Invalid bridge address");
        omniBridge = newBridge;
    }
}
```

```javascript
// Frontend integration with ethers.js
import { ethers } from 'ethers';
import CrossRollupMessengerABI from './CrossRollupMessengerABI.json';

const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Contract address (replace with your deployed contract address)
const contractAddress = "0x123...abc";
const contract = new ethers.Contract(
  contractAddress,
  CrossRollupMessengerABI,
  signer
);

/**
 * Send a cross-rollup message
 * @param {number} destinationChainId - Destination chain ID
 * @param {string} recipient - Recipient address
 * @param {string} message - Message to send
 * @param {number} fee - Fee amount in wei
 */
async function sendCrossRollupMessage(destinationChainId, recipient, message, fee) {
  try {
    const tx = await contract.sendMessage(
      destinationChainId,
      recipient,
      ethers.utils.toUtf8Bytes(message),
      { value: fee }
    );
    await tx.wait();
    console.log("Message sent successfully");
  } catch (error) {
    console.error("Error sending message:", error);
  }
}

/**
 * Listen for incoming messages
 */
function listenForMessages() {
  contract.on("MessageReceived", (sourceChainId, sender, message, event) => {
    console.log(`New message from chain ${sourceChainId}:`);
    console.log(`Sender: ${sender}`);
    console.log(`Message: ${ethers.utils.toUtf8String(message)}`);
  });
}

// Initialize message listener when dApp loads
window.addEventListener('load', () => {
  listenForMessages();
});
```

```javascript
// Hardhat deployment script
const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  // Deploy CrossRollupMessenger
  const CrossRollupMessenger = await hre.ethers.getContractFactory("CrossRollupMessenger");
  const omniBridgeAddress = "0xOmniBridgeAddress"; // Replace with actual Omni bridge address
  
  const messenger = await CrossRollupMessenger.deploy(omniBridgeAddress);
  await messenger.deployed();

  console.log("CrossRollupMessenger deployed to:", messenger.address);

  // Set initial fees for known chains
  const chains = [
    { id: 1, fee: ethers.utils.parseEther("0.01") },   // Ethereum
    { id: 137, fee: ethers.utils.parseEther("0.005") }, // Polygon
    { id: 42161, fee: ethers.utils.parseEther("0.007") } // Arbitrum
  ];

  for (const chain of chains) {
    await messenger.setChainFee(chain.id, chain.fee);
    console.log(`Set fee for chain ${chain.id} to ${ethers.utils.formatEther(chain.fee)} ETH`);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```solidity
// Mock Omni Bridge for testing
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./CrossRollupMessenger.sol";

contract MockOmniBridge {
    CrossRollupMessenger public messenger;
    
    constructor(address _messenger) {
        messenger = CrossRollupMessenger(_messenger);
    }
    
    function relayMessage(
        uint256 sourceChainId,
        address sender,
        bytes calldata message
    ) external {
        messenger.receiveMessage(sourceChainId, sender, message);
    }
}
```

```javascript
// Test script using Hardhat
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CrossRollupMessenger", function () {
  let messenger;
  let mockBridge;
  let owner, user;

  beforeEach(async function () {
    [owner, user] = await ethers.getSigners();
    
    const CrossRollupMessenger = await ethers.getContractFactory("CrossRollupMessenger");
    messenger = await CrossRollupMessenger.deploy(owner.address);
    await messenger.deployed();

    const MockOmniBridge = await ethers.getContractFactory("MockOmniBridge");
    mockBridge = await MockOmniBridge.deploy(messenger.address);
    await mockBridge.deployed();

    await messenger.updateOmniBridge(mockBridge.address);
  });

  it("Should set and get chain fee correctly", async function () {
    const chainId = 1;
    const fee = ethers.utils.parseEther("0.01");
    
    await messenger.setChainFee(chainId, fee);
    expect(await messenger.chainFee(chainId)).to.equal(fee);
  });

  it("Should emit MessageSent event", async function () {
    const chainId = 1;
    const fee = ethers.utils.parseEther("0.01");
    await messenger.setChainFee(chainId, fee);
    
    const recipient = user.address;
    const message = "Hello cross-rollup!";
    
    await expect(messenger.sendMessage(
      chainId,
      recipient,
      ethers.utils.toUtf8Bytes(message),
      { value: fee }
    ))
