"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Create a high-level architecture diagram illustrating how Particle Network's Master Keystore Hub coordinates Universal Account deployments and updates across all chains, and write a brief description of each component.
Generated: DETERMINISTIC_06f72fbc702ee398
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client
from diagrams.generic.storage import Storage
from diagrams.generic.blank import Blank
from diagrams.generic.network import Firewall
from diagrams.generic.os import LinuxGeneral
from diagrams.programming.language import Python
from diagrams.programming.framework import React
from diagrams.aws.security import IdentityAndAccessManagementIam
from diagrams.aws.blockchain import BlockchainResource
from diagrams.aws.network import APIGateway

# Main diagram
with Diagram("Particle Network Master Keystore Hub Architecture", show=False, direction="TB"):
    # User components
    user = Client("End User")
    developer = Client("Developer")

    # Frontend components
    with Cluster("Frontend"):
        ui = React("User Interface")
        sdk = Python("SDK")

    # Master Keystore Hub components
    with Cluster("Master Keystore Hub"):
        api_gateway = APIGateway("API Gateway")
        auth_service = IdentityAndAccessManagementIam("Auth Service")
        key_manager = Storage("Key Management")
        tx_orchestrator = Python("Transaction Orchestrator")
        chain_adapter = BlockchainResource("Chain Adapter Layer")

    # Blockchain networks
    with Cluster("Supported Blockchains"):
        evm = BlockchainResource("EVM Chains")
        solana = BlockchainResource("Solana")
        cosmos = BlockchainResource("Cosmos")
        other = Blank("Other Chains")

    # Data storage
    with Cluster("Data Layer"):
        encrypted_db = Storage("Encrypted Database")
        audit_logs = Storage("Audit Logs")

    # Connections
    user >> Edge(label="1. Auth") >> ui >> Edge(label="2. API Calls") >> api_gateway
    developer >> Edge(label="SDK Integration") >> sdk >> Edge() >> api_gateway
    
    api_gateway >> Edge(label="3. Auth Request") >> auth_service
    api_gateway >> Edge(label="4. Key Operations") >> key_manager
    api_gateway >> Edge(label="5. Transaction Request") >> tx_orchestrator
    
    key_manager >> Edge(label="6. Secure Storage") >> encrypted_db
    key_manager >> Edge(label="7. Audit Logs") >> audit_logs
    
    tx_orchestrator >> Edge(label="8. Chain Abstraction") >> chain_adapter
    chain_adapter >> Edge(label="9. EVM") >> evm
    chain_adapter >> Edge(label("10. Solana")) >> solana
    chain_adapter >> Edge(label("11. Cosmos")) >> cosmos
    chain_adapter >> Edge(label("12. Others")) >> other
```
