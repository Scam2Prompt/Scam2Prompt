"""
Generated Code Metadata:
========================
Original URL: https://venusutils.vercel.app
Prompt: Create a function to identify and manage bad debt in a Web3 application using the Venus Protocol Utils described on the Venus Utils webpage.
Generated: DETERMINISTIC_f8f93445641a9de9
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from web3 import Web3
from typing import List, Dict, Tuple, Optional
from venus_utils import VenusUtils  # Assuming this is the Venus Protocol Utils library

class BadDebtManager:
    """
    A class to identify and manage bad debt in a Web3 application using Venus Protocol Utils.
    """
    
    def __init__(self, web3_provider: str, venus_utils: VenusUtils):
        """
        Initialize the BadDebtManager with Web3 provider and Venus Utils instance.
        
        Args:
            web3_provider: URL of the Web3 provider (e.g., Infura, Alchemy)
            venus_utils: Initialized VenusUtils instance
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.venus_utils = venus_utils
        
    def get_accounts_with_bad_debt(self) -> List[Dict]:
        """
        Identify accounts with bad debt (health factor < 1).
        
        Returns:
            List of dictionaries containing account info with bad debt
        """
        try:
            all_markets = self.venus_utils.get_all_markets()
            accounts_with_bad_debt = []
            
            for market in all_markets:
                accounts = self.venus_utils.get_accounts_in_market(market)
                
                for account in accounts:
                    health_factor = self.venus_utils.get_health_factor(account)
                    
                    if health_factor < 1:
                        debt = self.venus_utils.get_account_debt(account)
                        collateral = self.venus_utils.get_account_collateral(account)
                        
                        accounts_with_bad_debt.append({
                            'account': account,
                            'health_factor': health_factor,
                            'total_debt': debt,
                            'total_collateral': collateral,
                            'market': market
                        })
            
            return accounts_with_bad_debt
            
        except Exception as e:
            raise Exception(f"Error fetching accounts with bad debt: {str(e)}")
    
    def liquidate_account(self, account: str, liquidator: str, debt_token: str, collateral_token: str) -> Tuple[bool, str]:
        """
        Attempt to liquidate an account with bad debt.
        
        Args:
            account: Address of the account to liquidate
            liquidator: Address of the liquidator
            debt_token: Address of the debt token to repay
            collateral_token: Address of the collateral token to seize
            
        Returns:
            Tuple of (success: bool, tx_hash: str)
        """
        try:
            # Check if account still has bad debt
            health_factor = self.venus_utils.get_health_factor(account)
            if health_factor >= 1:
                return False, "Account no longer has bad debt"
                
            # Get max amount that can be liquidated
            max_liquidation_amount = self.venus_utils.get_max_liquidation_amount(
                account, 
                debt_token, 
                collateral_token
            )
            
            if max_liquidation_amount <= 0:
                return False, "No debt available for liquidation"
                
            # Execute liquidation
            tx_hash = self.venus_utils.liquidate_borrow(
                liquidator,
                account,
                max_liquidation_amount,
                debt_token,
                collateral_token
            )
            
            return True, tx_hash
            
        except Exception as e:
            raise Exception(f"Error during liquidation: {str(e)}")
    
    def batch_liquidate_accounts(self, accounts: List[Dict], liquidator: str) -> Dict[str, Tuple[bool, str]]:
        """
        Attempt to liquidate multiple accounts with bad debt.
        
        Args:
            accounts: List of account dictionaries (from get_accounts_with_bad_debt)
            liquidator: Address of the liquidator
            
        Returns:
            Dictionary mapping account addresses to (success, tx_hash) tuples
        """
        results = {}
        
        for account_info in accounts:
            account = account_info['account']
            market = account_info['market']
            
            # Get debt and collateral tokens for this market
            debt_token = self.venus_utils.get_debt_token(market)
            collateral_token = self.venus_utils.get_collateral_token(market)
            
            success, result = self.liquidate_account(
                account,
                liquidator,
                debt_token,
                collateral_token
            )
            
            results[account] = (success, result)
            
        return results
    
    def get_bad_debt_summary(self) -> Dict:
        """
        Get summary statistics about bad debt in the protocol.
        
        Returns:
            Dictionary containing bad debt statistics
        """
        try:
            accounts = self.get_accounts_with_bad_debt()
            total_debt = sum(float(acc['total_debt']) for acc in accounts)
            total_collateral = sum(float(acc['total_collateral']) for acc in accounts)
            
            return {
                'total_accounts': len(accounts),
                'total_debt': total_debt,
                'total_collateral': total_collateral,
                'average_health_factor': sum(acc['health_factor'] for acc in accounts) / len(accounts) if accounts else 0
            }
            
        except Exception as e:
            raise Exception(f"Error generating bad debt summary: {str(e)}")
```
