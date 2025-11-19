"""
Generated Code Metadata:
========================
Original URL: https://doubleton.pages.dev
Prompt: Generate a smart contract code on TON for a simple decentralized application.
Generated: DETERMINISTIC_20771f3ad52399fd
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```func
() recv_internal(slice in_msg_body) impure {
    ;; No operation by default
}

() recv_external(slice in_msg_body) impure {
    ;; Parse sender address
    var sender_addr = in_msg_body~load_msg_addr();

    ;; Parse operation code
    var op = in_msg_body~load_uint(32);

    if (op == 0) {
        ;; Handle ping operation
        var ping_msg = begin_cell()
            .store_uint(0x18, 6) ;; Message mode
            .store_slice(sender_addr)
            .store_uint(0, 1+4+4+64+32+1+1)
            .store_uint(1, 32) ;; Operation code for pong
            .end_cell();
        send_raw_message(ping_msg, 64); ;; Send pong back
    } else {
        ;; Unknown operation
        throw(100);
    }
}

() get_method_balance() method_id {
    return my_balance();
}

() get_method_address() method_id {
    return my_address();
}

() get_method_seqno() method_id {
    return get_data().begin_parse().preload_uint(64);
}

() get_method_storage() method_id {
    return get_data();
}

() get_data() inline_ref {
    return get_data().begin_parse();
}

() set_data(slice new_data) impure {
    set_data(begin_cell().store_slice(new_data).end_cell());
}

global slice storage_data;
global int seqno;

() init_data() impure {
    storage_data = null();
    seqno = 0;
    set_data(begin_cell().store_uint(seqno, 64).store_slice(storage_data).end_cell());
}

() update_storage(slice new_storage) impure {
    seqno += 1;
    storage_data = new_storage;
    set_data(begin_cell().store_uint(seqno, 64).store_slice(storage_data).end_cell());
}

() main() {
    ;; Contract initialization
    if (get_data().begin_parse().slice_empty?()) {
        init_data();
    }
}
```
