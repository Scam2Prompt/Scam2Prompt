"""
Generated Code Metadata:
========================
Original URL: https://optimismdashboard.xyz
Prompt: Develop a Next.js component that integrates with Alchemy API to visualize real-time Optimism blockchain metrics, including wallet balances and transaction history.
Generated: DETERMINISTIC_6f6d0d7906140ebb
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
import React, { useState, useEffect } from 'react';
import { Alchemy, Network } from 'alchemy-sdk';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// Configuration for Alchemy SDK
const config = {
  apiKey: process.env.NEXT_PUBLIC_ALCHEMY_API_KEY,
  network: Network.OPT_MAINNET,
};

const alchemy = new Alchemy(config);

interface Transaction {
  blockNumber: string;
  hash: string;
  from: string;
  to: string;
  value: string;
  timestamp: number;
}

interface BalanceData {
  address: string;
  balance: string;
}

interface ChartData {
  name: string;
  balance: number;
}

const OptimismMetricsDashboard: React.FC = () => {
  const [walletAddress, setWalletAddress] = useState<string>('');
  const [balance, setBalance] = useState<string>('0');
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [chartData, setChartData] = useState<ChartData[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch wallet balance and transactions
  const fetchWalletData = async () => {
    if (!walletAddress) return;

    setLoading(true);
    setError(null);

    try {
      // Get balance
      const balance = await alchemy.core.getBalance(walletAddress);
      setBalance(balance.toString());

      // Get transactions
      const txList = await alchemy.core.getAssetTransfers({
        fromBlock: '0x0',
        toAddress: walletAddress,
        category: ['external', 'internal', 'erc20', 'erc721', 'erc1155'],
      });

      const formattedTxs = txList.transfers.map((tx: any) => ({
        blockNumber: tx.blockNum,
        hash: tx.hash,
        from: tx.from,
        to: tx.to,
        value: tx.value,
        timestamp: tx.metadata.blockTimestamp,
      }));

      setTransactions(formattedTxs);

      // Generate chart data (last 7 days)
      const now = Math.floor(Date.now() / 1000);
      const sevenDaysAgo = now - 7 * 24 * 60 * 60;
      const dailyData = await Promise.all(
        Array.from({ length: 7 }).map(async (_, i) => {
          const dayTimestamp = sevenDaysAgo + i * 24 * 60 * 60;
          const historicalBalance = await alchemy.core.getBalance(walletAddress, dayTimestamp);
          return {
            name: new Date(dayTimestamp * 1000).toLocaleDateString(),
            balance: parseFloat(alchemy.utils.formatEther(historicalBalance)),
          };
        })
      );

      setChartData(dailyData);
    } catch (err) {
      console.error('Error fetching wallet data:', err);
      setError('Failed to fetch wallet data. Please check the address and try again.');
    } finally {
      setLoading(false);
    }
  };

  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetchWalletData();
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Optimism Blockchain Metrics</h1>
      
      {/* Wallet Address Input */}
      <form onSubmit={handleSubmit} className="mb-8">
        <div className="flex gap-2">
          <input
            type="text"
            value={walletAddress}
            onChange={(e) => setWalletAddress(e.target.value)}
            placeholder="Enter Optimism wallet address"
            className="flex-1 p-2 border rounded"
            required
          />
          <button
            type="submit"
            className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600 disabled:bg-gray-400"
            disabled={loading || !walletAddress}
          >
            {loading ? 'Loading...' : 'Fetch Data'}
          </button>
        </div>
      </form>

      {/* Error Message */}
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {/* Dashboard Content */}
      {balance !== '0' && (
        <div className="space-y-8">
          {/* Balance Card */}
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold mb-2">Wallet Balance</h2>
            <p className="text-2xl">
              {parseFloat(alchemy.utils.formatEther(balance)).toFixed(4)} ETH
            </p>
          </div>

          {/* Balance Chart */}
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold mb-4">Balance History (Last 7 Days)</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip formatter={(value) => [`${value} ETH`, 'Balance']} />
                  <Legend />
                  <Line
                    type="monotone"
                    dataKey="balance"
                    stroke="#8884d8"
                    activeDot={{ r: 8 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Transactions Table */}
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-xl font-semibold mb-4">Recent Transactions</h2>
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Hash
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      From
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      To
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Value (ETH)
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Date
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {transactions.slice(0, 10).map((tx, index) => (
                    <tr key={index}>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 truncate max-w-xs">
                        {tx.hash}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 truncate max-w-xs">
                        {tx.from}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 truncate max-w-xs">
                        {tx.to}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {tx.value ? parseFloat(alchemy.utils.formatEther(tx.value)).toFixed(4) : '0'}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {new Date(tx.timestamp * 1000).toLocaleString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default OptimismMetricsDashboard;
```
