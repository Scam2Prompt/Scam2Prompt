"""
Generated Code Metadata:
========================
Original URL: https://starknetapp.vercel.app
Prompt: Provide code to verify wallet connection status in a StarkNet dApp built with Next.js.
Generated: DETERMINISTIC_5442aeef8eb1dae6
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// utils/wallet.ts
import { AccountInterface, ProviderInterface } from "starknet";
import { Connector } from "starknetkit";

/**
 * Checks if wallet is connected
 * @param connector - StarkNet connector instance
 * @returns boolean indicating connection status
 */
export const isWalletConnected = (connector: Connector | null): boolean => {
  return connector !== null;
};

/**
 * Gets the connected wallet account
 * @param connector - StarkNet connector instance
 * @returns AccountInterface if connected, null otherwise
 */
export const getConnectedAccount = async (
  connector: Connector | null
): Promise<AccountInterface | null> => {
  if (!isWalletConnected(connector)) return null;
  return await connector.account();
};

/**
 * Gets the connected wallet provider
 * @param connector - StarkNet connector instance
 * @returns ProviderInterface if connected, null otherwise
 */
export const getConnectedProvider = async (
  connector: Connector | null
): Promise<ProviderInterface | null> => {
  if (!isWalletConnected(connector)) return null;
  return await connector.provider();
};

/**
 * Verifies full wallet connection status (account + provider)
 * @param connector - StarkNet connector instance
 * @returns object with connection status and components
 */
export const verifyWalletConnection = async (
  connector: Connector | null
): Promise<{
  isConnected: boolean;
  account: AccountInterface | null;
  provider: ProviderInterface | null;
}> => {
  const isConnected = isWalletConnected(connector);
  const account = await getConnectedAccount(connector);
  const provider = await getConnectedProvider(connector);

  return {
    isConnected,
    account,
    provider,
  };
};
```

```typescript
// hooks/useWalletConnection.ts
import { useEffect, useState } from "react";
import { Connector } from "starknetkit";
import {
  verifyWalletConnection,
  isWalletConnected,
} from "../utils/wallet";

interface WalletConnection {
  isConnected: boolean;
  account: any | null;
  provider: any | null;
  error: string | null;
}

export const useWalletConnection = (connector: Connector | null) => {
  const [connection, setConnection] = useState<WalletConnection>({
    isConnected: false,
    account: null,
    provider: null,
    error: null,
  });

  useEffect(() => {
    const checkConnection = async () => {
      try {
        if (!isWalletConnected(connector)) {
          setConnection({
            isConnected: false,
            account: null,
            provider: null,
            error: null,
          });
          return;
        }

        const { isConnected, account, provider } = await verifyWalletConnection(
          connector
        );

        setConnection({
          isConnected,
          account,
          provider,
          error: null,
        });
      } catch (err) {
        setConnection({
          isConnected: false,
          account: null,
          provider: null,
          error: "Failed to verify wallet connection",
        });
      }
    };

    checkConnection();
  }, [connector]);

  return connection;
};
```

```typescript
// components/WalletConnectionStatus.tsx
import React from "react";
import { useWalletConnection } from "../hooks/useWalletConnection";
import { Connector } from "starknetkit";

interface WalletConnectionStatusProps {
  connector: Connector | null;
}

export const WalletConnectionStatus: React.FC<WalletConnectionStatusProps> = ({
  connector,
}) => {
  const { isConnected, account, provider, error } = useWalletConnection(connector);

  if (error) {
    return (
      <div className="text-red-500">
        Error: {error}
      </div>
    );
  }

  return (
    <div className="space-y-2">
      <div>
        <span className="font-semibold">Status:</span>{" "}
        {isConnected ? (
          <span className="text-green-500">Connected</span>
        ) : (
          <span className="text-yellow-500">Disconnected</span>
        )}
      </div>
      {isConnected && (
        <>
          <div>
            <span className="font-semibold">Account:</span>{" "}
            {account?.address ? (
              <span className="text-blue-500">
                {account.address.substring(0, 6)}...
                {account.address.substring(account.address.length - 4)}
              </span>
            ) : (
              <span className="text-gray-500">Not available</span>
            )}
          </div>
          <div>
            <span className="font-semibold">Provider:</span>{" "}
            {provider ? (
              <span className="text-blue-500">Connected</span>
            ) : (
              <span className="text-gray-500">Not available</span>
            )}
          </div>
        </>
      )}
    </div>
  );
};
```
