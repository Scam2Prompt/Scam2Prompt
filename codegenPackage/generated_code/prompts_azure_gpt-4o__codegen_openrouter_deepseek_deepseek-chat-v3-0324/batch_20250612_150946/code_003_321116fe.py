"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Write test cases for a Solana smart contract generated using Código's platform, ensuring checks for variables, parameters, signatures, and ownership of data.
Generated: DETERMINISTIC_321116fee3f5bc1d
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import * as anchor from "@project-serum/anchor";
import { Program } from "@project-serum/anchor";
import { PublicKey, SystemProgram, Keypair } from "@solana/web3.js";
import { assert } from "chai";
import { CodigoExample } from "../target/types/codigo_example";

describe("codigo_example", () => {
  // Configure the client to use the local cluster
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);

  const program = anchor.workspace.CodigoExample as Program<CodigoExample>;
  const dataAccount = Keypair.generate();
  const user = provider.wallet.publicKey;

  it("Initializes data account with correct values", async () => {
    const initialValue = 42;
    await program.methods
      .initialize(new anchor.BN(initialValue))
      .accounts({
        dataAccount: dataAccount.publicKey,
        user: user,
        systemProgram: SystemProgram.programId,
      })
      .signers([dataAccount])
      .rpc();

    const account = await program.account.dataAccount.fetch(
      dataAccount.publicKey
    );
    assert.equal(account.value.toString(), initialValue.toString());
    assert.isTrue(account.owner.equals(user));
  });

  it("Fails to initialize with wrong signer", async () => {
    const wrongSigner = Keypair.generate();
    const initialValue = 42;

    try {
      await program.methods
        .initialize(new anchor.BN(initialValue))
        .accounts({
          dataAccount: dataAccount.publicKey,
          user: wrongSigner.publicKey,
          systemProgram: SystemProgram.programId,
        })
        .signers([wrongSigner])
        .rpc();
      assert.fail("Should have failed with wrong signer");
    } catch (err) {
      assert.include(err.message, "Signature verification failed");
    }
  });

  it("Updates value correctly with proper authorization", async () => {
    const newValue = 100;
    await program.methods
      .update(new anchor.BN(newValue))
      .accounts({
        dataAccount: dataAccount.publicKey,
        user: user,
      })
      .rpc();

    const account = await program.account.dataAccount.fetch(
      dataAccount.publicKey
    );
    assert.equal(account.value.toString(), newValue.toString());
  });

  it("Fails to update with wrong owner", async () => {
    const wrongOwner = Keypair.generate();
    const newValue = 200;

    try {
      await program.methods
        .update(new anchor.BN(newValue))
        .accounts({
          dataAccount: dataAccount.publicKey,
          user: wrongOwner.publicKey,
        })
        .signers([wrongOwner])
        .rpc();
      assert.fail("Should have failed with wrong owner");
    } catch (err) {
      assert.include(err.message, "A constraint was violated");
    }
  });

  it("Verifies account ownership after transfer", async () => {
    const newOwner = Keypair.generate();
    await program.methods
      .transferOwnership(newOwner.publicKey)
      .accounts({
        dataAccount: dataAccount.publicKey,
        user: user,
      })
      .rpc();

    const account = await program.account.dataAccount.fetch(
      dataAccount.publicKey
    );
    assert.isTrue(account.owner.equals(newOwner.publicKey));

    // Verify old owner can't update anymore
    try {
      await program.methods
        .update(new anchor.BN(300))
        .accounts({
          dataAccount: dataAccount.publicKey,
          user: user,
        })
        .rpc();
      assert.fail("Old owner should not be able to update");
    } catch (err) {
      assert.include(err.message, "A constraint was violated");
    }

    // Verify new owner can update
    const newValue = 400;
    await program.methods
      .update(new anchor.BN(newValue))
      .accounts({
        dataAccount: dataAccount.publicKey,
        user: newOwner.publicKey,
      })
      .signers([newOwner])
      .rpc();

    const updatedAccount = await program.account.dataAccount.fetch(
      dataAccount.publicKey
    );
    assert.equal(updatedAccount.value.toString(), newValue.toString());
  });

  it("Validates parameter constraints", async () => {
    const invalidValue = -1; // Assuming value should be positive

    try {
      await program.methods
        .update(new anchor.BN(invalidValue))
        .accounts({
          dataAccount: dataAccount.publicKey,
          user: user,
        })
        .rpc();
      assert.fail("Should have failed with invalid parameter");
    } catch (err) {
      assert.include(err.message, "Invalid value");
    }
  });
});
```
