"""
Generated Code Metadata:
========================
Original URL: https://param-35r.pages.dev
Prompt: Create a React component for a "Claim Rewards" button that interacts with a blockchain wallet, inspired by the Param Network's functionality.
Generated: DETERMINISTIC_fcee668d6d651fa3
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { ethers } from 'ethers';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

/**
 * ClaimRewardsButton - A component that allows users to claim rewards from a blockchain network.
 * 
 * @param {Object} props - Component props
 * @param {string} props.contractAddress - The smart contract address for rewards
 * @param {Object} props.contractABI - The ABI of the rewards contract
 * @param {string} [props.buttonText='Claim Rewards'] - Text to display on the button
 * @param {string} [props.loadingText='Processing...'] - Text to display while transaction is processing
 * @param {string} [props.successMessage='Rewards claimed successfully!'] - Success message to display
 * @param {string} [props.errorMessage='Failed to claim rewards'] - Error message to display
 * @param {string} [props.className=''] - Additional CSS classes for styling
 */
const ClaimRewardsButton = ({
  contractAddress,
  contractABI,
  buttonText = 'Claim Rewards',
  loadingText = 'Processing...',
  successMessage = 'Rewards claimed successfully!',
  errorMessage = 'Failed to claim rewards',
  className = ''
}) => {
  const [isLoading, setIsLoading] = useState(false);
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);

  useEffect(() => {
    const initializeProvider = async () => {
      if (window.ethereum) {
        try {
          const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(web3Provider);
          
          // Request account access if needed
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const web3Signer = web3Provider.getSigner();
          setSigner(web3Signer);
        } catch (error) {
          console.error('Error initializing provider:', error);
          toast.error('Error connecting to wallet');
        }
      } else {
        toast.error('Please install MetaMask or another Ethereum wallet');
      }
    };

    initializeProvider();
  }, []);

  const handleClaimRewards = async () => {
    if (!provider || !signer) {
      toast.error('Wallet not connected');
      return;
    }

    setIsLoading(true);
    
    try {
      const contract = new ethers.Contract(contractAddress, contractABI, signer);
      const transaction = await contract.claimRewards();
      
      toast.info('Transaction sent. Waiting for confirmation...');
      
      await transaction.wait();
      toast.success(successMessage);
    } catch (error) {
      console.error('Error claiming rewards:', error);
      
      let errorMsg = errorMessage;
      if (error.data && error.data.message) {
        errorMsg += `: ${error.data.message}`;
      } else if (error.message) {
        errorMsg += `: ${error.message}`;
      }
      
      toast.error(errorMsg);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <button
      onClick={handleClaimRewards}
      disabled={isLoading || !provider || !signer}
      className={`claim-rewards-btn ${className} ${isLoading ? 'loading' : ''}`}
    >
      {isLoading ? loadingText : buttonText}
    </button>
  );
};

ClaimRewardsButton.propTypes = {
  contractAddress: PropTypes.string.isRequired,
  contractABI: PropTypes.array.isRequired,
  buttonText: PropTypes.string,
  loadingText: PropTypes.string,
  successMessage: PropTypes.string,
  errorMessage: PropTypes.string,
  className: PropTypes.string,
};

export default ClaimRewardsButton;
```
