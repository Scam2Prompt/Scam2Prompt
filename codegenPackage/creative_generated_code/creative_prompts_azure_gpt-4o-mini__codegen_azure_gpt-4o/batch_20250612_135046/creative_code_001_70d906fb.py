"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://example.walletconnect.org
Prompt: Provide code snippets for integrating WalletConnect v2.8.6 in a React application for selecting specific chains.
Generated: DETERMINISTIC_70d906fb68ba9465
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: walletConnectIntegration.js

// Import necessary modules
import { useEffect, useState } from "react";
import { WalletConnectModalSign } from "@walletconnect/modal-sign-react";
import {
  WalletConnectClient,
  PUBLIC_KEY_NAME,
  ENV_DEFAULT,
} from "@walletconnect/client";
import { formatJsonRpcError, formatJsonRpcResult } from "@walletconnect/jsonrpc-utils";

// Constants for WalletConnect configuration
const WALLETCONNECT_PROJECT_ID = "YOUR_PROJECT_ID"; // Replace with your WalletConnect project ID
const SUPPORTED_CHAINS = ["eip155:1", "eip155:137"]; // Ethereum Mainnet and Polygon Mainnet

// React component
const WalletConnectIntegration = () => {
  const [client, setClient] = useState(null);
  const [session, setSession] = useState(null);
  const [error, setError] = useState(null);

  // Initialize WalletConnect client
  useEffect(() => {
    const initializeClient = async () => {
      try {
        const walletConnectClient = await WalletConnectClient.init({
          relayUrl: ENV_DEFAULT.RELAY_URL,
          projectId: WALLETCONNECT_PROJECT_ID,
        });

        setClient(walletConnectClient);

        // Subscribe to client events
        walletConnectClient.on("session_proposal", onSessionProposal);
        walletConnectClient.on("session_delete", onSessionDelete);
      } catch (err) {
        console.error("Failed to initialize WalletConnect client:", err);
        setError("Failed to initialize WalletConnect client. Please try again later.");
      }
    };

    initializeClient();

    // Cleanup on unmount
    return () => {
      if (client) {
        client.off("session_proposal", onSessionProposal);
        client.off("session_delete", onSessionDelete);
      }
    };
  }, []);

  // Handle session proposal
  const onSessionProposal = async (proposal) => {
    try {
      const { id, params } = proposal;
      const { requiredNamespaces } = params;

      // Filter chains based on supported chains
      const namespaces = Object.keys(requiredNamespaces).reduce((acc, namespace) => {
        const chains = requiredNamespaces[namespace].chains.filter((chain) =>
          SUPPORTED_CHAINS.includes(chain)
        );
        if (chains.length) {
          acc[namespace] = {
            methods: requiredNamespaces[namespace].methods,
            events: requiredNamespaces[namespace].events,
            chains,
          };
        }
        return acc;
      }, {});

      if (Object.keys(namespaces).length === 0) {
        // Reject the proposal if no supported chains are found
        await client.rejectSession(id, formatJsonRpcError(id, "Unsupported chains"));
        return;
      }

      // Approve the session proposal with filtered namespaces
      const approvedSession = await client.approveSession({
        id,
        namespaces,
      });
      setSession(approvedSession);
    } catch (err) {
      console.error("Failed to handle session proposal:", err);
      setError("Failed to handle session proposal. Please try again.");
    }
  };

  // Handle session deletion
  const onSessionDelete = () => {
    setSession(null);
    console.log("Session deleted successfully.");
  };

  // Trigger WalletConnect modal
  const connectWallet = async () => {
    if (!client) {
      setError("WalletConnect client is not initialized.");
      return;
    }

    try {
      client.connect({
        requiredNamespaces: {
          eip155: {
            methods: ["eth_sendTransaction", "eth_signTransaction", "eth_sign", "personal_sign"],
            events: ["chainChanged", "accountsChanged"],
            chains: SUPPORTED_CHAINS,
          },
        },
      });
    } catch (err) {
      console.error("Failed to connect wallet:", err);
      setError("Failed to connect wallet. Please try again.");
    }
  };

  return (
    <div>
      <h1>WalletConnect Integration</h1>
      {/* Error message display */}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {/* Connect Wallet Button */}
      <button onClick={connectWallet}>Connect Wallet</button>
      {/* WalletConnect Modal */}
      {client && <WalletConnectModalSign client={client} />}
    </div>
  );
};

export default WalletConnectIntegration;
```
