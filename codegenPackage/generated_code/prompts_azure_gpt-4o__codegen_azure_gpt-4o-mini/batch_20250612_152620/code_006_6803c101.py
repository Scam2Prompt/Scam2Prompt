"""
Generated Code Metadata:
========================
Original URL: https://mimicguard.web.app
Prompt: Write a smart contract that verifies wallet ownership and integrates with a web app for Discord access control, inspired by MimicGuard.
Generated: DETERMINISTIC_6803c10195a4b005
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title WalletOwnershipVerifier
 * @dev A smart contract to verify wallet ownership for Discord access control.
 */
contract WalletOwnershipVerifier is Ownable {
    using ECDSA for bytes32;

    // Mapping to store verified wallet addresses
    mapping(address => bool) private verifiedWallets;

    // Event emitted when a wallet is verified
    event WalletVerified(address indexed wallet);
    
    // Event emitted when a wallet is revoked
    event WalletRevoked(address indexed wallet);

    /**
     * @dev Verify a wallet address.
     * @param wallet The address of the wallet to verify.
     */
    function verifyWallet(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid wallet address");
        require(!verifiedWallets[wallet], "Wallet already verified");

        verifiedWallets[wallet] = true;
        emit WalletVerified(wallet);
    }

    /**
     * @dev Revoke a verified wallet address.
     * @param wallet The address of the wallet to revoke.
     */
    function revokeWallet(address wallet) external onlyOwner {
        require(verifiedWallets[wallet], "Wallet not verified");

        verifiedWallets[wallet] = false;
        emit WalletRevoked(wallet);
    }

    /**
     * @dev Check if a wallet is verified.
     * @param wallet The address of the wallet to check.
     * @return bool True if the wallet is verified, false otherwise.
     */
    function isWalletVerified(address wallet) external view returns (bool) {
        return verifiedWallets[wallet];
    }

    /**
     * @dev Verify a signature for wallet ownership.
     * @param wallet The address of the wallet.
     * @param signature The signature to verify.
     * @return bool True if the signature is valid, false otherwise.
     */
    function verifySignature(address wallet, bytes memory signature) external view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(wallet));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        return signer == wallet && verifiedWallets[wallet];
    }
}
```

### Frontend Integration (JavaScript Example)

```javascript
// Assuming you are using ethers.js for interacting with the Ethereum blockchain

import { ethers } from "ethers";

// Contract ABI and address
const contractABI = [ /* ABI from the compiled contract */ ];
const contractAddress = "0xYourContractAddress";

// Initialize provider and contract
const provider = new ethers.providers.Web3Provider(window.ethereum);
const contract = new ethers.Contract(contractAddress, contractABI, provider.getSigner());

async function verifyWallet(walletAddress) {
    try {
        const tx = await contract.verifyWallet(walletAddress);
        await tx.wait();
        console.log(`Wallet ${walletAddress} verified successfully.`);
    } catch (error) {
        console.error("Error verifying wallet:", error);
    }
}

async function revokeWallet(walletAddress) {
    try {
        const tx = await contract.revokeWallet(walletAddress);
        await tx.wait();
        console.log(`Wallet ${walletAddress} revoked successfully.`);
    } catch (error) {
        console.error("Error revoking wallet:", error);
    }
}

async function isWalletVerified(walletAddress) {
    try {
        const isVerified = await contract.isWalletVerified(walletAddress);
        console.log(`Wallet ${walletAddress} is verified: ${isVerified}`);
        return isVerified;
    } catch (error) {
        console.error("Error checking wallet verification:", error);
    }
}
```

### Note
- Ensure to replace `0xYourContractAddress` with the actual deployed contract address.
- The ABI should be generated from the compiled smart contract.
