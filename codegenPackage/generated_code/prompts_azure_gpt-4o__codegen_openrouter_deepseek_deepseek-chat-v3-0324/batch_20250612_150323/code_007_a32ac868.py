"""
Generated Code Metadata:
========================
Original URL: https://web3inbox.com
Prompt: Generate code to switch between multiple wallets in Web3Inbox, ensuring notifications are managed for the active wallet.
Generated: DETERMINISTIC_a32ac868182f37b3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { useWeb3InboxAccount, useWeb3InboxClient } from "@web3inbox/react";
import { useAccount, useSwitchAccount } from "wagmi";
import { useCallback, useEffect } from "react";

interface WalletSwitchProps {
  onWalletSwitch?: (newAddress: string) => void;
}

/**
 * Component to handle switching between multiple wallets in Web3Inbox
 * and managing notifications for the active wallet.
 */
export const WalletSwitcher = ({ onWalletSwitch }: WalletSwitchProps) => {
  const { address: activeAddress } = useAccount();
  const { switchAccount } = useSwitchAccount();
  const { account: web3InboxAccount, setAccount } = useWeb3InboxAccount();
  const { client } = useWeb3InboxClient();

  /**
   * Handles switching to a new wallet address
   * @param newAddress The new wallet address to switch to
   */
  const handleSwitchWallet = useCallback(
    async (newAddress: string) => {
      try {
        // Switch the connected wallet
        await switchAccount({ address: newAddress });

        // Update Web3Inbox account if different from current
        if (web3InboxAccount !== newAddress) {
          await setAccount(newAddress);
        }

        // Optional callback for additional actions
        if (onWalletSwitch) {
          onWalletSwitch(newAddress);
        }
      } catch (error) {
        console.error("Failed to switch wallet:", error);
        throw error;
      }
    },
    [switchAccount, web3InboxAccount, setAccount, onWalletSwitch]
  );

  // Sync Web3Inbox account when active wallet changes
  useEffect(() => {
    if (activeAddress && activeAddress !== web3InboxAccount) {
      setAccount(activeAddress).catch(console.error);
    }
  }, [activeAddress, web3InboxAccount, setAccount]);

  /**
   * Fetches notifications for the active wallet
   */
  const fetchNotifications = useCallback(async () => {
    if (!client || !activeAddress) return;

    try {
      const notifications = await client.getNotifications({
        account: activeAddress,
      });
      return notifications;
    } catch (error) {
      console.error("Failed to fetch notifications:", error);
      throw error;
    }
  }, [client, activeAddress]);

  return {
    activeAddress,
    switchWallet: handleSwitchWallet,
    fetchNotifications,
  };
};
```
