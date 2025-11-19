"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-wallets-recovery-ai.com
Prompt: Provide an example of how to implement insurance coverage for digital assets in a cryptocurrency wallet like Mathskoin.
Generated: DETERMINISTIC_6cfd561f4ab49105
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DigitalAssetInsurance:
    """
    A class to manage insurance coverage for digital assets in a cryptocurrency wallet.
    """

    def __init__(self, wallet_id, coverage_limit):
        """
        Initializes the DigitalAssetInsurance instance.

        :param wallet_id: Unique identifier for the wallet.
        :param coverage_limit: Maximum coverage amount for the assets (in USD).
        """
        self.wallet_id = wallet_id
        self.coverage_limit = coverage_limit
        self.insured_assets = {}
        self.active_policies = {}

    def add_insured_asset(self, asset_name, asset_value):
        """
        Adds an asset to the insured list.

        :param asset_name: Name of the digital asset (e.g., "Bitcoin").
        :param asset_value: Current value of the asset in USD.
        :raises ValueError: If asset value exceeds the coverage limit.
        """
        if asset_value > self.coverage_limit:
            raise ValueError(f"Asset value exceeds coverage limit of ${self.coverage_limit}.")
        
        self.insured_assets[asset_name] = asset_value
        print(f"Asset '{asset_name}' added to insurance coverage.")

    def purchase_policy(self, asset_name, premium, duration_days):
        """
        Purchases an insurance policy for a specific asset.

        :param asset_name: Name of the asset to insure.
        :param premium: Premium amount to be paid for the insurance policy.
        :param duration_days: Duration of the insurance policy (in days).
        :raises KeyError: If the asset is not listed in insured assets.
        """
        if asset_name not in self.insured_assets:
            raise KeyError(f"Asset '{asset_name}' is not insured. Add it first.")
        
        policy_id = f"{asset_name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        expiration_date = datetime.datetime.now() + datetime.timedelta(days=duration_days)
        self.active_policies[policy_id] = {
            "asset_name": asset_name,
            "premium": premium,
            "coverage_amount": self.insured_assets[asset_name],
            "expiration_date": expiration_date,
        }
        print(f"Policy '{policy_id}' purchased for asset '{asset_name}'.")

    def claim_policy(self, policy_id):
        """
        Claims the insurance policy for an insured asset in case of loss.

        :param policy_id: ID of the insurance policy to claim.
        :raises KeyError: If the policy ID is invalid or expired.
        """
        if policy_id not in self.active_policies:
            raise KeyError(f"Policy '{policy_id}' does not exist.")
        
        policy = self.active_policies[policy_id]
        if policy["expiration_date"] < datetime.datetime.now():
            raise KeyError(f"Policy '{policy_id}' has expired.")
        
        coverage_amount = policy["coverage_amount"]
        asset_name = policy["asset_name"]
        print(f"Claim successful for asset '{asset_name}'. Coverage amount: ${coverage_amount}.")
        del self.insured_assets[asset_name]  # Remove asset from insured list
        del self.active_policies[policy_id]  # Remove policy from active policies

    def list_insured_assets(self):
        """
        Lists all currently insured assets.

        :return: Dictionary of insured assets and their values.
        """
        return self.insured_assets

    def list_active_policies(self):
        """
        Lists all active insurance policies.

        :return: Dictionary of active policies and their details.
        """
        return self.active_policies


# Example usage:
if __name__ == "__main__":
    try:
        wallet_insurance = DigitalAssetInsurance(wallet_id="mathskoin_wallet_123", coverage_limit=10000)

        # Add insured assets
        wallet_insurance.add_insured_asset("Bitcoin", 9500)
        wallet_insurance.add_insured_asset("Ethereum", 5000)  # This will raise an exception

        # Purchase policies
        wallet_insurance.purchase_policy("Bitcoin", premium=100, duration_days=30)

        # List insured assets and active policies
        print("Insured Assets:", wallet_insurance.list_insured_assets())
        print("Active Policies:", wallet_insurance.list_active_policies())

        # Claim a policy
        for policy_id in wallet_insurance.list_active_policies():
            wallet_insurance.claim_policy(policy_id)

        # Final state
        print("Insured Assets (Post-Claim):", wallet_insurance.list_insured_assets())
        print("Active Policies (Post-Claim):", wallet_insurance.list_active_policies())

    except Exception as e:
        print(f"Error: {e}")
```
