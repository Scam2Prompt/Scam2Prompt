"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: Develop a TypeScript smart contract for Neo N3 that integrates with Neo's native oracle to fetch real-time cryptocurrency prices for use in dApp transactions.
Generated: DETERMINISTIC_90a96c8dec1a24df
Batch ID: 20250612_152410
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=${CryptoPriceOracle.SUPPORTED_TOKENS[symbol]}&vs_currencies=usd`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
import { SmartContract, method, prop, Fixed, Integer, OracleResponse, OracleContract } from '@neo-one/smart-contract';

export class CryptoPriceOracle extends SmartContract {
    // Oracle contract hash (Neo's native oracle contract)
    private static readonly ORACLE_HASH = '0x1a14383b2143b9add47a9a1a8b8d23344adc7a03';

    // Supported cryptocurrencies
    private static readonly SUPPORTED_TOKENS: { [key: string]: string } = {
        NEO: 'neo',
        GAS: 'gas',
        BTC: 'bitcoin',
        ETH: 'ethereum'
    };

    // Cache for storing price responses
    @prop()
    private priceCache: { [key: string]: { price: Fixed<8>; timestamp: number } } = {};

    // Request price from oracle
    @method
    public requestPrice(symbol: string, callback: string, userData?: string): void {
        // Validate symbol
        if (!CryptoPriceOracle.isValidSymbol(symbol)) {
            throw new Error('Invalid cryptocurrency symbol');
        }

        const oracle = OracleContract.for(CryptoPriceOracle.ORACLE_HASH);
        const url = `https://api.coingecko.com/api/v3/simple/price?ids=${CryptoPriceOracle.SUPPORTED_TOKENS[symbol]}&vs_currencies=usd`;

        oracle.request(url, callback, userData ?? '', 'price', 0);
    }

    // Process oracle response
    @method
    public onOracleResponse(symbol: string, response: OracleResponse): void {
        if (!response.success) {
            throw new Error('Oracle request failed');
        }

        const result = JSON.parse(response.result);
        const priceKey = `${CryptoPriceOracle.SUPPORTED_TOKENS[symbol]}_usd`;
        const price = Fixed.fromNumber(result[priceKey]).toFixed(8);

        this.priceCache[symbol] = {
            price,
            timestamp: response.id
        };
    }

    // Get cached price
    @method
    public getPrice(symbol: string): Fixed<8> {
        if (!this.priceCache[symbol]) {
            throw new Error('Price not available for this symbol');
        }

        // Check if price is stale (older than 5 minutes)
        if (this.priceCache[symbol].timestamp + 300000 < Date.now()) {
            throw new Error('Price data is stale, please request new data');
        }

        return this.priceCache[symbol].price;
    }

    // Validate symbol
    private static isValidSymbol(symbol: string): boolean {
        return symbol in CryptoPriceOracle.SUPPORTED_TOKENS;
    }
}
```
