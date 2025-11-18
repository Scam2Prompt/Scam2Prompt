"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Create a smart contract for staking Toncoin on the TON blockchain and explain how to deploy it using TON tools.
Generated: DETERMINISTIC_b0ef1cafb1a2c627
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ts
// smart-contract.ts
// This is a simple staking smart contract for Toncoin on the TON blockchain.
// Written in FunC language (TON Smart Contract Language).

// Import necessary base libraries
#include "stdlib.fc"

// Define constants
const int MIN_STAKE_AMOUNT = 100000000; // Minimum staking amount in nanocoins (100 TON)
const int REWARD_PERCENTAGE = 5;       // Annual reward percentage

// Define global variables
int totalStaked;          // Stores the total amount staked in the contract
cell stakerData;          // Stores data about stakers (address -> amount)

// Contract entry points

// Constructor: Initializes the contract state
() init() {
    totalStaked = 0;
    stakerData = begin_dict();
}

// Function to stake Toncoin
() stake() {
    ;; Validate stake amount
    int stakeAmount = msg_value();  // Amount sent with the message in nanocoins
    require(stakeAmount >= MIN_STAKE_AMOUNT, "Stake amount is less than the minimum required.");

    ;; Update global state
    stakerData = dict_set_ref(stakerData, sender_addr(), just(stakeAmount));
    totalStaked = totalStaked + stakeAmount;

    ;; Return confirmation
    accept_message();
}

// Function to withdraw staked Toncoin
() withdraw() {
    ;; Retrieve staker's data
    var stakeData = dict_get_ref(stakerData, sender_addr());
    require(stakeData.not_empty(), "No staked amount found for this address.");
    int stakedAmount = stakeData.unbox();

    ;; Calculate rewards (for simplicity, assume 1 year has passed)
    int reward = (stakedAmount * REWARD_PERCENTAGE) / 100;
    int totalWithdrawal = stakedAmount + reward;

    ;; Update global state
    stakerData = dict_delete(stakerData, sender_addr());
    totalStaked = totalStaked - stakedAmount;

    ;; Send funds to caller
    send_msg(sender_addr(), totalWithdrawal);

    ;; Return confirmation
    accept_message();
}

// Function to check staked balance for a given address
(int) get_balance(slice address) {
    var stakeData = dict_get_ref(stakerData, address);
    if (stakeData.not_empty()) {
        return stakeData.unbox();
    } else {
        return 0;
    }
}

// Function to check total staked funds in the contract
(int) get_total_staked() {
    return totalStaked;
}

// Function to receive TON
() receive_external(slice inMsg) {
    ;; Allow receiving TON without any processing
    accept_message();
}

// Deploy instructions:
// 1. Compile the contract using TON's FunC compiler: `func -P smart-contract.ts`
// 2. Deploy the compiled `.fc` file using TON tools, such as `tonos-cli`.
//    a. Create a deployment transaction with the correct initialization parameters.
//    b. Send the transaction to the TON blockchain.
// 3. Verify deployment via the TON Explorer or appropriate tools.
```
