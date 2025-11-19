"""
Generated Code Metadata:
========================
Original URL: https://btc-xmr-mixer.com
Prompt: Generate code to implement a CoinJoin-based Bitcoin mixing service, similar to UniJoin, with a focus on low fees and enhanced privacy.
Generated: DETERMINISTIC_33cb8b1bbdf0764f
Batch ID: 20250612_142622
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://{CONFIG": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://{CONFIG['rpc_user']}:{CONFIG['rpc_password']}@{CONFIG['rpc_host']}:{CONFIG['rpc_port": {
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
#!/usr/bin/env python3
import hashlib
import hmac
import json
import os
import random
import secrets
import time
from typing import Dict, List, Optional, Tuple

import bitcoin
from bitcoin.core import CMutableTransaction, CMutableTxIn, CMutableTxOut
from bitcoin.core.script import CScript, OP_RETURN
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret
from bitcoin.rpc import RawProxy
from flask import Flask, jsonify, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Configuration
CONFIG = {
    "bitcoin_network": "testnet",  # or "mainnet"
    "rpc_user": "your_rpc_user",
    "rpc_password": "your_rpc_password",
    "rpc_host": "127.0.0.1",
    "rpc_port": 18332,  # 8332 for mainnet
    "min_participants": 3,
    "max_participants": 10,
    "min_amount": 10000,  # satoshis
    "max_amount": 100000000,  # satoshis
    "fee_percent": 0.5,  # 0.5% fee
    "session_timeout": 3600,  # 1 hour in seconds
    "anon_set_target": 50,  # target anonymity set size
}

# Database simulation (in production use a real database)
sessions_db = {}
participants_db = {}
transactions_db = {}

# Initialize Bitcoin RPC connection
try:
    bitcoin.SelectParams(CONFIG["bitcoin_network"])
    rpc_connection = RawProxy(
        service_url=f"http://{CONFIG['rpc_user']}:{CONFIG['rpc_password']}@{CONFIG['rpc_host']}:{CONFIG['rpc_port']}"
    )
except Exception as e:
    raise RuntimeError(f"Failed to connect to Bitcoin RPC: {str(e)}")

def generate_session_id() -> str:
    """Generate a unique session ID."""
    return secrets.token_hex(16)

def validate_address(address: str) -> bool:
    """Validate a Bitcoin address."""
    try:
        CBitcoinAddress(address)
        return True
    except Exception:
        return False

def calculate_fee(amount: int) -> int:
    """Calculate the service fee."""
    return int(amount * (CONFIG["fee_percent"] / 100))

def create_coinjoin_transaction(inputs: List[Tuple[str, int]], outputs: List[Tuple[str, int]]) -> str:
    """
    Create a CoinJoin transaction.
    
    Args:
        inputs: List of (txid, vout) tuples
        outputs: List of (address, amount) tuples
        
    Returns:
        Hex-encoded raw transaction
    """
    tx = CMutableTransaction()
    
    # Add inputs
    for txid, vout in inputs:
        txin = CMutableTxIn()
        txin.prevout.hash = bitcoin.core.lx(txid)
        txin.prevout.n = vout
        tx.vin.append(txin)
    
    # Add outputs
    for address, amount in outputs:
        txout = CMutableTxOut()
        txout.nValue = amount
        txout.scriptPubKey = CBitcoinAddress(address).to_scriptPubKey()
        tx.vout.append(txout)
    
    # Add OP_RETURN output for marking CoinJoin transactions
    op_return = CScript([OP_RETURN, b'CoinJoin'])
    tx.vout.append(CMutableTxOut(0, op_return))
    
    return bitcoin.core.b2x(tx.serialize())

def verify_transaction(tx_hex: str) -> bool:
    """Verify a transaction is valid."""
    try:
        tx = CMutableTransaction.deserialize(bitcoin.core.x(tx_hex))
        return True
    except Exception:
        return False

@app.route('/api/v1/create_session', methods=['POST'])
@limiter.limit("5 per minute")
def create_session():
    """Create a new CoinJoin session."""
    try:
        data = request.get_json()
        if not data or 'amount' not in data or 'input_address' not in data or 'output_address' not in data:
            return jsonify({"error": "Invalid request data"}), 400
        
        amount = int(data['amount'])
        input_address = data['input_address']
        output_address = data['output_address']
        
        if not validate_address(input_address) or not validate_address(output_address):
            return jsonify({"error": "Invalid Bitcoin address"}), 400
        
        if amount < CONFIG["min_amount"] or amount > CONFIG["max_amount"]:
            return jsonify({"error": f"Amount must be between {CONFIG['min_amount']} and {CONFIG['max_amount']} satoshis"}), 400
        
        session_id = generate_session_id()
        sessions_db[session_id] = {
            "created_at": int(time.time()),
            "participants": [],
            "amount": amount,
            "status": "pending",
            "transaction_hex": None,
            "transaction_id": None
        }
        
        return jsonify({"session_id": session_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/v1/join_session/<session_id>', methods=['POST'])
@limiter.limit("10 per minute")
def join_session(session_id: str):
    """Join an existing CoinJoin session."""
    try:
        if session_id not in sessions_db:
            return jsonify({"error": "Session not found"}), 404
        
        session = sessions_db[session_id]
        
        if session["status"] != "pending":
            return jsonify({"error": "Session is not accepting new participants"}), 400
        
        if len(session["participants"]) >= CONFIG["max_participants"]:
            return jsonify({"error": "Session is full"}), 400
        
        data = request.get_json()
        if not data or 'input_address' not in data or 'output_address' not in data:
            return jsonify({"error": "Invalid request data"}), 400
        
        input_address = data['input_address']
        output_address = data['output_address']
        
        if not validate_address(input_address) or not validate_address(output_address):
            return jsonify({"error": "Invalid Bitcoin address"}), 400
        
        # Verify the participant has sufficient funds
        try:
            utxos = rpc_connection.listunspent(0, 9999999, [input_address])
            total_amount = sum(int(utxo["amount"] * 100000000) for utxo in utxos)
            if total_amount < session["amount"]:
                return jsonify({"error": "Insufficient funds"}), 400
        except Exception:
            return jsonify({"error": "Failed to verify funds"}), 500
        
        participant_id = secrets.token_hex(8)
        participants_db[participant_id] = {
            "session_id": session_id,
            "input_address": input_address,
            "output_address": output_address,
            "amount": session["amount"],
            "status": "pending",
            "signed": False
        }
        
        session["participants"].append(participant_id)
        
        # Check if we have enough participants
        if len(session["participants"]) >= CONFIG["min_participants"]:
            session["status"] = "ready"
            _process_session(session_id)
        
        return jsonify({"participant_id": participant_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def _process_session(session_id: str):
    """Process a ready session by creating the CoinJoin transaction."""
    session = sessions_db[session_id]
    participants = [participants_db[pid] for pid in session["participants"]]
    
    # Collect inputs and outputs
    inputs = []
    outputs = []
    
    for participant in participants:
        try:
            utxos = rpc_connection.listunspent(0, 9999999, [participant["input_address"]])
            if not utxos:
                continue
                
            # Select a UTXO with sufficient amount
            selected_utxo = None
            for utxo in utxos:
                amount = int(utxo["amount"] * 100000000)
                if amount >= participant["amount"]:
                    selected_utxo = utxo
                    break
            
            if not selected_utxo:
                continue
                
            inputs.append((selected_utxo["txid"], selected_utxo["vout"]))
            
            # Calculate output amount after fee
            fee = calculate_fee(participant["amount"])
            output_amount = participant["amount"] - fee
            outputs.append((participant["output_address"], output_amount))
            
        except Exception as
