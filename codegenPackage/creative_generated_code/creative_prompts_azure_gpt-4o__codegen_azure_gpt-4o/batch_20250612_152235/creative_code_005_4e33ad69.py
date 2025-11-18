"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Generate a guide for integrating the WienerAI token purchase process into a React-based web application, including wallet connection and token swapping functionality.
Generated: DETERMINISTIC_4e33ad6940271507
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import React and required dependencies
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';
import Swal from 'sweetalert2';

// Constants
const WIENERAI_CONTRACT_ADDRESS = '0xYourWienerAIContractAddressHere';
const TOKEN_ABI = [
  // Replace with your WienerAI contract's ABI
];

const App = () => {
  // State variables
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [tokenBalance, setTokenBalance] = useState('0');
  const [swapAmount, setSwapAmount] = useState('');

  useEffect(() => {
    // Check if the user has MetaMask and establish connection
    const initializeWeb3 = async () => {
      const provider = await detectEthereumProvider();
      if (provider) {
        const web3Instance = new Web3(provider);
        setWeb3(web3Instance);

        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        setWalletConnected(true);

        const tokenContract = new web3Instance.eth.Contract(TOKEN_ABI, WIENERAI_CONTRACT_ADDRESS);
        setContract(tokenContract);
        fetchTokenBalance(tokenContract, accounts[0]);
      } else {
        Swal.fire({
          icon: 'error',
          title: 'No Wallet Found',
          text: 'Please install MetaMask to use this feature.',
        });
      }
    };

    initializeWeb3();
  }, []);

  // Fetch token balance for the connected wallet
  const fetchTokenBalance = async (contractInstance, userAccount) => {
    try {
      const balance = await contractInstance.methods.balanceOf(userAccount).call();
      setTokenBalance(web3.utils.fromWei(balance, 'ether'));
    } catch (error) {
      console.error('Error fetching token balance:', error);
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Unable to retrieve token balance.',
      });
    }
  };

  // Handle token swapping functionality
  const handleTokenSwap = async () => {
    if (!swapAmount || parseFloat(swapAmount) <= 0) {
      Swal.fire({
        icon: 'error',
        title: 'Invalid Swap Amount',
        text: 'Please enter a valid token amount to swap.',
      });
      return;
    }

    try {
      const weiAmount = web3.utils.toWei(swapAmount, 'ether');

      await contract.methods.swapTokens(weiAmount).send({
        from: account,
      });

      Swal.fire({
        icon: 'success',
        title: 'Swap Successful',
        text: `Successfully swapped ${swapAmount} tokens.`,
      });

      // Refresh token balance after swap
      fetchTokenBalance(contract, account);
    } catch (error) {
      console.error('Error during token swap:', error);
      Swal.fire({
        icon: 'error',
        title: 'Swap Failed',
        text: 'An error occurred while trying to swap tokens.',
      });
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>WienerAI Token Purchase</h1>
      {!walletConnected ? (
        <button onClick={() => window.location.reload()} style={{ padding: '10px', fontSize: '16px' }}>
          Connect Wallet
        </button>
      ) : (
        <div>
          <p>
            <strong>Wallet Address:</strong> {account}
          </p>
          <p>
            <strong>Token Balance:</strong> {tokenBalance} WIENERAI
          </p>
          <div>
            <input
              type="number"
              value={swapAmount}
              onChange={(e) => setSwapAmount(e.target.value)}
              placeholder="Enter token amount to swap"
              style={{ marginRight: '10px', padding: '5px' }}
            />
            <button onClick={handleTokenSwap} style={{ padding: '10px', fontSize: '16px' }}>
              Swap Tokens
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
```
