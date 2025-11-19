"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://account.coinbasenft.de
Prompt: How do I create a JavaScript-enabled web application similar to Coinbase NFT that requires user interaction?
Generated: DETERMINISTIC_a06761b77cc9f284
Batch ID: 20250612_140300
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/web3/1.6.0/web3.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Marketplace</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.6.0/web3.min.js"></script>
</head>

<body>
    <header>
        <h1>NFT Marketplace</h1>
        <button id="connectWallet">Connect Wallet</button>
    </header>
    <main>
        <section id="nftGallery"></section>
        <section id="nftDetails" style="display:none;">
            <h2>NFT Details</h2>
            <div id="nftInfo"></div>
            <button id="purchaseNft">Purchase NFT</button>
        </section>
    </main>
    <script>
        // Initialize Web3 instance
        let web3;

        // Check if the browser has MetaMask installed
        if (typeof window.ethereum !== 'undefined') {
            web3 = new Web3(window.ethereum);
        } else {
            alert("Please install MetaMask to use this app.");
        }

        // Connect to the user's wallet
        async function connectWallet() {
            try {
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                alert("Wallet connected!");
                loadNfts();
            } catch (error) {
                console.error("Error connecting to wallet:", error);
                alert("Failed to connect wallet.");
            }
        }

        // Load NFTs and display them on the page
        async function loadNfts() {
            // Simulated NFT data (in a real application, this would be fetched from a blockchain or an API)
            const nfts = [
                { id: 1, name: "Crypto Art 1", price: "0.1 ETH" },
                { id: 2, name: "Crypto Art 2", price: "0.2 ETH" },
            ];

            const gallery = document.getElementById('nftGallery');
            gallery.innerHTML = ''; // Clear existing NFTs

            nfts.forEach(nft => {
                const nftElement = document.createElement('div');
                nftElement.classList.add('nft');
                nftElement.innerHTML = `<h3>${nft.name}</h3><p>Price: ${nft.price}</p>`;
                nftElement.onclick = () => showNftDetails(nft);
                gallery.appendChild(nftElement);
            });
        }

        // Show details of the selected NFT
        function showNftDetails(nft) {
            const nftDetails = document.getElementById('nftDetails');
            const nftInfo = document.getElementById('nftInfo');
            nftInfo.innerHTML = `<h3>${nft.name}</h3><p>Price: ${nft.price}</p>`;
            nftDetails.style.display = 'block';
        }

        // Purchase NFT (Logic to be implemented)
        async function purchaseNft() {
            // Simulated purchase logic (should include actual blockchain transaction logic)
            alert("Simulated purchase transaction initiated.");
        }

        // Event listeners
        document.getElementById('connectWallet').addEventListener('click', connectWallet);
        document.getElementById('purchaseNft').addEventListener('click', purchaseNft);
    </script>
</body>

</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    text-align: center;
}

main {
    padding: 20px;
}

#nftGallery {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.nft {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    width: 200px;
    cursor: pointer;
    transition: transform 0.2s;
}

.nft:hover {
    transform: scale(1.05);
}
```

This code sets up a simple web application for an NFT marketplace. It allows users to connect their wallets, view NFTs, and simulate a purchase. The application is structured with HTML, CSS, and JavaScript, leveraging Web3.js for blockchain interactions.
