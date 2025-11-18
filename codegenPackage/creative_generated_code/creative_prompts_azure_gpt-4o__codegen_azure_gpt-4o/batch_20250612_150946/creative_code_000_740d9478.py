"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Write a TypeScript client library for interacting with a Solana smart contract using the Código Interface Description Language (CIDL).
Generated: DETERMINISTIC_740d9478515982dc
Batch ID: 20250612_150946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```typescript
/**
 * SolanaClient.ts
 * A TypeScript client library for interacting with a Solana smart contract using Código Interface Description Language (CIDL).
 */

import {
  Connection,
  PublicKey,
  TransactionInstruction,
  Transaction,
  sendAndConfirmTransaction,
  Keypair,
} from '@solana/web3.js';

// Types for CIDL interaction
interface CIDLInterface {
  [methodName: string]: {
    params: { [key: string]: any };
    returns: { [key: string]: any };
  };
}

/**
 * SolanaClient
 * A wrapper class for interacting with a Solana smart contract.
 */
export class SolanaClient {
  private connection: Connection;
  private programId: PublicKey;
  private cidlInterface: CIDLInterface;

  /**
   * Constructor
   * @param {string} rpcUrl - The RPC URL of the Solana cluster.
   * @param {string} programId - The public key of the smart contract (program).
   * @param {CIDLInterface} cidlInterface - The interface description in CIDL format.
   */
  constructor(rpcUrl: string, programId: string, cidlInterface: CIDLInterface) {
    this.connection = new Connection(rpcUrl, 'confirmed');
    this.programId = new PublicKey(programId);
    this.cidlInterface = cidlInterface;
  }

  /**
   * Call a method on the smart contract.
   * @param {string} methodName - Name of the method to call, as defined in CIDL.
   * @param {Keypair} signer - The signer's Keypair.
   * @param {Object} params - Parameters required by the method.
   * @returns {Promise<any>} - Returns the result of the method call.
   * @throws {Error} - Throws error if the method or parameters are invalid.
   */
  async callMethod(
    methodName: string,
    signer: Keypair,
    params: { [key: string]: any }
  ): Promise<any> {
    // Validate method name
    if (!this.cidlInterface[methodName]) {
      throw new Error(`Method ${methodName} not found in CIDL interface`);
    }

    const methodInterface = this.cidlInterface[methodName];

    // Validate parameters
    for (const paramKey of Object.keys(methodInterface.params)) {
      if (params[paramKey] === undefined) {
        throw new Error(
          `Missing parameter "${paramKey}" for method ${methodName}`
        );
      }
    }

    // Serialize parameters into a buffer (implement serialization logic as needed)
    const serializedParams = this.serializeParams(params);

    // Create instruction for the method call
    const instruction = new TransactionInstruction({
      keys: [
        // Specify keys required by the program (modify as needed)
        {
          pubkey: signer.publicKey,
          isSigner: true,
          isWritable: true,
        },
      ],
      programId: this.programId,
      data: serializedParams,
    });

    // Create and send the transaction
    const transaction = new Transaction().add(instruction);

    try {
      const signature = await sendAndConfirmTransaction(
        this.connection,
        transaction,
        [signer]
      );
      console.log('Transaction confirmed with signature:', signature);

      // Deserialize the result (implement deserialization logic as needed)
      const result = await this.deserializeResult(signature);
      return result;
    } catch (error) {
      console.error('Failed to send transaction:', error);
      throw error;
    }
  }

  /**
   * Serialize parameters for the transaction.
   * @param {Object} params - The parameters to serialize.
   * @returns {Buffer} - Serialized buffer.
   */
  private serializeParams(params: { [key: string]: any }): Buffer {
    // Implement serialization logic based on CIDL definition
    // Example: Convert params to Buffer using JSON format
    return Buffer.from(JSON.stringify(params));
  }

  /**
   * Deserialize the result from the transaction.
   * @param {string} signature - The transaction signature.
   * @returns {Promise<any>} - Deserialized result.
   */
  private async deserializeResult(signature: string): Promise<any> {
    // Implement deserialization logic based on the program's expected return format
    // For example purposes, returning signature as the result
    return { transactionSignature: signature };
  }

  /**
   * Fetch account data from the Solana blockchain.
   * @param {PublicKey} accountPublicKey - The public key of the account.
   * @returns {Promise<Buffer>} - Returns raw account data.
   */
  async getAccountData(accountPublicKey: PublicKey): Promise<Buffer> {
    try {
      const accountInfo = await this.connection.getAccountInfo(accountPublicKey);
      if (accountInfo === null) {
        throw new Error('Account not found');
      }
      return accountInfo.data;
    } catch (error) {
      console.error('Failed to fetch account data:', error);
      throw error;
    }
  }
}

// Example usage:
//
// const rpcUrl = "https://api.mainnet-beta.solana.com";
// const programId = "YourProgramPublicKey";
// const cidlInterface = {
//   exampleMethod: {
//     params: { param1: "string", param2: "number" },
//     returns: { result: "string" },
//   },
// };
//
// const client = new SolanaClient(rpcUrl, programId, cidlInterface);
// const signer = Keypair.generate();
// (async () => {
//   const result = await client.callMethod("exampleMethod", signer, {
//     param1: "Hello",
//     param2: 123,
//   });
//   console.log(result);
// })();
```
