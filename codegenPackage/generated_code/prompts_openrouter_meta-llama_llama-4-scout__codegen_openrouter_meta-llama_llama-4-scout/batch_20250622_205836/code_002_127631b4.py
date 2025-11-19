"""
Generated Code Metadata:
========================
Original URL: https://bafybeibasskry2ovpgydqzwiw46ea2lmyxe4fqb6jekaixqidxb6cvjn3m.ipfs.dweb.link
Prompt: Generate a code example for a multi-hop IBC specification using Polymer’s merged IBC repository.
Generated: DETERMINISTIC_127631b411a69d60
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { IBC } = require('@polymer/ibc');
const { ClientState } = require('@polymer/ibc-client-state');
const { ConnectionState } = require('@polymer/ibc-connection-state');
const { ChannelState } = require('@polymer/ibc-channel-state');

// Define a function to create a multi-hop IBC specification
async function createMultiHopIbcSpecification(
  sourceChainId,
  sourceClientId,
  sourceConnectionId,
  sourceChannelId,
  intermediateChainId,
  intermediateClientId,
  intermediateConnectionId,
  intermediateChannelId,
  destinationChainId,
  destinationClientId,
  destinationConnectionId,
  destinationChannelId
) {
  try {
    // Initialize the IBC instance
    const ibc = new IBC();

    // Create client states for each chain
    const sourceClientState = new ClientState(sourceChainId, sourceClientId);
    const intermediateClientState = new ClientState(intermediateChainId, intermediateClientId);
    const destinationClientState = new ClientState(destinationChainId, destinationClientId);

    // Create connection states for each chain
    const sourceConnectionState = new ConnectionState(sourceChainId, sourceConnectionId);
    const intermediateConnectionState = new ConnectionState(intermediateChainId, intermediateConnectionId);
    const destinationConnectionState = new ConnectionState(destinationChainId, destinationConnectionId);

    // Create channel states for each chain
    const sourceChannelState = new ChannelState(sourceChainId, sourceChannelId);
    const intermediateChannelState = new ChannelState(intermediateChainId, intermediateChannelId);
    const destinationChannelState = new ChannelState(destinationChainId, destinationChannelId);

    // Define the multi-hop IBC specification
    const multiHopIbcSpecification = {
      source: {
        chainId: sourceChainId,
        clientId: sourceClientId,
        connectionId: sourceConnectionId,
        channelId: sourceChannelId,
      },
      intermediate: {
        chainId: intermediateChainId,
        clientId: intermediateClientId,
        connectionId: intermediateConnectionId,
        channelId: intermediateChannelId,
      },
      destination: {
        chainId: destinationChainId,
        clientId: destinationClientId,
        connectionId: destinationConnectionId,
        channelId: destinationChannelId,
      },
    };

    // Validate the IBC specification
    await ibc.validateMultiHopIbcSpecification(multiHopIbcSpecification);

    // Return the multi-hop IBC specification
    return multiHopIbcSpecification;
  } catch (error) {
    // Handle any errors that occur during the creation of the multi-hop IBC specification
    console.error('Error creating multi-hop IBC specification:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    const multiHopIbcSpecification = await createMultiHopIbcSpecification(
      'chain-1',
      'client-1',
      'connection-1',
      'channel-1',
      'chain-2',
      'client-2',
      'connection-2',
      'channel-2',
      'chain-3',
      'client-3',
      'connection-3',
      'channel-3'
    );
    console.log('Multi-hop IBC specification:', multiHopIbcSpecification);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
