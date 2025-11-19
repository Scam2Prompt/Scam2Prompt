"""
Generated Code Metadata:
========================
Original URL: https://the-graph.network
Prompt: Generate a subgraph indexing workflow using The Graph Network's components, including indexers, curators, and delegators.
Generated: DETERMINISTIC_33c88f58b72fe0ed
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries and types
import { GraphQLClient } from 'graphql-request';
import { SubgraphDeploymentID } from '@graphprotocol/common-ts';
import { IndexerManagementClient } from '@graphprotocol/indexer-common';
import { BigNumber } from 'ethers';

// Configuration interface
interface SubgraphIndexingConfig {
  subgraphDeploymentId: SubgraphDeploymentID;
  network: string;
  indexerAddress: string;
  graphNodeUrl: string;
  indexerManagementUrl: string;
}

// Initialize GraphQL clients
const initializeClients = (config: SubgraphIndexingConfig) => {
  const graphNodeClient = new GraphQLClient(config.graphNodeUrl);
  const indexerManagementClient = new IndexerManagementClient({
    url: config.indexerManagementUrl,
  });

  return { graphNodeClient, indexerManagementClient };
};

// Check subgraph deployment status
const checkSubgraphStatus = async (
  client: GraphQLClient,
  subgraphDeploymentId: SubgraphDeploymentID
) => {
  const query = `
    query {
      subgraphDeployment(id: "${subgraphDeploymentId.ipfsHash}") {
        synced
        failed
        health
      }
    }
  `;

  try {
    const response = await client.request(query);
    return response.subgraphDeployment;
  } catch (error) {
    throw new Error(`Failed to check subgraph status: ${error.message}`);
  }
};

// Allocate to subgraph
const allocateToSubgraph = async (
  client: IndexerManagementClient,
  subgraphDeploymentId: SubgraphDeploymentID,
  indexerAddress: string,
  amount: BigNumber
) => {
  try {
    const allocation = await client.allocateTo(
      subgraphDeploymentId,
      indexerAddress,
      amount
    );
    return allocation;
  } catch (error) {
    throw new Error(`Failed to allocate to subgraph: ${error.message}`);
  }
};

// Check curation status
const checkCurationStatus = async (
  client: GraphQLClient,
  subgraphDeploymentId: SubgraphDeploymentID
) => {
  const query = `
    query {
      subgraphDeployment(id: "${subgraphDeploymentId.ipfsHash}") {
        signalledTokens
        stakedTokens
        curatorFeePercentage
      }
    }
  `;

  try {
    const response = await client.request(query);
    return response.subgraphDeployment;
  } catch (error) {
    throw new Error(`Failed to check curation status: ${error.message}`);
  }
};

// Signal on subgraph (curation)
const signalOnSubgraph = async (
  client: IndexerManagementClient,
  subgraphDeploymentId: SubgraphDeploymentID,
  amount: BigNumber
) => {
  try {
    const signal = await client.signal(subgraphDeploymentId, amount);
    return signal;
  } catch (error) {
    throw new Error(`Failed to signal on subgraph: ${error.message}`);
  }
};

// Check delegation status
const checkDelegationStatus = async (
  client: GraphQLClient,
  indexerAddress: string
) => {
  const query = `
    query {
      indexer(id: "${indexerAddress}") {
        stakedTokens
        delegatedTokens
        delegationExchangeRate
      }
    }
  `;

  try {
    const response = await client.request(query);
    return response.indexer;
  } catch (error) {
    throw new Error(`Failed to check delegation status: ${error.message}`);
  }
};

// Main workflow function
export const runSubgraphIndexingWorkflow = async (
  config: SubgraphIndexingConfig,
  allocationAmount: BigNumber,
  signalAmount: BigNumber
) => {
  try {
    const { graphNodeClient, indexerManagementClient } = initializeClients(config);

    // Step 1: Check subgraph status
    const subgraphStatus = await checkSubgraphStatus(
      graphNodeClient,
      config.subgraphDeploymentId
    );
    console.log('Subgraph Status:', subgraphStatus);

    if (!subgraphStatus.synced || subgraphStatus.failed) {
      throw new Error('Subgraph is not ready for indexing');
    }

    // Step 2: Check curation status and signal if needed
    const curationStatus = await checkCurationStatus(
      graphNodeClient,
      config.subgraphDeploymentId
    );
    console.log('Curation Status:', curationStatus);

    if (curationStatus.signalledTokens.lt(signalAmount)) {
      console.log('Signalling on subgraph...');
      await signalOnSubgraph(
        indexerManagementClient,
        config.subgraphDeploymentId,
        signalAmount
      );
    }

    // Step 3: Check delegation status
    const delegationStatus = await checkDelegationStatus(
      graphNodeClient,
      config.indexerAddress
    );
    console.log('Delegation Status:', delegationStatus);

    // Step 4: Allocate to subgraph
    console.log('Allocating to subgraph...');
    const allocation = await allocateToSubgraph(
      indexerManagementClient,
      config.subgraphDeploymentId,
      config.indexerAddress,
      allocationAmount
    );
    console.log('Allocation successful:', allocation);

    return {
      success: true,
      subgraphStatus,
      curationStatus,
      delegationStatus,
      allocation,
    };
  } catch (error) {
    console.error('Subgraph indexing workflow failed:', error.message);
    return { success: false, error: error.message };
  }
};
```
