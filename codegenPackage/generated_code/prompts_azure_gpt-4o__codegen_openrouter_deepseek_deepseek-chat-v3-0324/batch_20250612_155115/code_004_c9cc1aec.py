"""
Generated Code Metadata:
========================
Original URL: https://symbiosis-finance.cc
Prompt: Create a step-by-step guide for implementing cross-chain zaps using the Symbiosis SDK to move liquidity from Ethereum to Solana in a single transaction.
Generated: DETERMINISTIC_c9cc1aec5945e5b0
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries and SDKs
import { Symbiosis, Token, TokenAmount, ChainId, ChainType } from '@symbiosis-finance/sdk';
import { ethers } from 'ethers';
import { Connection, Keypair, PublicKey, Transaction } from '@solana/web3.js';
import { Token as SolanaToken, TOKEN_PROGRAM_ID } from '@solana/spl-token';

// Initialize providers for both chains
const ethereumProvider = new ethers.providers.JsonRpcProvider('ETHEREUM_RPC_URL');
const solanaConnection = new Connection('SOLANA_RPC_URL', 'confirmed');

// Initialize Symbiosis SDK
const symbiosis = new Symbiosis('mainnet', 'YOUR_API_KEY');

// User wallet setup (example with private keys - in production use secure storage)
const ethWallet = new ethers.Wallet('ETH_PRIVATE_KEY', ethereumProvider);
const solanaKeypair = Keypair.fromSecretKey(Buffer.from('SOLANA_PRIVATE_KEY', 'hex'));

// Token addresses
const ETH_TOKEN_ADDRESS = '0x...'; // ERC20 token address on Ethereum
const SOL_TOKEN_ADDRESS = '0x...'; // SPL token address on Solana

// Amount to transfer (in smallest units)
const amount = ethers.utils.parseUnits('10', 18); // 10 tokens with 18 decimals

async function crossChainZap() {
    try {
        // Step 1: Get token information
        const tokenIn = new Token({
            chainId: ChainId.ETHEREUM,
            address: ETH_TOKEN_ADDRESS,
            decimals: 18,
            symbol: 'TOKEN',
            name: 'Token'
        });

        const tokenAmountIn = new TokenAmount(tokenIn, amount.toString());

        // Step 2: Get zap transaction details
        const zapIn = await symbiosis.zapIn({
            tokenAmountIn,
            chainIdTo: ChainId.SOLANA,
            to: new PublicKey(solanaKeypair.publicKey).toString(),
            revertableAddress: ethWallet.address,
            slippage: 50 // 0.5%
        });

        // Step 3: Approve token spending if needed
        const approvalTx = await zapIn.getApproveTransaction();
        if (approvalTx) {
            const approved = await ethWallet.sendTransaction(approvalTx);
            await approved.wait();
        }

        // Step 4: Send the main transaction
        const transaction = await zapIn.getTransaction();
        const txResponse = await ethWallet.sendTransaction(transaction);
        console.log(`Ethereum transaction hash: ${txResponse.hash}`);

        // Step 5: Wait for transaction to be processed
        const receipt = await txResponse.wait();
        console.log('Transaction mined:', receipt.transactionHash);

        // Step 6: Wait for cross-chain completion
        const waitForComplete = await symbiosis.waitForComplete(receipt.transactionHash);
        console.log('Cross-chain transfer completed:', waitForComplete);

        // Step 7: Verify tokens arrived on Solana
        const solanaToken = new SolanaToken(
            solanaConnection,
            new PublicKey(SOL_TOKEN_ADDRESS),
            TOKEN_PROGRAM_ID,
            solanaKeypair
        );

        const balance = await solanaToken.getAccountInfo(
            await solanaToken.getOrCreateAssociatedAccountInfo(solanaKeypair.publicKey)
        );
        console.log(`Final balance on Solana: ${balance.amount.toString()}`);

    } catch (error) {
        console.error('Error in cross-chain zap:', error);
        throw error;
    }
}

// Execute the function
crossChainZap()
    .then(() => console.log('Cross-chain zap completed successfully'))
    .catch(console.error);
```
