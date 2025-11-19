"""
Generated Code Metadata:
========================
Original URL: https://orderly-network.pages.dev
Prompt: Create a technical documentation outline for Orderly Network's SDK, including code examples for building a spot or perps DEX on NEAR or EVM.
Generated: DETERMINISTIC_8d0c3148adb97be1
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```markdown
# Orderly Network SDK Technical Documentation Outline

## Table of Contents
1. Introduction
   - Overview of Orderly Network
   - Purpose of the SDK
   - Supported Blockchains (NEAR, EVM)

2. Getting Started
   - Installation
     - Prerequisites
     - Installation Steps
   - Configuration
     - API Keys
     - Network Configuration

3. SDK Structure
   - Overview of SDK Components
   - Key Classes and Functions

4. Building a Spot DEX
   - Overview of Spot DEX
   - Code Example: Initializing the SDK
     ```javascript
     // Import the Orderly Network SDK
     const OrderlySDK = require('orderly-sdk');

     // Initialize the SDK with configuration
     const sdk = new OrderlySDK({
         apiKey: 'YOUR_API_KEY',
         network: 'EVM' // or 'NEAR'
     });
     ```

   - Code Example: Creating a Spot Market
     ```javascript
     async function createSpotMarket() {
         try {
             const market = await sdk.createMarket({
                 baseAsset: 'ETH',
                 quoteAsset: 'USDT',
                 marketType: 'spot'
             });
             console.log('Spot Market Created:', market);
         } catch (error) {
             console.error('Error creating spot market:', error);
         }
     }
     ```

   - Code Example: Placing a Spot Order
     ```javascript
     async function placeSpotOrder() {
         try {
             const order = await sdk.placeOrder({
                 marketId: 'market_id_here',
                 side: 'buy', // or 'sell'
                 amount: 1,
                 price: 2000
             });
             console.log('Spot Order Placed:', order);
         } catch (error) {
             console.error('Error placing spot order:', error);
         }
     }
     ```

5. Building a Perpetual DEX
   - Overview of Perpetual DEX
   - Code Example: Initializing the SDK for Perpetuals
     ```javascript
     // Initialize the SDK for perpetual trading
     const sdkPerpetual = new OrderlySDK({
         apiKey: 'YOUR_API_KEY',
         network: 'EVM' // or 'NEAR'
     });
     ```

   - Code Example: Creating a Perpetual Market
     ```javascript
     async function createPerpetualMarket() {
         try {
             const market = await sdkPerpetual.createMarket({
                 baseAsset: 'BTC',
                 quoteAsset: 'USDT',
                 marketType: 'perpetual'
             });
             console.log('Perpetual Market Created:', market);
         } catch (error) {
             console.error('Error creating perpetual market:', error);
         }
     }
     ```

   - Code Example: Placing a Perpetual Order
     ```javascript
     async function placePerpetualOrder() {
         try {
             const order = await sdkPerpetual.placeOrder({
                 marketId: 'market_id_here',
                 side: 'sell', // or 'buy'
                 amount: 0.1,
                 leverage: 10
             });
             console.log('Perpetual Order Placed:', order);
         } catch (error) {
             console.error('Error placing perpetual order:', error);
         }
     }
     ```

6. Error Handling
   - Common Errors and Solutions
   - Best Practices for Error Handling

7. Conclusion
   - Summary of SDK Features
   - Future Enhancements
   - Community and Support

8. Appendices
   - API Reference
   - Glossary of Terms
   - Additional Resources
```
