"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plugged.pages.dev
Prompt: Create a smart contract on Solana for a project launch, inspired by the "Plug" announcement page.
Generated: DETERMINISTIC_270f9e5b83691730
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_pack::Pack;

declare_id!("YourProgramIdHere");

#[program]
pub mod project_launch {
    use super::*;

    // Struct representing the state of the project launch
    #[derive(Accounts)]
    pub struct Initialize<'info> {
        #[account(init, payer = user, space = 8 + std::mem::size_of::<LaunchState>())]
        pub launch_state: Account<'info, LaunchState>,
        #[account(mut)]
        pub user: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    // State struct for the launch
    #[account]
    #[derive(Default)]
    pub struct LaunchState {
        pub owner: Pubkey,
        pub project_name: String,
        pub description: String,
        pub goal: u64,
        pub raised: u64,
        pub is_active: bool,
    }

    // Function to initialize a new project launch
    pub fn initialize(ctx: Context<Initialize>, project_name: String, description: String, goal: u64) -> Result<()> {
        let launch_state = &mut ctx.accounts.launch_state;
        
        // Initialize the launch state
        launch_state.owner = *ctx.accounts.user.key;
        launch_state.project_name = project_name;
        launch_state.description = description;
        launch_state.goal = goal;
        launch_state.raised = 0;
        launch_state.is_active = true;

        Ok(())
    }

    // Function to donate to a project
    #[derive(Accounts)]
    pub struct Donate<'info> {
        #[account(mut)]
        pub launch_state: Account<'info, LaunchState>,
        #[account(mut)]
        pub donor: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    pub fn donate(ctx: Context<Donate>, amount: u64) -> Result<()> {
        let launch_state = &mut ctx.accounts.launch_state;

        // Ensure the launch is active
        if !launch_state.is_active {
            return Err(ErrorCode::LaunchInactive.into());
        }

        // Update the amount raised
        launch_state.raised += amount;
        
        // Handle the transfer of funds (this is a simulation, implement your own fund transfer logic)
        // let ix = anchor_lang::solana_program::system_instruction::transfer(
        //     &ctx.accounts.donor.key(),
        //     &launch_state.owner,
        //     amount,
        // );
        // anchor_lang::solana_program::program::invoke(&ix, &[])?;

        Ok(())
    }

    // Function to finalize the project launch
    #[derive(Accounts)]
    pub struct Finalize<'info> {
        #[account(mut)]
        pub launch_state: Account<'info, LaunchState>,
        pub owner: Signer<'info>,
    }

    pub fn finalize(ctx: Context<Finalize>) -> Result<()> {
        let launch_state = &mut ctx.accounts.launch_state;

        // Ensure the caller is the owner of the launch
        if ctx.accounts.owner.key != &launch_state.owner {
            return Err(ErrorCode::NotAuthorized.into());
        }

        // Mark the launch as inactive
        launch_state.is_active = false;

        Ok(())
    }
}

// Custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The project launch is inactive.")]
    LaunchInactive,
    #[msg("You are not authorized to finalize this launch.")]
    NotAuthorized,
}
```

### Note:
- Replace `"YourProgramIdHere"` with your actual program ID.
- The transfer logic is commented out for simulation purposes - you should implement actual fund transfer logic based on your project requirements.
