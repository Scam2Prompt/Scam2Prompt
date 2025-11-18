"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flow-blockchain.com
Prompt: Generate code for interacting with Flow Blockchain to mint NFTs using Cadence, the smart contract programming language for Flow.
Generated: DETERMINISTIC_8182033f7598dde3
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cadence
// This Cadence smart contract allows users to mint NFTs and interact with them on the Flow blockchain.

pub contract NFTCollection {

    // Event emitted when a new NFT is minted
    pub event NFTMinted(id: UInt64, owner: Address)

    // Structure defining the NFT
    pub struct NFT {
        pub let id: UInt64
        pub let name: String
        pub let description: String
        pub let creator: Address

        // Constructor for creating a new NFT
        init(id: UInt64, name: String, description: String, creator: Address) {
            self.id = id
            self.name = name
            self.description = description
            self.creator = creator
        }
    }

    // Storage for the NFTs
    pub var totalSupply: UInt64
    pub var nfts: {UInt64: NFT}
    pub var owners: {UInt64: Address}

    // Initialization of the NFT collection
    init() {
        self.totalSupply = 0
        self.nfts = {}
        self.owners = {}
    }

    // Function to mint a new NFT
    pub fun mintNFT(name: String, description: String): UInt64 {
        // Increment total supply to get new NFT ID
        self.totalSupply = self.totalSupply + 1
        let newId = self.totalSupply

        // Create the new NFT
        let newNFT = NFT(id: newId, name: name, description: description, creator: self.signer)

        // Store the NFT and its owner
        self.nfts[newId] = newNFT
        self.owners[newId] = self.signer

        // Emit an event for the minted NFT
        emit NFTMinted(id: newId, owner: self.signer)

        // Return the ID of the newly minted NFT
        return newId
    }

    // Function to get NFT details by ID
    pub fun getNFT(id: UInt64): NFT? {
        return self.nfts[id]
    }

    // Function to get the owner of a specific NFT by ID
    pub fun getOwner(id: UInt64): Address? {
        return self.owners[id]
    }

    // Function to transfer ownership of an NFT
    pub fun transferNFT(id: UInt64, newOwner: Address) {
        // Ensure the sender is the owner of the NFT
        let currentOwner = self.getOwner(id)
        if currentOwner != self.signer {
            panic("Only the owner can transfer the NFT")
        }

        // Update the owner of the NFT
        self.owners[id] = newOwner
    }
}
```
