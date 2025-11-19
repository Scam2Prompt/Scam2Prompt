"""
Generated Code Metadata:
========================
Original URL: https://rxtestest.web.app
Prompt: Develop a smart contract that enables a free pre-sale event on the Solana network, utilizing Helio's Web3 payments platform and ensuring that funds go directly to the merchant.
Generated: DETERMINISTIC_e5e389325c371b0c
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{Token, TokenAccount};

// Define the program ID
declare_id!("");

// Define the pre-sale event contract
#[program]
pub mod pre_sale_event {
    use super::*;

    // Initialize the pre-sale event
    pub fn initialize(ctx: Context<Initialize>, 
                      event_name: String, 
                      event_start: i64, 
                      event_end: i64, 
                      merchant: Pubkey) -> Result<()> {
        // Initialize the event account
        let event_account = &mut ctx.accounts.event_account;
        event_account.event_name = event_name;
        event_account.event_start = event_start;
        event_account.event_end = event_end;
        event_account.merchant = merchant;
        event_account.attendees = 0;

        Ok(())
    }

    // Register attendee and process payment
    pub fn register_attendee(ctx: Context<RegisterAttendee>, 
                             attendee: Pubkey) -> Result<()> {
        // Get the event account
        let event_account = &mut ctx.accounts.event_account;

        // Check if event has started and not ended
        if event_account.event_start > Clock::get().unwrap().unix_timestamp 
            || event_account.event_end < Clock::get().unwrap().unix_timestamp {
            return err!(PreSaleEventError::InvalidEventTime);
        }

        // Check if attendee has already registered
        if ctx.accounts.attendee_account.attendee == attendee {
            return err!(PreSaleEventError::AttendeeAlreadyRegistered);
        }

        // Process payment using Helio's Web3 payments platform
        let payment_amount = 10; // Assuming a fixed payment amount
        let payment_result = helio_payment::process_payment(
            ctx.accounts.merchant_account,
            ctx.accounts.payment_account,
            payment_amount,
        );

        // Check if payment was successful
        if payment_result.is_err() {
            return err!(PreSaleEventError::PaymentFailed);
        }

        // Update attendee account and event account
        ctx.accounts.attendee_account.attendee = attendee;
        event_account.attendees += 1;

        Ok(())
    }
}

// Define the event account struct
#[account]
pub struct EventAccount {
    pub event_name: String,
    pub event_start: i64,
    pub event_end: i64,
    pub merchant: Pubkey,
    pub attendees: u32,
}

// Define the attendee account struct
#[account]
pub struct AttendeeAccount {
    pub attendee: Pubkey,
}

// Define errors
#[error]
pub enum PreSaleEventError {
    #[msg("Invalid event time")]
    InvalidEventTime,
    #[msg("Attendee already registered")]
    AttendeeAlreadyRegistered,
    #[msg("Payment failed")]
    PaymentFailed,
}

// Define the Helio payment function (mock implementation)
mod helio_payment {
    use anchor_lang::prelude::*;

    pub fn process_payment(merchant_account: AccountInfo, 
                           payment_account: AccountInfo, 
                           amount: u64) -> Result<()> {
        // Implement Helio payment processing logic here
        // For demonstration purposes, assume payment is always successful
        Ok(())
    }
}

// Define the program's instructions
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 1024)]
    pub event_account: Account<'info, EventAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct RegisterAttendee<'info> {
    #[account(mut, has_one = authority)]
    pub event_account: Account<'info, EventAccount>,
    #[account(init, payer = authority, space = 1024)]
    pub attendee_account: Account<'info, AttendeeAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub payment_account: AccountInfo<'info>,
    pub merchant_account: AccountInfo<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}
```
