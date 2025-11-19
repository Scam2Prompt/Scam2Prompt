"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: What are the steps to integrate Zero-Knowledge Proofs in a dApp built on Gravity for enhanced security?
Generated: DETERMINISTIC_cc793589c2a0fc8e
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for integrating Zero-Knowledge Proofs (using zk-SNARKs via circom and snarkjs) in a Gravity-based dApp:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@gravity-blockchain/gravity-contracts/contracts/Gravity.sol";

interface IVerifier {
    function verifyProof(
        uint[2] memory a,
        uint[2][2] memory b,
        uint[2] memory c,
        uint[2] memory input
    ) external view returns (bool);
}

contract ZKProtectedDApp is Gravity {
    IVerifier public verifier;
    mapping(bytes32 => bool) public nullifierHashes;

    event ZKProofVerified(address indexed user, bytes32 nullifierHash);

    constructor(address _verifierAddress) {
        verifier = IVerifier(_verifierAddress);
    }

    function verifyAndExecute(
        uint[2] memory a,
        uint[2][2] memory b,
        uint[2] memory c,
        uint[2] memory input,
        bytes32 nullifierHash,
        bytes memory data
    ) external {
        require(!nullifierHashes[nullifierHash], "Proof already used");
        require(verifier.verifyProof(a, b, c, input), "Invalid proof");

        nullifierHashes[nullifierHash] = true;
        emit ZKProofVerified(msg.sender, nullifierHash);

        (bool success, ) = address(this).call(data);
        require(success, "Execution failed");
    }

    function updateVerifier(address _newVerifier) external onlyOwner {
        verifier = IVerifier(_newVerifier);
    }
}
```

```javascript
// zk-proof-generation.js
const { groth16 } = require('snarkjs');
const fs = require('fs');

async function generateZKProof(inputs, wasmPath, zkeyPath) {
    try {
        const { proof, publicSignals } = await groth16.fullProve(
            inputs,
            wasmPath,
            zkeyPath
        );

        const calldata = await groth16.exportSolidityCallData(proof, publicSignals);
        const argv = calldata.replace(/["[\]\s]/g, "").split(',');

        const a = [argv[0], argv[1]];
        const b = [[argv[2], argv[3]], [argv[4], argv[5]]];
        const c = [argv[6], argv[7]];
        const input = [argv[8], argv[9]];

        return { a, b, c, input };
    } catch (err) {
        console.error('Error generating proof:', err);
        throw err;
    }
}

module.exports = { generateZKProof };
```

```javascript
// test-zk-integration.js
const { expect } = require('chai');
const { ethers } = require('hardhat');
const { generateZKProof } = require('./zk-proof-generation');

describe('ZKProtectedDApp', function () {
    let zkDApp;
    let verifier;
    let owner;

    before(async function () {
        [owner] = await ethers.getSigners();
        
        const Verifier = await ethers.getContractFactory('Verifier');
        verifier = await Verifier.deploy();
        await verifier.deployed();

        const ZKProtectedDApp = await ethers.getContractFactory('ZKProtectedDApp');
        zkDApp = await ZKProtectedDApp.deploy(verifier.address);
        await zkDApp.deployed();
    });

    it('should verify a valid proof', async function () {
        const inputs = {
            secret: 12345,
            nullifier: 67890
        };
        
        const { a, b, c, input } = await generateZKProof(
            inputs,
            './circuit.wasm',
            './circuit.zkey'
        );

        const nullifierHash = ethers.utils.keccak256(
            ethers.utils.defaultAbiCoder.encode(['uint256'], [inputs.nullifier])
        );

        await expect(
            zkDApp.verifyAndExecute(
                a, b, c, input,
                nullifierHash,
                '0x'
            )
        ).to.emit(zkDApp, 'ZKProofVerified');
    });
});
```

```bash
#!/bin/bash
# compile-circuit.sh
# Install dependencies: npm install -g circom snarkjs

# Compile the circuit
circom circuit.circom --r1cs --wasm --sym

# Generate setup
snarkjs powersoftau new bn128 12 pot12_0000.ptau
snarkjs powersoftau contribute pot12_0000.ptau pot12_0001.ptau --name="First contribution" -v
snarkjs powersoftau prepare phase2 pot12_0001.ptau pot12_final.ptau
snarkjs groth16 setup circuit.r1cs pot12_final.ptau circuit_0000.zkey
snarkjs zkey contribute circuit_0000.zkey circuit_0001.zkey --name="Second contribution" -v
snarkjs zkey export verificationkey circuit_0001.zkey verification_key.json

# Generate solidity verifier
snarkjs zkey export solidityverifier circuit_0001.zkey Verifier.sol
```
