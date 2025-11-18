"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petoshi-dashboard.pages.dev
Prompt: Build a VueJS component that dynamically switches between Ethereum Mainnet and Polygon networks and updates the connected chain status, as outlined in the Petoshi dashboard.
Generated: DETERMINISTIC_61febee7b9af646f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```vue
<template>
  <div class="network-switcher">
    <h2>Network Switcher</h2>
    <p>Current Network: {{ currentNetwork }}</p>
    <button @click="switchNetwork('Ethereum')">Switch to Ethereum Mainnet</button>
    <button @click="switchNetwork('Polygon')">Switch to Polygon Network</button>
  </div>
</template>

<script>
export default {
  name: 'NetworkSwitcher',
  data() {
    return {
      currentNetwork: 'Unknown', // Tracks the currently connected network
    };
  },
  methods: {
    /**
     * Switches the connected network based on the passed network name.
     * @param {"Ethereum"|"Polygon"} networkName - The name of the network to switch to.
     */
    async switchNetwork(networkName) {
      try {
        // Define chain IDs for Ethereum and Polygon networks
        const networks = {
          Ethereum: {
            chainId: '0x1', // Ethereum Mainnet chain ID
          },
          Polygon: {
            chainId: '0x89', // Polygon chain ID
          },
        };

        // Validate if the networkName exists in the networks object
        if (!networks[networkName]) {
          throw new Error('Unsupported network name.');
        }

        // Request the network switch from the user's wallet provider
        const { chainId } = networks[networkName];
        await window.ethereum.request({
          method: 'wallet_switchEthereumChain',
          params: [{ chainId }],
        });

        // Update the current network state after a successful switch
        this.currentNetwork = networkName;
      } catch (error) {
        // Handle errors gracefully
        if (error.code === 4902) {
          // Error code for unrecognized chain ID
          alert(
            `${networkName} network is not added to your wallet. Please manually add it.`
          );
        } else {
          console.error('Failed to switch network:', error.message);
          alert('Error switching network. Check the console for details.');
        }
      }
    },
  },
};
</script>

<style scoped>
.network-switcher {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.network-switcher h2 {
  margin-bottom: 10px;
}

.network-switcher button {
  margin: 5px;
  padding: 10px 15px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.network-switcher button:hover {
  background-color: #0056b3;
}
</style>
```
