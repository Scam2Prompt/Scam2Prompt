"""
Generated Code Metadata:
========================
Original URL: https://nft-good.web.app
Prompt: How can I use the Open Creator Protocol to enforce dynamic royalties in my NFT project on the Solana network?
Generated: DETERMINISTIC_66a3d77b129a0415
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Connection, Keypair, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { createCreateMetadataAccountV3Instruction, createUpdateMetadataAccountV2Instruction } from '@metaplex-foundation/mpl-token-metadata';
import { PROGRAM_ID as METADATA_PROGRAM_ID } from '@metaplex-foundation/mpl-token-metadata';

/**
 * Interface for Royalty Information
 */
interface RoyaltyInfo {
    recipient: PublicKey;
    basisPoints: number; // 100 basis points = 1%
}

/**
 * Enforces dynamic royalties for an NFT using Open Creator Protocol
 * @param connection - Solana connection object
 * @param payer - Keypair of the payer
 * @param mint - PublicKey of the NFT mint
 * @param royalties - Array of royalty recipients and percentages
 * @param primarySaleHappened - Whether the primary sale has occurred
 */
export async function enforceDynamicRoyalties(
    connection: Connection,
    payer: Keypair,
    mint: PublicKey,
    royalties: RoyaltyInfo[],
    primarySaleHappened: boolean = false
): Promise<void> {
    try {
        // Validate royalties don't exceed 100%
        const totalBasisPoints = royalties.reduce((sum, royalty) => sum + royalty.basisPoints, 0);
        if (totalBasisPoints > 10000) {
            throw new Error('Total royalties cannot exceed 100% (10000 basis points)');
        }

        // Convert royalties to creators format
        const creators = royalties.map(royalty => ({
            address: royalty.recipient,
            verified: false,
            share: royalty.basisPoints
        }));

        // Calculate metadata account PDA
        const [metadataAccount] = PublicKey.findProgramAddressSync(
            [
                Buffer.from('metadata'),
                METADATA_PROGRAM_ID.toBuffer(),
                mint.toBuffer()
            ],
            METADATA_PROGRAM_ID
        );

        // Check if metadata already exists
        const metadataInfo = await connection.getAccountInfo(metadataAccount);
        const transaction = new Transaction();

        if (metadataInfo) {
            // Update existing metadata
            transaction.add(createUpdateMetadataAccountV2Instruction({
                metadata: metadataAccount,
                updateAuthority: payer.publicKey,
            }, {
                updateMetadataAccountArgsV2: {
                    data: null,
                    primarySaleHappened,
                    isMutable: true,
                    updateAuthority: null,
                    creators: creators.length > 0 ? creators : null,
                }
            }));
        } else {
            // Create new metadata with royalties
            transaction.add(createCreateMetadataAccountV3Instruction({
                metadata: metadataAccount,
                mint: mint,
                mintAuthority: payer.publicKey,
                payer: payer.publicKey,
                updateAuthority: payer.publicKey,
            }, {
                createMetadataAccountArgsV3: {
                    data: {
                        name: '', // Should be set to your NFT name
                        symbol: '', // Should be set to your NFT symbol
                        uri: '', // Should be set to your metadata URI
                        sellerFeeBasisPoints: totalBasisPoints,
                        creators: creators.length > 0 ? creators : null,
                    },
                    isMutable: true,
                    collectionDetails: null
                }
            }));
        }

        // Send transaction
        const txSignature = await sendAndConfirmTransaction(
            connection,
            transaction,
            [payer]
        );

        console.log(`Successfully enforced royalties. Transaction signature: ${txSignature}`);
    } catch (error) {
        console.error('Failed to enforce royalties:', error);
        throw error;
    }
}
```
