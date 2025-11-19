"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Generate a sample CIDL file that defines a smart contract interface for a token exchange application on Solana.
Generated: DETERMINISTIC_c5e1c434745e91e3
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# CIDL (Contract Interface Description Language) for Token Exchange on Solana
version: 1.0
name: token_exchange
description: A smart contract for token exchange on Solana

types:
  Token:
    fields:
      - name: mint
        type: publicKey
        description: The mint address of the token
      - name: balance
        type: u64
        description: The token balance

  ExchangeAccount:
    fields:
      - name: owner
        type: publicKey
        description: Owner of the exchange account
      - name: token_a
        type: Token
        description: First token in the exchange pair
      - name: token_b
        type: Token
        description: Second token in the exchange pair
      - name: fee_rate
        type: u8
        description: Exchange fee percentage (0-100)

methods:
  initialize:
    description: Initialize a new exchange account
    inputs:
      - name: owner
        type: publicKey
        description: Owner of the exchange account
      - name: token_a_mint
        type: publicKey
        description: Mint address of token A
      - name: token_b_mint
        type: publicKey
        description: Mint address of token B
      - name: fee_rate
        type: u8
        description: Exchange fee percentage
    outputs:
      - name: exchange_account
        type: ExchangeAccount

  deposit:
    description: Deposit tokens into the exchange
    inputs:
      - name: exchange_account
        type: publicKey
        description: Exchange account address
      - name: token_mint
        type: publicKey
        description: Mint address of token to deposit
      - name: amount
        type: u64
        description: Amount of tokens to deposit
    outputs:
      - name: updated_account
        type: ExchangeAccount

  withdraw:
    description: Withdraw tokens from the exchange
    inputs:
      - name: exchange_account
        type: publicKey
        description: Exchange account address
      - name: token_mint
        type: publicKey
        description: Mint address of token to withdraw
      - name: amount
        type: u64
        description: Amount of tokens to withdraw
    outputs:
      - name: updated_account
        type: ExchangeAccount

  swap:
    description: Swap tokens at current exchange rate
    inputs:
      - name: exchange_account
        type: publicKey
        description: Exchange account address
      - name: from_token
        type: publicKey
        description: Mint address of token to swap from
      - name: to_token
        type: publicKey
        description: Mint address of token to swap to
      - name: amount
        type: u64
        description: Amount of tokens to swap
    outputs:
      - name: updated_account
        type: ExchangeAccount
      - name: amount_received
        type: u64
        description: Amount of tokens received after swap

events:
  Deposited:
    fields:
      - name: exchange_account
        type: publicKey
      - name: token_mint
        type: publicKey
      - name: amount
        type: u64

  Withdrawn:
    fields:
      - name: exchange_account
        type: publicKey
      - name: token_mint
        type: publicKey
      - name: amount
        type: u64

  Swapped:
    fields:
      - name: exchange_account
        type: publicKey
      - name: from_token
        type: publicKey
      - name: to_token
        type: publicKey
      - name: amount_sent
        type: u64
      - name: amount_received
        type: u64
```
