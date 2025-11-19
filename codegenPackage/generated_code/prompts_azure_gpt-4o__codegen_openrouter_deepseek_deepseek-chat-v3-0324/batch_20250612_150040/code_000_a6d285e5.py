"""
Generated Code Metadata:
========================
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Write a script using web3.js to connect a wallet and mint a `.linea` username with a specified length and duration, referencing the pricing tiers from the Linea domains website.
Generated: DETERMINISTIC_a6d285e5d39aed41
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const Web3 = require('web3');
const { ethers } = require('ethers');

// Linea Domains contract ABI (simplified for minting)
const lineaDomainsABI = [
  {
    "inputs": [
      {"internalType": "string", "name": "name", "type": "string"},
      {"internalType": "address", "name": "owner", "type": "address"},
      {"internalType": "uint256", "name": "duration", "type": "uint256"}
    ],
    "name": "register",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
];

// Linea Domains contract address (replace with actual address)
const lineaDomainsAddress = '0xYourLineaDomainsContractAddress';

// Pricing tiers based on name length (in wei)
const PRICING_TIERS = {
  1: ethers.utils.parseEther('100'),  // 100 ETH for 1 char
  2: ethers.utils.parseEther('10'),   // 10 ETH for 2 chars
  3: ethers.utils.parseEther('1'),    // 1 ETH for 3 chars
  4: ethers.utils.parseEther('0.1'),  // 0.1 ETH for 4 chars
  5: ethers.utils.parseEther('0.01'), // 0.01 ETH for 5+ chars
};

// Duration pricing (in wei per year)
const BASE_PRICE_PER_YEAR = ethers.utils.parseEther('0.001');

async function connectWallet() {
  if (!window.ethereum) {
    throw new Error('No Ethereum provider found. Please install MetaMask.');
  }

  const web3 = new Web3(window.ethereum);
  await window.ethereum.request({ method: 'eth_requestAccounts' });
  const accounts = await web3.eth.getAccounts();
  return accounts[0];
}

async function calculatePrice(name, durationYears) {
  const nameLength = name.length;
  let basePrice;

  if (nameLength === 1) basePrice = PRICING_TIERS[1];
  else if (nameLength === 2) basePrice = PRICING_TIERS[2];
  else if (nameLength === 3) basePrice = PRICING_TIERS[3];
  else if (nameLength === 4) basePrice = PRICING_TIERS[4];
  else basePrice = PRICING_TIERS[5];

  const durationPrice = BASE_PRICE_PER_YEAR.mul(ethers.BigNumber.from(durationYears));
  return basePrice.add(durationPrice);
}

async function mintLineaName(name, durationYears) {
  try {
    // Connect wallet
    const userAddress = await connectWallet();
    console.log(`Connected with address: ${userAddress}`);

    // Validate name
    if (!name || name.length === 0) {
      throw new Error('Name cannot be empty');
    }

    if (!name.endsWith('.linea')) {
      name = name + '.linea';
    }

    // Validate duration
    if (durationYears < 1) {
      throw new Error('Duration must be at least 1 year');
    }

    // Calculate price
    const price = await calculatePrice(name.replace('.linea', ''), durationYears);
    console.log(`Price for ${name} (${durationYears} years): ${ethers.utils.formatEther(price)} ETH`);

    // Initialize contract
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const lineaDomains = new ethers.Contract(lineaDomainsAddress, lineaDomainsABI, signer);

    // Mint the name
    const tx = await lineaDomains.register(name, userAddress, durationYears * 31536000, {
      value: price
    });

    console.log('Transaction sent:', tx.hash);
    const receipt = await tx.wait();
    console.log('Transaction confirmed:', receipt.transactionHash);

    return {
      success: true,
      transactionHash: receipt.transactionHash,
      name: name,
      duration: durationYears
    };
  } catch (error) {
    console.error('Error minting .linea name:', error);
    return {
      success: false,
      error: error.message
    };
  }
}

// Example usage:
// mintLineaName('example', 1).then(console.log).catch(console.error);
```
