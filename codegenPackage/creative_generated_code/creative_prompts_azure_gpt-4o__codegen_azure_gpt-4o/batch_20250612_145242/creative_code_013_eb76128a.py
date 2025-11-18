"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-ibw3fg6lj-reown-com.vercel.app
Prompt: Write code to implement ERC-7715 permissions using Wagmi with asynchronous ecdsa key handling as described in AppKit's documentation.
Generated: DETERMINISTIC_eb76128a98cca12e
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";
import { useContract, useSigner } from "wagmi";

// ERC-7715 Contract ABI (replace with actual ABI)
const ERC7715_ABI = [
  // Replace this with the actual ERC-7715 ABI as per the specification
  {
    "constant": false,
    "inputs": [
      { "name": "to", "type": "address" },
      { "name": "tokenId", "type": "uint256" },
      { "name": "permissions", "type": "bytes32" }
    ],
    "name": "grantPermission",
    "outputs": [],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      { "name": "tokenId", "type": "uint256" },
      { "name": "permissions", "type": "bytes32" }
    ],
    "name": "revokePermission",
    "outputs": [],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      { "name": "tokenId", "type": "uint256" },
      { "name": "permissions", "type": "bytes32" }
    ],
    "name": "hasPermission",
    "outputs": [{ "name": "granted", "type": "bool" }],
    "type": "function"
  }
];

// ERC-7715 Contract Address (replace with deployed contract address)
const ERC7715_ADDRESS = "0xYourERC7715ContractAddressHere";

// Helper function for asynchronous ECDSA key handling
async function signData(message, signer) {
  try {
    const signedMessage = await signer.signMessage(message);
    return signedMessage;
  } catch (error) {
    console.error("Error signing the message:", error);
    throw new Error("Signing failed");
  }
}

// Hook to interact with the ERC-7715 contract
export function useERC7715() {
  const { data: signer } = useSigner();

  // Set up the contract instance
  const contract = useContract({
    addressOrName: ERC7715_ADDRESS,
    contractInterface: ERC7715_ABI,
    signerOrProvider: signer,
  });

  /**
   * Grants permission to an address for a specific token ID.
   * @param {string} to - The address to grant permission to.
   * @param {number} tokenId - The token ID.
   * @param {string} permissions - The permissions as a bytes32 string.
   */
  async function grantPermission(to, tokenId, permissions) {
    try {
      if (!contract) throw new Error("Contract not initialized");
      const tx = await contract.grantPermission(to, tokenId, permissions);
      await tx.wait(); // Wait for the transaction to be mined
      console.log("Permission granted successfully");
    } catch (error) {
      console.error("Error granting permission:", error);
      throw error;
    }
  }

  /**
   * Revokes permission for a specific token ID.
   * @param {number} tokenId - The token ID.
   * @param {string} permissions - The permissions as a bytes32 string.
   */
  async function revokePermission(tokenId, permissions) {
    try {
      if (!contract) throw new Error("Contract not initialized");
      const tx = await contract.revokePermission(tokenId, permissions);
      await tx.wait(); // Wait for the transaction to be mined
      console.log("Permission revoked successfully");
    } catch (error) {
      console.error("Error revoking permission:", error);
      throw error;
    }
  }

  /**
   * Checks if a specific permission is granted for a given token ID.
   * @param {number} tokenId - The token ID.
   * @param {string} permissions - The permissions as a bytes32 string.
   * @returns {Promise<boolean>} - True if the permission is granted, false otherwise.
   */
  async function hasPermission(tokenId, permissions) {
    try {
      if (!contract) throw new Error("Contract not initialized");
      const granted = await contract.hasPermission(tokenId, permissions);
      return granted;
    } catch (error) {
      console.error("Error checking permission:", error);
      throw error;
    }
  }

  return {
    grantPermission,
    revokePermission,
    hasPermission,
    signData,
  };
}
```
