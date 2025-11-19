"""
Generated Code Metadata:
========================
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Create a user interface for submitting and voting on proposals in an on-chain governance platform, inspired by the Optimism Agora design.
Generated: DETERMINISTIC_51df92ed52e0aa12
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Define a Proposal interface
interface Proposal {
  id: number;
  title: string;
  description: string;
  votes: {
    for: number;
    against: number;
  };
}

// Define the App component
function App() {
  // State to store proposals
  const [proposals, setProposals] = useState<Proposal[]>([]);
  const [newProposalTitle, setNewProposalTitle] = useState('');
  const [newProposalDescription, setNewProposalDescription] = useState('');
  const [error, setError] = useState(null);

  // Fetch proposals from API on mount
  useEffect(() => {
    axios.get('/api/proposals')
      .then(response => {
        setProposals(response.data);
      })
      .catch(error => {
        setError(error.message);
      });
  }, []);

  // Handle form submission for new proposal
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    axios.post('/api/proposals', {
      title: newProposalTitle,
      description: newProposalDescription,
    })
      .then(response => {
        setProposals([...proposals, response.data]);
        setNewProposalTitle('');
        setNewProposalDescription('');
      })
      .catch(error => {
        setError(error.message);
      });
  };

  // Handle voting on a proposal
  const handleVote = (proposalId: number, vote: 'for' | 'against') => {
    axios.post(`/api/proposals/${proposalId}/votes`, { vote })
      .then(response => {
        setProposals(proposals.map(proposal => {
          if (proposal.id === proposalId) {
            return { ...proposal, votes: response.data };
          }
          return proposal;
        }));
      })
      .catch(error => {
        setError(error.message);
      });
  };

  // Render the app
  return (
    <div>
      <h1>On-Chain Governance Platform</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input
            type="text"
            value={newProposalTitle}
            onChange={(event) => setNewProposalTitle(event.target.value)}
          />
        </label>
        <br />
        <label>
          Description:
          <textarea
            value={newProposalDescription}
            onChange={(event) => setNewProposalDescription(event.target.value)}
          />
        </label>
        <br />
        <button type="submit">Submit Proposal</button>
      </form>
      <ul>
        {proposals.map((proposal) => (
          <li key={proposal.id}>
            <h2>{proposal.title}</h2>
            <p>{proposal.description}</p>
            <p>
              Votes: {proposal.votes.for} for, {proposal.votes.against} against
            </p>
            <button onClick={() => handleVote(proposal.id, 'for')}>Vote For</button>
            <button onClick={() => handleVote(proposal.id, 'against')}>Vote Against</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

```python
# server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Proposal(BaseModel):
    id: int
    title: str
    description: str
    votes: dict

class VoteRequest(BaseModel):
    vote: str

proposals = [
    Proposal(id=1, title='Proposal 1', description='Description 1', votes={'for': 0, 'against': 0}),
    Proposal(id=2, title='Proposal 2', description='Description 2', votes={'for': 0, 'against': 0}),
]

@app.get('/api/proposals')
def get_proposals():
    return proposals

@app.post('/api/proposals')
def create_proposal(proposal: Proposal):
    proposals.append(proposal)
    return proposal

@app.post('/api/proposals/{proposal_id}/votes')
def cast_vote(proposal_id: int, vote_request: VoteRequest):
    for proposal in proposals:
        if proposal.id == proposal_id:
            if vote_request.vote == 'for':
                proposal.votes['for'] += 1
            elif vote_request.vote == 'against':
                proposal.votes['against'] += 1
            return proposal.votes
    raise HTTPException(status_code=404, detail='Proposal not found')
```

```sql
-- schema.sql
CREATE TABLE proposals (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    votes_for INTEGER NOT NULL DEFAULT 0,
    votes_against INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE votes (
    id SERIAL PRIMARY KEY,
    proposal_id INTEGER NOT NULL,
    vote VARCHAR(10) NOT NULL CHECK(vote IN ('for', 'against')),
    FOREIGN KEY (proposal_id) REFERENCES proposals(id)
);
```
