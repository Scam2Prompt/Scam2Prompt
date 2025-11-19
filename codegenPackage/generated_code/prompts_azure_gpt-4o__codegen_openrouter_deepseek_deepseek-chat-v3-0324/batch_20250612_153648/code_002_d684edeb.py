"""
Generated Code Metadata:
========================
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Generate a Next.js component that allows users to connect their Solana wallet and display their NFT assets.
Generated: DETERMINISTIC_d684edebacd3fe5a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
import { useConnection, useWallet } from '@solana/wallet-adapter-react';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { PublicKey } from '@solana/web3.js';
import { Metadata } from '@metaplex-foundation/mpl-token-metadata';
import { useEffect, useState } from 'react';
import { Connection } from '@solana/web3.js';

interface NFT {
  name: string;
  image: string;
  description: string;
}

const NFTGallery = () => {
  const { connection } = useConnection();
  const { publicKey, connected } = useWallet();
  const [nfts, setNfts] = useState<NFT[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!publicKey || !connected) {
      setNfts([]);
      return;
    }

    const fetchNFTs = async () => {
      setLoading(true);
      setError(null);

      try {
        const nfts = await getNFTsForOwner(connection, publicKey);
        setNfts(nfts);
      } catch (err) {
        console.error('Error fetching NFTs:', err);
        setError('Failed to fetch NFTs. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchNFTs();
  }, [publicKey, connected, connection]);

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">My NFT Gallery</h1>
        <WalletMultiButton className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded" />
      </div>

      {!connected ? (
        <div className="text-center py-12">
          <p className="text-xl mb-4">Please connect your wallet to view your NFTs</p>
        </div>
      ) : loading ? (
        <div className="text-center py-12">
          <p className="text-xl">Loading your NFTs...</p>
        </div>
      ) : error ? (
        <div className="text-center py-12">
          <p className="text-xl text-red-500">{error}</p>
        </div>
      ) : nfts.length === 0 ? (
        <div className="text-center py-12">
          <p className="text-xl">No NFTs found in your wallet</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {nfts.map((nft, index) => (
            <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden">
              <img
                src={nft.image}
                alt={nft.name}
                className="w-full h-48 object-cover"
                onError={(e) => {
                  (e.target as HTMLImageElement).src = '/placeholder-nft.png';
                }}
              />
              <div className="p-4">
                <h3 className="font-bold text-lg mb-2">{nft.name}</h3>
                <p className="text-gray-600">{nft.description}</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

async function getNFTsForOwner(connection: Connection, owner: PublicKey): Promise<NFT[]> {
  // Get all tokens owned by the user
  const tokenAccounts = await connection.getTokenAccountsByOwner(owner, {
    programId: new PublicKey('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'),
  });

  const nfts: NFT[] = [];

  for (const account of tokenAccounts.value) {
    try {
      // Check if the token is an NFT (amount = 1 and decimals = 0)
      const tokenInfo = await connection.getTokenAccountBalance(account.pubkey);
      if (tokenInfo.value.amount !== '1' || tokenInfo.value.decimals !== 0) continue;

      // Get the mint address
      const mint = new PublicKey(account.account.data.slice(0, 32));

      // Get the metadata account
      const metadataPDA = await Metadata.getPDA(mint);
      const metadataAccount = await connection.getAccountInfo(metadataPDA);

      if (!metadataAccount?.data) continue;

      // Parse the metadata
      const metadata = Metadata.deserialize(metadataAccount.data);
      const { name, symbol, uri } = metadata[0].data;

      // Fetch the off-chain metadata
      const response = await fetch(uri);
      const offChainMetadata = await response.json();

      nfts.push({
        name: name || symbol || 'Untitled',
        image: offChainMetadata.image || '',
        description: offChainMetadata.description || '',
      });
    } catch (err) {
      console.error(`Error processing token account ${account.pubkey}:`, err);
    }
  }

  return nfts;
}

export default NFTGallery;
```
