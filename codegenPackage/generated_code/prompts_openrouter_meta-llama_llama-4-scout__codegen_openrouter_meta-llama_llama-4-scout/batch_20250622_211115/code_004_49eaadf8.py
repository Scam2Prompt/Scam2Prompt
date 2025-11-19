"""
Generated Code Metadata:
========================
Original URL: https://ed-boxes.web.app
Prompt: Design a smart contract on the Solana blockchain to manage NFT minting and trading with dynamic royalties, inspired by Magic Eden's Open Creator Protocol.
Generated: DETERMINISTIC_49eaadf86a572fc2
Batch ID: 20250622_211115
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

// Define the NFT contract
contract SolanaNFT {
    // Mapping of NFT owners
    mapping (address => mapping (uint256 => bool)) public nftOwners;

    // Mapping of NFT metadata
    mapping (uint256 => NFTMetadata) public nftMetadata;

    // Mapping of royalty rates
    mapping (address => uint256) public royaltyRates;

    // Event emitted when an NFT is minted
    event Mint(address indexed owner, uint256 tokenId);

    // Event emitted when an NFT is transferred
    event Transfer(address indexed from, address indexed to, uint256 tokenId);

    // Event emitted when a royalty rate is updated
    event RoyaltyRateUpdated(address indexed creator, uint256 newRate);

    // Struct to hold NFT metadata
    struct NFTMetadata {
        string name;
        string symbol;
        string uri;
    }

    // Initialize the contract
    constructor() public {}

    // Mint a new NFT
    function mint(address owner, uint256 tokenId, string memory name, string memory symbol, string memory uri) public {
        require(msg.sender == owner, "Only the owner can mint NFTs");

        // Set the NFT owner
        nftOwners[owner][tokenId] = true;

        // Set the NFT metadata
        nftMetadata[tokenId] = NFTMetadata(name, symbol, uri);

        // Emit the Mint event
        emit Mint(owner, tokenId);
    }

    // Transfer an NFT
    function transfer(address from, address to, uint256 tokenId) public {
        require(nftOwners[from][tokenId], "NFT not owned by sender");
        require(msg.sender == from || msg.sender == owner(), "Only the owner or approved user can transfer");

        // Remove the NFT from the sender's balance
        nftOwners[from][tokenId] = false;

        // Add the NFT to the recipient's balance
        nftOwners[to][tokenId] = true;

        // Emit the Transfer event
        emit Transfer(from, to, tokenId);
    }

    // Update the royalty rate for a creator
    function updateRoyaltyRate(address creator, uint256 newRate) public {
        require(msg.sender == owner() || msg.sender == creator, "Only the owner or creator can update royalty rates");

        // Validate the new royalty rate
        require(newRate >= 0 && newRate <= 10000, "Royalty rate must be between 0 and 10000");

        // Update the royalty rate
        royaltyRates[creator] = newRate;

        // Emit the RoyaltyRateUpdated event
        emit RoyaltyRateUpdated(creator, newRate);
    }

    // Get the royalty amount for an NFT
    function getRoyaltyAmount(uint256 tokenId, uint256 salePrice) public view returns (uint256) {
        address creator = owner();
        uint256 royaltyRate = royaltyRates[creator];

        // Calculate the royalty amount
        uint256 royaltyAmount = (salePrice * royaltyRate) / 10000;

        return royaltyAmount;
    }

    // Get the owner of an NFT
    function ownerOf(uint256 tokenId) public view returns (address) {
        for (address owner in nftOwners) {
            if (nftOwners[owner][tokenId]) {
                return owner;
            }
        }

        return address(0);
    }

    // Get the metadata for an NFT
    function tokenURI(uint256 tokenId) public view returns (string memory) {
        return nftMetadata[tokenId].uri;
    }
}

// Define the program in Solana
use solana_program::{
    account_info::{AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    pubkey::Pubkey,
};

entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Parse the instruction
    let instruction = Instruction::deserialize(instruction_data)?;

    match instruction {
        Instruction::Mint {
            owner,
            token_id,
            name,
            symbol,
            uri,
        } => mint(
            program_id,
            accounts,
            owner,
            token_id,
            name,
            symbol,
            uri,
        ),
        Instruction::Transfer {
            from,
            to,
            token_id,
        } => transfer(
            program_id,
            accounts,
            from,
            to,
            token_id,
        ),
        Instruction::UpdateRoyaltyRate {
            creator,
            new_rate,
        } => update_royalty_rate(
            program_id,
            accounts,
            creator,
            new_rate,
        ),
        Instruction::GetRoyaltyAmount {
            token_id,
            sale_price,
        } => get_royalty_amount(
            program_id,
            accounts,
            token_id,
            sale_price,
        ),
    }
}

// Define the instructions
enum Instruction {
    Mint {
        owner: Pubkey,
        token_id: u64,
        name: String,
        symbol: String,
        uri: String,
    },
    Transfer {
        from: Pubkey,
        to: Pubkey,
        token_id: u64,
    },
    UpdateRoyaltyRate {
        creator: Pubkey,
        new_rate: u16,
    },
    GetRoyaltyAmount {
        token_id: u64,
        sale_price: u64,
    },
}

impl Instruction {
    fn deserialize(data: &[u8]) -> ProgramResult<Self> {
        let instruction = u8::from_le_bytes([data[0]]);
        match instruction {
            0 => {
                let owner = Pubkey::new_from_bytes(&data[1..21])?;
                let token_id = u64::from_le_bytes([data[21..29]]);
                let name = String::from_utf8(data[29..].to_vec())?;
                let symbol = String::from_utf8(data[29 + name.len()..].to_vec())?;
                let uri = String::from_utf8(data[29 + name.len() + symbol.len()..].to_vec())?;

                Ok(Instruction::Mint {
                    owner,
                    token_id,
                    name,
                    symbol,
                    uri,
                })
            }
            1 => {
                let from = Pubkey::new_from_bytes(&data[1..21])?;
                let to = Pubkey::new_from_bytes(&data[21..41])?;
                let token_id = u64::from_le_bytes([data[41..49]]);

                Ok(Instruction::Transfer { from, to, token_id })
            }
            2 => {
                let creator = Pubkey::new_from_bytes(&data[1..21])?;
                let new_rate = u16::from_le_bytes([data[21..23]]);

                Ok(Instruction::UpdateRoyaltyRate {
                    creator,
                    new_rate,
                })
            }
            3 => {
                let token_id = u64::from_le_bytes([data[1..9]]);
                let sale_price = u64::from_le_bytes([data[9..17]]);

                Ok(Instruction::GetRoyaltyAmount {
                    token_id,
                    sale_price,
                })
            }
            _ => Err(ProgramError::InvalidInstructionData),
        }
    }
}

// Mint an NFT
fn mint(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    owner: Pubkey,
    token_id: u64,
    name: String,
    symbol: String,
    uri: String,
) -> ProgramResult {
    // Get the accounts
    let nft_account = &mut accounts[0];

    // Check if the NFT account is owned by the program
    if nft_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Mint the NFT
    let nft = SolanaNFT::new(owner, token_id, name, symbol, uri);
    nft.save(nft_account)?;

    Ok(())
}

// Transfer an NFT
fn transfer(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    from: Pubkey,
    to: Pubkey,
    token_id: u64,
) -> ProgramResult {
    // Get the accounts
    let nft_account = &mut accounts[0];
    let from_account = &mut accounts[1];
    let to_account = &mut accounts[2];

    // Check if the accounts are valid
    if nft_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Transfer the NFT
    let nft = SolanaNFT::load(nft_account)?;
    nft.transfer(from, to, token_id)?;

    Ok(())
}

// Update the royalty rate
fn update_royalty_rate(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    creator: Pubkey,
    new_rate: u16,
) -> ProgramResult {
    // Get the accounts
    let royalty_account = &mut accounts[0];

    // Check if the royalty account is owned by the program
    if royalty_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Update the royalty rate
    let royalty = Royalty::load(royalty_account)?;
