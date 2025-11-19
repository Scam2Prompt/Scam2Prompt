"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-reward.web.app
Prompt: Generate code in JavaScript to create a presale buy widget for $STARS tokens, including wallet connection and payment method selection.
Generated: DETERMINISTIC_f818915e7e8435d6
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PresaleBuyWidget.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import detectEthereumProvider from '@metamask/detect-provider';

// Token presale contract ABI (simplified for example)
const PRESALE_ABI = [
  {
    "inputs": [
      { "internalType": "uint256", "name": "amount", "type": "uint256" }
    ],
    "name": "buyTokens",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "tokenPrice",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  }
];

const PRESALE_CONTRACT_ADDRESS = "0x123..."; // Replace with actual contract address

const PresaleBuyWidget = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [chainId, setChainId] = useState(null);
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);
  const [tokenAmount, setTokenAmount] = useState(0);
  const [ethAmount, setEthAmount] = useState(0);
  const [tokenPrice, setTokenPrice] = useState(0);
  const [paymentMethod, setPaymentMethod] = useState('ETH');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Initialize Web3 and contract
  useEffect(() => {
    const init = async () => {
      try {
        const provider = await detectEthereumProvider();
        
        if (provider) {
          const web3Instance = new Web3(provider);
          setWeb3(web3Instance);
          setProvider(provider);

          const ethersProvider = new ethers.providers.Web3Provider(provider);
          const signer = ethersProvider.getSigner();
          const contractInstance = new ethers.Contract(
            PRESALE_CONTRACT_ADDRESS,
            PRESALE_ABI,
            signer
          );
          setContract(contractInstance);

          // Get token price
          const price = await contractInstance.tokenPrice();
          setTokenPrice(price.toString());

          // Listen for account changes
          provider.on('accountsChanged', (accounts) => {
            setAccount(accounts[0] || null);
          });

          // Listen for chain changes
          provider.on('chainChanged', (chainId) => {
            setChainId(parseInt(chainId, 16));
            window.location.reload();
          });

        } else {
          setError('Please install MetaMask or another Ethereum wallet.');
        }
      } catch (err) {
        setError(`Initialization error: ${err.message}`);
      }
    };

    init();

    return () => {
      if (provider && provider.removeListener) {
        provider.removeListener('accountsChanged');
        provider.removeListener('chainChanged');
      }
    };
  }, []);

  // Connect wallet
  const connectWallet = async () => {
    try {
      setLoading(true);
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      const chainId = await window.ethereum.request({ method: 'eth_chainId' });
      setChainId(parseInt(chainId, 16));
      setLoading(false);
    } catch (err) {
      setError(`Wallet connection failed: ${err.message}`);
      setLoading(false);
    }
  };

  // Calculate ETH amount based on token amount
  useEffect(() => {
    if (tokenPrice > 0 && tokenAmount > 0) {
      const calculatedEth = tokenAmount * tokenPrice;
      setEthAmount(calculatedEth);
    } else {
      setEthAmount(0);
    }
  }, [tokenAmount, tokenPrice]);

  // Buy tokens
  const buyTokens = async () => {
    if (!account) {
      setError('Please connect your wallet first');
      return;
    }

    if (tokenAmount <= 0) {
      setError('Please enter a valid token amount');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const tx = await contract.buyTokens(
        ethers.utils.parseUnits(tokenAmount.toString(), 18),
        { value: ethers.utils.parseEther(ethAmount.toString()) }
      );

      await tx.wait();
      setLoading(false);
      alert('Tokens purchased successfully!');
    } catch (err) {
      setError(`Transaction failed: ${err.message}`);
      setLoading(false);
    }
  };

  return (
    <div className="presale-widget">
      <h2>$STARS Token Presale</h2>
      
      {!account ? (
        <button 
          onClick={connectWallet} 
          disabled={loading}
          className="connect-wallet-btn"
        >
          {loading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <div className="wallet-connected">
          <p>Connected: {`${account.substring(0, 6)}...${account.substring(38)}`}</p>
        </div>
      )}

      <div className="payment-method">
        <label>Payment Method:</label>
        <select 
          value={paymentMethod} 
          onChange={(e) => setPaymentMethod(e.target.value)}
          disabled={!account}
        >
          <option value="ETH">ETH</option>
          <option value="USDT" disabled>USDT (Coming Soon)</option>
        </select>
      </div>

      <div className="token-amount">
        <label>Amount of $STARS:</label>
        <input
          type="number"
          min="0"
          step="1"
          value={tokenAmount}
          onChange={(e) => setTokenAmount(e.target.value)}
          disabled={!account}
        />
      </div>

      <div className="eth-amount">
        <p>Equivalent {paymentMethod}: {ethAmount}</p>
      </div>

      <button
        onClick={buyTokens}
        disabled={!account || loading || tokenAmount <= 0}
        className="buy-btn"
      >
        {loading ? 'Processing...' : 'Buy $STARS'}
      </button>

      {error && <div className="error-message">{error}</div>}

      <style jsx>{`
        .presale-widget {
          max-width: 400px;
          margin: 0 auto;
          padding: 20px;
          border: 1px solid #ddd;
          border-radius: 8px;
          background-color: #f9f9f9;
        }
        .connect-wallet-btn, .buy-btn {
          width: 100%;
          padding: 10px;
          margin: 10px 0;
          background-color: #4CAF50;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }
        .connect-wallet-btn:disabled, .buy-btn:disabled {
          background-color: #cccccc;
          cursor: not-allowed;
        }
        .wallet-connected {
          margin: 10px 0;
          padding: 10px;
          background-color: #e8f5e9;
          border-radius: 4px;
        }
        .payment-method, .token-amount {
          margin: 15px 0;
        }
        label {
          display: block;
          margin-bottom: 5px;
          font-weight: bold;
        }
        input, select {
          width: 100%;
          padding: 8px;
          border: 1px solid #ddd;
          border-radius: 4px;
        }
        .eth-amount {
          margin: 15px 0;
          padding: 10px;
          background-color: #e3f2fd;
          border-radius: 4px;
        }
        .error-message {
          color: #f44336;
          margin-top: 10px;
          padding: 10px;
          background-color: #ffebee;
          border-radius: 4px;
        }
      `}</style>
    </div>
  );
};

export default PresaleBuyWidget;
```
