"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Generate a Java smart contract for Neo N3 that supports contract updates and destruction, ensuring only authorized users can perform these actions.
Generated: DETERMINISTIC_8a169e047eb0637b
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
package com.example;

import io.neow3j.devpack.annotations.ManifestExtra;
import io.neow3j.devpack.annotations.Permission;
import io.neow3j.devpack.contracts.Contract;
import io.neow3j.devpack.contracts.StdLib;
import io.neow3j.devpack.runtime.Blockchain;
import io.neow3j.devpack.runtime.Runtime;
import io.neow3j.devpack.runtime.Storage;
import io.neow3j.devpack.runtime.Notification;
import io.neow3j.devpack.runtime.Transaction;
import io.neow3j.devpack.runtime.Validator;
import io.neow3j.devpack.runtime.execution.ContractManagement;
import io.neow3j.devpack.types.Hash160;

// Manifest metadata
@ManifestExtra(key = "author", value = "YourName")
@ManifestExtra(key = "email", value = "your.email@example.com")
@ManifestExtra(key = "description", value = "Smart contract for Neo N3 supporting updates and destruction")

@Permission(contract = "*", methods = "*") // Allow access to all contracts
public class UpdateableContract {

    // Storage keys and contract owner
    private static final String OWNER_KEY = "owner";
    private static final Storage storage = Storage.getStorageContext();

    // Constructor to initialize the owner address
    static {
        Hash160 owner = Runtime.getCallingScriptHash(); // Initialize owner as the deployer
        storage.put(OWNER_KEY, owner.toByteArray());
    }

    // Modifier to ensure only the owner can execute certain functions
    private static boolean isOwner() {
        Hash160 caller = Runtime.getCallingScriptHash();
        Hash160 owner = new Hash160(storage.get(OWNER_KEY));
        return owner.equals(caller);
    }

    // Retrieve contract owner
    public static Hash160 getOwner() {
        return new Hash160(storage.get(OWNER_KEY));
    }

    // Update contract logic (only owner can update)
    public static void updateContract(byte[] nefFile, String manifestFile) {
        if (!isOwner()) {
            Runtime.log("Unauthorized access. Only the owner can update the contract.");
            throw new RuntimeException("Unauthorized access. Only the owner can update the contract.");
        }

        ContractManagement.update(nefFile, manifestFile);
        Runtime.log("Contract updated successfully.");
    }

    // Destroy the contract (only owner can destroy)
    public static void destroyContract() {
        if (!isOwner()) {
            Runtime.log("Unauthorized access. Only the owner can destroy the contract.");
            throw new RuntimeException("Unauthorized access. Only the owner can destroy the contract.");
        }

        ContractManagement.destroy();
        Runtime.log("Contract destroyed successfully.");
    }

    // Example function to demonstrate contract functionality
    public static String helloWorld() {
        return "Hello, Neo!";
    }

    // Transfer ownership of the contract (only owner can transfer)
    public static void transferOwnership(Hash160 newOwner) {
        if (!isOwner()) {
            Runtime.log("Unauthorized access. Only the owner can transfer ownership.");
            throw new RuntimeException("Unauthorized access. Only the owner can transfer ownership.");
        }

        storage.put(OWNER_KEY, newOwner.toByteArray());
        Runtime.log("Ownership transferred successfully.");
    }
}
```
