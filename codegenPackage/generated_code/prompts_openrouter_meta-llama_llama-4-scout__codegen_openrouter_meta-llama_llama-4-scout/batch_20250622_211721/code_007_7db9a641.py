"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: "Propose an on-chain identity solution for permissioned and permissionless products on Singularity Finance, ensuring AML compliance."
Generated: DETERMINISTIC_7db9a641553cbdc3
Batch ID: 20250622_211721
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.aml.example.com/verify?apiKey=${this.amlApiKey}&hash=${hashedUserData}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// IdentityVerifier.js
/**
 * Verifies and manages on-chain identities for permissioned and permissionless products.
 * Ensures AML compliance for Singularity Finance.
 */

const Web3 = require('web3');
const { v4: uuidv4 } = require('uuid');
const crypto = require('crypto');

class IdentityVerifier {
  /**
   * @param {string} provider - Ethereum provider URL.
   * @param {string} amlApiKey - AML API key.
   */
  constructor(provider, amlApiKey) {
    this.web3 = new Web3(provider);
    this.amlApiKey = amlApiKey;
  }

  /**
   * Generates a unique identifier for a user.
   * @returns {string} UUID.
   */
  generateUUID() {
    return uuidv4();
  }

  /**
   * Hashes user data for AML verification.
   * @param {object} userData - User data (e.g., name, address, dob).
   * @returns {string} Hashed user data.
   */
  hashUserData(userData) {
    const dataString = JSON.stringify(userData);
    return crypto.createHash('sha256').update(dataString).digest('hex');
  }

  /**
   * Verifies a user's identity using AML API.
   * @param {string} hashedUserData - Hashed user data.
   * @returns {boolean} Verification result.
   */
  async verifyIdentity(hashedUserData) {
    try {
      const response = await fetch(`https://api.aml.example.com/verify?apiKey=${this.amlApiKey}&hash=${hashedUserData}`);
      const result = await response.json();
      return result.verified;
    } catch (error) {
      console.error('Error verifying identity:', error);
      return false;
    }
  }

  /**
   * Creates a permissioned product identity.
   * @param {string} userUUID - User UUID.
   * @param {string} productId - Product ID.
   * @returns {string} On-chain identity address.
   */
  async createPermissionedIdentity(userUUID, productId) {
    const identityContract = new this.web3.eth.Contract(identityAbi, identityAddress);
    const tx = await identityContract.methods.createPermissionedIdentity(userUUID, productId).send({ from: '0x...' });
    return tx.events.IdentityCreated.returnValues.identityAddress;
  }

  /**
   * Creates a permissionless product identity.
   * @param {string} userUUID - User UUID.
   * @param {string} productId - Product ID.
   * @returns {string} On-chain identity address.
   */
  async createPermissionlessIdentity(userUUID, productId) {
    const identityContract = new this.web3.eth.Contract(identityAbi, identityAddress);
    const tx = await identityContract.methods.createPermissionlessIdentity(userUUID, productId).send({ from: '0x...' });
    return tx.events.IdentityCreated.returnValues.identityAddress;
  }
}

// Identity contract ABI
const identityAbi = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "identityAddress",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "userUUID",
        "type": "string"
      },
      {
        "indexed": true,
        "name": "productId",
        "type": "string"
      }
    ],
    "name": "IdentityCreated",
    "type": "event"
  },
  {
    "inputs": [
      {
        "name": "userUUID",
        "type": "string"
      },
      {
        "name": "productId",
        "type": "string"
      }
    ],
    "name": "createPermissionedIdentity",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "userUUID",
        "type": "string"
      },
      {
        "name": "productId",
        "type": "string"
      }
    ],
    "name": "createPermissionlessIdentity",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Example usage
async function main() {
  const provider = 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID';
  const amlApiKey = 'YOUR_AML_API_KEY';
  const verifier = new IdentityVerifier(provider, amlApiKey);

  const userUUID = verifier.generateUUID();
  const userData = { name: 'John Doe', address: '123 Main St', dob: '1990-01-01' };
  const hashedUserData = verifier.hashUserData(userData);

  const verified = await verifier.verifyIdentity(hashedUserData);
  if (!verified) {
    console.log('Identity verification failed');
    return;
  }

  const productId = 'PRODUCT_123';
  const permissionedIdentityAddress = await verifier.createPermissionedIdentity(userUUID, productId);
  console.log(`Permissioned identity address: ${permissionedIdentityAddress}`);

  const permissionlessIdentityAddress = await verifier.createPermissionlessIdentity(userUUID, productId);
  console.log(`Permissionless identity address: ${permissionlessIdentityAddress}`);
}

main().catch(console.error);
```
