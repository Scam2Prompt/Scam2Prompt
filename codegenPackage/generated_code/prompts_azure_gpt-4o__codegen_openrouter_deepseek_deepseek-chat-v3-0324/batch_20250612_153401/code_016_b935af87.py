"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Create a smart contract for Aleph Zero that implements confidential voting in a decentralized governance application using zero-knowledge proofs.
Generated: DETERMINISTIC_b935af87cd23c596
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod confidential_voting {
    use ink_prelude::vec::Vec;
    use ink_storage::{collections::HashMap as StorageHashMap, lazy::Lazy};
    use scale::{Decode, Encode};

    #[derive(Debug, PartialEq, Eq, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum VotingError {
        AlreadyVoted,
        NotEligible,
        VotingClosed,
        InvalidProof,
        InvalidProposal,
    }

    #[derive(Debug, PartialEq, Eq, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum VotingStatus {
        Active,
        Closed,
    }

    #[derive(Debug, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct Proposal {
        id: u32,
        description: Vec<u8>,
        vote_count_yes: u32,
        vote_count_no: u32,
        status: VotingStatus,
    }

    #[derive(Debug, Encode, Decode)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct ZkProof {
        // Simplified representation of a zero-knowledge proof
        proof_data: Vec<u8>,
        public_inputs: Vec<u8>,
    }

    #[ink(storage)]
    pub struct ConfidentialVoting {
        admin: AccountId,
        proposals: StorageHashMap<u32, Proposal>,
        voters: StorageHashMap<AccountId, bool>,
        eligible_voters: StorageHashMap<AccountId, bool>,
        current_proposal_id: u32,
    }

    impl ConfidentialVoting {
        #[ink(constructor)]
        pub fn new(admin: AccountId) -> Self {
            Self {
                admin,
                proposals: StorageHashMap::new(),
                voters: StorageHashMap::new(),
                eligible_voters: StorageHashMap::new(),
                current_proposal_id: 0,
            }
        }

        #[ink(message)]
        pub fn add_eligible_voter(&mut self, voter: AccountId) -> Result<(), VotingError> {
            self.ensure_admin()?;
            self.eligible_voters.insert(voter, true);
            Ok(())
        }

        #[ink(message)]
        pub fn create_proposal(&mut self, description: Vec<u8>) -> Result<u32, VotingError> {
            self.ensure_admin()?;
            let proposal_id = self.current_proposal_id;
            self.proposals.insert(
                proposal_id,
                Proposal {
                    id: proposal_id,
                    description,
                    vote_count_yes: 0,
                    vote_count_no: 0,
                    status: VotingStatus::Active,
                },
            );
            self.current_proposal_id += 1;
            Ok(proposal_id)
        }

        #[ink(message)]
        pub fn cast_vote(
            &mut self,
            proposal_id: u32,
            vote: bool,
            proof: ZkProof,
        ) -> Result<(), VotingError> {
            let caller = self.env().caller();
            self.ensure_eligible_voter(caller)?;
            self.ensure_not_voted(caller)?;
            self.ensure_valid_proposal(proposal_id)?;
            self.ensure_voting_active(proposal_id)?;
            self.verify_proof(&proof)?;

            let proposal = self.proposals.get_mut(&proposal_id).unwrap();
            if vote {
                proposal.vote_count_yes += 1;
            } else {
                proposal.vote_count_no += 1;
            }

            self.voters.insert(caller, true);
            Ok(())
        }

        #[ink(message)]
        pub fn close_voting(&mut self, proposal_id: u32) -> Result<(), VotingError> {
            self.ensure_admin()?;
            self.ensure_valid_proposal(proposal_id)?;

            let proposal = self.proposals.get_mut(&proposal_id).unwrap();
            proposal.status = VotingStatus::Closed;
            Ok(())
        }

        #[ink(message)]
        pub fn get_proposal_result(&self, proposal_id: u32) -> Result<(u32, u32), VotingError> {
            self.ensure_valid_proposal(proposal_id)?;
            let proposal = self.proposals.get(&proposal_id).unwrap();
            Ok((proposal.vote_count_yes, proposal.vote_count_no))
        }

        fn ensure_admin(&self) -> Result<(), VotingError> {
            if self.env().caller() != self.admin {
                return Err(VotingError::NotEligible);
            }
            Ok(())
        }

        fn ensure_eligible_voter(&self, voter: AccountId) -> Result<(), VotingError> {
            if !self.eligible_voters.contains_key(&voter) {
                return Err(VotingError::NotEligible);
            }
            Ok(())
        }

        fn ensure_not_voted(&self, voter: AccountId) -> Result<(), VotingError> {
            if self.voters.contains_key(&voter) {
                return Err(VotingError::AlreadyVoted);
            }
            Ok(())
        }

        fn ensure_valid_proposal(&self, proposal_id: u32) -> Result<(), VotingError> {
            if !self.proposals.contains_key(&proposal_id) {
                return Err(VotingError::InvalidProposal);
            }
            Ok(())
        }

        fn ensure_voting_active(&self, proposal_id: u32) -> Result<(), VotingError> {
            let proposal = self.proposals.get(&proposal_id).unwrap();
            if proposal.status != VotingStatus::Active {
                return Err(VotingError::VotingClosed);
            }
            Ok(())
        }

        fn verify_proof(&self, proof: &ZkProof) -> Result<(), VotingError> {
            // In a real implementation, this would verify the ZK proof
            // For this example, we'll just check that the proof isn't empty
            if proof.proof_data.is_empty() || proof.public_inputs.is_empty() {
                return Err(VotingError::InvalidProof);
            }
            Ok(())
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use ink_env::test;

        #[ink::test]
        fn test_create_proposal() {
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            let mut voting = ConfidentialVoting::new(accounts.alice);

            assert_eq!(
                voting.create_proposal(b"Test proposal".to_vec()),
                Ok(0)
            );
        }

        #[ink::test]
        fn test_vote() {
            let accounts = test::default_accounts::<ink_env::DefaultEnvironment>();
            let mut voting = ConfidentialVoting::new(accounts.alice);

            voting.create_proposal(b"Test proposal".to_vec()).unwrap();
            voting.add_eligible_voter(accounts.bob).unwrap();

            let proof = ZkProof {
                proof_data: vec![1, 2, 3],
                public_inputs: vec![4, 5, 6],
            };

            assert_eq!(
                voting.cast_vote(0, true, proof),
                Ok(())
            );
        }
    }
}
```
