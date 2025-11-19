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

```javascript
// Import required modules
const { 
  Address, 
  BigDecimal, 
  BigInt, 
  Bytes, 
  ethereum 
} = require('@graphprotocol/graph-ts');

// Define the LiquidityPool entity
export entity LiquidityPool {
  id: string;
  address: Address;
  token0: Address;
  token1: Address;
  liquidityProviderCount: BigInt;
  totalValueLocked: BigDecimal;
  liquidity: BigDecimal;
}

// Define the LiquidityPoolFactory entity
export entity LiquidityPoolFactory {
  id: string;
  address: Address;
  liquidityPoolCount: BigInt;
}

// Define the UniswapV2Factory contract ABI
const UNISWAP_V2_FACTORY_ABI = [
  {
    inputs: [],
    stateMutability: 'nonpayable',
    type: 'constructor',
  },
  {
    inputs: [],
    name: 'getPair',
    outputs: [
      { internalType: 'address', name: '', type: 'address' },
    ],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [],
    name: 'allPairs',
    outputs: [
      { internalType: 'address[]', name: '', type: 'address[]' },
    ],
    stateMutability: 'view',
    type: 'function',
  },
];

// Define the UniswapV2Pair contract ABI
const UNISWAP_V2_PAIR_ABI = [
  {
    inputs: [],
    stateMutability: 'nonpayable',
    type: 'constructor',
  },
  {
    inputs: [],
    name: 'token0',
    outputs: [
      { internalType: 'address', name: '', type: 'address' },
    ],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [],
    name: 'token1',
    outputs: [
      { internalType: 'address', name: '', type: 'address' },
    ],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [],
    name: 'getReserves',
    outputs: [
      { internalType: 'uint112', name: '_reserve0', type: 'uint112' },
      { internalType: 'uint112', name: '_reserve1', type: 'uint112' },
      { internalType: 'uint32', name: '_blockTimestampLast', type: 'uint32' },
    ],
    stateMutability: 'view',
    type: 'function',
  },
];

// Define the subgraph
export default function handleBlock(event: ethereum.Block): void {
  // Get the UniswapV2Factory contract instance
  const factoryAddress = '0x5C69bEe701ef814a8ec96CDe009496bf0Fcbd7EB6';
  const factoryContract = ethereum.contract(UNISWAP_V2_FACTORY_ABI, factoryAddress);

  // Get all liquidity pools
  const liquidityPools = factoryContract.getAllPairs();

  // Iterate over liquidity pools
  for (let i = 0; i < liquidityPools.length; i++) {
    const liquidityPoolAddress = liquidityPools[i];
    const liquidityPoolContract = ethereum.contract(UNISWAP_V2_PAIR_ABI, liquidityPoolAddress);

    // Get liquidity pool data
    const token0 = liquidityPoolContract.token0();
    const token1 = liquidityPoolContract.token1();
    const [reserve0, reserve1, ] = liquidityPoolContract.getReserves();

    // Calculate total value locked
    const totalValueLocked = BigDecimal.fromString(reserve0.toBigDecimal().plus(reserve1.toBigDecimal()));

    // Create or update the liquidity pool entity
    let liquidityPool = LiquidityPool.load(liquidityPoolAddress);
    if (!liquidityPool) {
      liquidityPool = new LiquidityPool(liquidityPoolAddress);
      liquidityPool.token0 = token0;
      liquidityPool.token1 = token1;
      liquidityPool.liquidityProviderCount = BigInt.fromString('0');
      liquidityPool.totalValueLocked = totalValueLocked;
      liquidityPool.liquidity = BigDecimal.fromString('0');
    } else {
      liquidityPool.totalValueLocked = totalValueLocked;
    }
    liquidityPool.save();

    // Create or update the liquidity pool factory entity
    let liquidityPoolFactory = LiquidityPoolFactory.load(factoryAddress);
    if (!liquidityPoolFactory) {
      liquidityPoolFactory = new LiquidityPoolFactory(factoryAddress);
      liquidityPoolFactory.liquidityPoolCount = BigInt.fromString('0');
    }
    liquidityPoolFactory.liquidityPoolCount = liquidityPoolFactory.liquidityPoolCount.plus(BigInt.fromString('1'));
    liquidityPoolFactory.save();
  }
}

// Define a handler for when a liquidity pool is created
export function handleLiquidityPoolCreated(event: ethereum.Event): void {
  // Get the liquidity pool address
  const liquidityPoolAddress = event.params.pair;

  // Create a new liquidity pool entity
  const liquidityPool = new LiquidityPool(liquidityPoolAddress);
  liquidityPool.token0 = event.params.token0;
  liquidityPool.token1 = event.params.token1;
  liquidityPool.liquidityProviderCount = BigInt.fromString('0');
  liquidityPool.totalValueLocked = BigDecimal.fromString('0');
  liquidityPool.liquidity = BigDecimal.fromString('0');
  liquidityPool.save();
}

// Define a handler for when a liquidity provider adds or removes liquidity
export function handleLiquidityPoolUpdate(event: ethereum.Event): void {
  // Get the liquidity pool address
  const liquidityPoolAddress = event.address;

  // Get the liquidity pool entity
  const liquidityPool = LiquidityPool.load(liquidityPoolAddress);

  // Update the liquidity pool entity
  if (liquidityPool) {
    // Update liquidity provider count
    const liquidityProviderCount = event.params.liquidityProviderCount;
    liquidityPool.liquidityProviderCount = liquidityProviderCount;
    liquidityPool.save();
  }
}
```
