"""
Generated Code Metadata:
========================
Original URL: https://flow-blockchain.com
Prompt: Generate code for interacting with Flow Blockchain to mint NFTs using Cadence, the smart contract programming language for Flow.
Generated: DETERMINISTIC_8182033f7598dde3
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cadence
// Cadence smart contract for minting NFTs on the Flow Blockchain

pub contract NFTMinter {

    // Define the NFT structure
    pub struct NFT {
        pub let id: UInt64
        pub let name: String
        pub let description: String
        pub let creator: Address

        // Initialize a new NFT
        init(id: UInt64, name: String, description: String, creator: Address) {
            self.id = id
            self.name = name
            self.description = description
            self.creator = creator
        }
    }

    // Store the total supply of NFTs
    pub var totalSupply: UInt64

    // Mapping from NFT ID to NFT
    pub var nfts: @{UInt64: NFT}

    // Event emitted when a new NFT is minted
    pub event NFTMinted(id: UInt64, name: String, description: String, creator: Address)

    // Initialize the contract
    init() {
        self.totalSupply = 0
        self.nfts = {}
    }

    // Function to mint a new NFT
    pub fun mintNFT(name: String, description: String): UInt64 {
        // Increment the total supply to get a new NFT ID
        let newID = self.totalSupply + 1
        self.totalSupply = newID

        // Create a new NFT instance
        let newNFT = NFT(id: newID, name: name, description: description, creator: self.signer)

        // Store the NFT in the mapping
        self.nfts[newID] <- newNFT

        // Emit the NFTMinted event
        emit NFTMinted(id: newID, name: name, description: description, creator: self.signer)

        // Return the new NFT ID
        return newID
    }

    // Function to retrieve an NFT by its ID
    pub fun getNFT(id: UInt64): NFT? {
        // Check if the NFT exists and return it
        return self.nfts[id]
    }

    // Function to get the total supply of NFTs
    pub fun getTotalSupply(): UInt64 {
        return self.totalSupply
    }
}
```
