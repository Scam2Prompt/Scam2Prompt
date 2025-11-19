"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Write a code snippet to implement financial literacy tools for kids using Next.js and NFTs.
Generated: DETERMINISTIC_4b4c0bda9f3cc03d
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js
import { useEffect, useState } from 'react';
import Head from 'next/head';
import Web3 from 'web3';

// Financial Literacy NFT Minting Component
const MintNFT = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [minting, setMinting] = useState(false);
    const [error, setError] = useState('');

    // Initialize Web3 and fetch user account
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                try {
                    const accounts = await web3Instance.eth.requestAccounts();
                    setAccount(accounts[0]);
                } catch (err) {
                    setError('Failed to fetch accounts. Ensure you have MetaMask installed.');
                    console.error(err);
                }
            } else {
                setError('Ethereum provider not found. Please install MetaMask.');
            }
        };

        initWeb3();
    }, []);

    // Function to mint NFT
    const mintNFT = async () => {
        if (!web3 || !account) {
            setError('Web3 or account not initialized.');
            return;
        }

        setMinting(true);
        setError('');

        try {
            // NFT minting logic goes here (dummy example)
            const txHash = await web3.eth.sendTransaction({
                from: account,
                to: '0xYourNFTContractAddress',
                value: web3.utils.toWei('0.01', 'ether'), // Assuming a minting cost
            });

            console.log('Transaction Hash:', txHash);
            alert('NFT minted successfully!');
        } catch (err) {
            setError('Minting failed. Please try again.');
            console.error(err);
        } finally {
            setMinting(false);
        }
    };

    return (
        <div>
            <Head>
                <title>Financial Literacy Tools for Kids</title>
                <meta name="description" content="Mint your Financial Literacy NFTs!" />
            </Head>

            <h1>Financial Literacy Tools for Kids</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Your account: {account}</p>
                    <button onClick={mintNFT} disabled={minting}>
                        {minting ? 'Minting...' : 'Mint NFT'}
                    </button>
                </div>
            ) : (
                <p>Please connect your MetaMask wallet.</p>
            )}
        </div>
    );
};

export default MintNFT;
```

```javascript
// pages/_app.js
import '../styles/globals.css';

// Custom App to include global styles
function MyApp({ Component, pageProps }) {
    return <Component {...pageProps} />;
}

export default MyApp;
```

```javascript
// styles/globals.css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
}

h1 {
    color: #343a40;
}

button {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}

button:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
}
```

### Notes:
1. Replace `'0xYourNFTContractAddress'` with the actual smart contract address for your NFT.
2. Ensure you handle the NFT minting logic on the smart contract side.
3. This code assumes the user has MetaMask installed and uses it to connect to Ethereum.
4. Consider improving the UX with proper loading indicators and more detailed error messages.
