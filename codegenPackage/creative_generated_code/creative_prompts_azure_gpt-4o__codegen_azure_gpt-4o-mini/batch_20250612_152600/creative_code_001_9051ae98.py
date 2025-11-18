"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-n76z148gg-reown-com.vercel.app
Prompt: Generate a sample implementation for "Sign In with Ethereum" (SIWE) using the AppKit library and Ethers as the driving library.
Generated: DETERMINISTIC_9051ae98a23a7544
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { SigninWithEthereum } from 'siwe';
import { ethers } from 'ethers';

// Define a class to handle Sign In with Ethereum
class EthereumAuthenticator {
    constructor() {
        // Initialize provider and signer
        this.provider = new ethers.providers.Web3Provider(window.ethereum);
        this.signer = this.provider.getSigner();
    }

    // Method to request user account access
    async requestAccount() {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Account access granted');
        } catch (error) {
            console.error('Error requesting account access:', error);
            throw new Error('Account access denied');
        }
    }

    // Method to create and sign the SIWE message
    async signIn(domain, statement) {
        try {
            // Ensure the user has granted account access
            await this.requestAccount();

            // Get the user's address
            const address = await this.signer.getAddress();
            const nonce = Math.floor(Math.random() * 1000000); // Generate a random nonce

            // Create the SIWE message
            const siweMessage = new SigninWithEthereum({
                domain: domain,
                address: address,
                statement: statement,
                nonce: nonce.toString(),
                uri: window.location.origin,
                version: '1',
                chainId: await this.provider.getNetwork().then(network => network.chainId),
                expirationTime: new Date(Date.now() + 60 * 60 * 1000).toISOString(), // 1 hour expiration
            });

            // Sign the SIWE message
            const signature = await this.signer.signMessage(siweMessage.prepareMessage());
            return {
                address: address,
                signature: signature,
                nonce: nonce,
                siweMessage: siweMessage,
            };
        } catch (error) {
            console.error('Error signing in:', error);
            throw new Error('Sign in failed');
        }
    }
}

// Example usage
(async () => {
    const authenticator = new EthereumAuthenticator();
    const domain = 'example.com';
    const statement = 'Sign in to access the application.';

    try {
        const signInData = await authenticator.signIn(domain, statement);
        console.log('Successfully signed in:', signInData);
        // Here you would typically send the sign-in data to your backend for verification
    } catch (error) {
        console.error('Sign in error:', error.message);
    }
})();
```
