"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Develop a supply chain management system using Código's platform, including a CIDL file, smart contract code, and client libraries for multiple programming languages.
Generated: DETERMINISTIC_203f1b09329fc84a
Batch ID: 20250622_211342
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://explorer.${this.networkId}.near.org`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.${this.networkId}.near.org`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.{network_id}.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://wallet.${this.networkId}.near.org`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://helper.${this.networkId}.near.org`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a production-ready implementation of a supply chain management system using Código's platform. The solution includes a CIDL file, smart contract code, and client libraries for JavaScript and Python.

### CIDL File (`supply_chain.cidl`)

```yaml
version: 1.0
name: SupplyChain
description: A decentralized supply chain management system

types:
  Product:
    fields:
      - id: string
      - name: string
      - description: string
      - manufacturer: string
      - timestamp: u64
      - status: string

  Shipment:
    fields:
      - id: string
      - productId: string
      - from: string
      - to: string
      - status: string
      - timestamp: u64

events:
  ProductCreated:
    fields:
      - id: string
      - name: string
      - manufacturer: string

  ShipmentCreated:
    fields:
      - id: string
      - productId: string
      - from: string
      - to: string

  StatusUpdated:
    fields:
      - id: string
      - newStatus: string
      - entityType: string

contract:
  methods:
    - name: createProduct
      inputs:
        - name: id
          type: string
        - name: name
          type: string
        - name: description
          type: string
        - name: manufacturer
          type: string
      outputs: void
      description: Creates a new product in the supply chain

    - name: createShipment
      inputs:
        - name: id
          type: string
        - name: productId
          type: string
        - name: from
          type: string
        - name: to
          type: string
      outputs: void
      description: Creates a new shipment for a product

    - name: updateStatus
      inputs:
        - name: id
          type: string
        - name: newStatus
          type: string
        - name: entityType
          type: string
      outputs: void
      description: Updates the status of a product or shipment

    - name: getProduct
      inputs:
        - name: id
          type: string
      outputs: Product
      description: Retrieves product details

    - name: getShipment
      inputs:
        - name: id
          type: string
      outputs: Shipment
      description: Retrieves shipment details
```

### Smart Contract (`supply_chain_contract.rs`)

```rust
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::collections::{LookupMap, UnorderedMap};
use near_sdk::{env, near_bindgen, AccountId, Promise};

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize)]
pub struct SupplyChain {
    products: UnorderedMap<String, Product>,
    shipments: UnorderedMap<String, Shipment>,
}

#[derive(BorshDeserialize, BorshSerialize)]
pub struct Product {
    id: String,
    name: String,
    description: String,
    manufacturer: AccountId,
    timestamp: u64,
    status: String,
}

#[derive(BorshDeserialize, BorshSerialize)]
pub struct Shipment {
    id: String,
    product_id: String,
    from: AccountId,
    to: AccountId,
    status: String,
    timestamp: u64,
}

#[near_bindgen]
impl SupplyChain {
    #[init]
    pub fn new() -> Self {
        Self {
            products: UnorderedMap::new(b"p".to_vec()),
            shipments: UnorderedMap::new(b"s".to_vec()),
        }
    }

    #[payable]
    pub fn create_product(
        &mut self,
        id: String,
        name: String,
        description: String,
        manufacturer: AccountId,
    ) {
        let product = Product {
            id: id.clone(),
            name,
            description,
            manufacturer,
            timestamp: env::block_timestamp(),
            status: "Manufactured".to_string(),
        };

        self.products.insert(&id, &product);
        
        env::log_str(
            format!(
                "ProductCreated {{\"id\": \"{}\", \"name\": \"{}\", \"manufacturer\": \"{}\"}}",
                product.id, product.name, product.manufacturer
            )
            .as_str(),
        );
    }

    pub fn create_shipment(
        &mut self,
        id: String,
        product_id: String,
        from: AccountId,
        to: AccountId,
    ) {
        assert!(
            self.products.get(&product_id).is_some(),
            "Product does not exist"
        );

        let shipment = Shipment {
            id: id.clone(),
            product_id,
            from,
            to,
            status: "In Transit".to_string(),
            timestamp: env::block_timestamp(),
        };

        self.shipments.insert(&id, &shipment);
        
        env::log_str(
            format!(
                "ShipmentCreated {{\"id\": \"{}\", \"productId\": \"{}\", \"from\": \"{}\", \"to\": \"{}\"}}",
                shipment.id, shipment.product_id, shipment.from, shipment.to
            )
            .as_str(),
        );
    }

    pub fn update_status(&mut self, id: String, new_status: String, entity_type: String) {
        match entity_type.as_str() {
            "product" => {
                let mut product = self.products.get(&id).expect("Product not found");
                product.status = new_status.clone();
                self.products.insert(&id, &product);
            }
            "shipment" => {
                let mut shipment = self.shipments.get(&id).expect("Shipment not found");
                shipment.status = new_status.clone();
                self.shipments.insert(&id, &shipment);
            }
            _ => panic!("Invalid entity type"),
        }

        env::log_str(
            format!(
                "StatusUpdated {{\"id\": \"{}\", \"newStatus\": \"{}\", \"entityType\": \"{}\"}}",
                id, new_status, entity_type
            )
            .as_str(),
        );
    }

    pub fn get_product(&self, id: String) -> Option<Product> {
        self.products.get(&id)
    }

    pub fn get_shipment(&self, id: String) -> Option<Shipment> {
        self.shipments.get(&id)
    }
}
```

### JavaScript Client Library (`supplyChain.js`)

```javascript
const { connect, keyStores } = require('near-api-js');

class SupplyChainClient {
    constructor(contractId, networkId = 'testnet') {
        this.contractId = contractId;
        this.networkId = networkId;
    }

    async init() {
        const keyStore = new keyStores.BrowserLocalStorageKeyStore();
        const config = {
            networkId: this.networkId,
            keyStore,
            nodeUrl: `https://rpc.${this.networkId}.near.org`,
            walletUrl: `https://wallet.${this.networkId}.near.org`,
            helperUrl: `https://helper.${this.networkId}.near.org`,
            explorerUrl: `https://explorer.${this.networkId}.near.org`,
        };
        this.near = await connect(config);
        this.account = this.near.account(process.env.NEAR_ACCOUNT_ID);
        this.contract = new near.Contract(this.account, this.contractId, {
            viewMethods: ['get_product', 'get_shipment'],
            changeMethods: ['create_product', 'create_shipment', 'update_status'],
        });
    }

    async createProduct(id, name, description, manufacturer) {
        return await this.contract.create_product({
            id,
            name,
            description,
            manufacturer,
        });
    }

    async createShipment(id, productId, from, to) {
        return await this.contract.create_shipment({
            id,
            product_id: productId,
            from,
            to,
        });
    }

    async updateStatus(id, newStatus, entityType) {
        return await this.contract.update_status({
            id,
            new_status: newStatus,
            entity_type: entityType,
        });
    }

    async getProduct(id) {
        return await this.contract.get_product({ id });
    }

    async getShipment(id) {
        return await this.contract.get_shipment({ id });
    }
}

module.exports = SupplyChainClient;
```

### Python Client Library (`supply_chain.py`)

```python
import json
from near_api.signer import KeyPair
from near_api.providers import JsonProvider
from near_api.account import Account

class SupplyChainClient:
    def __init__(self, contract_id, network_id='testnet'):
        self.contract_id = contract_id
        self.network_id = network_id
        self.provider = JsonProvider(f'https://rpc.{network_id}.near.org')
        self.account_id = None
        self.key_pair = None
        self.account = None
        self.contract = None

    def init(self, account_id, private_key):
