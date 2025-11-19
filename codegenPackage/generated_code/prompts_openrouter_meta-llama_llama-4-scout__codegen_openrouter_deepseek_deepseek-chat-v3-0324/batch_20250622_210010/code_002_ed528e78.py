"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-ibw3fg6lj-reown-com.vercel.app
Prompt: "Generate code for a SIWE configuration using ethers and implementing sign-in with Ethereum for AppKit."
Generated: DETERMINISTIC_ed528e78ab4eeb5b
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { ethers } from "ethers";
import { SiweMessage } from "siwe";

/**
 * SIWE Configuration for AppKit
 */
export class SiweConfig {
  private provider: ethers.providers.Web3Provider;
  private signer: ethers.Signer;
  private domain: string;
  private origin: string;

  /**
   * Initialize SIWE configuration
   * @param provider - Ethers Web3Provider instance
   * @param domain - Domain for SIWE message
   * @param origin - Origin of the application
   */
  constructor(
    provider: ethers.providers.Web3Provider,
    domain: string,
    origin: string
  ) {
    this.provider = provider;
    this.signer = provider.getSigner();
    this.domain = domain;
    this.origin = origin;
  }

  /**
   * Create a SIWE message and sign it
   * @param address - Ethereum address of the user
   * @param statement - Optional statement to include in the message
   * @returns Promise resolving to the signed message
   */
  async createSiweMessage(
    address: string,
    statement?: string
  ): Promise<string> {
    try {
      const nonce = await this.getNonce();
      const message = new SiweMessage({
        domain: this.domain,
        address,
        statement,
        uri: this.origin,
        version: "1",
        chainId: await this.signer.getChainId(),
        nonce,
      });

      const messageToSign = message.prepareMessage();
      const signature = await this.signer.signMessage(messageToSign);

      return JSON.stringify({ message: messageToSign, signature });
    } catch (error) {
      throw new Error(`Failed to create SIWE message: ${error.message}`);
    }
  }

  /**
   * Generate a nonce for SIWE message
   * @returns Promise resolving to a random nonce
   */
  private async getNonce(): Promise<string> {
    try {
      return ethers.utils.hexlify(ethers.utils.randomBytes(32));
    } catch (error) {
      throw new Error(`Failed to generate nonce: ${error.message}`);
    }
  }

  /**
   * Verify a SIWE message
   * @param message - The SIWE message to verify
   * @param signature - The signature to verify against
   * @returns Promise resolving to verification result
   */
  async verifySiweMessage(
    message: string,
    signature: string
  ): Promise<SiweMessage> {
    try {
      const siweMessage = new SiweMessage(message);
      await siweMessage.validate(signature);
      return siweMessage;
    } catch (error) {
      throw new Error(`Failed to verify SIWE message: ${error.message}`);
    }
  }
}
```
try {
      return await this.config.signer.signMessage(message);
    } catch (error) {
      console.error("Failed to sign message:", error);
      throw error;
    }
  }
}
```
