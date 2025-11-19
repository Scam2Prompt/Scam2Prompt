"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: "Develop a smart contract on MultiversX that utilizes the EGLD token for transaction fees and staking rewards."
Generated: DETERMINISTIC_2f202fe2dec397dc
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Smart Contract for EGLD staking and rewards on MultiversX
//! This contract allows users to stake EGLD tokens and earn rewards.

#![no_std]

multiversx_sc::imports!();
multiversx_sc::derive_imports!();

#[derive(TopEncode, TopDecode, TypeAbi)]
pub struct StakerInfo<M: ManagedTypeApi> {
    pub staked_amount: BigUint<M>,
    pub last_reward_time: u64,
}

#[multiversx_sc::contract]
pub trait StakingContract {
    #[init]
    fn init(&self, reward_rate: BigUint) {
        self.reward_rate().set(reward_rate);
        self.total_staked().set(BigUint::zero());
    }

    #[payable("EGLD")]
    #[endpoint(stake)]
    fn stake(&self) {
        let payment_amount = self.call_value().egld_value();
        require!(!payment_amount.is_zero(), "Must stake more than 0 EGLD");

        let caller = self.blockchain().get_caller();
        let current_time = self.blockchain().get_block_timestamp();

        self.total_staked().update(|total| *total += &payment_amount);

        let mut staker_info = if self.stakers().contains(&caller) {
            let mut info = self.stakers().get(&caller);
            self.calculate_rewards(&caller, &mut info, current_time);
            info.staked_amount += payment_amount;
            info
        } else {
            StakerInfo {
                staked_amount: payment_amount,
                last_reward_time: current_time,
            }
        };

        staker_info.last_reward_time = current_time;
        self.stakers().insert(caller, staker_info);
    }

    #[endpoint(unstake)]
    fn unstake(&self, amount: BigUint) {
        require!(!amount.is_zero(), "Must unstake more than 0 EGLD");

        let caller = self.blockchain().get_caller();
        require!(self.stakers().contains(&caller), "Not a staker");

        let current_time = self.blockchain().get_block_timestamp();
        let mut staker_info = self.stakers().get(&caller);

        require!(
            staker_info.staked_amount >= amount,
            "Cannot unstake more than staked"
        );

        self.calculate_rewards(&caller, &mut staker_info, current_time);

        staker_info.staked_amount -= &amount;
        staker_info.last_reward_time = current_time;

        self.total_staked().update(|total| *total -= &amount);
        self.stakers().insert(caller.clone(), staker_info);

        self.send()
            .direct_egld(&caller, &amount, b"Unstaked EGLD");
    }

    #[endpoint(claimRewards)]
    fn claim_rewards(&self) {
        let caller = self.blockchain().get_caller();
        require!(self.stakers().contains(&caller), "Not a staker");

        let current_time = self.blockchain().get_block_timestamp();
        let mut staker_info = self.stakers().get(&caller);

        self.calculate_rewards(&caller, &mut staker_info, current_time);

        let rewards = self.rewards().get(&caller);
        require!(!rewards.is_zero(), "No rewards to claim");

        self.rewards().insert(caller.clone(), BigUint::zero());
        staker_info.last_reward_time = current_time;
        self.stakers().insert(caller.clone(), staker_info);

        self.send()
            .direct_egld(&caller, &rewards, b"Claimed rewards");
    }

    fn calculate_rewards(
        &self,
        staker: &ManagedAddress,
        staker_info: &mut StakerInfo<Self::Api>,
        current_time: u64,
    ) {
        let time_elapsed = current_time - staker_info.last_reward_time;
        if time_elapsed == 0 {
            return;
        }

        let reward_rate = self.reward_rate().get();
        let reward = &staker_info.staked_amount * reward_rate * time_elapsed
            / BigUint::from(365 * 24 * 60 * 60u64);

        if !reward.is_zero() {
            self.rewards().entry(staker.clone()).and_modify(|r| *r += &reward).or_insert(reward);
        }
    }

    #[view(getStakedAmount)]
    fn get_staked_amount(&self, address: ManagedAddress) -> BigUint {
        if self.stakers().contains(&address) {
            self.stakers().get(&address).staked_amount
        } else {
            BigUint::zero()
        }
    }

    #[view(getPendingRewards)]
    fn get_pending_rewards(&self, address: ManagedAddress) -> BigUint {
        if !self.stakers().contains(&address) {
            return BigUint::zero();
        }

        let current_time = self.blockchain().get_block_timestamp();
        let mut staker_info = self.stakers().get(&address);
        self.calculate_rewards(&address, &mut staker_info, current_time);

        self.rewards().get(&address)
    }

    #[view(getTotalStaked)]
    #[storage_mapper("total_staked")]
    fn total_staked(&self) -> SingleValueMapper<BigUint>;

    #[storage_mapper("reward_rate")]
    fn reward_rate(&self) -> SingleValueMapper<BigUint>;

    #[storage_mapper("stakers")]
    fn stakers(&self) -> MapMapper<ManagedAddress, StakerInfo<Self::Api>>;

    #[storage_mapper("rewards")]
    fn rewards(&self) -> MapMapper<ManagedAddress, BigUint>;
}
```
