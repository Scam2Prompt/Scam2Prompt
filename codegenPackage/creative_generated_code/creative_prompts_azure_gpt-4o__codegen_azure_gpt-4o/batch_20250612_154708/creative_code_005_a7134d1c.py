"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defilellama.com
Prompt: Provide an example of using Swap Llama to scan liquidity sources for swapping USDT to DAI on Polygon with the lowest fees.
Generated: DETERMINISTIC_a7134d1c634f2497
Batch ID: 20250612_154708
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://swap.llama.fi": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import aiohttp

# Define constants for the Swap Llama API and token addresses
SWAP_LLAMAS_API = "https://swap.llama.fi"
CHAIN = "polygon"
USDT_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"  # USDT on Polygon
DAI_ADDRESS = "0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063"  # DAI on Polygon
AMOUNT_IN_USDT = 1000  # Amount to swap (in USDT)

async def find_best_swap():
    """
    Queries Swap Llama API to find the best swap route for converting USDT to DAI on Polygon.
    """
    try:
        # Prepare the request URL
        url = f"{SWAP_LLAMAS_API}/quote"
        payload = {
            "chain": CHAIN,
            "fromToken": USDT_ADDRESS,
            "toToken": DAI_ADDRESS,
            "amount": int(AMOUNT_IN_USDT * 10**6),  # Convert USDT amount to smallest unit (6 decimals)
        }
        
        # Perform the API request
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch swap quote: {response.status} {response.reason}")
                
                data = await response.json()
                
                # Ensure the response contains valid data
                if "routes" not in data or not data["routes"]:
                    raise Exception("No valid routes found in the response.")

                # Extract the route with the lowest fees
                best_route = min(data["routes"], key=lambda x: x["totalGasFee"])
                
                return best_route

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

async def main():
    """
    Main function to run the swap query and print the result.
    """
    print("Finding the best swap route for USDT->DAI on Polygon...")
    best_route = await find_best_swap()
    
    if best_route:
        print("Best Swap Route Found:")
        print(f"  Protocol: {best_route['protocol']}")
        print(f"  Estimated Gas Fee: {best_route['totalGasFee']}")
        print(f"  Output Amount (DAI): {best_route['amountTo'] / 10**18:.6f}")  # Convert DAI amount (18 decimals)
    else:
        print("Could not find a valid swap route.")

# Run the program
if __name__ == "__main__":
    asyncio.run(main())
```
