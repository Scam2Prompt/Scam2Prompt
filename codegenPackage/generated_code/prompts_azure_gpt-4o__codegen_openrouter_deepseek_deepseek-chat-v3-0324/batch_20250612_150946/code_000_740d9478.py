"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Write a TypeScript client library for interacting with a Solana smart contract using the Código Interface Description Language (CIDL).
Generated: DETERMINISTIC_740d9478515982dc
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Connection, Keypair, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { Program, Provider, AnchorProvider } from '@project-serum/anchor';
import { CIDL } from '@codigo-io/cidl';

/**
 * SolanaClient is a TypeScript client for interacting with Solana smart contracts
 * described using the Código Interface Description Language (CIDL).
 */
export class SolanaClient {
    private connection: Connection;
    private program: Program;
    private provider: Provider;
    private cidl: CIDL;

    /**
     * Initializes a new instance of the SolanaClient.
     * @param cidlJson The CIDL JSON object describing the smart contract interface.
     * @param programId The public key of the deployed program.
     * @param connection The Solana connection object.
     * @param wallet The wallet to use for transactions.
     */
    constructor(
        cidlJson: any,
        programId: PublicKey,
        connection: Connection,
        wallet: Keypair
    ) {
        this.connection = connection;
        this.provider = new AnchorProvider(connection, wallet, {});
        this.cidl = new CIDL(cidlJson);
        this.program = new Program(this.cidl.idl, programId, this.provider);
    }

    /**
     * Calls a method on the smart contract.
     * @param methodName The name of the method to call.
     * @param args The arguments to pass to the method.
     * @returns The result of the method call.
     */
    public async callMethod(
        methodName: string,
        args: any[]
    ): Promise<any> {
        try {
            const method = this.program.methods[methodName];
            if (!method) {
                throw new Error(`Method ${methodName} not found in program`);
            }

            const tx = await method(...args).transaction();
            const txId = await sendAndConfirmTransaction(
                this.connection,
                tx,
                [this.provider.wallet.payer]
            );

            return { txId };
        } catch (error) {
            console.error(`Error calling method ${methodName}:`, error);
            throw error;
        }
    }

    /**
     * Retrieves account data from the smart contract.
     * @param accountName The name of the account to fetch.
     * @param publicKey The public key of the account.
     * @returns The account data.
     */
    public async getAccountData(
        accountName: string,
        publicKey: PublicKey
    ): Promise<any> {
        try {
            const account = this.program.account[accountName];
            if (!account) {
                throw new Error(`Account ${accountName} not found in program`);
            }

            return await account.fetch(publicKey);
        } catch (error) {
            console.error(`Error fetching account ${accountName}:`, error);
            throw error;
        }
    }

    /**
     * Subscribes to account changes.
     * @param accountName The name of the account to subscribe to.
     * @param publicKey The public key of the account.
     * @param callback The callback to invoke when the account changes.
     * @returns The subscription ID.
     */
    public async subscribeToAccount(
        accountName: string,
        publicKey: PublicKey,
        callback: (data: any) => void
    ): Promise<number> {
        try {
            const account = this.program.account[accountName];
            if (!account) {
                throw new Error(`Account ${accountName} not found in program`);
            }

            return await account.subscribe(publicKey, callback);
        } catch (error) {
            console.error(`Error subscribing to account ${accountName}:`, error);
            throw error;
        }
    }

    /**
     * Unsubscribes from account changes.
     * @param subscriptionId The subscription ID to unsubscribe from.
     */
    public async unsubscribeFromAccount(subscriptionId: number): Promise<void> {
        try {
            await this.connection.removeAccountChangeListener(subscriptionId);
        } catch (error) {
            console.error('Error unsubscribing from account:', error);
            throw error;
        }
    }
}

/**
 * Helper function to initialize a SolanaClient instance.
 * @param cidlJson The CIDL JSON object.
 * @param programId The program public key as a base58 string.
 * @param rpcUrl The Solana RPC URL.
 * @param wallet The wallet keypair.
 * @returns A promise that resolves to a SolanaClient instance.
 */
export async function initializeSolanaClient(
    cidlJson: any,
    programId: string,
    rpcUrl: string,
    wallet: Keypair
): Promise<SolanaClient> {
    try {
        const connection = new Connection(rpcUrl, 'confirmed');
        const publicKey = new PublicKey(programId);
        return new SolanaClient(cidlJson, publicKey, connection, wallet);
    } catch (error) {
        console.error('Error initializing Solana client:', error);
        throw error;
    }
}
```
