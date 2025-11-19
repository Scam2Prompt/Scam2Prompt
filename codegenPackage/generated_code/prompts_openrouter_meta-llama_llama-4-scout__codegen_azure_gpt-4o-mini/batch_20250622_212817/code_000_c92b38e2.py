"""
Generated Code Metadata:
========================
Original URL: https://thegraph-the-graph.org
Prompt: "Write a subgraph for indexing real-time data on liquidity pools for a DeFi platform like Uniswap using The Graph protocol."
Generated: DETERMINISTIC_c92b38e21e0c5c8c
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```graphql
# This subgraph indexes real-time data on liquidity pools for a DeFi platform like Uniswap
# using The Graph protocol. It tracks liquidity pool events and updates the state accordingly.

# Define the schema for the subgraph
type LiquidityPool @entity {
  id: ID!                     # Unique identifier for the liquidity pool
  token0: String!             # Address of the first token in the pool
  token1: String!             # Address of the second token in the pool
  totalSupply: BigDecimal!    # Total supply of the liquidity pool tokens
  reserve0: BigDecimal!       # Reserve amount of the first token
  reserve1: BigDecimal!       # Reserve amount of the second token
  createdAt: BigInt!          # Timestamp of pool creation
}

# Define the event that will trigger updates to the liquidity pool data
type PoolCreated @entity {
  id: ID!                     # Unique identifier for the event
  pool: LiquidityPool!        # Reference to the liquidity pool created
  token0: String!             # Address of the first token
  token1: String!             # Address of the second token
  totalSupply: BigDecimal!    # Total supply of the liquidity pool tokens
  createdAt: BigInt!          # Timestamp of the event
}

# Define the event that will trigger updates to the liquidity pool reserves
type PoolUpdated @entity {
  id: ID!                     # Unique identifier for the event
  pool: LiquidityPool!        # Reference to the liquidity pool updated
  reserve0: BigDecimal!       # Updated reserve amount of the first token
  reserve1: BigDecimal!       # Updated reserve amount of the second token
  updatedAt: BigInt!          # Timestamp of the event
}

# Define the mappings for handling events and updating the state
mapping event PoolCreated {
  // Handle the PoolCreated event
  event: PoolCreated {
    id: event.params.pool.toHex()  # Use the pool address as the unique ID
    token0: event.params.token0
    token1: event.params.token1
    totalSupply: event.params.totalSupply
    createdAt: event.block.timestamp
  }
}

mapping event PoolUpdated {
  // Handle the PoolUpdated event
  event: PoolUpdated {
    id: event.params.pool.toHex()  # Use the pool address as the unique ID
    reserve0: event.params.reserve0
    reserve1: event.params.reserve1
    updatedAt: event.block.timestamp
  }
}

# Define the data source for the subgraph
dataSource {
  kind: ethereum
  name: "LiquidityPool"
  network: mainnet
  source {
    address: "0xYourDeFiPlatformAddress"  # Replace with the actual DeFi platform address
    abi: "UniswapV2"                       # Replace with the actual ABI name
  }
  mapping {
    event: "PoolCreated(address,address,uint256)"
    event: "PoolUpdated(address,uint256,uint256)"
  }
}
```
