"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Write code for a frontend interface in Next.js that displays deposit progress and calculates the total value of token deposits over time for a Solana-based value averaging system.
Generated: DETERMINISTIC_c07209d18fe64a22
Batch ID: 20250612_145130
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
import axios from 'axios';

// Function to fetch deposit data from an API (mockup)
const fetchDeposits = async () => {
    try {
        const response = await axios.get('/api/deposits');
        return response.data;
    } catch (error) {
        console.error('Error fetching deposit data:', error);
        throw new Error('Unable to fetch deposit data');
    }
};

// Main component for the deposit progress interface
const Home = () => {
    const [deposits, setDeposits] = useState([]);
    const [totalValue, setTotalValue] = useState(0);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Effect to fetch deposits when the component mounts
    useEffect(() => {
        const getDeposits = async () => {
            setLoading(true);
            try {
                const data = await fetchDeposits();
                setDeposits(data);

                // Calculate total deposit value
                const total = data.reduce((acc, deposit) => acc + deposit.value, 0);
                setTotalValue(total);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        getDeposits();
    }, []);

    // Function to display deposits
    const renderDeposits = () => (
        <ul>
            {deposits.map((deposit) => (
                <li key={deposit.id}>
                    {`Deposit ID: ${deposit.id}, Value: ${deposit.value}`}
                </li>
            ))}
        </ul>
    );

    return (
        <div>
            <Head>
                <title>Deposit Progress Tracker</title>
                <meta name="description" content="Track your Solana-based token deposits." />
            </Head>
            <main style={{ padding: '20px' }}>
                <h1>Deposit Progress Tracker</h1>
                {loading && <p>Loading deposits...</p>}
                {error && <p style={{ color: 'red' }}>{error}</p>}
                {!loading && !error && (
                    <>
                        <h2>Total Deposits Value: {totalValue}</h2>
                        {renderDeposits()}
                    </>
                )}
            </main>
        </div>
    );
};

export default Home;

// pages/api/deposits.js

// Mock API route to simulate deposit data retrieval
export default function handler(req, res) {
    // Sample deposit data
    const sampleDeposits = [
        { id: 1, value: 50 },
        { id: 2, value: 100 },
        { id: 3, value: 150 },
    ];

    // Respond with the sample data
    res.status(200).json(sampleDeposits);
}
```
