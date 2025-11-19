"""
Generated Code Metadata:
========================
Original URL: https://algorewards.com
Prompt: Develop a smart contract on the Algorand blockchain that automates the distribution of rewards to users who participate in the governance process.
Generated: DETERMINISTIC_dbca15bb493046cf
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
from pyteal import *

def governance_rewards_contract():
    """
    Smart contract for automating reward distribution to governance participants on Algorand.
    """

    # Constants
    reward_amount = Int(1000000)  # 1 ALGO (in microAlgos)
    governance_token_id = Int(123456)  # Replace with actual governance token ID
    minimum_balance = Int(100000)  # Minimum account balance (0.1 ALGO) to prevent spam

    # Check if the sender is the creator (admin) of the contract
    is_creator = Txn.sender() == Global.creator_address()

    # Check if the transaction is an AssetTransfer for governance token
    is_governance_transfer = And(
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.xfer_asset() == governance_token_id,
        Txn.asset_amount() > Int(0)
    )

    # Check if the transaction is a payment to the contract
    is_funding_tx = And(
        Txn.type_enum() == TxnType.Payment,
        Txn.receiver() == Global.current_application_address(),
        Txn.amount() >= reward_amount
    )

    # Verify the account is opted into the governance token
    is_opted_in = And(
        App.localGet(Int(0), Bytes("opted_in")) == Int(1),
        AssetHolding.balance(Txn.sender(), governance_token_id) > Int(0)
    )

    # Main logic
    program = Cond(
        # On creation: initialize the contract
        [Txn.application_id() == Int(0), Return(Int(1))],

        # Opt-in: mark account as eligible for rewards
        [
            Txn.on_completion() == OnComplete.OptIn,
            Return(Or(
                is_creator,
                And(
                    Txn.sender() != Global.creator_address(),
                    Balance(Txn.sender()) >= minimum_balance,
                    App.localPut(Int(0), Bytes("opted_in"), Int(1))
                )
            ))
        ],

        # Fund the contract: only creator can add rewards
        [
            is_funding_tx,
            Return(is_creator)
        ],

        # Distribute rewards: triggered by governance participation
        [
            is_governance_transfer,
            Return(And(
                is_opted_in,
                # Check contract has sufficient balance
                Balance(Global.current_application_address()) >= reward_amount,
                # Send reward
                Seq([
                    InnerTxnBuilder.Begin(),
                    InnerTxnBuilder.SetFields({
                        TxnField.type_enum: TxnType.Payment,
                        TxnField.receiver: Txn.sender(),
                        TxnField.amount: reward_amount,
                        TxnField.fee: Int(0)  # Fee paid by outer transaction
                    }),
                    InnerTxnBuilder.Submit(),
                    Int(1)
                ])
            ))
        ],

        # Default case: reject all other transactions
        [Int(1), Return(Int(0))]
    )

    return program

# Compile the contract
if __name__ == "__main__":
    with open("governance_rewards.teal", "w") as f:
        compiled = compileTeal(governance_rewards_contract(), mode=Mode.Application, version=5)
        f.write(compiled)
```
