"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blubhub.app
Prompt: Recommend libraries or tools to implement a presale form for a blockchain project, ensuring secure wallet integration.
Generated: DETERMINISTIC_97d0405ada3751f4
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import Web3 from 'web3';
import { useForm } from 'react-hook-form';

// PresaleForm component for handling presale transactions
const PresaleForm = () => {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const [transactionHash, setTransactionHash] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [loading, setLoading] = useState(false);
    
    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Handle form submission
    const onSubmit = async (data) => {
        setLoading(true);
        setErrorMessage('');
        
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Presale contract address and amount to send (in wei)
            const contractAddress = '0xYourContractAddress';
            const amount = web3.utils.toWei(data.amount, 'ether');
            
            // Create transaction object
            const transactionParameters = {
                to: contractAddress, // Required
                from: window.ethereum.selectedAddress, // User's wallet address
                value: amount, // Amount to send (in wei)
                gas: '2000000', // Set gas limit for the transaction
            };
            
            // Send transaction and get the transaction hash
            const txHash = await web3.eth.sendTransaction(transactionParameters);
            setTransactionHash(txHash.transactionHash);
        } catch (error) {
            // Handle errors
            setErrorMessage('Transaction failed: ' + error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Presale Form</h2>
            <form onSubmit={handleSubmit(onSubmit)}>
                <div>
                    <label htmlFor="amount">Amount (ETH):</label>
                    <input
                        id="amount"
                        type="number"
                        {...register('amount', { required: true, min: 0 })}
                    />
                    {errors.amount && <span>This field is required and must be a positive number.</span>}
                </div>
                <button type="submit" disabled={loading}>
                    {loading ? 'Processing...' : 'Participate in Presale'}
                </button>
            </form>
            {transactionHash && <p>Transaction Hash: {transactionHash}</p>}
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
        </div>
    );
};

export default PresaleForm;
```

**Dependencies:**
Ensure to install the following libraries in your project:
```bash
npm install web3 react-hook-form
```

**Note:** Replace `'0xYourContractAddress'` with the actual smart contract address for your presale project.
