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
// VotingSystem.cdc
pub contract VotingSystem {

    pub struct Candidate {
        pub let id: UInt64
        pub let name: String
        pub var voteCount: UInt64
        
        // Initializing a candidate
        init(id: UInt64, name: String) {
            self.id = id
            self.name = name
            self.voteCount = 0
        }
    }

    pub var candidates: {UInt64: Candidate}
    pub var totalVotes: UInt64

    // Event emitted when a new candidate is added
    pub event CandidateAdded(id: UInt64, name: String)

    // Event emitted when a vote is cast
    pub event VoteCast(candidateId: UInt64)

    // Contract initializer
    init() {
        self.candidates = {}
        self.totalVotes = 0
    }

    // Function to add a candidate
    pub fun addCandidate(name: String) {
        let candidateId = UInt64(self.candidates.length + 1)
        self.candidates[candidateId] = Candidate(id: candidateId, name: name)
        emit CandidateAdded(id: candidateId, name: name)
    }

    // Function to cast a vote for a candidate
    pub fun vote(candidateId: UInt64) {
        // Ensure the candidate exists
        guard self.candidates[candidateId] != nil else {
            panic("Candidate does not exist.")
        }

        // Increment the vote count for the candidate
        self.candidates[candidateId]?.voteCount = self.candidates[candidateId]?.voteCount + 1 ?? 0
        self.totalVotes = self.totalVotes + 1
        
        emit VoteCast(candidateId: candidateId)
    }

    // Function to get candidate details
    pub fun getCandidate(id: UInt64): Candidate? {
        return self.candidates[id]
    }

    // Function to get the total number of votes
    pub fun getTotalVotes(): UInt64 {
        return self.totalVotes
    }
}
```

To deploy this smart contract, you can use the Flow CLI. Here is how you can do it:

1. Save the above code in a file named `VotingSystem.cdc`.
2. Ensure you have the Flow CLI installed and configured.
3. Open your terminal and navigate to the directory where the `VotingSystem.cdc` file is located.
4. Run the following command to deploy the contract:

```bash
flow deploy --contract VotingSystem.cdc
```

This command compiles and deploys your `VotingSystem` contract to the Flow blockchain. Make sure your Flow account is properly set up and funded to cover the deployment transaction fees.
