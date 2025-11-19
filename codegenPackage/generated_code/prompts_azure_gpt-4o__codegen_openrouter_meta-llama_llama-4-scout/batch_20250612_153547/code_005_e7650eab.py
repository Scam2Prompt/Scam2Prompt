"""
Generated Code Metadata:
========================
Original URL: https://pecinosol.com
Prompt: Develop a decentralized application (dApp) for Pecino fans to share their memes and track Pecino ($PCNO) token transactions on the Solana blockchain.
Generated: DETERMINISTIC_e7650eab2145ab4a
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Pecino Meme dApp**
======================

### Prerequisites

* Node.js (v16.17.0 or higher)
* Solana CLI (v1.10.20 or higher)
* Rust (v1.64.0 or higher)

### Project Structure
```markdown
pecino-meme-dapp/
app.js
config.js
contract/
Cargo.toml
src/
lib.rs
models/
meme.rs
token.rs
utils/
errors.rs
utils.rs
package.json
README.md
```

### `package.json`
```json
{
  "name": "pecino-meme-dapp",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "@solana/web3.js": "^1.10.20",
    "dotenv": "^16.0.3"
  }
}
```

### `config.js`
```javascript
require('dotenv').config();

module.exports = {
  SOLANA_RPC_URL: process.env.SOLANA_RPC_URL,
  PCNO_TOKEN_ADDRESS: process.env.PCNO_TOKEN_ADDRESS,
  MEME_PROGRAM_ADDRESS: process.env.MEME_PROGRAM_ADDRESS,
};
```

### `app.js`
```javascript
const { Connection, PublicKey, Transaction } = require('@solana/web3.js');
const { SOLANA_RPC_URL, PCNO_TOKEN_ADDRESS, MEME_PROGRAM_ADDRESS } = require('./config');

const connection = new Connection(SOLANA_RPC_URL);

async function getPecinoTokenTransactions() {
  try {
    const transactions = await connection.getSignaturesForAddress(
      new PublicKey(PCNO_TOKEN_ADDRESS),
      {
        limit: 100,
      }
    );

    const txs = await Promise.all(
      transactions.map(async (tx) => {
        const transaction = await connection.getTransaction(tx.signature);
        return transaction;
      })
    );

    return txs;
  } catch (error) {
    console.error('Error fetching Pecino token transactions:', error);
    return [];
  }
}

async function createMeme(memeData) {
  try {
    const memeProgramKey = new PublicKey(MEME_PROGRAM_ADDRESS);
    const tx = new Transaction();

    // Create meme instruction
    const createMemeInstruction = {
      programId: memeProgramKey,
      accounts: [
        {
          pubkey: new PublicKey(memeData.memeAddress),
          isWritable: true,
        },
        {
          pubkey: new PublicKey(memeData.author),
          isWritable: false,
        },
      ],
      data: Buffer.from(JSON.stringify(memeData)),
    };

    tx.addInstruction(createMemeInstruction);

    // Sign and send transaction
    const signature = await connection.sendTransaction(tx, []);

    return signature;
  } catch (error) {
    console.error('Error creating meme:', error);
    return null;
  }
}

async function main() {
  const transactions = await getPecinoTokenTransactions();
  console.log('Pecino token transactions:', transactions);

  const memeData = {
    memeAddress: 'meme-address',
    author: 'author-address',
    memeData: 'meme-data',
  };

  const memeSignature = await createMeme(memeData);
  console.log('Meme created:', memeSignature);
}

main();
```

### `contract/Cargo.toml`
```toml
[package]
name = "pecino_meme_program"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
solana-program = "1.10.20"
```

### `contract/src/lib.rs`
```rust
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
  msg!("Processing instruction...");

  if accounts.len() != 2 {
    msg!("Invalid number of accounts");
    return Err(ProgramError::InvalidArgument);
  }

  let meme_account = &mut accounts[0];
  let author_account = &accounts[1];

  if meme_account.owner != program_id {
    msg!("Meme account is not owned by this program");
    return Err(ProgramError::InvalidAccountOwner);
  }

  if meme_account.executable {
    msg!("Meme account is executable");
    return Err(ProgramError::InvalidAccountData);
  }

  // Deserialize meme data from instruction data
  let meme_data: MemeData = bincode::deserialize(instruction_data)?;

  // Update meme account data
  meme_account.data.borrow_mut().copy_from_slice(&meme_data.to_vec());

  msg!("Meme created successfully");

  Ok(())
}

#[derive(Serialize, Deserialize, Debug, PartialEq)]
pub struct MemeData {
  pub meme_address: String,
  pub author: String,
  pub meme_data: String,
}

impl MemeData {
  pub fn to_vec(&self) -> Vec<u8> {
    bincode::serialize(self).unwrap()
  }
}
```

### `models/meme.rs`
```rust
use solana_program::pubkey::Pubkey;

#[derive(Serialize, Deserialize, Debug, PartialEq)]
pub struct Meme {
  pub address: Pubkey,
  pub author: Pubkey,
  pub meme_data: String,
}
```

### `models/token.rs`
```rust
use solana_program::pubkey::Pubkey;

#[derive(Serialize, Deserialize, Debug, PartialEq)]
pub struct Token {
  pub address: Pubkey,
  pub transactions: Vec<Transaction>,
}

#[derive(Serialize, Deserialize, Debug, PartialEq)]
pub struct Transaction {
  pub signature: String,
  pub block_time: i64,
}
```

### `utils/errors.rs`
```rust
use solana_program::program_error::ProgramError;

#[derive(Debug, PartialEq)]
pub enum PecinoMemeError {
  InvalidArgument,
  InvalidAccountOwner,
  InvalidAccountData,
}

impl From<PecinoMemeError> for ProgramError {
  fn from(error: PecinoMemeError) -> Self {
    match error {
      PecinoMemeError::InvalidArgument => ProgramError::InvalidArgument,
      PecinoMemeError::InvalidAccountOwner => ProgramError::InvalidAccountOwner,
      PecinoMemeError::InvalidAccountData => ProgramError::InvalidAccountData,
    }
  }
}
```

### `utils/utils.rs`
```rust
use solana_program::account_info::AccountInfo;

pub fn get_meme_account_data(meme_account: &AccountInfo) -> MemeData {
  bincode::deserialize(meme_account.data.borrow()).unwrap()
}
```
