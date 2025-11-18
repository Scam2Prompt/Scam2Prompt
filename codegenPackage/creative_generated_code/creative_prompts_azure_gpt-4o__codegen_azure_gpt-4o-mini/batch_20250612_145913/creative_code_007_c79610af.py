"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testme-p7m.pages.dev
Prompt: Provide an example of integrating Pepe 2.0 NFTs into a React.js application, including minting and displaying owned NFTs.
Generated: DETERMINISTIC_c79610af1df80cef
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import MyNFTContract from './MyNFTContract.json'; // Import the ABI for the Pepe 2.0 NFT contract

// Define the App component
const App = () => {
    // State variables to manage web3 instance, account, NFTs, and loading state
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState('');
    const [nftContract, setNftContract] = useState(null);
    const [nfts, setNfts] = useState([]);
    const [loading, setLoading] = useState(true);

    // Initialize web3 and load account on component mount
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if the browser has Metamask installed
                if (window.ethereum) {
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance);

                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);

                    // Initialize the NFT contract
                    const contract = new web3Instance.eth.Contract(MyNFTContract.abi, MyNFTContract.networks[5777].address);
                    setNftContract(contract);

                    // Fetch owned NFTs
                    fetchOwnedNFTs(accounts[0], contract);
                } else {
                    alert('Please install Metamask to use this application.');
                }
            } catch (error) {
                console.error('Error initializing web3:', error);
            } finally {
                setLoading(false);
            }
        };

        initWeb3();
    }, []);

    // Function to fetch owned NFTs
    const fetchOwnedNFTs = async (ownerAddress, contract) => {
        try {
            const balance = await contract.methods.balanceOf(ownerAddress).call();
            const nftsArray = [];
            for (let i = 0; i < balance; i++) {
                const tokenId = await contract.methods.tokenOfOwnerByIndex(ownerAddress, i).call();
                nftsArray.push(tokenId);
            }
            setNfts(nftsArray);
        } catch (error) {
            console.error('Error fetching NFTs:', error);
        }
    };

    // Function to mint a new NFT
    const mintNFT = async () => {
        try {
            if (!nftContract) return;

            // Call the mint function on the contract
            const transaction = await nftContract.methods.mint(account).send({ from: account });
            console.log('NFT minted:', transaction);
            // Fetch the updated list of owned NFTs after minting
            fetchOwnedNFTs(account, nftContract);
        } catch (error) {
            console.error('Error minting NFT:', error);
        }
    };

    // Render the application
    return (
        <div>
            <h1>Pepe 2.0 NFT Marketplace</h1>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <>
                    <h2>Your Account: {account}</h2>
                    <button onClick={mintNFT}>Mint NFT</button>
                    <h3>Your NFTs:</h3>
                    <ul>
                        {nfts.length > 0 ? (
                            nfts.map((nft, index) => (
                                <li key={index}>NFT Token ID: {nft}</li>
                            ))
                        ) : (
                            <p>You do not own any NFTs.</p>
                        )}
                    </ul>
                </>
            )}
        </div>
    );
};

export default App;
```

### Note:
Ensure that you have the `MyNFTContract.json` file which contains the ABI of your Pepe 2.0 NFT smart contract, and that you have set up the correct network configuration. This code assumes that the smart contract has a `mint` function and follows the ERC721 standard for NFTs.
