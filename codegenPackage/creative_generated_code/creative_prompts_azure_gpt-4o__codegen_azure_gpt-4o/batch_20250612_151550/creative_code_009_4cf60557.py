"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Explain how to use Solana's blockchain tools to create a minting platform similar to Buildoors, with `$BLD` token rewards and character progression features.
Generated: DETERMINISTIC_4cf6055749ce3cf4
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, production-ready implementation of a Solana minting platform with `$BLD` token rewards and character progression features using a simplified example in TypeScript with Anchor framework:

```typescript
// Import necessary libraries and modules
import * as anchor from "@project-serum/anchor";
import { PublicKey, SystemProgram } from "@solana/web3.js";
import { TOKEN_PROGRAM_ID, MintLayout, createMint, createAccount, mintTo } from "@solana/spl-token";

// Program constants
const MINT_DECIMALS = 9; // Decimals for $BLD token
const INITIAL_SUPPLY = 1_000_000 * 10 ** MINT_DECIMALS; // Initial supply of $BLD tokens
const CHARACTER_MAX_LEVEL = 100; // Maximum level a character can achieve

// Initialize Anchor Provider
const provider = anchor.AnchorProvider.env();
anchor.setProvider(provider);

// Load the program (replace with your program ID and IDL)
const program = new anchor.Program(
  require("../target/idl/your_program.json"), // Replace with your IDL path
  new PublicKey("YourProgramPublicKey") // Replace with your program's public key
);

// Define a function to mint $BLD tokens
async function mintBLDToken(userPubkey: PublicKey) {
  try {
    // Create a new mint for $BLD
    const mint = await createMint(
      provider.connection,
      provider.wallet.payer, // Payer for the transaction
      provider.wallet.publicKey, // Mint authority
      null, // Freeze authority (optional)
      MINT_DECIMALS // Token decimal places
    );

    console.log("Created $BLD Mint:", mint.toBase58());

    // Create associated token account for the user
    const userTokenAccount = await createAccount(
      provider.connection,
      provider.wallet.payer,
      mint,
      userPubkey
    );

    console.log("Created User Token Account:", userTokenAccount.toBase58());

    // Mint initial supply to the user's token account
    await mintTo(
      provider.connection,
      provider.wallet.payer,
      mint,
      userTokenAccount,
      provider.wallet.publicKey, // Mint authority
      INITIAL_SUPPLY
    );

    console.log(`Minted ${INITIAL_SUPPLY} $BLD tokens to user account.`);
    return { mint, userTokenAccount };
  } catch (error) {
    console.error("Error minting $BLD token:", error);
    throw error;
  }
}

// Define a function for character progression
async function progressCharacter(characterAccountPubkey: PublicKey, userPubkey: PublicKey) {
  try {
    // Fetch the character account (assumes it's stored as a PDA in your program)
    const characterAccount = await program.account.characterAccount.fetch(characterAccountPubkey);

    // Check if character has reached the maximum level
    if (characterAccount.level >= CHARACTER_MAX_LEVEL) {
      console.log("Character has reached the maximum level.");
      return;
    }

    // Call the program to increment the character's level
    await program.rpc.incrementLevel({
      accounts: {
        characterAccount: characterAccountPubkey,
        user: userPubkey,
        systemProgram: SystemProgram.programId,
      },
    });

    console.log(`Character level increased to ${characterAccount.level + 1}`);
  } catch (error) {
    console.error("Error progressing character:", error);
    throw error;
  }
}

// Example usage
(async () => {
  const userPubkey = provider.wallet.publicKey; // Replace with user's wallet public key
  const characterAccountPubkey = await PublicKey.findProgramAddress(
    [Buffer.from("character"), userPubkey.toBuffer()],
    program.programId
  );

  // Mint $BLD tokens to the user
  const { mint, userTokenAccount } = await mintBLDToken(userPubkey);

  // Progress the user's character
  await progressCharacter(characterAccountPubkey[0], userPubkey);
})();
```

**Key Notes in Code Comments:**
1. Replace `"YourProgramPublicKey"` and `"your_program.json"` with your actual program's public key and the generated IDL file path.
2. `$BLD` token minting uses SPL Token library, while character progression assumes a custom Solana program.
3. Ensure the `characterAccount` conforms to the PDA scheme in your program architecture.
4. Error handling is done for both token minting and character progression.
