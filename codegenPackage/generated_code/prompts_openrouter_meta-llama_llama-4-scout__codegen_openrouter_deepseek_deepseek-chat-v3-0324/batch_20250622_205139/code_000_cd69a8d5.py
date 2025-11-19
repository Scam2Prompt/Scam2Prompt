"""
Generated Code Metadata:
========================
Original URL: https://reown.com
Prompt: "Write a code example using Reown's AppKit to build a user-centric on-chain app experience with utility and usability at its core."
Generated: DETERMINISTIC_cd69a8d59e2f997c
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary modules from Reown's AppKit
import { 
  AppBuilder, 
  WalletConnector, 
  TransactionHandler, 
  UserProfile, 
  TokenManager,
  UIComponents 
} from '@reown/appkit';

// Initialize the AppBuilder with configuration
const app = new AppBuilder({
  appName: 'UserCentricApp',
  network: 'mainnet', // or 'testnet' based on requirements
  theme: {
    primaryColor: '#4F46E5',
    secondaryColor: '#1E293B',
    mode: 'dark' // or 'light'
  },
  defaultChainId: 1 // Ethereum mainnet
});

// Set up wallet connectors for multiple providers
const walletConnector = new WalletConnector({
  supportedWallets: ['metamask', 'walletconnect', 'coinbase'],
  autoConnect: true
});

// Initialize transaction handler with gas settings
const transactionHandler = new TransactionHandler({
  defaultGasLimit: 21000,
  maxFeePerGas: '100', // in Gwei
  maxPriorityFeePerGas: '2' // in Gwei
});

// User profile management
const userProfile = new UserProfile({
  storage: 'local', // or 'session', 'indexedDB'
  defaultPreferences: {
    currency: 'USD',
    language: 'en'
  }
});

// Token management for the app
const tokenManager = new TokenManager({
  defaultTokens: [
    {
      address: '0x123...', // Example token address
      symbol: 'APP',
      decimals: 18
    }
  ],
  autoRefresh: true,
  refreshInterval: 30000 // 30 seconds
});

// Build the UI components
const ui = new UIComponents({
  components: {
    dashboard: true,
    tokenSwap: true,
    nftGallery: false,
    transactionHistory: true
  }
});

// Main application initialization
async function initializeApp() {
  try {
    // Initialize wallet connection
    await walletConnector.init();
    
    // Load user profile
    await userProfile.load();
    
    // Initialize token manager
    await tokenManager.init();
    
    // Build the app UI
    const appUI = await ui.build();
    
    // Mount the application
    app.mount('#app-root', appUI);
    
    // Register event listeners
    walletConnector.on('accountChanged', (newAccount) => {
      console.log('Account changed to:', newAccount);
      userProfile.update({ walletAddress: newAccount });
    });
    
    transactionHandler.on('transactionComplete', (receipt) => {
      console.log('Transaction completed:', receipt);
      ui.notify('Transaction completed successfully!', 'success');
    });
    
    transactionHandler.on('transactionError', (error) => {
      console.error('Transaction failed:', error);
      ui.notify('Transaction failed: ' + error.message, 'error');
    });
    
    console.log('App initialized successfully');
  } catch (error) {
    console.error('Failed to initialize app:', error);
    ui.notify('Failed to initialize application', 'error');
  }
}

// Example transaction function
async function executeSampleTransaction() {
  try {
    const txParams = {
      to: '0x123...', // Recipient address
      value: '1000000000000000000', // 1 ETH in wei
      data: '0x' // Optional data
    };
    
    const txHash = await transactionHandler.sendTransaction(txParams);
    console.log('Transaction hash:', txHash);
    return txHash;
  } catch (error) {
    console.error('Transaction error:', error);
    throw error;
  }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeApp);
```
