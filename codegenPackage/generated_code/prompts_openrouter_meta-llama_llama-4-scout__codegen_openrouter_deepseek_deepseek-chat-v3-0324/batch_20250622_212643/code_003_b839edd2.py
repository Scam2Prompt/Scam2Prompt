"""
Generated Code Metadata:
========================
Original URL: https://ton-448f1f.webflow.io
Prompt: Design a smart contract on TON blockchain for airdrop distribution, inspired by TON Capital's airdrop node sale and rewards campaign.
Generated: DETERMINISTIC_b839edd22f1539b6
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```func
() recv_internal(slice in_msg_body) impure {
    ;; Constants
    int const MIN_DEPOSIT = 1000000000; ;; 1 TON
    int const AIRDROP_AMOUNT = 500000000; ;; 0.5 TON per eligible address
    int const MAX_RECIPIENTS = 100; ;; Max recipients per transaction
    
    ;; Load persistent data
    var (owner_address, airdrop_start_time, airdrop_end_time, total_distributed, recipients) = load_data();
    
    ;; Check if message is from owner
    slice sender = in_msg_body~load_msg_addr();
    if (sender == owner_address) {
        ;; Owner commands
        int op = in_msg_body~load_uint(32);
        if (op == 1) { ;; Set airdrop period
            airdrop_start_time = in_msg_body~load_uint(64);
            airdrop_end_time = in_msg_body~load_uint(64);
            save_data(owner_address, airdrop_start_time, airdrop_end_time, total_distributed, recipients);
            return ();
        } elseif (op == 2) { ;; Withdraw funds
            int amount = in_msg_body~load_uint(128);
            send_raw_message(
                begin_cell()
                    .store_uint(0x18, 6) ;; mode
                    .store_slice(owner_address)
                    .store_coins(amount)
                    .store_uint(0, 1 + 4 + 4 + 64 + 32 + 1 + 1)
                .end_cell(),
                64 ;; send mode
            );
            return ();
        }
    }
    
    ;; Check if airdrop is active
    int current_time = now();
    if (current_time < airdrop_start_time || current_time > airdrop_end_time) {
        return ();
    }
    
    ;; Check if sender is eligible
    if (~ recipients.exists(sender)) {
        return ();
    }
    
    ;; Check minimum deposit
    int msg_value = in_msg_body.preload_uint(128);
    if (msg_value < MIN_DEPOSIT) {
        return ();
    }
    
    ;; Mark recipient as claimed
    recipients.delete(sender);
    total_distributed += AIRDROP_AMOUNT;
    save_data(owner_address, airdrop_start_time, airdrop_end_time, total_distributed, recipients);
    
    ;; Send airdrop
    send_raw_message(
        begin_cell()
            .store_uint(0x18, 6) ;; mode
            .store_slice(sender)
            .store_coins(AIRDROP_AMOUNT)
            .store_uint(0, 1 + 4 + 4 + 64 + 32 + 1 + 1)
        .end_cell(),
        64 ;; send mode
    );
    
    ;; Return excess funds if any
    if (msg_value > MIN_DEPOSIT) {
        send_raw_message(
            begin_cell()
                .store_uint(0x18, 6) ;; mode
                .store_slice(sender)
                .store_coins(msg_value - MIN_DEPOSIT)
                .store_uint(0, 1 + 4 + 4 + 64 + 32 + 1 + 1)
            .end_cell(),
            64 ;; send mode
        );
    }
}

() save_data(slice owner_address, int airdrop_start_time, int airdrop_end_time, int total_distributed, cell recipients) impure {
    set_data(
        begin_cell()
            .store_slice(owner_address)
            .store_uint(airdrop_start_time, 64)
            .store_uint(airdrop_end_time, 64)
            .store_uint(total_distributed, 128)
            .store_dict(recipients)
        .end_cell()
    );
}

(slice, int, int, int, cell) load_data() {
    var ds = get_data().begin_parse();
    return (
        ds~load_msg_addr(), ;; owner_address
        ds~load_uint(64), ;; airdrop_start_time
        ds~load_uint(64), ;; airdrop_end_time
        ds~load_uint(128), ;; total_distributed
        ds~load_dict() ;; recipients
    );
}

() init() {
    slice owner_address = my_address();
    int airdrop_start_time = 0;
    int airdrop_end_time = 0;
    int total_distributed = 0;
    cell recipients = new_dict();
    
    save_data(owner_address, airdrop_start_time, airdrop_end_time, total_distributed, recipients);
}
```
