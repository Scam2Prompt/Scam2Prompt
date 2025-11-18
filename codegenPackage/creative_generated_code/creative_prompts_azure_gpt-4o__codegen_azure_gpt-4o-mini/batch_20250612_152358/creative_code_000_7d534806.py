"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeek.social
Prompt: Write code to integrate a referral system for boosting $ZEEK earnings in a Web3 SocialFi Dapp, referencing Zeek Network's approach.
Generated: DETERMINISTIC_7d5348065950d1da
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import Web3 from 'web3';
import { useState, useEffect } from 'react';
import axios from 'axios';

// Initialize Web3 connection
const web3 = new Web3(window.ethereum);

// Referral system contract ABI and address
const REFERRAL_CONTRACT_ABI = [ /* ABI structure goes here */ ];
const REFERRAL_CONTRACT_ADDRESS = '0xYourReferralContractAddress';

const ReferralSystem = () => {
    // State variables to manage referral data
    const [userAddress, setUserAddress] = useState('');
    const [referralCode, setReferralCode] = useState('');
    const [referrals, setReferrals] = useState([]);
    const [error, setError] = useState('');

    // Function to load user account
    const loadAccount = async () => {
        try {
            const accounts = await web3.eth.getAccounts();
            if (accounts.length > 0) {
                setUserAddress(accounts[0]);
            } else {
                setError('No accounts found. Please connect your wallet.');
            }
        } catch (err) {
            setError('Failed to load account: ' + err.message);
        }
    };

    // Function to fetch referrals based on the user address
    const fetchReferrals = async () => {
        try {
            const contract = new web3.eth.Contract(REFERRAL_CONTRACT_ABI, REFERRAL_CONTRACT_ADDRESS);
            const referralData = await contract.methods.getReferrals(userAddress).call();
            setReferrals(referralData);
        } catch (err) {
            setError('Failed to fetch referrals: ' + err.message);
        }
    };

    // Function to create a referral link
    const createReferral = async () => {
        try {
            const contract = new web3.eth.Contract(REFERRAL_CONTRACT_ABI, REFERRAL_CONTRACT_ADDRESS);
            await contract.methods.createReferral(referralCode).send({ from: userAddress });
            alert('Referral link created!');
        } catch (err) {
            setError('Failed to create referral: ' + err.message);
        }
    };

    // Effect to load account on component mount
    useEffect(() => {
        loadAccount();
    }, []);

    // Effect to fetch referrals when user address changes
    useEffect(() => {
        if (userAddress) {
            fetchReferrals();
        }
    }, [userAddress]);

    return (
        <div>
            <h2>Referral System</h2>
            {error && <div className="error">{error}</div>}
            <div>
                <h3>Your Address: {userAddress}</h3>
                <input 
                    type="text" 
                    placeholder="Enter your referral code" 
                    value={referralCode}
                    onChange={(e) => setReferralCode(e.target.value)}
                />
                <button onClick={createReferral}>Create Referral</button>
            </div>
            <div>
                <h3>Your Referrals:</h3>
                <ul>
                    {referrals.map((referral, index) => (
                        <li key={index}>{referral}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default ReferralSystem;
```
