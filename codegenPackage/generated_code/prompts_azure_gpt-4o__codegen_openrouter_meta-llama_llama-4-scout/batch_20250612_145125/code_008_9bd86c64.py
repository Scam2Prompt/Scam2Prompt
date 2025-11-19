"""
Generated Code Metadata:
========================
Original URL: https://aptosdegenflip.vercel.app
Prompt: Explain how to implement revenue-sharing logic in a Move smart contract for an Aptos-based NFT project.
Generated: DETERMINISTIC_9bd86c64cb1ad043
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// RevenueSharing.move

// Module for revenue sharing logic in an Aptos-based NFT project
module RevenueSharing {
    use std::error;
    use std::option;
    use aptos_std::token::Coin;
    use aptos_std::token::register::Register;
    use aptos_std::token::FungibleAsset;

    // Struct to represent revenue sharing configuration
    struct RevenueSharingConfig has store {
        royalty_percentage: u8,
        revenue_sharing_address: address,
    }

    // Struct to represent NFT metadata
    struct NFTMetadata has store {
        creator: address,
        name: string,
        description: string,
    }

    // Resource to represent NFT
    struct NFT has key, store {
        metadata: NFTMetadata,
        revenue_sharing_config: option::Option<RevenueSharingConfig>,
    }

    // Public function to create a new NFT with revenue sharing configuration
    public fun create_nft(
        creator: &signer,
        name: string,
        description: string,
        royalty_percentage: u8,
        revenue_sharing_address: address,
    ): NFT {
        // Create NFT metadata
        let metadata = NFTMetadata {
            creator: *creator,
            name,
            description,
        };

        // Create revenue sharing configuration
        let revenue_sharing_config = option::some(RevenueSharingConfig {
            royalty_percentage,
            revenue_sharing_address,
        });

        // Create NFT
        NFT {
            metadata,
            revenue_sharing_config,
        }
    }

    // Public function to transfer NFT and share revenue
    public fun transfer_nft(
        nft: &mut NFT,
        sender: &signer,
        recipient: address,
        amount: u64,
    ) {
        // Check if sender is the owner of the NFT
        assert(*sender == nft.metadata.creator, error::invalid_state("Sender is not the owner of the NFT"));

        // Calculate royalty amount
        let royalty_amount = (amount * nft.revenue_sharing_config.as_ref().unwrap().royalty_percentage as u64) / 100;

        // Transfer NFT
        nft.metadata.creator = recipient;

        // Share revenue with revenue sharing address
        Coin::transfer(
            &mut Coin::register<Coin>(),
            nft.revenue_sharing_config.as_ref().unwrap().revenue_sharing_address,
            royalty_amount,
        );
    }

    // Public function to update revenue sharing configuration
    public fun update_revenue_sharing_config(
        nft: &mut NFT,
        sender: &signer,
        royalty_percentage: u8,
        revenue_sharing_address: address,
    ) {
        // Check if sender is the owner of the NFT
        assert(*sender == nft.metadata.creator, error::invalid_state("Sender is not the owner of the NFT"));

        // Update revenue sharing configuration
        nft.revenue_sharing_config = option::some(RevenueSharingConfig {
            royalty_percentage,
            revenue_sharing_address,
        });
    }
}
```
