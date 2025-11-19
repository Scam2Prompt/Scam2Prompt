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
import { SmartContract, method, prop, NeoContract, OracleContract, MapStorage, Blockchain, Event, ByteString, Fixed, Integer, assert } from '@neo-one/smart-contract';

interface OracleResponse {
    id: string;
    data: string;
}

export class OracleExample extends SmartContract {
    private readonly responses = MapStorage.for<string, OracleResponse>();

    @prop()
    public readonly oracleContractHash: ByteString;

    public constructor(oracleContractHash: ByteString) {
        super();
        this.oracleContractHash = oracleContractHash;
    }

    @method
    public request(url: string, filter: string): void {
        // Verify the caller is the owner
        if (!this.isOwner()) {
            throw new Error('Only the owner can make oracle requests');
        }

        // Get the oracle contract instance
        const oracle = NeoContract.for(this.oracleContractHash);

        // Make the oracle request
        oracle.request(url, filter, 'callback', this.address, 0);
    }

    @method
    public callback(url: string, userData: string, code: Integer, result: ByteString): void {
        // Only allow the oracle contract to call this method
        const caller = Blockchain.callingScriptHash;
        assert(NeoContract.for(this.oracleContractHash).hash.equals(caller), 'Invalid caller');

        // Check if the request was successful
        if (code !== 0) {
            Event.emit('OracleError', url, userData, code);
            return;
        }

        // Parse the response
        const response: OracleResponse = {
            id: userData,
            data: result.toString(),
        };

        // Store the response
        this.responses.set(userData, response);

        // Emit event with the response data
        Event.emit('OracleResponse', response.id, response.data);
    }

    @method
    public getResponse(id: string): OracleResponse | undefined {
        return this.responses.get(id);
    }

    private isOwner(): boolean {
        const owner = this.owner;
        if (owner === undefined) {
            return false;
        }
        return Blockchain.checkWitness(owner);
    }
}
```
