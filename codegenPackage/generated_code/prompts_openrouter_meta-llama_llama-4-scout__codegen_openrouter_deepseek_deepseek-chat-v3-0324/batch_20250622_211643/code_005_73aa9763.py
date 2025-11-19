"""
Generated Code Metadata:
========================
Original URL: https://mimnzm-main.pages.dev
Prompt: Design a smart contract that utilizes Multichain's cross-chain bridging and smart contract methods on other chains, and write a code snippet to deploy and interact with the contract.
Generated: DETERMINISTIC_73aa9763c4e2db9d
Batch ID: 20250622_211643
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
 * @title CrossChainBridge
 * @dev A smart contract that facilitates cross-chain token transfers using Multichain's bridge
 */
contract CrossChainBridge is Ownable, ReentrancyGuard {
    // Mapping to store supported tokens and their corresponding bridge addresses
    mapping(address => address) public tokenToBridge;

    // Event emitted when a cross-chain transfer is initiated
    event CrossChainTransferInitiated(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 targetChainId,
        address recipient
    );

    // Event emitted when a token is added/updated in the bridge
    event TokenBridgeUpdated(address indexed token, address indexed bridge);

    /**
     * @dev Add or update a token and its bridge address
     * @param token Address of the token to be bridged
     * @param bridge Address of the bridge contract for the token
     */
    function setTokenBridge(address token, address bridge) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(bridge != address(0), "Invalid bridge address");

        tokenToBridge[token] = bridge;
        emit TokenBridgeUpdated(token, bridge);
    }

    /**
     * @dev Initiate a cross-chain transfer
     * @param token Address of the token to transfer
     * @param amount Amount of tokens to transfer
     * @param targetChainId Chain ID of the destination chain
     * @param recipient Address of the recipient on the target chain
     */
    function transferCrossChain(
        address token,
        uint256 amount,
        uint256 targetChainId,
        address recipient
    ) external nonReentrant {
        require(tokenToBridge[token] != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        IERC20 tokenContract = IERC20(token);
        address bridgeAddress = tokenToBridge[token];

        // Transfer tokens from sender to this contract
        tokenContract.transferFrom(msg.sender, address(this), amount);

        // Approve bridge to spend tokens
        tokenContract.approve(bridgeAddress, amount);

        // Call the bridge contract's method to initiate cross-chain transfer
        // Note: The exact method signature may vary based on the bridge implementation
        (bool success, ) = bridgeAddress.call(
            abi.encodeWithSignature(
                "swapOut(uint256,uint256,address)",
                amount,
                targetChainId,
                recipient
            )
        );
        require(success, "Bridge transfer failed");

        emit CrossChainTransferInitiated(
            msg.sender,
            token,
            amount,
            targetChainId,
            recipient
        );
    }

    /**
     * @dev Emergency withdraw tokens from the contract
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```

```javascript
// Deployment and interaction script (using ethers.js)
const { ethers } = require("ethers");
const CrossChainBridgeArtifact = require("./artifacts/contracts/CrossChainBridge.sol/CrossChainBridge.json");

async function deployAndInteract() {
    // Initialize provider and signer
    const provider = new ethers.providers.JsonRpcProvider("YOUR_RPC_URL");
    const signer = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

    // Deploy contract
    const CrossChainBridgeFactory = new ethers.ContractFactory(
        CrossChainBridgeArtifact.abi,
        CrossChainBridgeArtifact.bytecode,
        signer
    );
    const crossChainBridge = await CrossChainBridgeFactory.deploy();
    await crossChainBridge.deployed();
    console.log("Contract deployed at:", crossChainBridge.address);

    // Set token bridge (example with dummy addresses)
    const tokenAddress = "0xTOKEN_ADDRESS";
    const bridgeAddress = "0xBRIDGE_ADDRESS";
    await crossChainBridge.setTokenBridge(tokenAddress, bridgeAddress);
    console.log("Token bridge set");

    // Example cross-chain transfer
    const amount = ethers.utils.parseUnits("100", 18); // 100 tokens
    const targetChainId = 56; // BSC chain ID
    const recipient = "0xRECIPIENT_ADDRESS";

    // Approve token transfer first (if needed)
    const tokenContract = new ethers.Contract(
        tokenAddress,
        ["function approve(address,uint256)"],
        signer
    );
    await tokenContract.approve(crossChainBridge.address, amount);

    // Initiate transfer
    const tx = await crossChainBridge.transferCrossChain(
        tokenAddress,
        amount,
        targetChainId,
        recipient
    );
    await tx.wait();
    console.log("Cross-chain transfer initiated");
}

deployAndInteract().catch(console.error);
```
