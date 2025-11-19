"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Develop a smart contract that allows coin holders to loan or stake their tokens quarterly, representing electricity available for miners, as per eosGAS's staking mechanism.
Generated: DETERMINISTIC_3bab38002b1ad462
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <eosiolib/eosio.hpp>
#include <eosiolib/asset.hpp>
#include <eosiolib/time.hpp>

using namespace eosio;

class [[eosio::contract]] eosgas : public contract {
  public:
    using contract::contract;

    // Action to stake tokens
    [[eosio::action]] void stake( name account, asset quantity ) {
      // Check if account and quantity are valid
      eosio_assert( quantity.amount > 0, "Quantity must be greater than 0" );
      eosio_assert( has_auth( account ), "Account must be the same as the one authorizing the action" );

      // Get the staked balance for the account
      auto staked = staked_balance( account );
      
      // Add the new stake to the existing balance
      staked += quantity;

      // Update the staked balance
      _staked_balance[ account ] = staked;

      // Transfer tokens from account to contract
      transfer( account, get_self(), quantity );
    }

    // Action to unstake tokens
    [[eosio::action]] void unstake( name account, asset quantity ) {
      // Check if account and quantity are valid
      eosio_assert( quantity.amount > 0, "Quantity must be greater than 0" );
      eosio_assert( has_auth( account ), "Account must be the same as the one authorizing the action" );

      // Get the staked balance for the account
      auto staked = _staked_balance[ account ];

      // Check if account has sufficient staked balance
      eosio_assert( staked >= quantity, "Insufficient staked balance" );

      // Subtract the unstaked quantity from the existing balance
      staked -= quantity;

      // Update the staked balance
      _staked_balance[ account ] = staked;

      // Transfer tokens from contract to account
      transfer( get_self(), account, quantity );
    }

    // Action to loan tokens
    [[eosio::action]] void loan( name account, asset quantity, name miner ) {
      // Check if account, quantity and miner are valid
      eosio_assert( quantity.amount > 0, "Quantity must be greater than 0" );
      eosio_assert( has_auth( account ), "Account must be the same as the one authorizing the action" );
      eosio_assert( miner != account, "Miner cannot be the same as the lender" );

      // Get the available loan balance for the account
      auto available_loan = available_loan_balance( account );

      // Add the new loan to the existing balance
      available_loan += quantity;

      // Update the available loan balance
      _available_loan_balance[ account ] = available_loan;

      // Transfer tokens from account to contract
      transfer( account, get_self(), quantity );

      // Notify the miner about the loan
      // action( "notify", { {account, miner} }, {{"quantity", quantity}} );
    }

    // Action to repay loan
    [[eosio::action]] void repay( name miner, asset quantity ) {
      // Check if quantity is valid
      eosio_assert( quantity.amount > 0, "Quantity must be greater than 0" );

      // Get the loan balance for the miner
      auto loan_balance = _loan_balance[ miner ];

      // Check if miner has a loan
      eosio_assert( loan_balance > 0, "Miner has no loan" );

      // Subtract the repaid quantity from the existing loan balance
      loan_balance -= quantity;

      // Update the loan balance
      _loan_balance[ miner ] = loan_balance;

      // Transfer tokens from miner to contract
      transfer( miner, get_self(), quantity );
    }

  private:
    // Table to store staked balances
    struct [[eosio::table]] staked_balance_table {
      name primary_key;
      asset staked;
    };

    // Table to store available loan balances
    struct [[eosio::table]] available_loan_balance_table {
      name primary_key;
      asset available_loan;
    };

    // Table to store loan balances
    struct [[eosio::table]] loan_balance_table {
      name primary_key;
      asset loan;
    };

    // Multi-index for staked balance table
    typedef eosio::multi_index< "staked", staked_balance_table > staked_balance_idx;

    // Multi-index for available loan balance table
    typedef eosio::multi_index< "available", available_loan_balance_table > available_loan_balance_idx;

    // Multi-index for loan balance table
    typedef eosio::multi_index< "loan", loan_balance_table > loan_balance_idx;

    // Get staked balance for an account
    asset staked_balance( name account ) {
      staked_balance_idx staked_tbl( get_self(), get_self() );
      auto itr = staked_tbl.find( account );
      if ( itr == staked_tbl.end() ) {
        return asset( 0, "EOS" );
      }
      return itr->staked;
    }

    // Get available loan balance for an account
    asset available_loan_balance( name account ) {
      available_loan_balance_idx available_tbl( get_self(), get_self() );
      auto itr = available_tbl.find( account );
      if ( itr == available_tbl.end() ) {
        return asset( 0, "EOS" );
      }
      return itr->available_loan;
    }

    // Data members
    staked_balance_idx _staked_balance;
    available_loan_balance_idx _available_loan_balance;
    loan_balance_idx _loan_balance;
};

EOSIO_DISPATCH( eosgas, (stake)(unstake)(loan)(repay) )
```
