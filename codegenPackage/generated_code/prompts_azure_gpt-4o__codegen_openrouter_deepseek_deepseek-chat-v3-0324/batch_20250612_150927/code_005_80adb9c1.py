"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Write a CIDL file for a decentralized application that interacts with multiple smart contracts. Use Código's tools to generate boilerplate code and client libraries in TypeScript.
Generated: DETERMINISTIC_80adb9c1746c7bc7
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# CIDL (Contract Interface Description Language) file
# Describes a decentralized application interacting with multiple smart contracts

version: 1.0.0
name: MultiContractDApp
description: A decentralized application that interacts with Token, NFT, and Governance contracts
author: Your Name
license: MIT

contracts:
  - name: TokenContract
    description: ERC20 compatible token contract
    address: "0x1234567890123456789012345678901234567890"
    networks:
      - name: ethereum
        chainId: 1
        address: "0x1234567890123456789012345678901234567890"
      - name: polygon
        chainId: 137
        address: "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd"
    methods:
      - name: transfer
        description: Transfer tokens to another address
        inputs:
          - name: to
            type: address
            description: Recipient address
          - name: amount
            type: uint256
            description: Amount of tokens to transfer
        outputs:
          - name: success
            type: bool
            description: Whether the transfer was successful
        payable: false

      - name: balanceOf
        description: Get token balance of an address
        inputs:
          - name: owner
            type: address
            description: Address to query balance for
        outputs:
          - name: balance
            type: uint256
            description: Token balance of the address
        payable: false

  - name: NFTContract
    description: ERC721 compatible NFT contract
    address: "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd"
    networks:
      - name: ethereum
        chainId: 1
        address: "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd"
    methods:
      - name: mint
        description: Mint a new NFT
        inputs:
          - name: to
            type: address
            description: Recipient address
          - name: tokenId
            type: uint256
            description: Unique token ID
          - name: uri
            type: string
            description: Metadata URI
        outputs: []
        payable: true

      - name: ownerOf
        description: Get owner of an NFT
        inputs:
          - name: tokenId
            type: uint256
            description: NFT token ID
        outputs:
          - name: owner
            type: address
            description: Owner address of the NFT
        payable: false

  - name: GovernanceContract
    description: DAO governance contract
    address: "0x9876543210987654321098765432109876543210"
    networks:
      - name: ethereum
        chainId: 1
        address: "0x9876543210987654321098765432109876543210"
    methods:
      - name: propose
        description: Create a new governance proposal
        inputs:
          - name: description
            type: string
            description: Proposal description
          - name: targets
            type: address[]
            description: Target addresses for proposal
          - name: values
            type: uint256[]
            description: Values for proposal
          - name: calldatas
            type: bytes[]
            description: Calldata for proposal
        outputs:
          - name: proposalId
            type: uint256
            description: ID of the created proposal
        payable: false

      - name: vote
        description: Vote on a governance proposal
        inputs:
          - name: proposalId
            type: uint256
            description: ID of the proposal to vote on
          - name: support
            type: uint8
            description: 1 for yes, 0 for no
        outputs: []
        payable: false

events:
  - contract: TokenContract
    name: Transfer
    description: Emitted when tokens are transferred
    inputs:
      - name: from
        type: address
        indexed: true
      - name: to
        type: address
        indexed: true
      - name: value
        type: uint256

  - contract: NFTContract
    name: Transfer
    description: Emitted when NFT ownership changes
    inputs:
      - name: from
        type: address
        indexed: true
      - name: to
        type: address
        indexed: true
      - name: tokenId
        type: uint256
        indexed: true

  - contract: GovernanceContract
    name: ProposalCreated
    description: Emitted when a new proposal is created
    inputs:
      - name: proposalId
        type: uint256
        indexed: true
      - name: proposer
        type: address
        indexed: true
      - name: targets
        type: address[]
      - name: values
        type: uint256[]
      - name: calldatas
        type: bytes[]

client:
  language: typescript
  outputDir: ./client
  settings:
    framework: ethers
    includeTests: true
    includeExamples: true
```
