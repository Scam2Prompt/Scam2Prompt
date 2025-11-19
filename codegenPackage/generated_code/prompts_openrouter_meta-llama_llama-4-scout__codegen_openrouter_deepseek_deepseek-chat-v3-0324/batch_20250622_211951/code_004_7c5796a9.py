"""
Generated Code Metadata:
========================
Original URL: https://uniswap.trade
Prompt: Describe how to use Uniswap's SDK to build a custom decentralized exchange frontend.
Generated: DETERMINISTIC_7c5796a9c08e77fd
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries and types
import { ChainId, Token, Fetcher, Route, Trade, TradeType, TokenAmount } from '@uniswap/sdk'
import { ethers } from 'ethers'
import { Web3Provider } from '@ethersproject/providers'

// Interface for token pair
interface TokenPair {
  tokenA: Token
  tokenB: Token
}

// Interface for trade details
interface TradeDetails {
  executionPrice: string
  nextMidPrice: string
  minimumAmountOut: string
  maximumAmountIn: string
}

// Initialize provider
const provider = new ethers.providers.Web3Provider(window.ethereum)

// Function to fetch token pair data
async function fetchTokenPair(tokenAAddress: string, tokenBAddress: string, chainId: ChainId): Promise<TokenPair> {
  const tokenA = await Fetcher.fetchTokenData(chainId, tokenAAddress, provider)
  const tokenB = await Fetcher.fetchTokenData(chainId, tokenBAddress, provider)
  return { tokenA, tokenB }
}

// Function to fetch pair and create route
async function createRoute(
  tokenA: Token,
  tokenB: Token,
  inputAmount: string,
  chainId: ChainId
): Promise<Route> {
  const pair = await Fetcher.fetchPairData(tokenA, tokenB, provider)
  const route = new Route([pair], tokenA)
  return route
}

// Function to create trade
function createTrade(
  route: Route,
  inputAmount: string,
  tradeType: TradeType
): Trade {
  const amountIn = new TokenAmount(route.input, inputAmount)
  return new Trade(route, amountIn, tradeType)
}

// Function to get trade details
function getTradeDetails(trade: Trade): TradeDetails {
  return {
    executionPrice: trade.executionPrice.toSignificant(6),
    nextMidPrice: trade.nextMidPrice.toSignificant(6),
    minimumAmountOut: trade.minimumAmountOut().toSignificant(6),
    maximumAmountIn: trade.maximumAmountIn().toSignificant(6)
  }
}

// Function to execute swap
async function executeSwap(
  trade: Trade,
  signer: ethers.Signer,
  slippageTolerance: number
): Promise<ethers.providers.TransactionResponse> {
  const path = [trade.inputAmount.token.address, trade.outputAmount.token.address]
  const to = await signer.getAddress()
  const deadline = Math.floor(Date.now() / 1000) + 60 * 20 // 20 minutes from now
  const value = trade.inputAmount.raw.toString()

  const tx = {
    data: '', // Will be populated with swap method data
    to: '', // Will be populated with router address
    value,
    from: to,
    gasLimit: ethers.utils.hexlify(1000000),
    gasPrice: ethers.utils.hexlify(20000000000)
  }

  return signer.sendTransaction(tx)
}

// Main function to perform swap
async function performSwap(
  tokenAAddress: string,
  tokenBAddress: string,
  inputAmount: string,
  chainId: ChainId,
  tradeType: TradeType,
  slippageTolerance: number
): Promise<void> {
  try {
    // Request account access if needed
    await provider.send('eth_requestAccounts', [])

    // Get token pair
    const { tokenA, tokenB } = await fetchTokenPair(tokenAAddress, tokenBAddress, chainId)

    // Create route
    const route = await createRoute(tokenA, tokenB, inputAmount, chainId)

    // Create trade
    const trade = createTrade(route, inputAmount, tradeType)

    // Get trade details
    const tradeDetails = getTradeDetails(trade)
    console.log('Trade Details:', tradeDetails)

    // Execute swap
    const signer = provider.getSigner()
    const tx = await executeSwap(trade, signer, slippageTolerance)
    console.log('Transaction Hash:', tx.hash)

    // Wait for transaction to be mined
    const receipt = await tx.wait()
    console.log('Transaction Receipt:', receipt)
  } catch (error) {
    console.error('Error performing swap:', error)
    throw error
  }
}

// Example usage
// Note: In a real app, these values would come from user input
const tokenAAddress = '0x...' // Token A contract address
const tokenBAddress = '0x...' // Token B contract address
const inputAmount = '1000000000000000000' // 1.0 token (in wei)
const chainId = ChainId.MAINNET
const tradeType = TradeType.EXACT_INPUT
const slippageTolerance = 50 // 0.5%

performSwap(tokenAAddress, tokenBAddress, inputAmount, chainId, tradeType, slippageTolerance)
  .catch(console.error)
```
