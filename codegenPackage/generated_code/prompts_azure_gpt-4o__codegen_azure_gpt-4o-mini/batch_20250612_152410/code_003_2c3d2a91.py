"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: Develop a TypeScript smart contract for Neo N3 that utilizes the built-in oracle to fetch off-chain data and trigger events based on the retrieved information.
Generated: DETERMINISTIC_2c3d2a912fc7aa5d
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary modules from the Neo Smart Contract framework
import { SmartContract, u, oracle, storage, log } from '@neo-one/smart-contract';

// Define the smart contract class
export class OracleContract extends SmartContract {
    // Define an event to emit when data is fetched
    public static DataFetched: (data: string) => void;

    // Function to request data from the oracle
    public requestData(url: string): void {
        // Validate the URL format
        if (!this.isValidUrl(url)) {
            throw new Error('Invalid URL format');
        }

        // Request data from the oracle
        const requestId = oracle.request(url);
        log(`Data request sent with ID: ${requestId}`);
    }

    // Callback function that the oracle will call with the response
    public onDataReceived(requestId: string, data: string): void {
        // Log the received data
        log(`Data received for request ID ${requestId}: ${data}`);

        // Emit the DataFetched event with the retrieved data
        OracleContract.DataFetched(data);

        // Store the data in contract storage for future reference
        storage.put(requestId, data);
    }

    // Function to validate the URL format
    private isValidUrl(url: string): boolean {
        const urlPattern = new RegExp('^(https?:\\/\\/)?' + // protocol
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])?)\\.)+[a-z]{2,}|' + // domain name
            'localhost|' + // localhost
            '\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}|' + // IPv4
            '\\[([0-9a-f]{1,4}:){7,7}[0-9a-f]{1,4}\\]|' + // IPv6
            '([0-9a-f]{1,4}:){1,7}:|::([0-9a-f]{1,4}:){0,6}[0-9a-f]{1,4}|([0-9a-f]{1,4}:){1,6}:[0-9a-f]{1,4}|([0-9a-f]{1,4}:){1,5}(:[0-9a-f]{1,4}){1,2}|([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,3}|([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,4}|([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5}|[0-9a-f]{1,4}:((:[0-9a-f]{1,4}){1,6})|:((:[0-9a-f]{1,4}){1,7}|:)|fe80:(:[0-9a-f]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}' + // IPv6
            '((25[0-5]|(2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9]))\\.){3}' + // IPv4
            '(25[0-5]|(2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9]))' + // IPv4
            '(:\\d+)?$'); // port

        return urlPattern.test(url);
    }
}
```
