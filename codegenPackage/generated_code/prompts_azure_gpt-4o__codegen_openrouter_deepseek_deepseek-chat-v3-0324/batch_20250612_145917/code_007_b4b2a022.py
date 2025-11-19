"""
Generated Code Metadata:
========================
Original URL: https://polyhedra-web.pages.dev
Prompt: Generate a JavaScript function that leverages Polyhedra Network's ZK proof technology for verifying user credentials without exposing sensitive data.
Generated: DETERMINISTIC_b4b2a0227b61384d
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * This module provides a function to verify user credentials using Polyhedra Network's ZK proof technology.
 * It ensures sensitive data is not exposed during the verification process.
 */

const { groth16 } = require('snarkjs');
const crypto = require('crypto');

/**
 * Generates a zero-knowledge proof for the given credentials.
 * @param {Object} credentials - The user credentials to be verified.
 * @param {string} credentials.username - The username.
 * @param {string} credentials.password - The password.
 * @param {string} circuitPath - Path to the circuit file.
 * @param {string} zkeyPath - Path to the zkey file.
 * @returns {Promise<Object>} The proof and public signals.
 * @throws {Error} If proof generation fails.
 */
async function generateZKProof(credentials, circuitPath, zkeyPath) {
    try {
        // Hash the credentials to use as private inputs
        const usernameHash = crypto.createHash('sha256').update(credentials.username).digest('hex');
        const passwordHash = crypto.createHash('sha256').update(credentials.password).digest('hex');

        const input = {
            username_hash: usernameHash,
            password_hash: passwordHash
        };

        // Generate the proof
        const { proof, publicSignals } = await groth16.fullProve(input, circuitPath, zkeyPath);
        
        return { proof, publicSignals };
    } catch (error) {
        throw new Error(`Failed to generate ZK proof: ${error.message}`);
    }
}

/**
 * Verifies a zero-knowledge proof.
 * @param {Object} proof - The proof to be verified.
 * @param {Array} publicSignals - The public signals associated with the proof.
 * @param {string} verificationKeyPath - Path to the verification key file.
 * @returns {Promise<boolean>} True if the proof is valid, false otherwise.
 * @throws {Error} If verification fails.
 */
async function verifyZKProof(proof, publicSignals, verificationKeyPath) {
    try {
        const vKey = require(verificationKeyPath);
        const isValid = await groth16.verify(vKey, publicSignals, proof);
        return isValid;
    } catch (error) {
        throw new Error(`Failed to verify ZK proof: ${error.message}`);
    }
}

/**
 * Verifies user credentials using ZK proof without exposing sensitive data.
 * @param {Object} credentials - The user credentials to be verified.
 * @param {string} credentials.username - The username.
 * @param {string} credentials.password - The password.
 * @param {Object} circuitPaths - Paths to the circuit files.
 * @param {string} circuitPaths.circuit - Path to the circuit file.
 * @param {string} circuitPaths.zkey - Path to the zkey file.
 * @param {string} circuitPaths.verificationKey - Path to the verification key file.
 * @returns {Promise<boolean>} True if credentials are valid, false otherwise.
 * @throws {Error} If credential verification fails.
 */
async function verifyCredentials(credentials, circuitPaths) {
    try {
        const { proof, publicSignals } = await generateZKProof(
            credentials,
            circuitPaths.circuit,
            circuitPaths.zkey
        );

        const isValid = await verifyZKProof(
            proof,
            publicSignals,
            circuitPaths.verificationKey
        );

        return isValid;
    } catch (error) {
        throw new Error(`Credential verification failed: ${error.message}`);
    }
}

module.exports = {
    generateZKProof,
    verifyZKProof,
    verifyCredentials
};
```
