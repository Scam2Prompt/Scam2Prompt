"""
Generated Code Metadata:
========================
Original URL: https://raydium-ui-v3-inner-5sgvrxxmt-raydium.vercel.app
Prompt: How do I implement order routing for token swaps using Raydium's features?
Generated: DETERMINISTIC_4b233b086e917ac8
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Connection, Keypair, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';
import { Liquidity, LiquidityPoolKeys, LiquidityAssociatedPoolKeys } from '@raydium-io/raydium-sdk';
import { Wallet } from '@project-serum/anchor';

/**
 * Order routing for token swaps using Raydium's liquidity pools
 */
export class RaydiumSwapRouter {
    private connection: Connection;
    private wallet: Wallet;

    /**
     * Initialize the swap router with a Solana connection and wallet
     * @param connection Solana connection
     * @param wallet User wallet
     */
    constructor(connection: Connection, wallet: Wallet) {
        this.connection = connection;
        this.wallet = wallet;
    }

    /**
     * Find the best liquidity pool for a token pair
     * @param tokenA Mint address of token A
     * @param tokenB Mint address of token B
     * @returns Best liquidity pool keys or null if none found
     */
    private async findBestPool(tokenA: PublicKey, tokenB: PublicKey): Promise<LiquidityPoolKeys | null> {
        try {
            const pools = await Liquidity.getAssociatedPools({
                connection: this.connection,
                programId: Liquidity.RAYDIUM_LIQUIDITY_PROGRAM_ID,
                mints: {
                    mintA: tokenA,
                    mintB: tokenB,
                },
            });

            if (pools.length === 0) return null;

            // Sort by liquidity (descending) to find the most liquid pool
            pools.sort((a, b) => b.liquidity.sub(a.liquidity).toNumber());
            return pools[0].poolKeys;
        } catch (error) {
            console.error('Error finding liquidity pool:', error);
            return null;
        }
    }

    /**
     * Execute a token swap through Raydium
     * @param inputToken Input token mint
     * @param outputToken Output token mint
     * @param amountIn Amount of input tokens to swap
     * @param slippage Slippage tolerance (0.01 for 1%)
     * @returns Transaction ID
     * @throws Error if swap fails
     */
    public async swap(
        inputToken: PublicKey,
        outputToken: PublicKey,
        amountIn: number,
        slippage: number = 0.01
    ): Promise<string> {
        try {
            // Validate inputs
            if (amountIn <= 0) throw new Error('Amount must be positive');
            if (slippage < 0 || slippage > 1) throw new Error('Slippage must be between 0 and 1');

            // Find the best pool for the token pair
            const poolKeys = await this.findBestPool(inputToken, outputToken);
            if (!poolKeys) throw new Error('No liquidity pool found for this token pair');

            // Get token accounts
            const userInputTokenAccount = await Token.getAssociatedTokenAddress(
                TOKEN_PROGRAM_ID,
                inputToken,
                this.wallet.publicKey
            );
            const userOutputTokenAccount = await Token.getAssociatedTokenAddress(
                TOKEN_PROGRAM_ID,
                outputToken,
                this.wallet.publicKey
            );

            // Create swap instruction
            const swapInstruction = await Liquidity.makeSwapInstruction({
                poolKeys,
                userKeys: {
                    tokenAccountIn: userInputTokenAccount,
                    tokenAccountOut: userOutputTokenAccount,
                    owner: this.wallet.publicKey,
                },
                amountIn,
                minAmountOut: 0, // Will be calculated based on slippage
                fixedSide: 'in',
                connection: this.connection,
            });

            // Build and send transaction
            const transaction = new Transaction().add(swapInstruction);
            transaction.feePayer = this.wallet.publicKey;
            transaction.recentBlockhash = (await this.connection.getRecentBlockhash()).blockhash;

            const signedTx = await this.wallet.signTransaction(transaction);
            const txId = await sendAndConfirmTransaction(this.connection, signedTx, []);

            return txId;
        } catch (error) {
            console.error('Swap failed:', error);
            throw new Error(`Swap failed: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    /**
     * Get the estimated output amount for a swap
     * @param inputToken Input token mint
     * @param outputToken Output token mint
     * @param amountIn Amount of input tokens
     * @returns Estimated output amount and price impact
     */
    public async getSwapQuote(
        inputToken: PublicKey,
        outputToken: PublicKey,
        amountIn: number
    ): Promise<{ amountOut: number; priceImpact: number }> {
        try {
            const poolKeys = await this.findBestPool(inputToken, outputToken);
            if (!poolKeys) throw new Error('No liquidity pool found for this token pair');

            const quote = await Liquidity.computeAmountOut({
                poolKeys,
                amountIn,
                currencyIn: inputToken,
                currencyOut: outputToken,
                slippage: 0,
            });

            return {
                amountOut: quote.amountOut.toNumber(),
                priceImpact: quote.priceImpact,
            };
        } catch (error) {
            console.error('Error getting swap quote:', error);
            throw new Error(`Failed to get swap quote: ${error instanceof Error ? error.message : String(error)}`);
        }
    }
}
```
