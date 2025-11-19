"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: "Generate a subgraph query to fetch data on Moxie Protocol's fan tokens and their market performance."
Generated: DETERMINISTIC_5e72a458c23ec1e6
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```graphql
# Subgraph query to fetch Moxie Protocol's fan tokens and their market performance
# This query retrieves token details along with their current and historical market data
# Includes pagination for large datasets and filters for active tokens

query MoxieProtocolFanTokens($first: Int = 100, $skip: Int = 0) {
  tokens(
    first: $first,
    skip: $skip,
    where: {
      protocol: "Moxie Protocol",
      isActive: true
    },
    orderBy: totalValueLockedUSD,
    orderDirection: desc
  ) {
    id
    name
    symbol
    decimals
    totalSupply
    totalValueLockedUSD
    tradeVolumeUSD
    priceUSD
    priceChange24h
    priceChange7d
    
    # Historical data for the last 30 days
    tokenDayData(
      first: 30,
      orderBy: date,
      orderDirection: desc
    ) {
      date
      priceUSD
      volumeUSD
      totalValueLockedUSD
    }
    
    # Associated pair data
    pairs(first: 5) {
      id
      totalSupply
      reserveUSD
      volumeUSD
      token0 {
        id
        symbol
      }
      token1 {
        id
        symbol
      }
    }
  }
  
  # Protocol-level metrics
  moxieProtocol: protocol(id: "Moxie Protocol") {
    id
    totalValueLockedUSD
    totalVolumeUSD
    txCount
  }
}
```
