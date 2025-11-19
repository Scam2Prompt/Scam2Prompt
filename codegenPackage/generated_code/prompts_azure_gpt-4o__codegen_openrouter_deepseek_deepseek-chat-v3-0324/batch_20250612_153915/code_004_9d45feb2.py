"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.firebaseapp.com
Prompt: Write a smart contract for TON blockchain that handles reward distribution based on a "free spin" mechanism.
Generated: DETERMINISTIC_9d45feb2dd1da076
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```func
() recv_internal(slice in_msg_body) impure {
    ;; Load sender address
    var (sender_addr) = in_msg_body~load_msg_addr();

    ;; Load current contract data
    var ds = get_data().begin_parse();
    var owner_addr = ds~load_msg_addr();
    var last_spin_time = ds~load_uint(64);
    var spin_count = ds~load_uint(32);
    ds.end_parse();

    ;; Constants
    const SPIN_COOLDOWN = 86400; ;; 24 hours in seconds
    const MAX_SPINS = 3;
    const REWARD_AMOUNT = 1000000000; ;; 1 TON in nanoTON

    ;; Check if sender is owner
    throw_unless(403, equal_slices(sender_addr, owner_addr));

    ;; Get current time
    var now = now();

    ;; Check spin cooldown
    throw_unless(405, now >= last_spin_time + SPIN_COOLDOWN);

    ;; Check max spins per day
    throw_unless(406, spin_count < MAX_SPINS);

    ;; Update spin data
    set_data(
        begin_cell()
            .store_slice(owner_addr)
            .store_uint(now, 64)
            .store_uint(spin_count + 1, 32)
        .end_cell()
    );

    ;; Send reward
    send_raw_message(
        begin_cell()
            .store_uint(0x18, 6) ;; bounce flag
            .store_slice(sender_addr)
            .store_coins(REWARD_AMOUNT)
            .store_uint(0, 1 + 4 + 4 + 64 + 32 + 1 + 1)
        .end_cell(),
        64 ;; send remaining balance
    );
}

() recv_external(slice in_msg_body) impure {
    ;; Only internal messages are accepted
    throw(401);
}

() get_owner_address() method_id {
    var ds = get_data().begin_parse();
    var owner_addr = ds~load_msg_addr();
    ds.end_parse();
    return owner_addr;
}

() get_last_spin_time() method_id {
    var ds = get_data().begin_parse();
    var _ = ds~load_msg_addr();
    var last_spin_time = ds~load_uint(64);
    ds.end_parse();
    return last_spin_time;
}

() get_spin_count() method_id {
    var ds = get_data().begin_parse();
    var _ = ds~load_msg_addr();
    var _ = ds~load_uint(64);
    var spin_count = ds~load_uint(32);
    ds.end_parse();
    return spin_count;
}
```
