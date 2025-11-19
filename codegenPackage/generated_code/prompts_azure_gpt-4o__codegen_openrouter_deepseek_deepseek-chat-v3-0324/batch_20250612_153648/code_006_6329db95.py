"""
Generated Code Metadata:
========================
Original URL: https://qqqqqqqtestu.web.app
Prompt: Create a Solana blockchain-based dashboard that visualizes NFT trading metrics such as floor price, 24-hour volume, and TPS (transactions per second), inspired by Tensor's interface.
Generated: DETERMINISTIC_6329db95395da252
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey } from '@solana/web3.js';
import { Chart } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Register ChartJS components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

// Solana connection configuration
const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com';
const connection = new Connection(SOLANA_RPC_URL);

// NFT Collection addresses (example collections)
const NFT_COLLECTIONS = {
  'Degenerate Ape Academy': new PublicKey('DSwfRF1hhuW6aQ5Y9F6Qq57P9A1yMbVYjFqEAp7gVfr1'),
  'Solana Monkey Business': new PublicKey('SMBH3wF6baUj6JWtzYvqcKuj2XCKWDqQxzspY12xPND'),
};

// Main Dashboard Component
const NFTAnalyticsDashboard = () => {
  const [selectedCollection, setSelectedCollection] = useState(Object.keys(NFT_COLLECTIONS)[0]);
  const [floorPrice, setFloorPrice] = useState(0);
  const [dailyVolume, setDailyVolume] = useState(0);
  const [tps, setTps] = useState(0);
  const [priceHistory, setPriceHistory] = useState([]);
  const [volumeHistory, setVolumeHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch NFT metrics
  const fetchMetrics = async () => {
    try {
      setLoading(true);
      setError(null);

      // Mock data fetching - in a real app, you'd use APIs like Tensor's or MagicEden's
      // For demo purposes, we're simulating data
      const mockFloorPrice = Math.random() * 10;
      const mockVolume = Math.random() * 1000;
      
      // Get recent TPS from Solana network
      const performanceSamples = await connection.getRecentPerformanceSamples(5);
      const avgTps = performanceSamples.reduce((sum, sample) => sum + sample.numTransactions / sample.samplePeriodSecs, 0) / performanceSamples.length;
      
      // Generate mock historical data
      const mockPriceHistory = Array.from({ length: 7 }, (_, i) => ({
        date: new Date(Date.now() - (6 - i) * 24 * 60 * 60 * 1000).toLocaleDateString(),
        price: mockFloorPrice * (0.9 + Math.random() * 0.2)
      }));
      
      const mockVolumeHistory = Array.from({ length: 7 }, (_, i) => ({
        date: new Date(Date.now() - (6 - i) * 24 * 60 * 60 * 1000).toLocaleDateString(),
        volume: mockVolume * (0.8 + Math.random() * 0.4)
      }));

      // Update state
      setFloorPrice(mockFloorPrice);
      setDailyVolume(mockVolume);
      setTps(avgTps);
      setPriceHistory(mockPriceHistory);
      setVolumeHistory(mockVolumeHistory);
    } catch (err) {
      console.error('Error fetching metrics:', err);
      setError('Failed to load data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Fetch data on component mount and collection change
  useEffect(() => {
    fetchMetrics();
    
    // Set up polling every 30 seconds
    const interval = setInterval(fetchMetrics, 30000);
    return () => clearInterval(interval);
  }, [selectedCollection]);

  // Chart data configuration
  const priceChartData = {
    labels: priceHistory.map(item => item.date),
    datasets: [
      {
        label: 'Floor Price (SOL)',
        data: priceHistory.map(item => item.price),
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.1,
        type: 'line'
      }
    ]
  };

  const volumeChartData = {
    labels: volumeHistory.map(item => item.date),
    datasets: [
      {
        label: 'Daily Volume (SOL)',
        data: volumeHistory.map(item => item.volume),
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        type: 'bar'
      }
    ]
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">NFT Analytics Dashboard</h1>
        
        {/* Collection Selector */}
        <div className="mb-6">
          <label htmlFor="collection" className="block text-sm font-medium text-gray-700 mb-2">
            Select NFT Collection
          </label>
          <select
            id="collection"
            value={selectedCollection}
            onChange={(e) => setSelectedCollection(e.target.value)}
            className="block w-full p-2 border border-gray-300 rounded-md shadow-sm"
          >
            {Object.keys(NFT_COLLECTIONS).map(collection => (
              <option key={collection} value={collection}>{collection}</option>
            ))}
          </select>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-6" role="alert">
            <p>{error}</p>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="flex justify-center items-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
          </div>
        )}

        {/* Metrics Grid */}
        {!loading && !error && (
          <>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
              {/* Floor Price Card */}
              <div className="bg-white p-6 rounded-lg shadow">
                <h3 className="text-lg font-medium text-gray-500">Floor Price</h3>
                <p className="text-3xl font-bold text-gray-800">{floorPrice.toFixed(2)} SOL</p>
                <p className="text-sm text-gray-500 mt-1">Current lowest listed price</p>
              </div>

              {/* 24h Volume Card */}
              <div className="bg-white p-6 rounded-lg shadow">
                <h3 className="text-lg font-medium text-gray-500">24h Volume</h3>
                <p className="text-3xl font-bold text-gray-800">{dailyVolume.toFixed(2)} SOL</p>
                <p className="text-sm text-gray-500 mt-1">Total trading volume</p>
              </div>

              {/* TPS Card */}
              <div className="bg-white p-6 rounded-lg shadow">
                <h3 className="text-lg font-medium text-gray-500">Network TPS</h3>
                <p className="text-3xl font-bold text-gray-800">{tps.toFixed(2)}</p>
                <p className="text-sm text-gray-500 mt-1">Transactions per second</p>
              </div>
            </div>

            {/* Charts Section */}
            <div className="grid grid-cols-1 gap-6">
              {/* Price Chart */}
              <div className="bg-white p-6 rounded-lg shadow">
                <h3 className="text-lg font-medium text-gray-800 mb-4">Floor Price History (7 Days)</h3>
                <div className="h-64">
                  <Chart 
                    data={priceChartData} 
                    options={{
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                        legend: { position: 'top' },
                      },
                      scales: {
                        y: {
                          beginAtZero: false
                        }
                      }
                    }} 
                  />
                </div>
              </div>

              {/* Volume Chart */}
              <div className="bg-white p-6 rounded-lg shadow">
                <h3 className="text-lg font-medium text-gray-800 mb-4">Trading Volume History (7 Days)</h3>
                <div className="h-64">
                  <Chart 
                    data={volumeChartData} 
                    options={{
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                        legend: { position: 'top' },
                      },
                      scales: {
                        y: {
                          beginAtZero: true
                        }
                      }
                    }} 
                  />
                </div>
              </div>
            </div>
          </>
        )}
