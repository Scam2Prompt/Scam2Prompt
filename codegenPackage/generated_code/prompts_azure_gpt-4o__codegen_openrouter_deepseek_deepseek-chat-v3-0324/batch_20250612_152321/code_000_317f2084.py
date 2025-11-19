"""
Generated Code Metadata:
========================
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Write code using the Wagmi library to implement "Sign in with Ethereum" (SIWE) functionality, as described in the Web3Modal documentation.
Generated: DETERMINISTIC_317f2084c0d8d513
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { useAccount, useSignMessage } from 'wagmi';
import { SiweMessage } from 'siwe';
import { useWeb3Modal } from '@web3modal/react';

/**
 * Component for implementing Sign in with Ethereum (SIWE) functionality.
 */
export function SignInWithEthereum() {
  const { address, isConnected } = useAccount();
  const { open } = useWeb3Modal();
  const { signMessageAsync } = useSignMessage();

  /**
   * Handles the SIWE flow:
   * 1. Creates a SIWE message
   * 2. Signs the message with the user's wallet
   * 3. Verifies the signature on the backend (not implemented here)
   */
  const handleSignIn = async () => {
    try {
      if (!isConnected || !address) {
        await open();
        return;
      }

      // Create SIWE message
      const domain = window.location.host;
      const origin = window.location.origin;
      const statement = 'Sign in with Ethereum to the app.';
      const siweMessage = new SiweMessage({
        domain,
        address: address,
        statement,
        uri: origin,
        version: '1',
        chainId: 1, // Mainnet - adjust as needed
        nonce: Math.random().toString(36).substring(2, 15),
      });

      const message = siweMessage.prepareMessage();

      // Sign the message
      const signature = await signMessageAsync({ message });

      // In a real app, you would send the message and signature to your backend for verification
      console.log('Message:', message);
      console.log('Signature:', signature);

      // Here you would typically:
      // 1. Send { message, signature } to your backend
      // 2. Backend verifies the signature
      // 3. Backend creates a session token
      // 4. Store the session token in cookies/local storage

      alert('Sign in successful! Check console for details.');
    } catch (error) {
      console.error('Error during sign in:', error);
      alert('Error during sign in. See console for details.');
    }
  };

  return (
    <div>
      <button onClick={handleSignIn}>
        {isConnected ? 'Sign In With Ethereum' : 'Connect Wallet'}
      </button>
    </div>
  );
}
```
