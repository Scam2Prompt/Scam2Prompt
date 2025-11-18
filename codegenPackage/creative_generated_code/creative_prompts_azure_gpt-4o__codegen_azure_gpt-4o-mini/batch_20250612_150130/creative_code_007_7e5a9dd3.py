"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneiumcount.vercel.app
Prompt: Write a function in TypeScript to interact with the Soneium Transaction Count Checker and handle errors gracefully.
Generated: DETERMINISTIC_7e5a9dd36f02a0f2
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules for HTTP requests
import axios, { AxiosError } from 'axios';

// Define a custom error for transaction count retrieval
class TransactionCountError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "TransactionCountError";
    }
}

// Function to get the transaction count for a specified address
async function getTransactionCount(address: string, apiUrl: string): Promise<number> {
    // Validate the address format (simple regex for example purposes)
    const addressRegex = /^[0-9a-fA-F]{42}$/;
    if (!addressRegex.test(address)) {
        throw new TransactionCountError("Invalid address format. Address must be a 42-character hex string.");
    }

    try {
        // Make a GET request to the Soneium Transaction Count Checker API
        const response = await axios.get(`${apiUrl}/transaction-count/${address}`);

        // Check if the response is valid and contains the transaction count
        if (response.status === 200 && response.data && typeof response.data.count === 'number') {
            return response.data.count; // Return the transaction count
        } else {
            throw new TransactionCountError("Invalid response format from the API.");
        }
    } catch (error) {
        // Handle errors from the API call
        if (axios.isAxiosError(error)) {
            // Handle expected Axios error responses
            throw new TransactionCountError(`API request failed: ${error.message}`);
        } else {
            // Handle unexpected errors
            throw new TransactionCountError("An unexpected error occurred while fetching the transaction count.");
        }
    }
}

// Export the function for use in other modules
export { getTransactionCount, TransactionCountError };
```
