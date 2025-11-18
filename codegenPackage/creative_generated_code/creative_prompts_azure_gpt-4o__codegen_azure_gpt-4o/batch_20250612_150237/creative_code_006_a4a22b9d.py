"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a function in TypeScript that retrieves the user's blockchain account details and displays them, referencing the Dapp Starter's integration of Web3 React.
Generated: DETERMINISTIC_a4a22b9d124bc9cb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules from @web3-react/core and ethers
import { Web3ReactProvider, useWeb3React } from "@web3-react/core";
import { ethers } from "ethers";

// Define the type for account details
interface AccountDetails {
  address: string;
  balance: string; // Balance in ETH
}

/**
 * Function to retrieve and display blockchain account details
 * @returns Promise<AccountDetails | null>
 */
export async function getBlockchainAccountDetails(): Promise<AccountDetails | null> {
  try {
    // Use the web3-react hook to access the blockchain provider and account
    const { library, account } = useWeb3React();

    // If no account is connected, return null
    if (!account || !library) {
      console.error("No connected account or provider found.");
      return null;
    }

    // Get the balance of the connected account
    const balanceBigNumber = await library.getBalance(account);

    // Convert the BigNumber balance to a human-readable string (ETH)
    const balance = ethers.utils.formatEther(balanceBigNumber);

    // Create the account details object
    const accountDetails: AccountDetails = {
      address: account,
      balance: balance,
    };

    // Display account details in the console
    console.log("Account Details:", accountDetails);

    // Return account details
    return accountDetails;
  } catch (error: unknown) {
    // Catch and log any errors that occur
    console.error("Error retrieving blockchain account details:", error);
    return null;
  }
}

// Wrap the app with Web3ReactProvider in your main application file
// Example:
// <Web3ReactProvider getLibrary={getLibrary}>
//   <YourApp />
// </Web3ReactProvider>

// Helper function to get the Web3 provider library
function getLibrary(provider: any): ethers.providers.Web3Provider {
  return new ethers.providers.Web3Provider(provider);
}

// Usage example
// Call `getBlockchainAccountDetails()` from a component that uses the Web3ReactProvider
```
