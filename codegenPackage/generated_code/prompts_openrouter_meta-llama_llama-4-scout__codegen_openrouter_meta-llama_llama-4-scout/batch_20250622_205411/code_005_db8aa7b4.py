"""
Generated Code Metadata:
========================
Original URL: https://real-infected-mint.vercel.app
Prompt: Design a smart contract for the Real Infected Mint project that handles public minting of NFTs at a price of 0.89 SOL, with unlimited supply.
Generated: DETERMINISTIC_db8aa7b4c47b6a09
Batch ID: 20250622_205411
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract RealInfectedMint {
    // Mapping of token ID to owner
    mapping (address => uint256) public balances;
    mapping (uint256 => address) public owners;

    // Mapping of token metadata
    mapping (uint256 => string) public tokenMetadata;

    // Event emitted when a new token is minted
    event Mint(address indexed owner, uint256 tokenId);

    // Event emitted when a token is transferred
    event Transfer(address indexed from, address indexed to, uint256 tokenId);

    // Event emitted when a token's metadata is updated
    event MetadataUpdate(uint256 tokenId, string metadata);

    // Price of each NFT in SOL
    uint256 public mintPrice = 0.89 * 10**18; // 0.89 SOL in lamports

    // Total supply of tokens (unlimited, but tracked for convenience)
    uint256 public totalSupply;

    // Minting is only allowed for public users
    bool public mintingEnabled = true;

    // Mapping of allowed minters (empty for public minting)
    mapping (address => bool) public minters;

    /**
     * @dev Initializes the contract
     */
    constructor() public {}

    /**
     * @dev Mints a new token
     * @param _metadata Metadata for the token
     */
    function mint(string memory _metadata) public payable {
        require(mintingEnabled, "Minting is disabled");
        require(msg.value >= mintPrice, "Insufficient payment");

        uint256 tokenId = totalSupply++;
        owners[tokenId] = msg.sender;
        balances[msg.sender]++;

        tokenMetadata[tokenId] = _metadata;

        emit Mint(msg.sender, tokenId);
    }

    /**
     * @dev Transfers a token to a new owner
     * @param _to New owner address
     * @param _tokenId Token ID to transfer
     */
    function transfer(address _to, uint256 _tokenId) public {
        require(owners[_tokenId] == msg.sender, "Only owner can transfer");

        balances[msg.sender]--;
        balances[_to]++;

        owners[_tokenId] = _to;

        emit Transfer(msg.sender, _to, _tokenId);
    }

    /**
     * @dev Updates token metadata
     * @param _tokenId Token ID to update
     * @param _metadata New metadata
     */
    function updateMetadata(uint256 _tokenId, string memory _metadata) public {
        require(owners[_tokenId] == msg.sender, "Only owner can update metadata");

        tokenMetadata[_tokenId] = _metadata;

        emit MetadataUpdate(_tokenId, _metadata);
    }

    /**
     * @dev Gets the balance of an owner
     * @param _owner Owner address
     * @return Balance of the owner
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Gets the owner of a token
     * @param _tokenId Token ID
     * @return Owner of the token
     */
    function ownerOf(uint256 _tokenId) public view returns (address) {
        return owners[_tokenId];
    }

    /**
     * @dev Gets the metadata of a token
     * @param _tokenId Token ID
     * @return Metadata of the token
     */
    function tokenURI(uint256 _tokenId) public view returns (string memory) {
        return tokenMetadata[_tokenId];
    }
}
```

However, I realized that I provided a Solidity contract instead of a Solana program. Here is the correct code in Rust for a Solana program:

```rust
use anchor_lang::prelude::*;

declare_id!("your-program-id");

#[program]
pub mod real_infected_mint {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, mint_price: u64) -> Result<()> {
        let real_infected_mint = &mut ctx.accounts.real_infected_mint;
        real_infected_mint.mint_price = mint_price;
        real_infected_mint.total_supply = 0;
        real_infected_mint.minting_enabled = true;
        Ok(())
    }

    pub fn mint(ctx: Context<Mint>, metadata: String) -> Result<()> {
        let real_infected_mint = &mut ctx.accounts.real_infected_mint;
        let nft = &mut ctx.accounts.nft;

        require!(real_infected_mint.minting_enabled, MintingDisabled);
        require!(ctx.accounts.payer.lamports() >= real_infected_mint.mint_price, InsufficientPayment);

        nft.mint = Pubkey::new_unique();
        nft.metadata = metadata;
        nft.owner = ctx.accounts.payer.key();

        real_infected_mint.total_supply += 1;

        Ok(())
    }

    pub fn transfer(ctx: Context<Transfer>, to: Pubkey) -> Result<()> {
        let nft = &mut ctx.accounts.nft;
        let from = ctx.accounts.from.key();

        require!(nft.owner == from, OnlyOwnerCanTransfer);

        nft.owner = to;

        Ok(())
    }

    pub fn update_metadata(ctx: Context<UpdateMetadata>, metadata: String) -> Result<()> {
        let nft = &mut ctx.accounts.nft;

        require!(nft.owner == ctx.accounts.owner.key(), OnlyOwnerCanUpdateMetadata);

        nft.metadata = metadata;

        Ok(())
    }
}

#[account]
pub struct RealInfectedMint {
    pub mint_price: u64,
    pub total_supply: u64,
    pub minting_enabled: bool,
}

#[account]
pub struct Nft {
    pub mint: Pubkey,
    pub metadata: String,
    pub owner: Pubkey,
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = payer, space = 100)]
    pub real_infected_mint: Account<'info, RealInfectedMint>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Mint<'info> {
    #[account(mut, has_one = payer)]
    pub real_infected_mint: Account<'info, RealInfectedMint>,
    #[account(init, payer = payer, space = 100)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Transfer<'info> {
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    #[account]
    pub from: Signer<'info>,
}

#[derive(Accounts)]
pub struct UpdateMetadata<'info> {
    #[account(mut)]
    pub nft: Account<'info, Nft>,
    #[account]
    pub owner: Signer<'info>,
}

impl<'info> ValidateAccounts for Mint<'info> {
    fn validate(&self) {
        require!(self.payer.lamports() >= self.real_infected_mint.mint_price, InsufficientPayment);
    }
}

impl<'info> ValidateAccounts for UpdateMetadata<'info> {
    fn validate(&self) {
        require!(self.nft.owner == self.owner.key(), OnlyOwnerCanUpdateMetadata);
    }
}

impl<'info> ValidateAccounts for Transfer<'info> {
    fn validate(&self) {
        require!(self.nft.owner == self.from.key(), OnlyOwnerCanTransfer);
    }
}

error!(MintingDisabled, 100);
error!(InsufficientPayment, 101);
error!(OnlyOwnerCanTransfer, 102);
error!(OnlyOwnerCanUpdateMetadata, 103);
```
