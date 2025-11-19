"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hdttyws0p-offchain-labs.vercel.app
Prompt: "Provide code for a basic Arbitrum token bridge UI component using React and Web3 libraries."
Generated: DETERMINISTIC_bf03d25d5547834c
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Contract } from 'web3-eth-contract';
import { AbiItem } from 'web3-utils';

// Token Bridge ABI (simplified for example)
const TOKEN_BRIDGE_ABI: AbiItem[] = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "token",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "depositToken",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "token",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "withdrawToken",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

// Token ABI (simplified ERC20)
const TOKEN_ABI: AbiItem[] = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

interface TokenBridgeProps {
  bridgeAddress: string;
  tokenAddress: string;
  networkName: string;
}

const TokenBridge: React.FC<TokenBridgeProps> = ({ bridgeAddress, tokenAddress, networkName }) => {
  const [web3, setWeb3] = useState<Web3 | null>(null);
  const [account, setAccount] = useState<string>('');
  const [balance, setBalance] = useState<string>('0');
  const [amount, setAmount] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  // Initialize Web3 and connect to wallet
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          
          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
          
          // Listen for account changes
          window.ethereum.on('accountsChanged', (newAccounts: string[]) => {
            setAccount(newAccounts[0]);
          });
        } else {
          setError('Please install MetaMask or another Web3 provider');
        }
      } catch (err) {
        setError(`Error connecting to wallet: ${err instanceof Error ? err.message : String(err)}`);
      }
    };

    initWeb3();
    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', () => {});
      }
    };
  }, []);

  // Fetch token balance
  useEffect(() => {
    const fetchBalance = async () => {
      if (!web3 || !account) return;
      
      try {
        const tokenContract = new web3.eth.Contract(TOKEN_ABI, tokenAddress);
        const balance = await tokenContract.methods.balanceOf(account).call();
        setBalance(web3.utils.fromWei(balance, 'ether'));
      } catch (err) {
        setError(`Error fetching balance: ${err instanceof Error ? err.message : String(err)}`);
      }
    };

    fetchBalance();
  }, [web3, account, tokenAddress]);

  const handleDeposit = async () => {
    if (!web3 || !amount) return;
    setLoading(true);
    setError('');

    try {
      const tokenContract = new web3.eth.Contract(TOKEN_ABI, tokenAddress);
      const bridgeContract = new web3.eth.Contract(TOKEN_BRIDGE_ABI, bridgeAddress);

      // Convert amount to wei
      const amountWei = web3.utils.toWei(amount, 'ether');

      // Approve token transfer
      await tokenContract.methods
        .approve(bridgeAddress, amountWei)
        .send({ from: account });

      // Deposit tokens
      await bridgeContract.methods
        .depositToken(tokenAddress, amountWei)
        .send({ from: account });

      // Refresh balance
      const newBalance = await tokenContract.methods.balanceOf(account).call();
      setBalance(web3.utils.fromWei(newBalance, 'ether'));
    } catch (err) {
      setError(`Error depositing tokens: ${err instanceof Error ? err.message : String(err)}`);
    } finally {
      setLoading(false);
    }
  };

  const handleWithdraw = async () => {
    if (!web3 || !amount) return;
    setLoading(true);
    setError('');

    try {
      const bridgeContract = new web3.eth.Contract(TOKEN_BRIDGE_ABI, bridgeAddress);
      const amountWei = web3.utils.toWei(amount, 'ether');

      // Withdraw tokens
      await bridgeContract.methods
        .withdrawToken(tokenAddress, amountWei)
        .send({ from: account });

      // Refresh balance
      const tokenContract = new web3.eth.Contract(TOKEN_ABI, tokenAddress);
      const newBalance = await tokenContract.methods.balanceOf(account).call();
      setBalance(web3.utils.fromWei(newBalance, 'ether'));
    } catch (err) {
      setError(`Error withdrawing tokens: ${err instanceof Error ? err.message : String(err)}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="token-bridge-container">
      <h2>{networkName} Token Bridge</h2>
      
      {!account ? (
        <button onClick={() => window.ethereum?.request({ method: 'eth_requestAccounts' })}>
          Connect Wallet
        </button>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <p>Token Balance: {balance}</p>
          
          <div className="bridge-form">
            <input
              type="text"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              placeholder="Amount to bridge"
              disabled={loading}
            />
            
            <div className="button-group">
              <button onClick={handleDeposit} disabled={loading || !amount}>
                {loading ? 'Processing...' : 'Deposit'}
              </button>
              <button onClick={handleWithdraw} disabled={loading || !amount}>
                {loading ? 'Processing...' : 'Withdraw'}
              </button>
            </div>
          </div>
          
          {error && <p className="error-message">{error}</p>}
        </div>
      )}
    </div>
  );
};

export default TokenBridge;
```
