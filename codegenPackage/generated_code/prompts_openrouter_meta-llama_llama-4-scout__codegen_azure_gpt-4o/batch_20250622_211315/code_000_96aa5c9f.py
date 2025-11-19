"""
Generated Code Metadata:
========================
Original URL: https://disperse-zk.vercel.app
Prompt: "Generate a simple example of a zero-knowledge proof using JavaScript."
Generated: DETERMINISTIC_96aa5c9ff5845a7b
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Zero-Knowledge Proof Example in JavaScript
 * 
 * This example demonstrates a simple zero-knowledge proof concept using a discrete logarithm problem.
 * The prover wants to prove knowledge of a secret `x` such that `g^x = y (mod p)` without revealing `x`.
 * 
 * Note: This is a simplified example for educational purposes and should not be used in production.
 */

// Import a cryptographic library for big integer operations (e.g., 'big-integer')
const bigInt = require('big-integer');

// Parameters for the proof (publicly known)
const p = bigInt("23"); // A prime number
const g = bigInt("5");  // A generator

// Prover's secret (private knowledge)
const x = bigInt("6");  // Secret exponent

// Compute the public value y = g^x mod p
const y = g.modPow(x, p);

// Zero-Knowledge Proof Process
function zeroKnowledgeProof() {
  try {
    console.log("=== Zero-Knowledge Proof ===");

    // Step 1: Prover generates a random value (commitment)
    const r = bigInt.randBetween(1, p.minus(1)); // Random value
    const c = g.modPow(r, p); // Commitment: g^r mod p

    console.log("Prover sends commitment (c):", c.toString());

    // Step 2: Verifier sends a challenge (e.g., 0 or 1)
    const challenge = Math.floor(Math.random() * 2); // Random challenge (0 or 1)
    console.log("Verifier sends challenge:", challenge);

    // Step 3: Prover computes response based on the challenge
    let response;
    if (challenge === 0) {
      // If challenge is 0, response is r
      response = r;
    } else if (challenge === 1) {
      // If challenge is 1, response is r + x (mod p-1)
      response = r.add(x).mod(p.minus(1));
    }

    console.log("Prover sends response:", response.toString());

    // Step 4: Verifier checks the response
    let verifierCheck;
    if (challenge === 0) {
      // If challenge is 0, verifier checks g^response mod p === c
      verifierCheck = g.modPow(response, p).equals(c);
    } else if (challenge === 1) {
      // If challenge is 1, verifier checks g^response mod p === c * y mod p
      verifierCheck = g.modPow(response, p).equals(c.multiply(y).mod(p));
    }

    console.log("Verifier's check result:", verifierCheck ? "Valid proof" : "Invalid proof");
  } catch (error) {
    console.error("An error occurred during the zero-knowledge proof process:", error.message);
  }
}

// Run the zero-knowledge proof example
zeroKnowledgeProof();
```

**Dependencies:**
To run this code, you need to install the `big-integer` library:
```bash
npm install big-integer
```
