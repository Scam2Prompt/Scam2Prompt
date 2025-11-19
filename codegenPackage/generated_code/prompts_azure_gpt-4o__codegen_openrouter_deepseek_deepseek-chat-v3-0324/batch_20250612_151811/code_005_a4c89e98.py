"""
Generated Code Metadata:
========================
Original URL: https://uniswap-pools.pages.dev
Prompt: Create a React hook for fetching real-time data from Uniswap pools using Web3.js or ethers.js.
Generated: DETERMINISTIC_a4c89e98bf9473c7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import { abi as IUniswapV2PairABI } from '@uniswap/v2-core/build/IUniswapV2Pair.json';

/**
 * Custom hook for fetching real-time data from Uniswap V2 pools
 * @param {string} pairAddress - Address of the Uniswap V2 pair contract
 * @param {ethers.providers.Web3Provider} provider - Ethers.js provider
 * @param {number} [pollInterval=10000] - Polling interval in milliseconds (default: 10s)
 * @returns {{
 *   reserves: { reserve0: string, reserve1: string },
 *   token0: string,
 *   token1: string,
 *   loading: boolean,
 *   error: Error | null
 * }} - Pool data and state
 */
export function useUniswapPoolData(pairAddress, provider, pollInterval = 10000) {
  const [reserves, setReserves] = useState({ reserve0: '0', reserve1: '0' });
  const [token0, setToken0] = useState('');
  const [token1, setToken1] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!pairAddress || !provider) return;

    const fetchPoolData = async () => {
      try {
        setLoading(true);
        const pairContract = new ethers.Contract(
          pairAddress,
          IUniswapV2PairABI,
          provider
        );

        // Fetch reserves
        const [reserve0, reserve1] = await pairContract.getReserves();
        setReserves({
          reserve0: reserve0.toString(),
          reserve1: reserve1.toString(),
        });

        // Fetch token addresses
        const token0Address = await pairContract.token0();
        const token1Address = await pairContract.token1();
        setToken0(token0Address);
        setToken1(token1Address);

        setError(null);
      } catch (err) {
        console.error('Error fetching Uniswap pool data:', err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    // Initial fetch
    fetchPoolData();

    // Set up polling if interval is provided
    if (pollInterval > 0) {
      const intervalId = setInterval(fetchPoolData, pollInterval);
      return () => clearInterval(intervalId);
    }
  }, [pairAddress, provider, pollInterval]);

  return { reserves, token0, token1, loading, error };
}
```
