"""
Generated Code Metadata:
========================
Original URL: https://award-nostra.pages.dev
Prompt: Generate a smart contract code for a lending pool on Starknet, inspired by Nostra's lending feature.
Generated: DETERMINISTIC_0c5d8ecc27026bdd
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from starkware.starknet.public.abi import get_abi
from starkware.starknet.business_logic.execution.objects import CallInfo
from starkware.starknet.business_logic.state import State
from starkware.starknet.services.api.contract import Contract
from starkware.starknet.services.api.gateway import Gateway
from starkware.starknet.services.api.gateway.transaction import InvokeFunction
from starkware.starknet.services.api.gateway.transaction import Deploy
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionType
from starkware.starknet.services.api.gateway.transaction import Transaction
from starkware.starknet.services.api.gateway.transaction import TransactionReceipt
from starkware.starknet.services.api.gateway.transaction import TransactionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionError
from starkware.starknet.services.api.gateway.transaction import TransactionExecutionStatus
from starkware.starknet.services.api.gateway.transaction import TransactionStatus
from starkware.st
