"""
Generated Code Metadata:
========================
Original URL: https://sui-dapps.vercel.app
Prompt: Using the Sui Typescript SDK, write a code snippet to create a blockchain-based loyalty program for commerce applications.
Generated: DETERMINISTIC_f0e57c3e2ca14092
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required modules from Sui Typescript SDK
import { SuiClient, Keypair, JsonRpcProvider, LocalnetConfig } from "@sui/client";
import { Ed25519Keypair } from "@sui/cryptography";

// Set up localnet configuration
const config = new LocalnetConfig();
const provider = new JsonRpcProvider(config);

// Create a new Sui client
const suiClient = new SuiClient(provider);

// Define the LoyaltyProgram object
interface LoyaltyProgram {
  id: string;
  name: string;
  description: string;
  rewards: { [key: string]: number };
}

// Define the User object
interface User {
  id: string;
  address: string;
  balance: number;
  loyaltyPrograms: { [key: string]: number };
}

// Create a new keypair for the loyalty program
const keypair: Ed25519Keypair = new Ed25519Keypair();
const programAddress = keypair.getPublicKey().toString();

// Initialize the loyalty program
async function createLoyaltyProgram(
  name: string,
  description: string,
  rewards: { [key: string]: number }
): Promise<LoyaltyProgram> {
  try {
    // Create a new loyalty program object
    const loyaltyProgram: LoyaltyProgram = {
      id: suiClient.getAddress().toString(),
      name,
      description,
      rewards,
    };

    // Publish the loyalty program on the blockchain
    const tx = await suiClient.publish({
      packageObject: {
        // Assume the package object ID is known
        id: "0x1234567890",
      },
      modules: [
        {
          // Assume the module name is known
          name: "LoyaltyProgram",
          code: `
            // Define the loyalty program module
            module ${programAddress}::loyalty_program {
              use sui::object::{Self, UID};
              use sui::transfer;
              use sui::coin::{Self, Coin};

              struct LoyaltyProgram has key, store {
                id: UID,
                name: string,
                description: string,
                rewards: map<string, u64>,
              }

              fun create_loyalty_program(
                ctx: &mut TxContext,
                name: string,
                description: string,
                rewards: map<string, u64>,
              ): LoyaltyProgram {
                let loyalty_program = LoyaltyProgram {
                  id: UID::new(ctx),
                  name,
                  description,
                  rewards,
                };
                transfer::transfer(loyalty_program, ctx.sender());
                loyalty_program
              }
            }
          `,
        },
      ],
      dependencies: [],
    });

    // Wait for the transaction to complete
    await suiClient.waitForTransaction(tx.digest);

    return loyaltyProgram;
  } catch (error) {
    console.error("Error creating loyalty program:", error);
    throw error;
  }
}

// Create a new user
async function createUser(address: string, balance: number): Promise<User> {
  try {
    // Create a new user object
    const user: User = {
      id: suiClient.getAddress().toString(),
      address,
      balance,
      loyaltyPrograms: {},
    };

    // Create a new coin object for the user
    const coin = await suiClient.createCoin({
      owner: address,
      amount: balance,
    });

    // Wait for the transaction to complete
    await suiClient.waitForTransaction(coin.digest);

    return user;
  } catch (error) {
    console.error("Error creating user:", error);
    throw error;
  }
}

// Enroll a user in a loyalty program
async function enrollUserInLoyaltyProgram(
  userId: string,
  loyaltyProgramId: string
): Promise<void> {
  try {
    // Get the user's loyalty programs
    const user = await suiClient.getObject<User>(userId);

    // Get the loyalty program
    const loyaltyProgram = await suiClient.getObject<LoyaltyProgram>(
      loyaltyProgramId
    );

    // Add the loyalty program to the user's loyalty programs
    user.loyaltyPrograms[loyaltyProgramId] = 0;

    // Update the user's object
    await suiClient.updateObject({
      objectId: userId,
      fields: {
        loyaltyPrograms: user.loyaltyPrograms,
      },
    });
  } catch (error) {
    console.error("Error enrolling user in loyalty program:", error);
    throw error;
  }
}

// Example usage
async function main() {
  // Create a new loyalty program
  const loyaltyProgram = await createLoyaltyProgram(
    "Example Loyalty Program",
    "This is an example loyalty program",
    { "reward-1": 10, "reward-2": 20 }
  );

  // Create a new user
  const user = await createUser(
    "0x1234567890",
    100
  );

  // Enroll the user in the loyalty program
  await enrollUserInLoyaltyProgram(user.id, loyaltyProgram.id);
}

main().catch((error) => console.error("Error:", error));
```
