"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: How do I customize the "Connect Wallet" button in RainbowKit to match the design shown in the RainbowKit example demo?
Generated: DETERMINISTIC_b435dffe6c7afdef
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary components and hooks from RainbowKit and React
import { ConnectButton } from '@rainbow-me/rainbowkit';
import React from 'react';

// Define a custom ConnectButton component to match the design as per the RainbowKit example demo
const CustomConnectButton = () => {
  return (
    <ConnectButton.Custom>
      {({
        account,
        chain,
        openAccountModal,
        openChainModal,
        openConnectModal,
        authenticationStatus,
        mounted,
      }) => {
        // If the component is not mounted or the authentication status is loading, render nothing
        const ready = mounted && authenticationStatus !== 'loading';
        const connected =
          ready &&
          account &&
          chain &&
          (!authenticationStatus || authenticationStatus === 'authenticated');

        return (
          <div
            {...(!ready && {
              'aria-hidden': true,
              style: {
                opacity: 0,
                pointerEvents: 'none',
                userSelect: 'none',
              },
            })}
          >
            {/* Render different button states based on connection status */}
            {(() => {
              // If not connected, show "Connect Wallet" button
              if (!connected) {
                return (
                  <button
                    onClick={openConnectModal}
                    type="button"
                    style={{
                      padding: '12px 24px',
                      backgroundColor: '#4CAF50',
                      color: 'white',
                      border: 'none',
                      borderRadius: '8px',
                      cursor: 'pointer',
                      fontSize: '16px',
                    }}
                  >
                    Connect Wallet
                  </button>
                );
              }

              // If the chain is unsupported, show "Wrong Network" button
              if (chain.unsupported) {
                return (
                  <button
                    onClick={openChainModal}
                    type="button"
                    style={{
                      padding: '12px 24px',
                      backgroundColor: '#FF5722',
                      color: 'white',
                      border: 'none',
                      borderRadius: '8px',
                      cursor: 'pointer',
                      fontSize: '16px',
                    }}
                  >
                    Wrong Network
                  </button>
                );
              }

              // If connected and the chain is supported, show account details
              return (
                <div style={{ display: 'flex', gap: '12px' }}>
                  <button
                    onClick={openChainModal}
                    type="button"
                    style={{
                      padding: '12px 24px',
                      backgroundColor: '#2196F3',
                      color: 'white',
                      border: 'none',
                      borderRadius: '8px',
                      cursor: 'pointer',
                      fontSize: '16px',
                    }}
                  >
                    {chain.name}
                  </button>
                  <button
                    onClick={openAccountModal}
                    type="button"
                    style={{
                      padding: '12px 24px',
                      backgroundColor: '#FFC107',
                      color: 'white',
                      border: 'none',
                      borderRadius: '8px',
                      cursor: 'pointer',
                      fontSize: '16px',
                    }}
                  >
                    {account.displayName}
                  </button>
                </div>
              );
            })()}
          </div>
        );
      }}
    </ConnectButton.Custom>
  );
};

// Export the custom button for use in the application
export default CustomConnectButton;
```
