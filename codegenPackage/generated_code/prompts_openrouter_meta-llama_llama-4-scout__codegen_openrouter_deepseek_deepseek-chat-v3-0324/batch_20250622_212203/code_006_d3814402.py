"""
Generated Code Metadata:
========================
Original URL: https://flarenetdrops.com
Prompt: Create a technical documentation for Flare Network's layer-1 oracle network, including its architecture, data access mechanisms, and integration with EVM-compatible networks.
Generated: DETERMINISTIC_d3814402c0798542
Batch ID: 20250622_212203
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://songbird-api.flare.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oracle.flare.network/sports": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oracle.flare.network/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://flare-api.flare.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oracle.flare.network/random": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oracle.flare.network/price/BTC-USD": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Flare Network Oracle Documentation Generator

This script generates technical documentation for Flare Network's Layer-1 Oracle system,
including architecture diagrams, data access mechanisms, and EVM integration details.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto

class OracleType(Enum):
    """Types of oracles supported by Flare Network"""
    PRICE = auto()
    RANDOMNESS = auto()
    WEATHER = auto()
    SPORTS = auto()
    CUSTOM = auto()

@dataclass
class OracleProvider:
    """Represents an oracle data provider"""
    name: str
    description: str
    oracle_type: OracleType
    endpoints: List[str]
    is_active: bool = True

@dataclass
class EVMNetwork:
    """Represents an EVM-compatible network"""
    chain_id: int
    name: str
    rpc_url: str
    is_supported: bool = True

class FlareOracleDocumentation:
    """Main class for generating Flare Network Oracle documentation"""
    
    def __init__(self):
        self.providers: List[OracleProvider] = []
        self.evm_networks: List[EVMNetwork] = []
        self._load_default_providers()
        self._load_default_networks()
    
    def _load_default_providers(self) -> None:
        """Load default oracle providers"""
        self.providers = [
            OracleProvider(
                name="FlarePriceOracle",
                description="Provides real-time price feeds for various assets",
                oracle_type=OracleType.PRICE,
                endpoints=["https://oracle.flare.network/price"]
            ),
            OracleProvider(
                name="FlareRandomnessOracle",
                description="Provides verifiable random numbers",
                oracle_type=OracleType.RANDOMNESS,
                endpoints=["https://oracle.flare.network/random"]
            )
        ]
    
    def _load_default_networks(self) -> None:
        """Load default EVM networks"""
        self.evm_networks = [
            EVMNetwork(
                chain_id=14,
                name="Flare",
                rpc_url="https://flare-api.flare.network"
            ),
            EVMNetwork(
                chain_id=16,
                name="Songbird",
                rpc_url="https://songbird-api.flare.network"
            ),
            EVMNetwork(
                chain_id=1,
                name="Ethereum",
                rpc_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
                is_supported=False
            )
        ]
    
    def add_provider(self, provider: OracleProvider) -> None:
        """Add a new oracle provider"""
        self.providers.append(provider)
    
    def add_network(self, network: EVMNetwork) -> None:
        """Add a new EVM network"""
        self.evm_networks.append(network)
    
    def get_provider(self, name: str) -> Optional[OracleProvider]:
        """Get provider by name"""
        for provider in self.providers:
            if provider.name.lower() == name.lower():
                return provider
        return None
    
    def get_network(self, chain_id: int) -> Optional[EVMNetwork]:
        """Get network by chain ID"""
        for network in self.evm_networks:
            if network.chain_id == chain_id:
                return network
        return None
    
    def generate_architecture_diagram(self) -> Dict:
        """Generate architecture diagram data"""
        return {
            "components": [
                {
                    "name": "Oracle Core",
                    "description": "Central oracle smart contract that manages data requests",
                    "interfaces": ["EVM", "REST"]
                },
                {
                    "name": "Data Providers",
                    "description": "External data sources that feed information to the oracle",
                    "providers": [p.name for p in self.providers]
                },
                {
                    "name": "EVM Adapter",
                    "description": "Bridge between EVM networks and the oracle core",
                    "supported_networks": [n.name for n in self.evm_networks if n.is_supported]
                }
            ],
            "data_flow": [
                "User contract makes request → Oracle Core → Data Provider → Oracle Core → User contract"
            ]
        }
    
    def generate_data_access_guide(self) -> Dict:
        """Generate data access mechanisms documentation"""
        return {
            "access_methods": [
                {
                    "name": "Direct Smart Contract Call",
                    "description": "Call oracle contract directly from your smart contract",
                    "example": "FlareOracle.getPrice('BTC/USD')"
                },
                {
                    "name": "REST API",
                    "description": "Access oracle data via HTTP REST API",
                    "example": "GET https://oracle.flare.network/price/BTC-USD"
                },
                {
                    "name": "WebSocket Stream",
                    "description": "Subscribe to real-time data updates",
                    "example": "wss://oracle.flare.network/stream/price/BTC-USD"
                }
            ],
            "security": [
                "All requests are cryptographically signed",
                "Data is verified on-chain before being accepted",
                "Providers are vetted and reputation-scored"
            ]
        }
    
    def generate_evm_integration_guide(self) -> Dict:
        """Generate EVM integration documentation"""
        return {
            "integration_steps": [
                "1. Deploy your contract with oracle interface",
                "2. Import FlareOracle interface in your contract",
                "3. Make requests to oracle contract address",
                "4. Handle callback with verified data"
            ],
            "example_contract": """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFlareOracle {
    function getPrice(string memory pair) external returns (uint256);
}

contract MyContract {
    IFlareOracle public oracle;
    address public oracleAddress = 0x123...;
    
    constructor() {
        oracle = IFlareOracle(oracleAddress);
    }
    
    function getBTCPrice() public returns (uint256) {
        return oracle.getPrice("BTC/USD");
    }
}
            """,
            "supported_networks": [
                {
                    "name": network.name,
                    "chain_id": network.chain_id,
                    "oracle_address": "0x123...",  # Placeholder
                    "rpc_url": network.rpc_url
                } for network in self.evm_networks if network.is_supported
            ]
        }
    
    def generate_full_documentation(self) -> Dict:
        """Generate complete documentation package"""
        return {
            "architecture": self.generate_architecture_diagram(),
            "data_access": self.generate_data_access_guide(),
            "evm_integration": self.generate_evm_integration_guide(),
            "providers": [{
                "name": p.name,
                "type": p.oracle_type.name,
                "endpoints": p.endpoints,
                "description": p.description
            } for p in self.providers],
            "networks": [{
                "name": n.name,
                "chain_id": n.chain_id,
                "rpc_url": n.rpc_url,
                "supported": n.is_supported
            } for n in self.evm_networks],
            "version": "1.0.0",
            "timestamp": "2023-11-15T00:00:00Z"
        }
    
    def save_documentation(self, filename: str = "flare_oracle_docs.json") -> None:
        """Save documentation to JSON file"""
        docs = self.generate_full_documentation()
        with open(filename, 'w') as f:
            json.dump(docs, f, indent=2)

# Example usage
if __name__ == "__main__":
    docs = FlareOracleDocumentation()
    
    # Add custom provider
    docs.add_provider(
        OracleProvider(
            name="SportsDataOracle",
            description="Provides live sports data and results",
            oracle_type=OracleType.SPORTS,
            endpoints=["https://oracle.flare.network/sports"]
        )
    )
    
    # Generate and save documentation
    docs.save_documentation()
```
