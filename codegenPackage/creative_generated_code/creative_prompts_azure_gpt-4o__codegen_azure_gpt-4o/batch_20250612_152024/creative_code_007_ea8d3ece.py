"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetfoundation.io
Prompt: Generate a Cairo smart contract for a decentralized voting system on StarkNet. Include instructions for compiling and deploying the contract.
Generated: DETERMINISTIC_ea8d3ece2a1c541d
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: voting.cairo
# A decentralized voting system smart contract for StarkNet

%lang starknet
%builtins poseidon

from starkware.cairo.common.uint256 import Uint256
from starkware.cairo.common.math_utils import assert_not_zero

@storage_var
func candidate_votes(candidate_id : felt) -> felt {
}

@storage_var
func has_voted(voter_address : felt) -> felt {
}

@storage_var
func total_candidates() -> felt {
}

@event
func VotingEvent(voter : felt, candidate_id : felt) {
}

# Initialize the voting system with candidates
@constructor
func constructor(initial_candidates : felt*) {
    let num_candidates = len(initial_candidates)

    # Store the total number of candidates
    total_candidates.write(num_candidates)

    # Initialize votes for each candidate
    for candidate_id in initial_candidates {
        candidate_votes.write(candidate_id, 0)
    }
    return ()
}

# Cast a vote for a specific candidate
@external
func vote(voter_address : felt, candidate_id : felt) {
    # Ensure voter has not voted before
    let has_already_voted = has_voted.read(voter_address)
    if has_already_voted != 0 {
        assert(0, 'Voter has already voted.')
    }

    # Ensure the candidate exists
    let candidate_exist_votes = candidate_votes.read(candidate_id)
    assert_not_zero(candidate_exist_votes)

    # Record the vote
    has_voted.write(voter_address, 1)
    let current_votes = candidate_votes.read(candidate_id)
    candidate_votes.write(candidate_id, current_votes + 1)

    # Emit voting event
    VotingEvent.emit(voter_address, candidate_id)
    return ()
}

# Query votes for a specific candidate
@view
func get_candidate_votes(candidate_id : felt) -> (votes : felt) {
    let votes = candidate_votes.read(candidate_id)
    return (votes)
}

# Query if a voter has voted
@view
func has_voter_voted(voter_address : felt) -> (voted : felt) {
    let voted = has_voted.read(voter_address)
    return (voted)
}

# Query the total number of candidates
@view
func get_total_candidates() -> (count : felt) {
    let count = total_candidates.read()
    return (count)
}

# End of contract

```

### Compilation and Deployment Instructions:

1. Install the necessary tools:
   - Install `cairo-lang` and StarkNet CLI using `pip install cairo-lang`.

2. Compile the contract:
   ```bash
   starknet-compile voting.cairo --output voting_compiled.json --abi voting_abi.json
   ```

3. Deploy the contract:
   ```bash
   starknet deploy --contract voting_compiled.json
   ```

4. The deployment command will return the contract address and transaction hash. Store the contract address for interacting with the contract later.
