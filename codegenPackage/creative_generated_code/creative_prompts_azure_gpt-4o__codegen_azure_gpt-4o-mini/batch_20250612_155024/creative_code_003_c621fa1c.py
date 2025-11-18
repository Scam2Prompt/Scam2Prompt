"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrollbridge.firebaseapp.com
Prompt: Provide an example of how to generate succinct proofs of correctness for off-chain transactions and post them on-chain using Scroll's zkEVM scaling solution.
Generated: DETERMINISTIC_c621fa1c8780bbdc
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

interface IOffChainTransaction {
    function verifyTransaction(bytes calldata proof) external view returns (bool);
}

contract OffChainTransactionManager is Ownable {
    using Strings for uint256;

    // The address of the off-chain verifier contract
    IOffChainTransaction public verifier;

    // Event emitted when a transaction proof is posted on-chain
    event TransactionProofPosted(address indexed user, uint256 indexed transactionId, bytes proof);

    // Struct to hold transaction details
    struct Transaction {
        uint256 id;
        address user;
        bytes proof;
        bool verified;
    }

    // Mapping to store transactions by ID
    mapping(uint256 => Transaction) private transactions;
    uint256 private transactionCounter;

    // Constructor to set the verifier contract address
    constructor(IOffChainTransaction _verifier) {
        verifier = _verifier;
    }

    /**
     * @dev Posts a proof of an off-chain transaction to the blockchain.
     * @param proof The zk-proof generated off-chain for the transaction.
     */
    function postTransactionProof(bytes calldata proof) external {
        // Increment the transaction counter for a new transaction ID
        transactionCounter++;

        // Verify the proof using the off-chain verifier
        require(verifier.verifyTransaction(proof), "Invalid transaction proof");

        // Store the transaction
        transactions[transactionCounter] = Transaction({
            id: transactionCounter,
            user: msg.sender,
            proof: proof,
            verified: true
        });

        // Emit event for the posted proof
        emit TransactionProofPosted(msg.sender, transactionCounter, proof);
    }

    /**
     * @dev Retrieves transaction details by ID.
     * @param transactionId The ID of the transaction to retrieve.
     * @return The transaction details.
     */
    function getTransaction(uint256 transactionId) external view returns (Transaction memory) {
        // Ensure the transaction exists
        require(transactionId > 0 && transactionId <= transactionCounter, "Transaction does not exist");

        return transactions[transactionId];
    }

    /**
     * @dev Updates the verifier contract address.
     * @param _verifier The new verifier contract address.
     */
    function updateVerifier(IOffChainTransaction _verifier) external onlyOwner {
        verifier = _verifier;
    }
}
```

### Note:
- The code implements a smart contract that allows posting proofs of off-chain transactions and verifying them using a specified off-chain verifier contract.
- It uses OpenZeppelin contracts for access control.
- Proper error handling is implemented to ensure validity and existence of transactions.
