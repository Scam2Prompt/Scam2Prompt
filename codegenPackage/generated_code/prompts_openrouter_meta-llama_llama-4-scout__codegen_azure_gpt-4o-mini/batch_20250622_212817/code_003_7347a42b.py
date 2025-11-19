"""
Generated Code Metadata:
========================
Original URL: https://thegraph-the-graph.org
Prompt: "Explain how to define and organize data using subgraphs for indexing blockchain data, as per The Graph's documentation."
Generated: DETERMINISTIC_7347a42b4ffa8b8c
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```graphql
# Define a subgraph for indexing blockchain data using The Graph's protocol

# The Graph schema definition
type User @entity {
  id: ID!                # Unique identifier for the user
  name: String!         # Name of the user
  createdAt: BigInt!    # Timestamp of user creation
  posts: [Post!]!       # List of posts created by the user
}

type Post @entity {
  id: ID!               # Unique identifier for the post
  title: String!        # Title of the post
  content: String!      # Content of the post
  author: User!         # Reference to the user who created the post
  createdAt: BigInt!    # Timestamp of post creation
}

# Define the data source for the subgraph
dataSource UserDataSource {
  kind: ethereum         # Specify the kind of blockchain (Ethereum)
  network: mainnet      # Specify the network (mainnet, testnet, etc.)
  source: {
    address: "0xYourContractAddress"  # Address of the smart contract to index
    startBlock: 12345678  # Block number to start indexing from
  }
  mapping: {
    kind: ethereum/events  # Specify that we are indexing events
    apiVersion: 0.0.5      # Specify the API version
    language: wasm          # Specify the language for the mapping
    entities: ["User", "Post"]  # Entities to be indexed
    abis: [                # Define the ABIs for the contract
      {
        name: "YourContract",
        file: "./abis/YourContract.json"
      }
    ]
    eventHandlers: [       # Define event handlers for the events to listen to
      {
        event: "UserCreated(id: ID!, name: String!)",
        handler: "handleUserCreated"
      },
      {
        event: "PostCreated(id: ID!, title: String!, content: String!, author: ID!)",
        handler: "handlePostCreated"
      }
    ]
    file: "./src/mapping.ts"  # Path to the mapping file
  }
}

# Mapping file (mapping.ts) for handling events
import { User, Post } from "../generated/schema";  // Import generated schema types
import { UserCreated, PostCreated } from "../generated/YourContract/YourContract";  // Import event types

// Handler for UserCreated event
export function handleUserCreated(event: UserCreated): void {
  let user = new User(event.params.id.toHex());  // Create a new User entity
  user.name = event.params.name;                  // Set the user's name
  user.createdAt = event.block.timestamp;         // Set the creation timestamp
  user.save();                                    // Save the entity to the store
}

// Handler for PostCreated event
export function handlePostCreated(event: PostCreated): void {
  let post = new Post(event.params.id.toHex());  // Create a new Post entity
  post.title = event.params.title;                // Set the post's title
  post.content = event.params.content;            // Set the post's content
  post.author = event.params.author;              // Set the author reference
  post.createdAt = event.block.timestamp;         // Set the creation timestamp
  post.save();                                    // Save the entity to the store
}
```
