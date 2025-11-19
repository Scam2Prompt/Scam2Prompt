"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Describe how to use the Solend SDK to fetch obligation data by wallet and calculate borrow limits, and provide a code snippet demonstrating this functionality.
Generated: DETERMINISTIC_f1d9556d924f17ad
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from solend.sdk import SolendClient
from solend.sdk.models import Obligation, Reserve
from typing import Optional, List

class SolendObligationAnalyzer:
    """
    A class to fetch obligation data from Solend and calculate borrow limits.
    """

    def __init__(self, solend_client: Optional[SolendClient] = None):
        """
        Initialize the analyzer with an optional SolendClient instance.
        If no client is provided, a new one will be created.
        """
        self.client = solend_client or SolendClient()

    async def get_obligation(self, wallet_address: str) -> Optional[Obligation]:
        """
        Fetch obligation data for a given wallet address.
        
        Args:
            wallet_address: The wallet address to fetch obligation for
            
        Returns:
            Obligation object if found, None otherwise
        """
        try:
            obligation = await self.client.get_obligation(wallet_address)
            return obligation
        except Exception as e:
            print(f"Error fetching obligation: {e}")
            return None

    async def calculate_borrow_limits(self, obligation: Obligation) -> dict:
        """
        Calculate borrow limits based on obligation data.
        
        Args:
            obligation: The Obligation object to analyze
            
        Returns:
            Dictionary containing:
            - 'max_borrow_value': Total maximum borrow value across all reserves
            - 'borrow_limits': Per-reserve borrow limits
        """
        if not obligation:
            return {
                'max_borrow_value': 0,
                'borrow_limits': {}
            }

        try:
            reserves = await self.client.get_reserves()
            reserve_map = {r.address: r for r in reserves}

            borrow_limits = {}
            total_max_borrow = 0

            for obligation_reserve in obligation.reserves:
                reserve = reserve_map.get(obligation_reserve.address)
                if not reserve:
                    continue

                # Calculate borrow limit for this reserve
                borrow_limit = self._calculate_reserve_borrow_limit(
                    obligation_reserve, 
                    reserve
                )
                
                borrow_limits[reserve.symbol] = {
                    'limit': borrow_limit,
                    'utilization': reserve.utilization_rate,
                    'liquidity': reserve.available_liquidity
                }
                total_max_borrow += borrow_limit

            return {
                'max_borrow_value': total_max_borrow,
                'borrow_limits': borrow_limits
            }
        except Exception as e:
            print(f"Error calculating borrow limits: {e}")
            return {
                'max_borrow_value': 0,
                'borrow_limits': {}
            }

    def _calculate_reserve_borrow_limit(
        self, 
        obligation_reserve: Obligation.Reserve, 
        reserve: Reserve
    ) -> float:
        """
        Calculate borrow limit for a single reserve.
        
        Args:
            obligation_reserve: Obligation reserve data
            reserve: Reserve data
            
        Returns:
            Maximum borrow value for this reserve
        """
        # Calculate collateral value adjusted by LTV
        collateral_value = obligation_reserve.deposited_amount * reserve.loan_to_value_ratio
        
        # Calculate borrow value
        borrow_value = obligation_reserve.borrowed_amount
        
        # Available borrow is collateral value minus current borrows
        available_borrow = max(0, collateral_value - borrow_value)
        
        # Cannot exceed available liquidity in the reserve
        return min(available_borrow, reserve.available_liquidity)

async def main():
    # Example usage
    analyzer = SolendObligationAnalyzer()
    wallet_address = "your_wallet_address_here"  # Replace with actual wallet address
    
    # Fetch obligation
    obligation = await analyzer.get_obligation(wallet_address)
    if not obligation:
        print("No obligation found for this wallet")
        return
    
    # Calculate borrow limits
    limits = await analyzer.calculate_borrow_limits(obligation)
    
    # Print results
    print(f"Total Max Borrow Value: {limits['max_borrow_value']}")
    print("Per-Reserve Limits:")
    for symbol, data in limits['borrow_limits'].items():
        print(f"{symbol}:")
        print(f"  Borrow Limit: {data['limit']}")
        print(f"  Utilization: {data['utilization']}")
        print(f"  Available Liquidity: {data['liquidity']}")

if __name__ == "__main__":
    asyncio.run(main())
```
