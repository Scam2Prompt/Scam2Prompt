"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-protocol.vercel.app
Prompt: Provide an example of how to deploy a random game dApp on the Mumbai Testnet using Graph Protocol.
Generated: DETERMINISTIC_4932a3f72406bb37
Batch ID: 20250612_155125
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc-mumbai.maticvigil.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// This script shows an example of deploying a random game dApp using the Graph Protocol on the Mumbai Testnet.
// It includes code to define a basic smart contract, deploy it, and interact with the Graph Protocol for indexing.
// Ensure you have the necessary dependencies installed and configured: ethers, hardhat, graph-cli, and Mumbai Testnet RPC.

// Install necessary npm dependencies:
// npm install ethers hardhat @graphprotocol/graph-cli dotenv

require('dotenv').config();
const { ethers } = require("hardhat");

// RandomGame.sol - Smart contract for the dApp
// Save this contract as contracts/RandomGame.sol
/*
pragma solidity ^0.8.0;

contract RandomGame {
    event GamePlayed(address indexed player, uint256 randomNumber);

    function playGame() public {
        uint256 randomNumber = generateRandomNumber();
        emit GamePlayed(msg.sender, randomNumber);
    }

    function generateRandomNumber() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 100;
    }
}
*/

// Deployment script - scripts/deploy.js
async function main() {
  // Load the RandomGame smart contract
  const RandomGame = await ethers.getContractFactory("RandomGame");

  console.log("Deploying RandomGame contract...");
  const randomGame = await RandomGame.deploy();
  await randomGame.deployed();

  console.log(`RandomGame deployed successfully at address: ${randomGame.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Error deploying contract:", error);
    process.exit(1);
  });

// Graph Protocol Setup
// 1. Create a subgraph project using the Graph CLI
//    Run: graph init --product hosted-service [subgraph-name]
//    Example: graph init --product hosted-service random-game-mumbai

// 2. Define the subgraph manifest (subgraph.yaml)
/*
specVersion: 0.0.2
schema:
  file: ./schema.graphql
dataSources:
  - kind: ethereum/contract
    name: RandomGame
    network: mumbai
    source:
      address: "CONTRACT_ADDRESS_HERE"
      abi: RandomGame
      startBlock: BLOCK_NUMBER_HERE
    mapping:
      kind: ethereum/events
      apiVersion: 0.0.5
      language: wasm/assemblyscript
      file: ./src/mapping.ts
      entities:
        - GamePlayed
*/

// 3. Define the GraphQL schema - schema.graphql
/*
type GamePlayed @entity {
  id: ID!
  player: Bytes!
  randomNumber: Int!
}
*/

// 4. Write the AssemblyScript mapping logic - src/mapping.ts
/*
import { GamePlayed } from "../generated/RandomGame/RandomGame"
import { GamePlayed as GamePlayedEntity } from "../generated/schema"

export function handleGamePlayed(event: GamePlayed): void {
  let entity = new GamePlayedEntity(event.transaction.hash.toHex())
  entity.player = event.params.player
  entity.randomNumber = event.params.randomNumber.toI32()
  entity.save()
}
*/

// 5. Deploy the subgraph
//    Replace CONTRACT_ADDRESS_HERE and BLOCK_NUMBER_HERE in subgraph.yaml with actual values.
//    Run:
//    graph codegen
//    graph build
//    graph deploy --product hosted-service [SUBGRAPH_NAME]

// Ensure you have Mumbai Testnet RPC and an account with test MATIC configured in your .env file:
// .env
/*
MUMBAI_RPC_URL=https://rpc-mumbai.maticvigil.com
PRIVATE_KEY=YOUR_PRIVATE_KEY
*/

module.exports = {
  solidity: "0.8.4",
  networks: {
    mumbai: {
      url: process.env.MUMBAI_RPC_URL,
      accounts: [process.env.PRIVATE_KEY],
    },
  },
};
```
