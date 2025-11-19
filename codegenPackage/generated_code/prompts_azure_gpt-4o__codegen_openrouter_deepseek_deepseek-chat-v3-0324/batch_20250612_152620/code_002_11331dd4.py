"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Generate Rust code for implementing a staking mechanism for NFT holders, where staking rewards are distributed via airdrops, as outlined in the Meta Rebelz roadmap.
Generated: DETERMINISTIC_11331dd44c3c5326
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};

// Error types for staking operations
#[derive(Debug)]
pub enum StakingError {
    AlreadyStaked,
    NotStaked,
    InvalidDuration,
    InsufficientBalance,
    AirdropFailed,
}

// Represents an NFT with owner and metadata
#[derive(Debug, Clone)]
pub struct NFT {
    pub id: u64,
    pub owner: String,
    pub metadata: String,
}

// Represents a staking position
#[derive(Debug, Clone)]
pub struct StakingPosition {
    pub nft_id: u64,
    pub staker: String,
    pub staked_at: u64,
    pub duration: u64, // in seconds
    pub claimed_rewards: u64,
}

// Main staking contract
pub struct NFTStakingContract {
    pub staked_nfts: HashMap<u64, StakingPosition>,
    pub reward_rate: f64, // rewards per second per NFT
    pub total_rewards_distributed: u64,
}

impl NFTStakingContract {
    /// Creates a new staking contract with given reward rate
    pub fn new(reward_rate: f64) -> Self {
        NFTStakingContract {
            staked_nfts: HashMap::new(),
            reward_rate,
            total_rewards_distributed: 0,
        }
    }

    /// Stake an NFT for a given duration
    pub fn stake(&mut self, nft: NFT, duration: u64) -> Result<(), StakingError> {
        if duration == 0 {
            return Err(StakingError::InvalidDuration);
        }

        if self.staked_nfts.contains_key(&nft.id) {
            return Err(StakingError::AlreadyStaked);
        }

        let current_time = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();

        let position = StakingPosition {
            nft_id: nft.id,
            staker: nft.owner,
            staked_at: current_time,
            duration,
            claimed_rewards: 0,
        };

        self.staked_nfts.insert(nft.id, position);
        Ok(())
    }

    /// Unstake an NFT and claim rewards
    pub fn unstake(&mut self, nft_id: u64) -> Result<u64, StakingError> {
        let position = self.staked_nfts.get(&nft_id).ok_or(StakingError::NotStaked)?;

        let current_time = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();

        // Calculate rewards
        let staked_time = current_time - position.staked_at;
        let effective_duration = std::cmp::min(staked_time, position.duration);
        let rewards = (effective_duration as f64 * self.reward_rate) as u64;

        // Remove from staked NFTs
        self.staked_nfts.remove(&nft_id);
        self.total_rewards_distributed += rewards;

        Ok(rewards)
    }

    /// Calculate current pending rewards for an NFT
    pub fn calculate_rewards(&self, nft_id: u64) -> Result<u64, StakingError> {
        let position = self.staked_nfts.get(&nft_id).ok_or(StakingError::NotStaked)?;

        let current_time = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();

        let staked_time = current_time - position.staked_at;
        let effective_duration = std::cmp::min(staked_time, position.duration);
        let rewards = (effective_duration as f64 * self.reward_rate) as u64;

        Ok(rewards - position.claimed_rewards)
    }

    /// Airdrop rewards to all stakers
    pub fn airdrop_rewards(&mut self) -> Result<u64, StakingError> {
        let current_time = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();

        let mut total_distributed = 0;

        for (_, position) in self.staked_nfts.iter_mut() {
            let staked_time = current_time - position.staked_at;
            let effective_duration = std::cmp::min(staked_time, position.duration);
            let rewards = (effective_duration as f64 * self.reward_rate) as u64;
            let pending_rewards = rewards - position.claimed_rewards;

            if pending_rewards > 0 {
                // In a real implementation, this would transfer tokens to the staker
                position.claimed_rewards = rewards;
                total_distributed += pending_rewards;
            }
        }

        self.total_rewards_distributed += total_distributed;
        Ok(total_distributed)
    }

    /// Get total rewards distributed so far
    pub fn total_rewards_distributed(&self) -> u64 {
        self.total_rewards_distributed
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_staking_flow() {
        let mut contract = NFTStakingContract::new(0.1); // 0.1 tokens per second
        let nft = NFT {
            id: 1,
            owner: "Alice".to_string(),
            metadata: "MetaRebelz #1".to_string(),
        };

        // Stake NFT for 100 seconds
        assert!(contract.stake(nft.clone(), 100).is_ok());

        // Try to stake same NFT again
        assert!(matches!(
            contract.stake(nft.clone(), 100),
            Err(StakingError::AlreadyStaked)
        ));

        // Calculate rewards after 50 seconds (simulated)
        {
            let mut position = contract.staked_nfts.get_mut(&1).unwrap();
            position.staked_at = SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .unwrap()
                .as_secs()
                - 50;
        }

        let rewards = contract.calculate_rewards(1).unwrap();
        assert_eq!(rewards, 5); // 50 * 0.1 = 5

        // Airdrop rewards
        let airdropped = contract.airdrop_rewards().unwrap();
        assert_eq!(airdropped, 5);

        // Unstake and claim remaining rewards
        let remaining_rewards = contract.unstake(1).unwrap();
        assert!(remaining_rewards <= 5); // Depending on exact timing

        assert_eq!(contract.total_rewards_distributed(), 5 + remaining_rewards);
    }
}
```
