"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph-the-graph.org
Prompt: How can I use The Graph to create a subgraph for indexing DeFi data from Uniswap?
Generated: DETERMINISTIC_6b95b82573348dbf
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```graphql
# The Graph Subgraph Manifest
# This subgraph indexes DeFi data from Uniswap

# Specify the subgraph version
specVersion: 0.0.2

# Define the data source for the Uniswap factory contract
dataSources:
  - kind: ethereum/contract
    name: UniswapFactory
    network: mainnet
    source:
      address: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6"
      startBlock: 10838678 # Block where Uniswap was deployed
    mapping:
      kind: ethereum/events
      apiVersion: 0.0.4
      language: wasm/assemblyscript
      entities: ["Pair", "Token"]
      abis:
        - name: UniswapV2Factory
          file: ./abis/UniswapV2Factory.json
        - name: UniswapV2Pair
          file: ./abis/UniswapV2Pair.json
      eventHandlers:
        - event: PairCreated(address,address,uint256,uint256)
          handler: handlePairCreated
      file: ./src/mapping.ts

# Entity definitions
entities:
  - name: Pair
    fields:
      id: ID! @id
      token0: String!
      token1: String!
      totalSupply: BigInt!
      createdAt: BigInt!

  - name: Token
    fields:
      id: ID! @id
      name: String!
      symbol: String!
      totalLiquidity: BigInt!

# Mapping file to handle events
```

```typescript
// src/mapping.ts
import { PairCreated } from "../generated/UniswapFactory/UniswapV2Factory"
import { Pair, Token } from "../generated/schema"

// Handle the PairCreated event from the Uniswap factory
export function handlePairCreated(event: PairCreated): void {
  // Create a new Pair entity
  let pair = new Pair(event.params.pair.toHex())

  // Set entity fields with event parameters
  pair.token0 = event.params.token0.toHex()
  pair.token1 = event.params.token1.toHex()
  pair.totalSupply = event.params.initialSupply
  pair.createdAt = event.block.timestamp

  // Save the Pair entity to the store
  pair.save()

  // Optionally, create or update Token entities
  updateToken(event.params.token0)
  updateToken(event.params.token1)
}

// Update or create Token entity
function updateToken(tokenAddress: Address): void {
  let token = Token.load(tokenAddress.toHex())
  
  // If the token doesn't exist, create a new one
  if (!token) {
    token = new Token(tokenAddress.toHex())
    token.name = "Unknown Token" // Placeholder, ideally fetch from token contract
    token.symbol = "UNK" // Placeholder
    token.totalLiquidity = BigInt.fromI32(0) // Initial liquidity
  }

  // Update logic for totalLiquidity can be added here

  // Save the Token entity
  token.save()
}
```

```json
// abis/UniswapV2Factory.json
{
  "name": "UniswapV2Factory",
  "inputs": [],
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function",
  "payable": false
  // ABI details for PairCreated event and other functions can be included here
}
```

```json
// abis/UniswapV2Pair.json
{
  "name": "UniswapV2Pair",
  "inputs": [],
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function",
  "payable": false
  // ABI details for pair functions can be included here
}
``` 

This code represents a well-structured subgraph for indexing data from Uniswap on The Graph platform, including essential components like event handling and entity definitions.
