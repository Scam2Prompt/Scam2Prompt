"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Generate a Next.js component that allows users to connect their Solana wallet and display their NFT assets.
Generated: DETERMINISTIC_d684edebacd3fe5a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/SolanaWalletNFTs.js
import { useState, useEffect } from "react";
import { Connection, PublicKey } from "@solana/web3.js";
import { Metadata } from "@metaplex-foundation/mpl-token-metadata";
import { WalletAdapterNetwork } from "@solana/wallet-adapter-base";
import { WalletModalProvider, WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import { useWallet } from "@solana/wallet-adapter-react";
import { clusterApiUrl } from "@solana/web3.js";

// CSS for the wallet button
import "@solana/wallet-adapter-react-ui/styles.css";

// Constants
const SOLANA_NETWORK = WalletAdapterNetwork.Mainnet; // Use Mainnet by default
const CONNECTION_URL = clusterApiUrl(SOLANA_NETWORK);

export default function SolanaWalletNFTs() {
  const wallet = useWallet(); // Access wallet state from Solana Wallet Adapter
  const [nfts, setNfts] = useState([]); // State to hold NFT metadata
  const [loading, setLoading] = useState(false); // State for loading status

  /**
   * Fetch NFTs for a given wallet address.
   * @param {string} walletAddress
   */
  const fetchNFTs = async (walletAddress) => {
    setLoading(true); // Start loading
    try {
      const connection = new Connection(CONNECTION_URL, "confirmed");
      const publicKey = new PublicKey(walletAddress);

      // Fetch all tokens owned by the wallet
      const tokenAccounts = await connection.getParsedTokenAccountsByOwner(publicKey, {
        programId: new PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
      });

      const nftMetadata = [];
      for (let tokenAccount of tokenAccounts.value) {
        const tokenAmount = tokenAccount.account.data.parsed.info.tokenAmount;
        
        // Check if the token is an NFT (amount = 1 and decimals = 0)
        if (tokenAmount.amount === "1" && tokenAmount.decimals === 0) {
          const mintAddress = tokenAccount.account.data.parsed.info.mint;

          // Fetch metadata for the NFT
          const metadataPDA = await Metadata.getPDA(new PublicKey(mintAddress));
          const metadataAccount = await connection.getAccountInfo(metadataPDA);
          if (metadataAccount) {
            const metadata = Metadata.deserialize(metadataAccount.data);
            nftMetadata.push(metadata.data);
          }
        }
      }

      setNfts(nftMetadata); // Update NFT state
    } catch (error) {
      console.error("Error fetching NFTs:", error);
      alert("Failed to fetch NFTs. Please try again later.");
    } finally {
      setLoading(false); // End loading
    }
  };

  // Effect to fetch NFTs when wallet connects and disconnects
  useEffect(() => {
    if (wallet.connected && wallet.publicKey) {
      fetchNFTs(wallet.publicKey.toString());
    } else {
      setNfts([]); // Clear NFTs if wallet disconnects
    }
  }, [wallet.connected, wallet.publicKey]);

  return (
    <div>
      <h1>Solana Wallet NFT Viewer</h1>
      {/* Wallet connection button */}
      <WalletModalProvider>
        <WalletMultiButton />
      </WalletModalProvider>

      {/* Display loading indicator */}
      {loading && <p>Loading...</p>}

      {/* Display NFTs */}
      {!loading && nfts.length > 0 ? (
        <div>
          <h2>Your NFTs:</h2>
          <ul>
            {nfts.map((nft, index) => (
              <li key={index}>
                <p><strong>Name:</strong> {nft.name}</p>
                <p><strong>Symbol:</strong> {nft.symbol}</p>
                {nft.uri && (
                  <p>
                    <strong>Metadata URI:</strong>{" "}
                    <a href={nft.uri} target="_blank" rel="noopener noreferrer">
                      {nft.uri}
                    </a>
                  </p>
                )}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        !loading && <p>No NFTs found.</p>
      )}
    </div>
  );
}
```

### Notes:
1. Ensure that `@solana/web3.js`, `@metaplex-foundation/mpl-token-metadata`, and `@solana/wallet-adapter-*` dependencies are installed in your project.
2. Use `npm install` or `yarn add` to install the required packages:
   ```
   npm install @solana/web3.js @metaplex-foundation/mpl-token-metadata \
               @solana/wallet-adapter-react @solana/wallet-adapter-react-ui \
               @solana/wallet-adapter-base
   ```
