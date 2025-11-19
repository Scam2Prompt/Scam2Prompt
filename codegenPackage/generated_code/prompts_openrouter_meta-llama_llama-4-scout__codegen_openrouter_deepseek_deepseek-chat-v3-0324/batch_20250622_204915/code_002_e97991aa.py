"""
Generated Code Metadata:
========================
Original URL: https://smog-token-st.web.app
Prompt: Develop a step-by-step guide on how to participate in the $SMOG airdrop on Solana, including buying and holding tokens, and completing tasks on Zealy.
Generated: DETERMINISTIC_e97991aa2dd1926d
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting a step-by-step guide rather than executable code, I'll provide a structured markdown document that could be used in a codebase's documentation (e.g., README.md). Here's the production-ready documentation:

```markdown
# $SMOG Airdrop Participation Guide

## Prerequisites
- A Solana-compatible wallet (e.g., Phantom, Solflare)
- SOL tokens for gas fees
- Zealy account (formerly Crew3)

## Step 1: Set Up Your Wallet
1. Install a Solana wallet extension (e.g., Phantom)
2. Create a new wallet or import an existing one
3. Ensure you have enough SOL for transactions (~0.1 SOL recommended)

## Step 2: Acquire $SMOG Tokens
```javascript
// Example: Buying SMOG on Raydium
const buySmog = async (amountInSOL) => {
  try {
    // Connect wallet
    const provider = getWalletProvider(); // Implement wallet connection
    const connection = new Connection(CLUSTER_URL);
    
    // Get SMOG token info
    const smogToken = new PublicKey(SMOG_TOKEN_MINT);
    
    // Create swap transaction
    const swapTx = await RaydiumSwap.swap(
      connection,
      provider,
      NATIVE_SOL.mint, // SOL
      smogToken,
      amountInSOL,
      0.5 // Slippage %
    );
    
    // Send transaction
    const txHash = await sendTransaction(swapTx);
    console.log(`Transaction successful: ${txHash}`);
  } catch (error) {
    console.error('Transaction failed:', error);
    throw new Error('Failed to buy SMOG tokens');
  }
};
```

## Step 3: Hold $SMOG Tokens
- Maintain a minimum balance (check airdrop requirements)
- Avoid transferring out during qualification period

## Step 4: Complete Zealy Tasks
```javascript
// Example: Automating Zealy task completion (conceptual)
const completeZealyTasks = async (walletAddress) => {
  try {
    // Authenticate with Zealy API
    const auth = await zealyAuth(API_KEY);
    
    // Get available tasks
    const tasks = await getTasks(auth, 'smog-quest');
    
    // Complete each task
    for (const task of tasks) {
      if (task.status === 'available') {
        await submitTaskProof(auth, task.id, {
          wallet: walletAddress,
          proof: generateProof(walletAddress, task)
        });
      }
    }
    
    console.log('All tasks completed successfully');
  } catch (error) {
    console.error('Task completion failed:', error);
    throw new Error('Failed to complete Zealy tasks');
  }
};
```

## Step 5: Verify Eligibility
1. Check your wallet address on the official $SMOG airdrop dashboard
2. Confirm completed tasks show as verified on Zealy

## Step 6: Claim Your Airdrop
```javascript
// Example: Claiming airdrop (when live)
const claimAirdrop = async () => {
  try {
    const provider = getWalletProvider();
    const program = new Program(SMOG_AIRDROP_IDL, SMOG_PROGRAM_ID, provider);
    
    const tx = await program.methods
      .claim()
      .accounts({
        claimant: provider.wallet.publicKey,
        airdropAccount: AIRDROP_ACCOUNT_PDA,
      })
      .rpc();
    
    console.log(`Airdrop claimed: ${tx}`);
  } catch (error) {
    console.error('Claim failed:', error);
    throw new Error('Failed to claim airdrop');
  }
};
```

## Important Notes
- Always use official links (beware of phishing)
- Never share your private key
- Transaction fees apply for all on-chain actions
```
