"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Create a Next.js application page that allows users to connect their Solana wallet, select input and output tokens, and submit a form to initiate value averaging deposits.
Generated: DETERMINISTIC_eaf7f7415b8ad09c
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/value-averaging-deposit.js

import { useState } from 'react';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { useWallet } from '@solana/wallet-adapter-react';
import { PublicKey } from '@solana/web3.js';

// Import necessary React packages for Solana Wallet management
export default function ValueAveragingDeposit() {
  // State variables
  const { connected, publicKey } = useWallet();
  const [inputToken, setInputToken] = set ( '' );'selection.status
