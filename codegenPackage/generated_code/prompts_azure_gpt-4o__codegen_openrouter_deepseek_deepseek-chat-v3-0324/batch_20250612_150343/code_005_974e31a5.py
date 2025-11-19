"""
Generated Code Metadata:
========================
Original URL: https://taiko-46v.pages.dev
Prompt: Write a tutorial for developers to integrate Taiko's ZK-EVM into an existing Ethereum-based dApp, ensuring compatibility with its decentralized infrastructure.
Generated: DETERMINISTIC_974e31a507bc9086
Batch ID: 20250612_150343
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

// Import Taiko's ZK-EVM interface
interface ITaikoZkEvm {
    function verifyProof(
        bytes32[] calldata proof,
        bytes32[] calldata publicInputs
    ) external returns (bool);
    
    function submitBlock(
        bytes32 blockHash,
        bytes32 stateRoot,
        bytes calldata transactions
    ) external;
}

contract TaikoZkEvmIntegration {
    ITaikoZkEvm public taikoZkEvm;
    address public owner;
    
    // Events for tracking important actions
    event ProofVerified(bool success);
    event BlockSubmitted(bytes32 blockHash);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Error messages
    error OnlyOwner();
    error ProofVerificationFailed();
    error InvalidTaikoAddress();
    
    /**
     * @dev Constructor that initializes the Taiko ZK-EVM contract address
     * @param _taikoZkEvmAddress The address of the Taiko ZK-EVM contract
     */
    constructor(address _taikoZkEvmAddress) {
        if (_taikoZkEvmAddress == address(0)) revert InvalidTaikoAddress();
        taikoZkEvm = ITaikoZkEvm(_taikoZkEvmAddress);
        owner = msg.sender;
    }
    
    /**
     * @dev Modifier to restrict function access to only the owner
     */
    modifier onlyOwner() {
        if (msg.sender != owner) revert OnlyOwner();
        _;
    }
    
    /**
     * @dev Verifies a ZK proof using Taiko's ZK-EVM
     * @param proof The ZK proof to verify
     * @param publicInputs The public inputs for the proof
     * @return success Whether the proof verification was successful
     */
    function verifyZkProof(
        bytes32[] calldata proof,
        bytes32[] calldata publicInputs
    ) external returns (bool success) {
        success = taikoZkEvm.verifyProof(proof, publicInputs);
        if (!success) revert ProofVerificationFailed();
        emit ProofVerified(success);
        return success;
    }
    
    /**
     * @dev Submits a block to Taiko's ZK-EVM
     * @param blockHash The hash of the block
     * @param stateRoot The state root of the block
     * @param transactions The transactions in the block
     */
    function submitBlockToTaiko(
        bytes32 blockHash,
        bytes32 stateRoot,
        bytes calldata transactions
    ) external onlyOwner {
        taikoZkEvm.submitBlock(blockHash, stateRoot, transactions);
        emit BlockSubmitted(blockHash);
    }
    
    /**
     * @dev Transfers ownership of the contract to a new address
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) external onlyOwner {
        if (newOwner == address(0)) revert InvalidTaikoAddress();
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```

```javascript
// taiko-integration.js
const { ethers } = require("ethers");
const TaikoZkEvmIntegrationABI = require("./artifacts/contracts/TaikoZkEvmIntegration.sol/TaikoZkEvmIntegration.json").abi;

class TaikoIntegration {
    constructor(provider, contractAddress) {
        this.provider = provider;
        this.contract = new ethers.Contract(
            contractAddress,
            TaikoZkEvmIntegrationABI,
            provider.getSigner()
        );
    }

    /**
     * Verifies a ZK proof using Taiko's ZK-EVM
     * @param {Array} proof - The ZK proof to verify
     * @param {Array} publicInputs - The public inputs for the proof
     * @returns {Promise<boolean>} - Whether the proof verification was successful
     */
    async verifyZkProof(proof, publicInputs) {
        try {
            const tx = await this.contract.verifyZkProof(proof, publicInputs);
            await tx.wait();
            return true;
        } catch (error) {
            console.error("Proof verification failed:", error);
            return false;
        }
    }

    /**
     * Submits a block to Taiko's ZK-EVM (owner only)
     * @param {string} blockHash - The hash of the block
     * @param {string} stateRoot - The state root of the block
     * @param {string} transactions - The transactions in the block
     * @returns {Promise<boolean>} - Whether the submission was successful
     */
    async submitBlock(blockHash, stateRoot, transactions) {
        try {
            const tx = await this.contract.submitBlockToTaiko(
                ethers.utils.hexlify(blockHash),
                ethers.utils.hexlify(stateRoot),
                transactions
            );
            await tx.wait();
            return true;
        } catch (error) {
            console.error("Block submission failed:", error);
            return false;
        }
    }

    /**
     * Transfers ownership of the contract (owner only)
     * @param {string} newOwner - The new owner address
     * @returns {Promise<boolean>} - Whether the transfer was successful
     */
    async transferOwnership(newOwner) {
        try {
            const tx = await this.contract.transferOwnership(newOwner);
            await tx.wait();
            return true;
        } catch (error) {
            console.error("Ownership transfer failed:", error);
            return false;
        }
    }
}

module.exports = TaikoIntegration;
```

```javascript
// test/test-taiko-integration.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("TaikoZkEvmIntegration", function () {
    let taikoIntegration;
    let owner, otherAccount;
    const mockProof = [ethers.utils.formatBytes32String("proof1"), ethers.utils.formatBytes32String("proof2")];
    const mockPublicInputs = [ethers.utils.formatBytes32String("input1"), ethers.utils.formatBytes32String("input2")];

    before(async function () {
        [owner, otherAccount] = await ethers.getSigners();
        
        // Deploy mock Taiko ZK-EVM
        const MockTaikoZkEvm = await ethers.getContractFactory("MockTaikoZkEvm");
        const mockTaiko = await MockTaikoZkEvm.deploy();
        await mockTaiko.deployed();
        
        // Deploy integration contract
        const TaikoZkEvmIntegration = await ethers.getContractFactory("TaikoZkEvmIntegration");
        taikoIntegration = await TaikoZkEvmIntegration.deploy(mockTaiko.address);
        await taikoIntegration.deployed();
    });

    it("Should verify proof successfully", async function () {
        await expect(taikoIntegration.verifyZkProof(mockProof, mockPublicInputs))
            .to.emit(taikoIntegration, "ProofVerified")
            .withArgs(true);
    });

    it("Should submit block (owner only)", async function () {
        const blockHash = ethers.utils.formatBytes32String("block123");
        const stateRoot = ethers.utils.formatBytes32String("root123");
        const transactions = "0x1234";
        
        await expect(taikoIntegration.connect(owner).submitBlockToTaiko(blockHash, stateRoot, transactions))
            .to.emit(taikoIntegration, "BlockSubmitted")
            .withArgs(blockHash);
    });

    it("Should prevent non-owners from submitting blocks", async function () {
        await expect(
            taikoIntegration.connect(otherAccount).submitBlockToTaiko(
                ethers.utils.formatBytes32String("block123"),
                ethers.utils.formatBytes32String("root123"),
                "0x1234"
            )
        ).to.be.revertedWith("OnlyOwner()");
    });

    it("Should transfer ownership", async function () {
        await expect(taikoIntegration.transferOwnership(otherAccount.address))
            .to.emit(taikoIntegration, "OwnershipTransferred")
            .withArgs(owner.address, otherAccount.address);
    });
});
```

```solidity
// MockTaikoZkEvm.sol - For testing purposes
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MockTaikoZkEvm {
    function verifyProof(
        bytes32[] calldata /* proof */,
        bytes32[] calldata /* publicInputs */
    ) external pure returns (bool) {
        return true;
    }
    
    function submitBlock(
        bytes32 /* blockHash */,
        bytes32 /* stateRoot */,
        bytes calldata /* transactions */
    ) external pure {
        // Mock implementation
    }
}
```
