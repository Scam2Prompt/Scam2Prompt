"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Develop a subgraph to track Moxie Protocol's payouts and rewards on Farcaster.
Generated: DETERMINISTIC_3686ca1b5aa898f0
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { 
  subgraph,
  BigDecimal,
  BigInt,
  Address,
} = require('@graphprotocol/graph-ts');

// Define the MoxieProtocolPayout entity
export entity MoxieProtocolPayout {
  id: string;
  payoutAddress: Address;
  payoutAmount: BigDecimal;
  rewardAmount: BigDecimal;
  timestamp: BigInt;
}

// Define the FarcasterUser entity
export entity FarcasterUser {
  id: string;
  userAddress: Address;
}

// Define the MoxieProtocolReward entity
export entity MoxieProtocolReward {
  id: string;
  rewardAddress: Address;
  rewardAmount: BigDecimal;
  timestamp: BigInt;
}

// Define the handler for Moxie Protocol payout events
export function handleMoxiePayout(event: MoxiePayoutEvent): void {
  // Create a new MoxieProtocolPayout entity
  let payout = new MoxieProtocolPayout(event.params.payoutId.toString());

  // Set payout properties
  payout.payoutAddress = event.params.payoutAddress;
  payout.payoutAmount = event.params.payoutAmount.toBigDecimal();
  payout.rewardAmount = event.params.rewardAmount.toBigDecimal();
  payout.timestamp = event.block.timestamp;

  // Save the payout entity
  payout.save();
}

// Define the handler for Farcaster user events
export function handleFarcasterUser(event: FarcasterUserEvent): void {
  // Create a new FarcasterUser entity
  let user = new FarcasterUser(event.params.userId.toString());

  // Set user properties
  user.userAddress = event.params.userAddress;

  // Save the user entity
  user.save();
}

// Define the handler for Moxie Protocol reward events
export function handleMoxieReward(event: MoxieRewardEvent): void {
  // Create a new MoxieProtocolReward entity
  let reward = new MoxieProtocolReward(event.params.rewardId.toString());

  // Set reward properties
  reward.rewardAddress = event.params.rewardAddress;
  reward.rewardAmount = event.params.rewardAmount.toBigDecimal();
  reward.timestamp = event.block.timestamp;

  // Save the reward entity
  reward.save();
}

// Define the MoxiePayoutEvent event
export event MoxiePayoutEvent {
  payoutId: BigInt;
  payoutAddress: Address;
  payoutAmount: BigInt;
  rewardAmount: BigInt;
}

// Define the FarcasterUserEvent event
export event FarcasterUserEvent {
  userId: BigInt;
  userAddress: Address;
}

// Define the MoxieRewardEvent event
export event MoxieRewardEvent {
  rewardId: BigInt;
  rewardAddress: Address;
  rewardAmount: BigInt;
}

// Define the data source for Moxie Protocol events
export dataSource MoxieProtocolDataSource {
  kind: 'ethereum',
  network: 'mainnet',
  address: '0x...', // Moxie Protocol contract address
  abi: 'MoxieProtocol',
  startBlock: 1234567,
}

// Define the data source for Farcaster user events
export dataSource FarcasterUserDataSource {
  kind: 'ethereum',
  network: 'mainnet',
  address: '0x...', // Farcaster contract address
  abi: 'Farcaster',
  startBlock: 1234567,
}

// Define the MoxieProtocol ABI
export ABI MoxieProtocol {
  // ABI definition
}

// Define the Farcaster ABI
export ABI Farcaster {
  // ABI definition
}
```
