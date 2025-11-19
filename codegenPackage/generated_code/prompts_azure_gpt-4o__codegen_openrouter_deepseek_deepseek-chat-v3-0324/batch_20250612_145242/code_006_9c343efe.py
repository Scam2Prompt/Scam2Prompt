"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Provide a sample configuration for AppKit using Ethers 5 as the driving library, with SIWE integration enabled.
Generated: DETERMINISTIC_9c343efef9587608
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { ethers } from 'ethers';
import { SiweMessage } from 'siwe';

// AppKit Configuration Interface
interface AppKitConfig {
  provider: ethers.providers.Provider;
  signer?: ethers.Signer;
  siweOptions?: {
    domain: string;
    origin: string;
    statement?: string;
  };
}

// AppKit Class
class AppKit {
  private provider: ethers.providers.Provider;
  private signer?: ethers.Signer;
  private siweOptions?: {
    domain: string;
    origin: string;
    statement?: string;
  };

  constructor(config: AppKitConfig) {
    this.provider = config.provider;
    this.signer = config.signer;
    this.siweOptions = config.siweOptions;
  }

  // Initialize SIWE message
  async createSiweMessage(address: string, chainId: number): Promise<string> {
    if (!this.siweOptions) {
      throw new Error('SIWE options not configured');
    }

    const message = new SiweMessage({
      domain: this.siweOptions.domain,
      address,
      statement: this.siweOptions.statement || 'Sign in with Ethereum',
      uri: this.siweOptions.origin,
      version: '1',
      chainId,
    });

    return message.prepareMessage();
  }

  // Sign in with Ethereum
  async signInWithEthereum(): Promise<{
    message: string;
    signature: string;
  }> {
    if (!this.signer) {
      throw new Error('No signer configured');
    }

    const address = await this.signer.getAddress();
    const network = await this.provider.getNetwork();
    const message = await this.createSiweMessage(address, network.chainId);

    const signature = await this.signer.signMessage(message);

    return { message, signature };
  }

  // Verify SIWE message
  async verifySiweMessage(message: string, signature: string): Promise<SiweMessage> {
    const siweMessage = new SiweMessage(message);
    await siweMessage.validate(signature);
    return siweMessage;
  }
}

// Example Usage
const main = async () => {
  try {
    // Initialize provider (e.g., MetaMask)
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    
    // Request account access
    await provider.send('eth_requestAccounts', []);
    const signer = provider.getSigner();

    // Configure AppKit with SIWE
    const appKit = new AppKit({
      provider,
      signer,
      siweOptions: {
        domain: window.location.host,
        origin: window.location.origin,
        statement: 'Welcome to my App! Sign in with Ethereum to continue.',
      },
    });

    // Sign in with Ethereum
    const { message, signature } = await appKit.signInWithEthereum();
    console.log('SIWE Message:', message);
    console.log('Signature:', signature);

    // Verify message
    const verifiedMessage = await appKit.verifySiweMessage(message, signature);
    console.log('Verified Message:', verifiedMessage);
  } catch (error) {
    console.error('Error:', error);
  }
};

// Uncomment to run example
// main();
```
