"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myflownfts.vercel.app
Prompt: Write a Cadence smart contract to transfer ownership of an NFT, such as "Seb 2.66" or "Charlotte Phoenix #43," from one wallet to another.
Generated: DETERMINISTIC_e6350b137bb2c85b
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cadence
// SPDX-License-Identifier: MIT
// Cadence Smart Contract for transferring ownership of an NFT
// This contract assumes the NFT follows the NonFungibleToken standard.
// Ensure the NFT resource and capabilities are correctly set up in your environment.

import NonFungibleToken from 0x01 // Replace with the correct account address for the NonFungibleToken standard
import ExampleNFT from 0x02 // Replace with the correct account address for the NFT implementation

pub contract NFTTransfer {

    // Event to log NFT transfers for transparency and tracking
    pub event NFTTransferred(id: UInt64, from: Address, to: Address)

    // Function to transfer ownership of an NFT
    pub fun transferNFT(
        nftID: UInt64,          // ID of the NFT to transfer
        sender: Address,        // Address of the current owner
        recipient: Address      // Address of the new owner
    ) {
        // Validate the inputs
        pre {
            sender != recipient: "Sender and recipient addresses must be different"
            nftID > 0: "Invalid NFT ID"
        }

        // Access the sender's account to retrieve the NFT
        let senderAccount = getAccount(sender)

        // Borrow the NFT from the sender's collection
        let senderCollectionRef = senderAccount.getCapability<&ExampleNFT.Collection{NonFungibleToken.Provider}>(
            ExampleNFT.CollectionPublicPath
        ).borrow()
            ?? panic("Sender's collection not found or does not provide NFTs")

        // Withdraw the NFT from the sender's collection
        let nft <- senderCollectionRef.withdraw(withdrawID: nftID)

        // Access the recipient's account to deposit the NFT
        let recipientAccount = getAccount(recipient)

        // Borrow the recipient's collection
        let recipientCollectionRef = recipientAccount.getCapability<&ExampleNFT.Collection{NonFungibleToken.Receiver}>(
            ExampleNFT.CollectionPublicPath
        ).borrow()
            ?? panic("Recipient's collection not found or does not accept NFTs")

        // Deposit the NFT into the recipient's collection
        recipientCollectionRef.deposit(token: <-nft)

        // Emit an event to signal the transfer
        emit NFTTransferred(id: nftID, from: sender, to: recipient)
    }
}
```
