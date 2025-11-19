"""
Generated Code Metadata:
========================
Original URL: https://nearfans.com
Prompt: Generate a smart contract code for a NEAR-based project that utilizes decentralized governance and open-source principles.
Generated: DETERMINISTIC_ed626d7bc9b9fee5
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A smart contract for decentralized governance on NEAR protocol.
//! Allows token holders to propose, vote on, and execute governance actions.

use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::collections::{LookupMap, UnorderedSet};
use near_sdk::json_types::{U128, U64};
use near_sdk::{
    env, near_bindgen, AccountId, Balance, BorshStorageKey, PanicOnDefault, Promise, PromiseOrValue,
};
use std::collections::HashMap;

// Constants
const MIN_PROPOSAL_DEPOSIT: Balance = 10_000_000_000_000_000_000_000; // 10 NEAR
const VOTING_PERIOD: u64 = 7 * 24 * 60 * 60 * 1_000_000_000; // 7 days in nanoseconds
const EXECUTION_DELAY: u64 = 1 * 24 * 60 * 60 * 1_000_000_000; // 1 day in nanoseconds
const QUORUM_THRESHOLD: u128 = 30_000; // 30% of total supply
const APPROVAL_THRESHOLD: u128 = 50_000; // 50% of votes

#[derive(BorshSerialize, BorshStorageKey)]
enum StorageKey {
    Proposals,
    Votes,
    Voters,
    Members,
}

#[derive(BorshSerialize, BorshDeserialize)]
pub enum ProposalType {
    TransferFunds { recipient: AccountId, amount: U128 },
    ChangeCode { hash: String },
    AddMember { account_id: AccountId },
    RemoveMember { account_id: AccountId },
}

#[derive(BorshSerialize, BorshDeserialize)]
pub struct Proposal {
    id: u64,
    proposer: AccountId,
    proposal_type: ProposalType,
    description: String,
    deposit: Balance,
    start_time: u64,
    end_time: u64,
    executed: bool,
    votes_for: Balance,
    votes_against: Balance,
}

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct GovernanceContract {
    owner: AccountId,
    token_contract: AccountId,
    total_supply: Balance,
    proposals: LookupMap<u64, Proposal>,
    proposal_ids: UnorderedSet<u64>,
    votes: LookupMap<u64, HashMap<AccountId, bool>>,
    members: UnorderedSet<AccountId>,
}

#[near_bindgen]
impl GovernanceContract {
    #[init]
    pub fn new(owner: AccountId, token_contract: AccountId) -> Self {
        assert!(!env::state_exists(), "Contract is already initialized");
        Self {
            owner,
            token_contract,
            total_supply: 0,
            proposals: LookupMap::new(StorageKey::Proposals),
            proposal_ids: UnorderedSet::new(StorageKey::Proposals),
            votes: LookupMap::new(StorageKey::Votes),
            members: UnorderedSet::new(StorageKey::Members),
        }
    }

    /// Update total token supply (should be called by token contract)
    pub fn update_total_supply(&mut self, supply: U128) {
        assert_eq!(
            env::predecessor_account_id(),
            self.token_contract,
            "Only token contract can update supply"
        );
        self.total_supply = supply.into();
    }

    /// Create a new governance proposal
    #[payable]
    pub fn create_proposal(
        &mut self,
        proposal_type: ProposalType,
        description: String,
    ) -> u64 {
        let deposit = env::attached_deposit();
        assert!(deposit >= MIN_PROPOSAL_DEPOSIT, "Deposit too small");

        let proposer = env::predecessor_account_id();
        let id = self.proposal_ids.len() + 1;
        let now = env::block_timestamp();

        let proposal = Proposal {
            id,
            proposer: proposer.clone(),
            proposal_type,
            description,
            deposit,
            start_time: now,
            end_time: now + VOTING_PERIOD,
            executed: false,
            votes_for: 0,
            votes_against: 0,
        };

        self.proposals.insert(&id, &proposal);
        self.proposal_ids.insert(&id);

        id
    }

    /// Vote on a proposal
    pub fn vote(&mut self, proposal_id: u64, vote_for: bool) {
        let voter = env::predecessor_account_id();
        let mut proposal = self.proposals.get(&proposal_id).expect("Proposal not found");

        assert!(
            env::block_timestamp() < proposal.end_time,
            "Voting period ended"
        );
        assert!(!proposal.executed, "Proposal already executed");

        let votes = self.votes.get(&proposal_id).unwrap_or_default();
        assert!(!votes.contains_key(&voter), "Already voted");

        let voter_balance = self.get_voter_balance(&voter);

        if vote_for {
            proposal.votes_for += voter_balance;
        } else {
            proposal.votes_against += voter_balance;
        }

        let mut new_votes = votes;
        new_votes.insert(voter, vote_for);

        self.votes.insert(&proposal_id, &new_votes);
        self.proposals.insert(&proposal_id, &proposal);
    }

    /// Execute a proposal that has passed
    pub fn execute_proposal(&mut self, proposal_id: u64) -> PromiseOrValue<String> {
        let mut proposal = self.proposals.get(&proposal_id).expect("Proposal not found");
        let now = env::block_timestamp();

        assert!(
            now > proposal.end_time && now < proposal.end_time + EXECUTION_DELAY,
            "Not in execution window"
        );
        assert!(!proposal.executed, "Proposal already executed");

        let total_votes = proposal.votes_for + proposal.votes_against;
        let quorum = (total_votes * 100_000) / self.total_supply;
        let approval = (proposal.votes_for * 100_000) / total_votes;

        assert!(quorum >= QUORUM_THRESHOLD, "Quorum not met");
        assert!(approval >= APPROVAL_THRESHOLD, "Approval threshold not met");

        proposal.executed = true;
        self.proposals.insert(&proposal_id, &proposal);

        match &proposal.proposal_type {
            ProposalType::TransferFunds { recipient, amount } => {
                let amount: Balance = amount.into();
                Promise::new(recipient.clone()).transfer(amount).into()
            }
            ProposalType::ChangeCode { hash } => {
                Promise::new(env::current_account_id())
                    .deploy_contract(hash.as_bytes().to_vec())
                    .into()
            }
            ProposalType::AddMember { account_id } => {
                self.members.insert(account_id);
                PromiseOrValue::Value("Member added".to_string())
            }
            ProposalType::RemoveMember { account_id } => {
                self.members.remove(account_id);
                PromiseOrValue::Value("Member removed".to_string())
            }
        }
    }

    /// Get voter's token balance (would call into token contract in production)
    fn get_voter_balance(&self, voter: &AccountId) -> Balance {
        // In production, this would make a cross-contract call to token contract
        // For demo purposes, we return a fixed value
        100_000_000_000_000_000_000_000 // 100 NEAR
    }

    /// View method to get proposal details
    pub fn get_proposal(&self, proposal_id: u64) -> Option<Proposal> {
        self.proposals.get(&proposal_id)
    }

    /// View method to check if account is member
    pub fn is_member(&self, account_id: AccountId) -> bool {
        self.members.contains(&account_id)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use near_sdk::test_utils::{accounts, VMContextBuilder};
    use near_sdk::{testing_env, MockedBlockchain};

    fn get_context(predecessor: AccountId) -> VMContextBuilder {
        let mut builder = VMContextBuilder::new();
        builder
            .current_account_id(accounts(0))
            .signer_account_id(predecessor.clone())
            .predecessor_account_id(predecessor);
        builder
    }

    #[test]
    fn test_create_proposal() {
        let owner = accounts(0);
        let token_contract = accounts(1);
        let mut context = get_context(owner.clone());
        testing_env!(context.build());

        let mut contract = GovernanceContract::new(owner.clone(), token_contract.clone());
        contract.update_total_supply(U128(1_000_000_000_000_000_000_000_000)); // 1M NE
