"""
Generated Code Metadata:
========================
Original URL: https://bonkai-buy.pages.dev
Prompt: Create a dashboard in Vue.js to visualize BONKAI's tokenomics, including total supply, distribution, and burn statistics, with real-time updates from the Solana blockchain.
Generated: DETERMINISTIC_5a82f9baf260ae81
Batch ID: 20250612_150601
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.solscan.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://solscan.io/tx/${tx.txHash}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

```vue
<template>
  <div class="dashboard">
    <header class="header">
      <h1>BONKAI Tokenomics Dashboard</h1>
      <div class="last-updated">
        Last updated: {{ lastUpdated }}
      </div>
    </header>

    <div class="stats-grid">
      <!-- Total Supply Card -->
      <div class="stat-card">
        <h2>Total Supply</h2>
        <div class="stat-value">{{ formatNumber(totalSupply) }}</div>
        <div class="stat-description">BONKAI Tokens</div>
      </div>

      <!-- Circulating Supply Card -->
      <div class="stat-card">
        <h2>Circulating Supply</h2>
        <div class="stat-value">{{ formatNumber(circulatingSupply) }}</div>
        <div class="stat-description">BONKAI Tokens</div>
      </div>

      <!-- Burned Tokens Card -->
      <div class="stat-card">
        <h2>Burned Tokens</h2>
        <div class="stat-value">{{ formatNumber(burnedTokens) }}</div>
        <div class="stat-description">BONKAI Tokens</div>
        <div class="burn-percentage">{{ burnPercentage }}% of total supply</div>
      </div>

      <!-- Market Cap Card -->
      <div class="stat-card">
        <h2>Market Cap</h2>
        <div class="stat-value">${{ formatNumber(marketCap) }}</div>
        <div class="stat-description">USD</div>
      </div>
    </div>

    <div class="charts-container">
      <!-- Distribution Pie Chart -->
      <div class="chart-card">
        <h2>Token Distribution</h2>
        <div class="chart-wrapper">
          <PieChart
            :chart-data="distributionData"
            :options="pieChartOptions"
          />
        </div>
      </div>

      <!-- Burn History Line Chart -->
      <div class="chart-card">
        <h2>Burn History (Last 30 Days)</h2>
        <div class="chart-wrapper">
          <LineChart
            :chart-data="burnHistoryData"
            :options="lineChartOptions"
          />
        </div>
      </div>
    </div>

    <div class="transaction-history">
      <h2>Recent Burn Transactions</h2>
      <div class="transactions-list">
        <div v-if="recentBurns.length === 0" class="empty-state">
          Loading recent burns...
        </div>
        <div v-else>
          <div v-for="(tx, index) in recentBurns" :key="index" class="transaction-item">
            <div class="tx-hash">
              <a :href="`https://solscan.io/tx/${tx.txHash}`" target="_blank" rel="noopener noreferrer">
                {{ shortenHash(tx.txHash) }}
              </a>
            </div>
            <div class="tx-amount">{{ formatNumber(tx.amount) }} BONKAI</div>
            <div class="tx-time">{{ formatTime(tx.timestamp) }}</div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="error" class="error-message">
      Error fetching data: {{ error }}
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { PieChart, LineChart } from 'vue-chart-3';
import { Chart, registerables } from 'chart.js';
import axios from 'axios';

Chart.register(...registerables);

export default {
  name: 'BonkaiDashboard',
  components: { PieChart, LineChart },
  setup() {
    // State
    const totalSupply = ref(0);
    const circulatingSupply = ref(0);
    const burnedTokens = ref(0);
    const marketCap = ref(0);
    const distribution = ref({
      team: 0,
      ecosystem: 0,
      liquidity: 0,
      staking: 0,
      community: 0
    });
    const burnHistory = ref([]);
    const recentBurns = ref([]);
    const lastUpdated = ref(new Date().toLocaleString());
    const error = ref(null);
    const isLoading = ref(true);

    // Constants
    const BONKAI_TOKEN_ADDRESS = 'YOUR_BONKAI_TOKEN_ADDRESS_HERE';
    const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com';
    const SOLSCAN_API_URL = 'https://api.solscan.io';

    // Computed
    const burnPercentage = computed(() => {
      if (totalSupply.value === 0) return 0;
      return ((burnedTokens.value / totalSupply.value) * 100).toFixed(2);
    });

    const distributionData = computed(() => ({
      labels: Object.keys(distribution.value),
      datasets: [
        {
          data: Object.values(distribution.value),
          backgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56',
            '#4BC0C0',
            '#9966FF'
          ],
          borderWidth: 1
        }
      ]
    }));

    const burnHistoryData = computed(() => ({
      labels: burnHistory.value.map(item => new Date(item.date).toLocaleDateString()),
      datasets: [
        {
          label: 'Burned Tokens',
          data: burnHistory.value.map(item => item.amount),
          borderColor: '#FF6384',
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          tension: 0.1,
          fill: true
        }
      ]
    }));

    const pieChartOptions = computed(() => ({
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'right'
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const label = context.label || '';
              const value = context.raw || 0;
              const total = context.dataset.data.reduce((a, b) => a + b, 0);
              const percentage = Math.round((value / total) * 100);
              return `${label}: ${value.toLocaleString()} (${percentage}%)`;
            }
          }
        }
      }
    }));

    const lineChartOptions = computed(() => ({
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: function(value) {
              return value.toLocaleString();
            }
          }
        }
      },
      plugins: {
        tooltip: {
          callbacks: {
            label: function(context) {
              return `${context.dataset.label}: ${context.raw.toLocaleString()}`;
            }
          }
        }
      }
    }));

    // Methods
    const formatNumber = (num) => {
      return new Intl.NumberFormat('en-US').format(num);
    };

    const shortenHash = (hash) => {
      return `${hash.substring(0, 4)}...${hash.substring(hash.length - 4)}`;
    };

    const formatTime = (timestamp) => {
      return new Date(timestamp).toLocaleString();
    };

    const fetchTokenData = async () => {
      try {
        // In a real implementation, replace with actual API calls to Solana RPC
        // This is a mock implementation for demonstration
        totalSupply.value = 1000000000;
        circulatingSupply.value = 750000000;
        burnedTokens.value = 250000000;
        marketCap.value = 50000000;

        distribution.value = {
          team: 200000000,
          ecosystem: 300000000,
          liquidity: 150000000,
          staking: 200000000,
          community: 150000000
        };

        // Mock burn history data (last 30 days)
        const mockBurnHistory = [];
        for (let i = 0; i < 30; i++) {
          mockBurnHistory.push({
            date: new Date(Date.now() - (30 - i) * 24 * 60 * 60 * 1000),
            amount: Math.floor(Math.random() * 1000000) + 500000
          });
        }
        burnHistory.value = mockBurnHistory;

        // Mock recent burns
        recentBurns.value = [
          {
            txHash: '5J3b4t1oN2yLp9qR8s7T6uM1vX2wZ3e4r5t6y7u8i9o0p',
            amount: 1250000,
            timestamp: Date.now() - 3600000
          },
          {
            txHash: '7K4b5t2oP3yM9qS8t7U6vN1wX3e5r6t7y8u9i0o1p2a',
            amount: 875000,
            timestamp: Date.now() - 7200000
          },
          {
            txHash: '9L5
