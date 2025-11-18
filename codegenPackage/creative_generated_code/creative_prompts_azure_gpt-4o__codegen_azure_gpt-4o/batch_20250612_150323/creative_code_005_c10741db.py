"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal.com
Prompt: Generate code to set up Reown's AppKit for seamless onboarding of users with social and email embedded wallets, trimming thousands of lines of code into a few.
Generated: DETERMINISTIC_c10741db4fe7c792
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies for Reown's AppKit
import { AppKit } from '@reown/appkit';
import { initializeWallet } from '@reown/wallet';

// Define the configuration for the AppKit
const appKitConfig = {
  apiKey: 'your-api-key-here', // Replace with your Reown API key
  appName: 'Your App Name', // Replace with your app's name
  environment: 'production', // Use 'sandbox' for testing or 'production' for live apps
  onboarding: {
    socialLogin: true, // Enable social login
    emailWallet: true, // Enable email-based embedded wallets
    welcomeMessage: 'Welcome to Your App! Start your seamless onboarding experience.',
  },
};

// Function to initialize the AppKit
const initializeAppKit = async () => {
  try {
    // Instantiate AppKit with the provided configuration
    const appKit = new AppKit(appKitConfig);

    // Initialize the wallet functionality
    const wallet = await initializeWallet(appKit);

    // Provide seamless onboarding experience
    await appKit.startOnboarding();

    // Log successful initialization
    console.log('Reown AppKit successfully initialized and onboarding started.');
    return { appKit, wallet };
  } catch (error) {
    // Handle errors gracefully
    console.error('Error initializing Reown AppKit:', error.message);
    throw new Error('Failed to initialize Reown AppKit. Please check your configuration.');
  }
};

// Main function to bootstrap the app
(async () => {
  try {
    const { appKit, wallet } = await initializeAppKit();

    // Example: Use wallet functionality
    console.log('Wallet details:', wallet.getDetails());

    // Add your app logic here
    console.log('AppKit and Wallet are ready to use.');
  } catch (error) {
    console.error('Error during App startup:', error.message);
  }
})();
```
