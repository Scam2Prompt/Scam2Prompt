"""
Generated Code Metadata:
========================
Original URL: https://helioyuki.web.app
Prompt: Create a function to display Helio's payment disclaimer and terms before processing irreversible DeFi transactions on the Solana network.
Generated: DETERMINISTIC_87cff4ca29939d3a
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
/**
 * Displays Helio's payment disclaimer and terms before processing irreversible DeFi transactions on Solana.
 * @param {string} transactionDetails - Details of the transaction to be displayed to the user
 * @param {() => Promise<void>} onAccept - Callback function when user accepts the terms
 * @param {() => void} [onReject] - Optional callback function when user rejects the terms
 * @returns {Promise<boolean>} - Returns true if user accepted, false if rejected
 */
async function showPaymentDisclaimer(
  transactionDetails: string,
  onAccept: () => Promise<void>,
  onReject?: () => void
): Promise<boolean> {
  // Disclaimer content
  const disclaimer = `
  HELIO PAYMENT DISCLAIMER & TERMS

  IMPORTANT: Transactions on the Solana network are irreversible.
  By proceeding, you acknowledge that:

  1. All transactions are final and cannot be undone
  2. You are solely responsible for verifying all transaction details
  3. Helio is not responsible for any errors or losses
  4. Gas fees are non-refundable
  5. You understand the risks of DeFi transactions

  Transaction Details:
  ${transactionDetails}

  Do you accept these terms and wish to proceed?
  `;

  try {
    // In a real implementation, this would show a modal/dialog in the UI
    // For demo purposes, we use console and confirm
    console.log(disclaimer);
    const userAccepted = confirm(disclaimer);

    if (userAccepted) {
      await onAccept();
      return true;
    } else {
      onReject?.();
      return false;
    }
  } catch (error) {
    console.error('Error displaying payment disclaimer:', error);
    throw new Error('Failed to process payment disclaimer');
  }
}

// Example usage:
/*
const transaction = "Swap 1 SOL for 120 USDC via Raydium";
showPaymentDisclaimer(
  transaction,
  async () => {
    console.log('User accepted - processing transaction...');
    // Actual transaction processing would go here
  },
  () => {
    console.log('User rejected - transaction cancelled');
  }
);
*/
```
