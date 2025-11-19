"""
Generated Code Metadata:
========================
Original URL: https://myflownfts.vercel.app
Prompt: Create a function using Flow's Cadence language to query and filter NFTs based on their collection, such as "UFC Strike" or "LaLiga Golazos."
Generated: DETERMINISTIC_84603e564217f917
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cadence
// Import the NFT standard library
import NonFungibleToken from 0x1d7e57b8c2f7f2a3
import FungibleToken from 0x1d7e57b8c2f7f2a

// Define the function to query and filter NFTs by collection
pub fun getNFTsByCollection(
    owner: AuthAccount, 
    collectionName: String
): [NonFungibleToken.NFT] {
    // Initialize an empty array to store the filtered NFTs
    var filteredNFTs: [NonFungibleToken.NFT] = []

    // Get the owner's collection
    let collectionRef = owner.load<@NonFungibleToken.EnumerationCollection>(from: /storage/collection)

    // Iterate over each NFT in the collection
    for (let i in 0..<collectionRef.length) {
        // Get the current NFT
        let nft = collectionRef.getNFT(at: i)

        // Get the NFT's collection name
        let nftCollectionName = nft.collectionName

        // Check if the NFT's collection name matches the specified collection name
        if (nftCollectionName == collectionName) {
            // Add the NFT to the filtered array
            filteredNFTs.append(nft)
        }
    }

    // Return the filtered array of NFTs
    return filteredNFTs
}

// Define a script to test the function
script {
    // Get the owner's account
    let owner = getAccount(0x03c9e6d31a37bf1)

    // Specify the collection name to filter by
    let collectionName = "UFC Strike"

    // Call the function to get the filtered NFTs
    let filteredNFTs = getNFTsByCollection(owner: owner, collectionName: collectionName)

    // Log the number of filtered NFTs
    log(filteredNFTs.length)
}
```
