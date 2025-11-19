"""
Generated Code Metadata:
========================
Original URL: https://shibuswap.github.io
Prompt: Design a staking system using ShibaSwap's BURY feature as a reference, and write a simple Node.js script to simulate staking and reward distribution.
Generated: DETERMINISTIC_bd7509050dbcaa4f
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { ethers } = require('ethers');
const { BigNumber } = require('ethers');
const { formatEther, parseEther } = require('ethers/lib/utils');

// Simulated Staking Contract
class ShibaStaking {
    constructor() {
        this.stakers = new Map(); // Map<address, {amount: BigNumber, rewardDebt: BigNumber}>
        this.totalStaked = BigNumber.from(0);
        this.accShibPerShare = BigNumber.from(0); // Accumulated SHIB per share, times 1e12
        this.rewardPerBlock = parseEther('100'); // 100 SHIB per block as reward
        this.lastRewardBlock = 0;
    }

    /**
     * Update the staking pool's reward variables
     * @param {number} currentBlock - The current block number
     */
    updatePool(currentBlock) {
        if (currentBlock <= this.lastRewardBlock) {
            return;
        }

        if (this.totalStaked.isZero()) {
            this.lastRewardBlock = currentBlock;
            return;
        }

        const blocksSinceLastReward = BigNumber.from(currentBlock - this.lastRewardBlock);
        const shibReward = blocksSinceLastReward.mul(this.rewardPerBlock);
        this.accShibPerShare = this.accShibPerShare.add(
            shibReward.mul(BigNumber.from(10).pow(12)).div(this.totalStaked)
        );
        this.lastRewardBlock = currentBlock;
    }

    /**
     * Stake SHIB tokens
     * @param {string} address - The staker's address
     * @param {BigNumber} amount - Amount of SHIB to stake
     * @param {number} currentBlock - Current block number
     */
    stake(address, amount, currentBlock) {
        this.updatePool(currentBlock);

        if (this.stakers.has(address)) {
            const staker = this.stakers.get(address);
            const pending = staker.amount.mul(this.accShibPerShare).div(BigNumber.from(10).pow(12)).sub(staker.rewardDebt);
            if (!pending.isZero()) {
                console.log(`Distributing ${formatEther(pending)} SHIB rewards to ${address}`);
            }
        } else {
            this.stakers.set(address, {
                amount: BigNumber.from(0),
                rewardDebt: BigNumber.from(0)
            });
        }

        const staker = this.stakers.get(address);
        staker.amount = staker.amount.add(amount);
        staker.rewardDebt = staker.amount.mul(this.accShibPerShare).div(BigNumber.from(10).pow(12));
        this.totalStaked = this.totalStaked.add(amount);

        console.log(`${address} staked ${formatEther(amount)} SHIB`);
    }

    /**
     * Withdraw staked SHIB and claim rewards
     * @param {string} address - The staker's address
     * @param {number} currentBlock - Current block number
     */
    withdraw(address, currentBlock) {
        if (!this.stakers.has(address)) {
            throw new Error('No staked amount found');
        }

        this.updatePool(currentBlock);
        const staker = this.stakers.get(address);
        const pending = staker.amount.mul(this.accShibPerShare).div(BigNumber.from(10).pow(12)).sub(staker.rewardDebt);
        
        if (!pending.isZero()) {
            console.log(`Distributing ${formatEther(pending)} SHIB rewards to ${address}`);
        }

        console.log(`${address} withdrew ${formatEther(staker.amount)} SHIB`);
        this.totalStaked = this.totalStaked.sub(staker.amount);
        this.stakers.delete(address);
    }

    /**
     * Claim pending rewards without withdrawing staked SHIB
     * @param {string} address - The staker's address
     * @param {number} currentBlock - Current block number
     */
    claimRewards(address, currentBlock) {
        if (!this.stakers.has(address)) {
            throw new Error('No staked amount found');
        }

        this.updatePool(currentBlock);
        const staker = this.stakers.get(address);
        const pending = staker.amount.mul(this.accShibPerShare).div(BigNumber.from(10).pow(12)).sub(staker.rewardDebt);
        
        if (pending.isZero()) {
            console.log(`No pending rewards for ${address}`);
            return;
        }

        console.log(`Distributing ${formatEther(pending)} SHIB rewards to ${address}`);
        staker.rewardDebt = staker.amount.mul(this.accShibPerShare).div(BigNumber.from(10).pow(12));
    }
}

// Simulation Script
(async () => {
    try {
        const staking = new ShibaStaking();
        const [alice, bob] = [
            '0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B',
            '0x4dEadD128d85Fc5F0d6fDfcf5aC2aD5F0b4eD3e0'
        ];

        // Simulate blocks and staking
        let currentBlock = 1000;

        // Alice stakes 1000 SHIB at block 1000
        staking.stake(alice, parseEther('1000'), currentBlock);

        // Bob stakes 500 SHIB at block 1005
        currentBlock = 1005
