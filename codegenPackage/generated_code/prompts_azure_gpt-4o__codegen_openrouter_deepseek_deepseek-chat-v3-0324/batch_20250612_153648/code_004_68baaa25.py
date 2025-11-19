"""
Generated Code Metadata:
========================
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Suggest an approach to integrate animation tools with NFT creation and management in a Next.js project.
Generated: DETERMINISTIC_68baaa25ae72cd5a
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/api/nft/create.js
import { ThirdwebSDK } from "@thirdweb-dev/sdk";
import { NextApiRequest, NextApiResponse } from "next";
import fs from "fs";
import path from "path";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    // Initialize SDK with private key and network
    const sdk = ThirdwebSDK.fromPrivateKey(
      process.env.PRIVATE_KEY as string,
      "polygon" // or your preferred network
    );

    // Parse animation file and metadata from request
    const { animationFile, name, description } = req.body;

    // Validate required fields
    if (!animationFile || !name || !description) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    // Save animation file temporarily
    const tempFilePath = path.join("/tmp", `${Date.now()}.gif`);
    fs.writeFileSync(tempFilePath, Buffer.from(animationFile, "base64"));

    // Upload animation to IPFS
    const animationUri = await sdk.storage.upload(tempFilePath);

    // Create NFT metadata
    const metadata = {
      name,
      description,
      image: animationUri,
      animation_url: animationUri,
    };

    // Upload metadata to IPFS
    const metadataUri = await sdk.storage.upload(metadata);

    // Get NFT Collection contract
    const contract = await sdk.getContract(
      process.env.NFT_COLLECTION_ADDRESS as string,
      "nft-collection"
    );

    // Mint NFT with metadata
    const tx = await contract.mintTo(process.env.WALLET_ADDRESS as string, {
      name,
      description,
      image: animationUri,
      animation_url: animationUri,
    });

    // Clean up temp file
    fs.unlinkSync(tempFilePath);

    return res.status(200).json({
      success: true,
      tokenId: tx.id,
      metadataUri,
      animationUri,
    });
  } catch (error) {
    console.error("NFT creation error:", error);
    return res.status(500).json({ error: "Failed to create NFT" });
  }
}
```

```javascript
// components/AnimationNFTMinter.jsx
import { useState, useRef } from "react";
import { useAddress, useContract, useNFTs } from "@thirdweb-dev/react";
import { Web3Button } from "@thirdweb-dev/react";

export default function AnimationNFTMinter() {
  const [animationFile, setAnimationFile] = useState(null);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [previewUrl, setPreviewUrl] = useState("");
  const fileInputRef = useRef(null);
  const address = useAddress();

  // Connect to NFT Collection contract
  const { contract } = useContract(process.env.NEXT_PUBLIC_NFT_COLLECTION_ADDRESS);
  const { data: nfts, isLoading } = useNFTs(contract);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Validate file type (GIF, MP4, WebM, etc.)
    const validTypes = ["image/gif", "video/mp4", "video/webm"];
    if (!validTypes.includes(file.type)) {
      alert("Please upload a GIF, MP4, or WebM file");
      return;
    }

    setAnimationFile(file);
    setPreviewUrl(URL.createObjectURL(file));
  };

  const handleSubmit = async (contract) => {
    if (!animationFile || !name || !description) {
      alert("Please fill all fields and upload an animation");
      return;
    }

    try {
      // Read file as base64
      const reader = new FileReader();
      reader.readAsDataURL(animationFile);
      reader.onload = () => {
        const base64Data = reader.result.split(",")[1];
        // The Web3Button will handle the transaction
      };
    } catch (error) {
      console.error("Error processing animation:", error);
    }
  };

  return (
    <div className="container">
      <h1>Create Animated NFT</h1>
      
      <div className="form-group">
        <label>Animation File (GIF/MP4/WebM)</label>
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileChange}
          accept="image/gif,video/mp4,video/webm"
        />
      </div>

      {previewUrl && (
        <div className="preview">
          {animationFile.type === "image/gif" ? (
            <img src={previewUrl} alt="Preview" style={{ maxWidth: "300px" }} />
          ) : (
            <video controls style={{ maxWidth: "300px" }}>
              <source src={previewUrl} type={animationFile.type} />
            </video>
          )}
        </div>
      )}

      <div className="form-group">
        <label>Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Description</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>

      <Web3Button
        contractAddress={process.env.NEXT_PUBLIC_NFT_COLLECTION_ADDRESS}
        action={handleSubmit}
        onSuccess={() => {
          alert("NFT created successfully!");
          setAnimationFile(null);
          setName("");
          setDescription("");
          setPreviewUrl("");
          if (fileInputRef.current) fileInputRef.current.value = "";
        }}
      >
        Mint Animated NFT
      </Web3Button>

      <div className="nft-list">
        <h2>Your NFTs</h2>
        {isLoading ? (
          <p>Loading...</p>
        ) : (
          <div className="grid">
            {nfts
              ?.filter((nft) => nft.owner === address)
              ?.map((nft) => (
                <div key={nft.metadata.id} className="nft-card">
                  {nft.metadata.animation_url ? (
                    <video controls>
                      <source src={nft.metadata.animation_url} />
                    </video>
                  ) : (
                    <img src={nft.metadata.image} alt={nft.metadata.name} />
                  )}
                  <h3>{nft.metadata.name}</h3>
                  <p>{nft.metadata.description}</p>
                </div>
              ))}
          </div>
        )}
      </div>
    </div>
  );
}
```

```javascript
// pages/_app.js
import { ThirdwebProvider, ChainId } from "@thirdweb-dev/react";
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  return (
    <ThirdwebProvider
      desiredChainId={ChainId.Polygon}
      authConfig={{
        authUrl: "/api/auth",
        domain: process.env.NEXT_PUBLIC_THIRDWEB_AUTH_DOMAIN,
      }}
    >
      <Component {...pageProps} />
    </ThirdwebProvider>
  );
}

export default MyApp;
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ["ipfs.io", "thirdweb.infura-ipfs.io"],
  },
};

module.exports = nextConfig;
```

```javascript
// .env.local
PRIVATE_KEY=your_wallet_private_key
NFT_COLLECTION_ADDRESS=your_nft_collection_contract_address
WALLET_ADDRESS=your_wallet_address
NEXT_PUBLIC_NFT_COLLECTION_ADDRESS=your_nft_collection_contract_address
NEXT_PUBLIC_THIRDWEB_AUTH_DOMAIN=your_domain.com
```
