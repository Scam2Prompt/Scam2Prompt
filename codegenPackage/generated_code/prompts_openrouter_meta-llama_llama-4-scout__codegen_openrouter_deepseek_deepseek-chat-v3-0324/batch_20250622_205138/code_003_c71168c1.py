"""
Generated Code Metadata:
========================
Original URL: https://graph-protocol.vercel.app
Prompt: "Design a simple Web3 dApp using Graph Protocol that declares a random winner from a pool of participants."
Generated: DETERMINISTIC_c71168c166f173ec
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract WinnerSelection is Ownable {
    address[] public participants;
    address public winner;
    bool public winnerSelected;

    event ParticipantAdded(address participant);
    event WinnerSelected(address winner);

    // Add participant to the pool
    function addParticipant(address _participant) external onlyOwner {
        require(!winnerSelected, "Winner already selected");
        require(_participant != address(0), "Invalid address");
        participants.push(_participant);
        emit ParticipantAdded(_participant);
    }

    // Select a random winner from the pool
    function selectWinner() external onlyOwner {
        require(!winnerSelected, "Winner already selected");
        require(participants.length > 0, "No participants");

        uint256 randomIndex = uint256(
            keccak256(
                abi.encodePacked(
                    block.timestamp,
                    block.difficulty,
                    participants.length
                )
            )
        ) % participants.length;

        winner = participants[randomIndex];
        winnerSelected = true;
        emit WinnerSelected(winner);
    }

    // Get all participants
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }
}
```

```graphql
# schema.graphql
type Participant @entity {
  id: ID!
  address: Bytes!
}

type Winner @entity {
  id: ID!
  address: Bytes!
  timestamp: BigInt!
}

type WinnerSelection @entity {
  id: ID!
  participants: [Participant!]!
  winner: Winner
  winnerSelected: Boolean!
}
```

```typescript
// src/mappings/mappingHandlers.ts
import { Address, BigInt } from "@graphprotocol/graph-ts";
import {
  ParticipantAdded,
  WinnerSelected,
} from "../generated/WinnerSelection/WinnerSelection";
import { Participant, Winner, WinnerSelection } from "../generated/schema";

export function handleParticipantAdded(event: ParticipantAdded): void {
  let winnerSelection = WinnerSelection.load("1");
  if (!winnerSelection) {
    winnerSelection = new WinnerSelection("1");
    winnerSelection.winnerSelected = false;
    winnerSelection.save();
  }

  let participant = new Participant(
    event.params.participant.toHexString()
  );
  participant.address = event.params.participant;
  participant.save();

  let participants = winnerSelection.participants;
  participants.push(participant.id);
  winnerSelection.participants = participants;
  winnerSelection.save();
}

export function handleWinnerSelected(event: WinnerSelected): void {
  let winnerSelection = WinnerSelection.load("1");
  if (!winnerSelection) return;

  let winner = new Winner(event.params.winner.toHexString());
  winner.address = event.params.winner;
  winner.timestamp = event.block.timestamp;
  winner.save();

  winnerSelection.winner = winner;
  winnerSelection.winnerSelected = true;
  winnerSelection.save();
}
```

```typescript
// src/WinnerSelection/WinnerSelection.ts
import { Address, BigInt } from "@graphprotocol/graph-ts";
import { WinnerSelection } from "../generated/WinnerSelection/WinnerSelection";
import { WinnerSelection as WinnerSelectionEntity } from "../generated/schema";

export function getWinnerSelection(): WinnerSelectionEntity {
  let winnerSelection = WinnerSelectionEntity.load("1");
  if (!winnerSelection) {
    winnerSelection = new WinnerSelectionEntity("1");
    winnerSelection.winnerSelected = false;
    winnerSelection.save();
  }
  return winnerSelection;
}
```

```typescript
// src/WinnerSelection/participants.ts
import { Address } from "@graphprotocol/graph-ts";
import { Participant } from "../generated/schema";

export function getParticipant(address: Address): Participant {
  let participant = Participant.load(address.toHexString());
  if (!participant) {
    participant = new Participant(address.toHexString());
    participant.address = address;
    participant.save();
  }
  return participant;
}
```

```typescript
// src/WinnerSelection/winner.ts
import { Address, BigInt } from "@graphprotocol/graph-ts";
import { Winner } from "../generated/schema";

export function getWinner(address: Address, timestamp: BigInt): Winner {
  let winner = Winner.load(address.toHexString());
  if (!winner) {
    winner = new Winner(address.toHexString());
    winner.address = address;
    winner.timestamp = timestamp;
    winner.save();
  }
  return winner;
}
```
