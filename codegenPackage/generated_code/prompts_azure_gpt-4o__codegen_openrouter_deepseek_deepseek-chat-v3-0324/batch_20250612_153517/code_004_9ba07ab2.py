"""
Generated Code Metadata:
========================
Original URL: https://fetch-livid-nine.vercel.app
Prompt: Provide an example of using Fetch.ai's autonomous agents for supply chain optimization, including code for data trading between agents.
Generated: DETERMINISTIC_9ba07ab2464f6c21
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, Optional
from aea.agent import Agent
from aea.configurations.base import ConnectionConfig
from aea.connections.base import Connection
from aea.helpers.transaction.base import Terms
from aea.identity.base import Identity
from aea.protocols.base import Message
from aea.skills.base import Handler, Skill
from aea.crypto.ledger_apis import LedgerApis
from aea.crypto.wallet import Wallet
from aea.decision_maker.base import DecisionMaker
from fetchai.connections.p2p_libp2p.connection import P2PLibp2pConnection
from fetchai.protocols.fipa.message import FIPAMessage
from fetchai.protocols.oef_search.message import OefSearchMessage
from fetchai.protocols.tac.message import TacMessage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupplyChainAgent(Agent):
    """An autonomous agent for supply chain optimization."""
    
    def __init__(
        self,
        name: str,
        wallet: Wallet,
        ledger_apis: LedgerApis,
        identity: Identity,
        decision_maker: DecisionMaker,
        connections: Optional[Dict[str, Connection]] = None,
    ):
        """Initialize the supply chain agent."""
        super().__init__(
            name=name,
            wallet=wallet,
            ledger_apis=ledger_apis,
            identity=identity,
            decision_maker=decision_maker,
            connections=connections,
        )
        
        # Register supply chain specific protocols
        self.register_protocol(FIPAMessage.protocol_id)
        self.register_protocol(OefSearchMessage.protocol_id)
        self.register_protocol(TacMessage.protocol_id)
        
        # Initialize agent state
        self.inventory = {}
        self.orders = {}
        self.suppliers = set()
        self.customers = set()

    def setup(self) -> None:
        """Set up the agent."""
        logger.info(f"Setting up SupplyChainAgent {self.name}")
        self._register_services()
        
    def _register_services(self) -> None:
        """Register the agent's services on the OEF."""
        # Register as a supplier
        supplier_service = {
            "key": "supplier",
            "value": True,
            "attributes": {
                "products": list(self.inventory.keys()),
                "location": "warehouse_A",
                "delivery_time": "24h"
            }
        }
        self._register_service(supplier_service)
        
        # Register as a customer
        customer_service = {
            "key": "customer",
            "value": True,
            "attributes": {
                "demand": ["product_A", "product_B"],
                "location": "retail_store_X",
                "budget": 1000
            }
        }
        self._register_service(customer_service)
        
    def _register_service(self, service: Dict) -> None:
        """Helper method to register a service."""
        msg = OefSearchMessage(
            performative=OefSearchMessage.Performative.REGISTER_SERVICE,
            service_description=service
        )
        self.outbox.put_message(msg)
        
    def act(self) -> None:
        """Perform agent actions."""
        self._check_inventory()
        self._process_orders()
        self._negotiate_with_suppliers()
        
    def _check_inventory(self) -> None:
        """Check inventory levels and trigger reordering if needed."""
        for product, quantity in self.inventory.items():
            if quantity < 10:  # Reorder threshold
                logger.info(f"Low inventory for {product}. Initiating reorder.")
                self._create_order(product, 50)  # Default reorder quantity
                
    def _create_order(self, product: str, quantity: int) -> None:
        """Create a new purchase order."""
        order_id = f"order_{len(self.orders) + 1}"
        self.orders[order_id] = {
            "product": product,
            "quantity": quantity,
            "status": "pending"
        }
        logger.info(f"Created order {order_id} for {quantity} units of {product}")
        
    def _process_orders(self) -> None:
        """Process pending orders."""
        for order_id, order in list(self.orders.items()):
            if order["status"] == "pending":
                self._find_supplier(order_id, order)
                
    def _find_supplier(self, order_id: str, order: Dict) -> None:
        """Find a supplier for the given order."""
        query = {
            "key": "supplier",
            "value": True,
            "constraints": [
                {"key": "products", "value": order["product"], "op": "=="}
            ]
        }
        msg = OefSearchMessage(
            performative=OefSearchMessage.Performative.SEARCH_SERVICES,
            query=query
        )
        self.outbox.put_message(msg)
        logger.info(f"Searching for suppliers of {order['product']}")
        
    def _negotiate_with_suppliers(self) -> None:
        """Negotiate terms with potential suppliers."""
        # In a real implementation, this would involve FIPA negotiation
        pass
        
    def handle_message(self, message: Message) -> None:
        """Handle incoming messages."""
        if message.protocol_id == OefSearchMessage.protocol_id:
            self._handle_oef_search(message)
        elif message.protocol_id == FIPAMessage.protocol_id:
            self._handle_fipa(message)
        elif message.protocol_id == TacMessage.protocol_id:
            self._handle_tac(message)
            
    def _handle_oef_search(self, message: OefSearchMessage) -> None:
        """Handle OEF search messages."""
        if message.performative == OefSearchMessage.Performative.SEARCH_RESULT:
            logger.info(f"Received search results: {message.agents}")
            # Process search results and initiate negotiations
            
    def _handle_fipa(self, message: FIPAMessage) -> None:
        """Handle FIPA negotiation messages."""
        if message.performative == FIPAMessage.Performative.CFP:
            self._handle_cfp(message)
        elif message.performative == FIPAMessage.Performative.PROPOSE:
            self._handle_propose(message)
        elif message.performative == FIPAMessage.Performative.ACCEPT:
            self._handle_accept(message)
            
    def _handle_cfp(self, message: FIPAMessage) -> None:
        """Handle Call For Proposal."""
        # Evaluate the CFP and respond with a proposal if interested
        proposal = {
            "price": 10.0,
            "delivery_time": "24h",
            "quantity": message.content["quantity"]
        }
        reply = FIPAMessage(
            performative=FIPAMessage.Performative.PROPOSE,
            dialogue_reference=message.dialogue_reference,
            target=message.message_id,
            content=proposal
        )
        self.outbox.put_message(reply)
        
    def _handle_propose(self, message: FIPAMessage) -> None:
        """Handle a proposal from a supplier."""
        # Evaluate the proposal and accept if terms are favorable
        if message.content["price"] <= 12.0:  # Accept threshold
            accept_msg = FIPAMessage(
                performative=FIPAMessage.Performative.ACCEPT,
                dialogue_reference=message.dialogue_reference,
                target=message.message_id,
                content={"confirmation": True}
            )
            self.outbox.put_message(accept_msg)
            
    def _handle_accept(self, message: FIPAMessage) -> None:
        """Handle acceptance of our proposal."""
        # Prepare the transaction
        terms = Terms(
            ledger_id="fetchai",
            sender_address=self.identity.address,
            counterparty_address=message.sender,
            amount_by_currency_id={"FET": int(message.content["price"] * 100)},
            quantities_by_good_id={message.content["product"]: message.content["quantity"]},
            is_sender_payable_tx_fee=True,
            nonce="12345",
        )
        
        # Sign and send the transaction
        tx = self.wallet.generate_transaction(
            terms=terms,
            tx_fee=1000,
            is_waiting_for_confirmation=True
        )
        self.ledger_apis.send_signed_transaction(tx)
        
    def _handle_tac(self, message: TacMessage) -> None:
        """Handle TAC messages."""
        pass

class SupplyChainSkill(Skill):
    """Skill for supply chain optimization."""
    
    def __init__(self, **kwargs):
        """Initialize the skill."""
        super().__init__(**kwargs)
        self.register_handler(SupplyChainHandler)

class SupplyChainHandler(Handler):
    """Handler for supply chain messages."""
    
    def __init__(self, **kwargs):
        """Initialize the handler."""
        super().__init__(**kwargs)
        
    def setup(self) -> None:
        """Set up the handler."""
        pass
        
    def handle(self, message: Message) -> None:
        """Handle messages."""
        self.context.agent
