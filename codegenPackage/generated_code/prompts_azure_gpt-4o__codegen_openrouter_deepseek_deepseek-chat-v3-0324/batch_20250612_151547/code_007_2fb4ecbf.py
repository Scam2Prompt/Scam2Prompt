"""
Generated Code Metadata:
========================
Original URL: https://signalsx.com
Prompt: Write code to compare U.S. and international stock and forex brokers, incorporating criteria discussed by SignalsX for evaluating brokers.
Generated: DETERMINISTIC_2fb4ecbfa58c99fb
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

class BrokerType(Enum):
    STOCK = "Stock"
    FOREX = "Forex"
    MULTI_ASSET = "Multi-Asset"

class Regulation(Enum):
    SEC = "SEC (US)"
    FINRA = "FINRA"
    CFTC = "CFTC"
    NFA = "NFA"
    FCA = "FCA (UK)"
    ASIC = "ASIC (Australia)"
    IIROC = "IIROC (Canada)"
    MAS = "MAS (Singapore)"
    FSA = "FSA (Japan)"
    CYSEC = "CySEC (Cyprus)"
    OTHER = "Other"

@dataclass
class FeeStructure:
    commission_per_trade: float  # USD
    spread_markup: float  # Percentage
    withdrawal_fee: float  # USD
    inactivity_fee: float  # USD per month
    currency_conversion_fee: float  # Percentage

@dataclass
class TradingPlatform:
    name: str
    mobile_support: bool
    desktop_support: bool
    web_based: bool
    api_support: bool
    charting_tools: bool
    automated_trading: bool

@dataclass
class Broker:
    name: str
    broker_type: BrokerType
    regulations: List[Regulation]
    min_deposit: float  # USD
    leverage: float  # Ratio (e.g., 50:1)
    fee_structure: FeeStructure
    platforms: List[TradingPlatform]
    asset_coverage: List[str]
    customer_support_rating: float  # 1-5
    execution_speed_ms: int  # Milliseconds
    is_us_based: bool
    additional_features: Dict[str, str] = field(default_factory=dict)

class BrokerComparator:
    def __init__(self, brokers: List[Broker]):
        self.brokers = brokers

    def compare_by_fees(self) -> List[Broker]:
        """Compare brokers by total estimated fees for active trading."""
        return sorted(
            self.brokers,
            key=lambda b: (
                b.fee_structure.commission_per_trade +
                b.fee_structure.spread_markup +
                b.fee_structure.currency_conversion_fee
            )
        )

    def compare_by_regulation(self, regulation: Regulation) -> List[Broker]:
        """Filter brokers by specific regulation."""
        return [b for b in self.brokers if regulation in b.regulations]

    def compare_by_platform_features(self) -> List[Broker]:
        """Rank brokers by platform feature completeness."""
        return sorted(
            self.brokers,
            key=lambda b: (
                sum([
                    p.mobile_support,
                    p.desktop_support,
                    p.web_based,
                    p.api_support,
                    p.charting_tools,
                    p.automated_trading
                ]) for p in b.platforms
            ),
            reverse=True
        )

    def compare_by_customer_support(self) -> List[Broker]:
        """Sort brokers by customer support rating."""
        return sorted(self.brokers, key=lambda b: b.customer_support_rating, reverse=True)

    def compare_by_execution_speed(self) -> List[Broker]:
        """Sort brokers by trade execution speed."""
        return sorted(self.brokers, key=lambda b: b.execution_speed_ms)

    def us_vs_international(self) -> Dict[str, List[Broker]]:
        """Separate brokers into US and international groups."""
        return {
            "US": [b for b in self.brokers if b.is_us_based],
            "International": [b for b in self.brokers if not b.is_us_based]
        }

    def get_broker_details(self, broker_name: str) -> Optional[Broker]:
        """Get detailed information for a specific broker."""
        for broker in self.brokers:
            if broker.name.lower() == broker_name.lower():
                return broker
        return None

def load_brokers_from_json(file_path: str) -> List[Broker]:
    """Load broker data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        brokers = []
        for broker_data in data:
            fee_data = broker_data['fee_structure']
            fee_structure = FeeStructure(
                commission_per_trade=fee_data['commission_per_trade'],
                spread_markup=fee_data['spread_markup'],
                withdrawal_fee=fee_data['withdrawal_fee'],
                inactivity_fee=fee_data['inactivity_fee'],
                currency_conversion_fee=fee_data['currency_conversion_fee']
            )
            
            platforms = []
            for platform_data in broker_data['platforms']:
                platforms.append(TradingPlatform(
                    name=platform_data['name'],
                    mobile_support=platform_data['mobile_support'],
                    desktop_support=platform_data['desktop_support'],
                    web_based=platform_data['web_based'],
                    api_support=platform_data['api_support'],
                    charting_tools=platform_data['charting_tools'],
                    automated_trading=platform_data['automated_trading']
                ))
            
            regulations = [Regulation[r] for r in broker_data['regulations']]
            
            brokers.append(Broker(
                name=broker_data['name'],
                broker_type=BrokerType[broker_data['broker_type']],
                regulations=regulations,
                min_deposit=broker_data['min_deposit'],
                leverage=broker_data['leverage'],
                fee_structure=fee_structure,
                platforms=platforms,
                asset_coverage=broker_data['asset_coverage'],
                customer_support_rating=broker_data['customer_support_rating'],
                execution_speed_ms=broker_data['execution_speed_ms'],
                is_us_based=broker_data['is_us_based'],
                additional_features=broker_data.get('additional_features', {})
            ))
        
        return brokers
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}.")
        return []
    except KeyError as e:
        print(f"Error: Missing required field in JSON data - {str(e)}")
        return []

def save_comparison_results(results: Dict, output_file: str) -> bool:
    """Save comparison results to JSON file."""
    try:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, default=lambda o: o.__dict__)
        return True
    except Exception as e:
        print(f"Error saving results: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    # Load broker data
    brokers = load_brokers_from_json("brokers.json")
    
    if brokers:
        comparator = BrokerComparator(brokers)
        
        # Perform comparisons
        fee_comparison = comparator.compare_by_fees()
        regulated_brokers = comparator.compare_by_regulation(Regulation.FCA)
        platform_comparison = comparator.compare_by_platform_features()
        support_comparison = comparator.compare_by_customer_support()
        speed_comparison = comparator.compare_by_execution_speed()
        us_vs_intl = comparator.us_vs_international()
        
        # Save results
        results = {
            "fee_comparison": fee_comparison,
            "fca_regulated": regulated_brokers,
            "platform_features": platform_comparison,
            "customer_support": support_comparison,
            "execution_speed": speed_comparison,
            "us_vs_international": us_vs_intl
        }
        
        if save_comparison_results(results, "comparison_results.json"):
            print("Comparison completed and saved successfully.")
        else:
            print("Comparison completed but failed to save results.")
    else:
        print("No broker data loaded. Please check the input file.")
```
