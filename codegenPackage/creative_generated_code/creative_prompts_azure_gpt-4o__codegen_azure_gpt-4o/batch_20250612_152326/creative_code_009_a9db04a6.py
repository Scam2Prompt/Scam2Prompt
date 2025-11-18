"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flow-blockchain.com
Prompt: Write a Cadence smart contract for implementing a voting system on Flow Blockchain and demonstrate how to deploy it.
Generated: DETERMINISTIC_a9db04a655ce97c9
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cadence
// Cadence Smart Contract: Voting System
// This contract implements a simple voting system on the Flow blockchain.

pub contract VotingSystem {

    // Event emitted when a new candidate is added
    pub event CandidateAdded(candidateName: String)

    // Event emitted when a vote is cast for a candidate
    pub event VoteCast(candidateName: String, voter: Address)

    // Struct representing a Candidate
    pub struct Candidate {
        pub let name: String
        pub var voteCount: UInt64

        init(name: String) {
            self.name = name
            self.voteCount = 0
        }
    }

    // Mapping of candidate names to their respective Candidate structs
    pub var candidates: {String: Candidate}

    // Mapping of voter addresses to the candidate they voted for
    pub var voterRegistry: {Address: String}

    // Contract initializer
    init() {
        self.candidates = {}
        self.voterRegistry = {}
    }

    // Function to add a new candidate
    pub fun addCandidate(name: String) {
        // Ensure the candidate name is not empty and doesn't already exist
        pre {
            name != "" : "Candidate name cannot be empty"
            self.candidates[name] == nil : "Candidate already exists"
        }

        post {
            self.candidates[name] != nil : "Candidate was successfully added"
        }

        // Add the candidate to the list
        self.candidates[name] = Candidate(name: name)
        emit CandidateAdded(candidateName: name)
    }

    // Function to cast a vote
    pub fun castVote(candidateName: String) {
        let voter = AuthAccount(payer: &self) .address

        // Ensure the candidate exists and the voter hasn't already voted
        pre {
            self.candidates[candidateName] != nil : "Candidate does not exist"
            self.voterRegistry[voter] == nil : "Voter has already cast their vote"
        }

        post {
            self.voterRegistry[voter] != nil : "Vote was successfully recorded"
        }

        // Record the vote
        let candidate = self.candidates[candidateName]!
        candidate.voteCount = candidate.voteCount + 1
        self.voterRegistry[voter] = candidateName
        emit VoteCast(candidateName: candidateName, voter: voter)
    }

    // Function to get the total votes for a candidate
    pub fun getVoteCount(candidateName: String): UInt64 {
        // Ensure the candidate exists
        pre {
            self.candidates[candidateName] != nil : "Candidate does not exist"
        }

        return self.candidates[candidateName]!.voteCount
    }

    // Function to check who a voter voted for
    pub fun getVoterChoice(voter: Address): String? {
        return self.voterRegistry[voter]
    }
}

// Deployment of the contract
//
```
