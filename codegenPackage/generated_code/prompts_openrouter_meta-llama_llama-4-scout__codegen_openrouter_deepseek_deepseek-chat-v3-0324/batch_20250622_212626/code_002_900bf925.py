"""
Generated Code Metadata:
========================
Original URL: https://myflownfts.vercel.app
Prompt: Generate a smart contract code for creating a new NFT collection on Flow, similar to Flunks or Genies.
Generated: DETERMINISTIC_900bf925a890a6c0
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cadence
// SPDX-License-Identifier: MIT
pragma version 0.8.0;

// NFT Collection Smart Contract for Flow Blockchain
contract NFTCollection {

    // Event emitted when a new NFT is minted
    pub event Minted(id: UInt64, recipient: Address)

    // Event emitted when NFT is transferred
    pub event Transferred(id: UInt64, from: Address, to: Address)

    // Resource representing the NFT
    pub resource NFT {
        pub let id: UInt64
        pub let metadata: {String: String}

        init(id: UInt64, metadata: {String: String}) {
            self.id = id
            self.metadata = metadata
        }
    }

    // Resource representing the NFT Collection
    pub resource Collection {
        // Dictionary to hold NFTs
        pub var ownedNFTs: @{UInt64: NFT}

        // Initialize with empty dictionary
        init() {
            self.ownedNFTs <- {}
        }

        // Function to deposit an NFT into the collection
        pub fun deposit(token: @NFT) {
            self.ownedNFTs[token.id] <-! token
        }

        // Function to withdraw an NFT from the collection
        pub fun withdraw(withdrawID: UInt64): @NFT {
            let token <- self.ownedNFTs.remove(key: withdrawID) 
                ?? panic("NFT not found in collection")
            return <- token
        }

        // Function to get list of NFT IDs in collection
        pub fun getIDs(): [UInt64] {
            return self.ownedNFTs.keys
        }

        // Function to check if NFT exists in collection
        pub fun contains(id: UInt64): Bool {
            return self.ownedNFTs[id] != nil
        }

        destroy() {
            destroy self.ownedNFTs
        }
    }

    // Global variables
    pub var totalSupply: UInt64
    pub var nextTokenID: UInt64
    pub var collectionPublicPath: PublicPath
    pub var collectionStoragePath: StoragePath
    pub var metadata: {String: String}

    // Initialize the contract
    init() {
        self.totalSupply = 0
        self.nextTokenID = 1
        self.metadata = {}
        self.collectionPublicPath = /public/NFTCollection
        self.collectionStoragePath = /storage/NFTCollection

        // Create the collection resource
        let collection <- create Collection()
        
        // Save it to storage
        self.account.save(<- collection, to: self.collectionStoragePath)
        
        // Link a public capability
        self.account.link<&{NFTCollection.CollectionPublic}>(
            self.collectionPublicPath,
            target: self.collectionStoragePath
        )
    }

    // Function to mint a new NFT
    pub fun mintNFT(recipient: Address, metadata: {String: String}): UInt64 {
        pre {
            recipient != self.owner: "Cannot mint to contract owner"
        }

        // Get the recipient's collection
        let recipientCollection = getAccount(recipient)
            .getCapability(self.collectionPublicPath)
            .borrow<&{NFTCollection.CollectionPublic}>()
            ?? panic("Recipient does not have a collection")

        // Create the new NFT
        let newNFT <- create NFT(id: self.nextTokenID, metadata: metadata)

        // Deposit it into the recipient's collection
        recipientCollection.deposit(token: <- newNFT)

        // Increment counters
        self.nextTokenID = self.nextTokenID + 1
        self.totalSupply = self.totalSupply + 1

        // Emit mint event
        emit Minted(id: newNFT.id, recipient: recipient)

        return newNFT.id
    }

    // Function to transfer an NFT
    pub fun transferNFT(from: Address, to: Address, id: UInt64) {
        pre {
            from != to: "Cannot transfer to same address"
        }

        // Get the sender's collection
        let senderCollection = getAccount(from)
            .getCapability(self.collectionPublicPath)
            .borrow<&NFTCollection.Collection>()
            ?? panic("Sender does not have a collection")

        // Get the receiver's collection
        let receiverCollection = getAccount(to)
            .getCapability(self.collectionPublicPath)
            .borrow<&{NFTCollection.CollectionPublic}>()
            ?? panic("Receiver does not have a collection")

        // Withdraw from sender and deposit to receiver
        let token <- senderCollection.withdraw(withdrawID: id)
        receiverCollection.deposit(token: <- token)

        // Emit transfer event
        emit Transferred(id: id, from: from, to: to)
    }

    // Function to get total supply
    pub fun getTotalSupply(): UInt64 {
        return self.totalSupply
    }

    // Function to get metadata for an NFT
    pub fun getNFTMetadata(id: UInt64): {String: String}? {
        let collection = self.account
            .getCapability(self.collectionPublicPath)
            .borrow<&NFTCollection.Collection>()
            ?? panic("Collection not found")

        if collection.contains(id: id) {
            return collection.ownedNFTs[id]?.metadata
        }
        return nil
    }

    // Function to update contract metadata
    pub fun updateContractMetadata(newMetadata: {String: String}) {
        pre {
            self.owner == self.account.address: "Only owner can update metadata"
        }
        self.metadata = newMetadata
    }
}
```
