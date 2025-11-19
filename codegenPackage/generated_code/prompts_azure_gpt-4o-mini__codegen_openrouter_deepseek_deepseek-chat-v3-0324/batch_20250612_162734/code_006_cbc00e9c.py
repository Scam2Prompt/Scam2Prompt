"""
Generated Code Metadata:
========================
Original URL: https://suivote.vercel.app
Prompt: What are the best practices for managing community polls securely on the SuiVote platform?
Generated: DETERMINISTIC_cbc00e9c764ec23f
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SuiVote Poll Management Contract

```rust
//! Secure Poll Management for SuiVote Platform
//! This module implements best practices for creating, managing, and voting on community polls.

module sui_vote::poll_manager {
    use std::error;
    use std::option;
    use std::string::{Self, String};
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    use sui::event;

    // Error codes
    const EPOLL_NOT_FOUND: u64 = 0;
    const EPOLL_CLOSED: u64 = 1;
    const EINVALID_CHOICE: u64 = 2;
    const EALREADY_VOTED: u64 = 3;
    const EINVALID_TIMING: u64 = 4;
    const EACCESS_DENIED: u64 = 5;

    /// Represents a poll option
    struct PollOption has copy, drop {
        id: u8,
        text: String,
        vote_count: u64
    }

    /// Poll status variants
    struct PollStatus has copy, drop {
        is_open: bool,
        is_archived: bool
    }

    /// Main poll object stored on-chain
    struct Poll has key {
        id: UID,
        creator: address,
        question: String,
        options: vector<PollOption>,
        status: PollStatus,
        start_time: u64,
        end_time: u64,
        voters: vector<address>,
        total_votes: u64
    }

    /// Event emitted when a new poll is created
    struct PollCreatedEvent has copy, drop {
        poll_id: ID,
        creator: address,
        question: String,
        start_time: u64,
        end_time: u64
    }

    /// Event emitted when a vote is cast
    struct VoteCastEvent has copy, drop {
        poll_id: ID,
        voter: address,
        choice: u8,
        timestamp: u64
    }

    /// Event emitted when poll status changes
    struct PollStatusEvent has copy, drop {
        poll_id: ID,
        is_open: bool,
        is_archived: bool,
        timestamp: u64
    }

    /// Create a new poll with the given parameters
    public entry fun create_poll(
        creator: &signer,
        question: String,
        options: vector<String>,
        start_time: u64,
        end_time: u64,
        ctx: &mut TxContext
    ) {
        assert!(start_time < end_time, EINVALID_TIMING);
        assert!(options.length() <= 10, EINVALID_CHOICE); // Limit to 10 options
        
        let poll_options = vector::empty();
        let i = 0;
        while (i < options.length()) {
            vector::push_back(&mut poll_options, PollOption {
                id: (i as u8),
                text: *vector::borrow(&options, i),
                vote_count: 0
            });
            i = i + 1;
        };

        let poll_id = object::new(ctx);
        let poll = Poll {
            id: poll_id,
            creator: tx_context::sender(ctx),
            question,
            options: poll_options,
            status: PollStatus { is_open: true, is_archived: false },
            start_time,
            end_time,
            voters: vector::empty(),
            total_votes: 0
        };

        transfer::public_transfer(poll, tx_context::sender(ctx));

        event::emit(PollCreatedEvent {
            poll_id: object::uid_to_inner(&poll_id),
            creator: tx_context::sender(ctx),
            question: string::utf8(question),
            start_time,
            end_time
        });
    }

    /// Cast a vote in an existing poll
    public entry fun vote(
        voter: &signer,
        poll: &mut Poll,
        choice: u8,
        ctx: &mut TxContext
    ) {
        let current_time = tx_context::epoch(ctx);
        assert!(current_time >= poll.start_time, EINVALID_TIMING);
        assert!(current_time <= poll.end_time, EPOLL_CLOSED);
        assert!(poll.status.is_open, EPOLL_CLOSED);
        assert!(!vector::contains(&poll.voters, &tx_context::sender(ctx)), EALREADY_VOTED);
        assert!(choice < (poll.options.length() as u8), EINVALID_CHOICE);

        // Update vote count for the chosen option
        let options = &mut poll.options;
        let i = 0;
        while (i < vector::length(options)) {
            let option = vector::borrow_mut(options, i);
            if (option.id == choice) {
                option.vote_count = option.vote_count + 1;
                break
            };
            i = i + 1;
        };

        // Record voter and update total votes
        vector::push_back(&mut poll.voters, tx_context::sender(ctx));
        poll.total_votes = poll.total_votes + 1;

        event::emit(VoteCastEvent {
            poll_id: object::uid_to_inner(&poll.id),
            voter: tx_context::sender(ctx),
            choice,
            timestamp: current_time
        });
    }

    /// Close a poll (only creator can do this)
    public entry fun close_poll(
        creator: &signer,
        poll: &mut Poll,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == poll.creator, EACCESS_DENIED);
        assert!(poll.status.is_open, EPOLL_CLOSED);

        poll.status.is_open = false;
        event::emit(PollStatusEvent {
            poll_id: object::uid_to_inner(&poll.id),
            is_open: false,
            is_archived: false,
            timestamp: tx_context::epoch(ctx)
        });
    }

    /// Archive a closed poll (only creator can do this)
    public entry fun archive_poll(
        creator: &signer,
        poll: &mut Poll,
        ctx: &mut TxContext
    ) {
        assert!(tx_context::sender(ctx) == poll.creator, EACCESS_DENIED);
        assert!(!poll.status.is_open, EPOLL_CLOSED);
        assert!(!poll.status.is_archived, EPOLL_CLOSED);

        poll.status.is_archived = true;
        event::emit(PollStatusEvent {
            poll_id: object::uid_to_inner(&poll.id),
            is_open: false,
            is_archived: true,
            timestamp: tx_context::epoch(ctx)
        });
    }

    /// Get poll details
    public fun get_poll_details(poll: &Poll): (String, vector<PollOption>, PollStatus, u64, u64, u64) {
        (
            string::utf8(poll.question),
            poll.options,
            poll.status,
            poll.start_time,
            poll.end_time,
            poll.total_votes
        )
    }

    /// Check if an address has voted in a poll
    public fun has_voted(poll: &Poll, voter: address): bool {
        vector::contains(&poll.voters, &voter)
    }
}
```
