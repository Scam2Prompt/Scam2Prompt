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

```typescript
// ProposalSubmissionAndVotingUI.tsx
import React, { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Contract, ethers } from 'ethers';
import GovernanceABI from './GovernanceABI.json';

interface Proposal {
  id: number;
  title: string;
  description: string;
  proposer: string;
  startBlock: number;
  endBlock: number;
  forVotes: number;
  againstVotes: number;
  abstainVotes: number;
}

const ProposalSubmissionAndVotingUI: React.FC = () => {
  const { account, library, chainId } = useWeb3React();
  const [proposals, setProposals] = useState<Proposal[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [newProposal, setNewProposal] = useState({
    title: '',
    description: '',
  });
  const [selectedVote, setSelectedVote] = useState<number | null>(null);
  const [currentBlock, setCurrentBlock] = useState<number>(0);

  // Replace with your actual contract address
  const GOVERNANCE_CONTRACT_ADDRESS = '0x123...abc';

  const governanceContract = new Contract(
    GOVERNANCE_CONTRACT_ADDRESS,
    GovernanceABI,
    library?.getSigner()
  );

  useEffect(() => {
    if (!account || !library) return;

    const fetchProposals = async () => {
      try {
        setLoading(true);
        const proposalCount = await governanceContract.proposalCount();
        const fetchedProposals: Proposal[] = [];

        for (let i = 0; i < proposalCount; i++) {
          const proposal = await governanceContract.proposals(i);
          fetchedProposals.push({
            id: i,
            title: proposal.title,
            description: proposal.description,
            proposer: proposal.proposer,
            startBlock: proposal.startBlock.toNumber(),
            endBlock: proposal.endBlock.toNumber(),
            forVotes: proposal.forVotes.toNumber(),
            againstVotes: proposal.againstVotes.toNumber(),
            abstainVotes: proposal.abstainVotes.toNumber(),
          });
        }

        setProposals(fetchedProposals);
      } catch (err) {
        console.error('Error fetching proposals:', err);
        setError('Failed to load proposals');
      } finally {
        setLoading(false);
      }
    };

    const fetchCurrentBlock = async () => {
      try {
        const block = await library.getBlockNumber();
        setCurrentBlock(block);
      } catch (err) {
        console.error('Error fetching current block:', err);
      }
    };

    fetchProposals();
    fetchCurrentBlock();
  }, [account, library]);

  const handleSubmitProposal = async () => {
    if (!newProposal.title || !newProposal.description) {
      setError('Title and description are required');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const tx = await governanceContract.propose(
        newProposal.title,
        newProposal.description
      );
      await tx.wait();
      setNewProposal({ title: '', description: '' });
      // Refresh proposals after submission
      const proposalCount = await governanceContract.proposalCount();
      const newProposalData = await governanceContract.proposals(proposalCount - 1);
      setProposals([
        ...proposals,
        {
          id: proposalCount - 1,
          title: newProposalData.title,
          description: newProposalData.description,
          proposer: account || '',
          startBlock: newProposalData.startBlock.toNumber(),
          endBlock: newProposalData.endBlock.toNumber(),
          forVotes: 0,
          againstVotes: 0,
          abstainVotes: 0,
        },
      ]);
    } catch (err) {
      console.error('Error submitting proposal:', err);
      setError('Failed to submit proposal');
    } finally {
      setLoading(false);
    }
  };

  const handleVote = async (proposalId: number) => {
    if (selectedVote === null) {
      setError('Please select a vote option');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const tx = await governanceContract.castVote(proposalId, selectedVote);
      await tx.wait();

      // Refresh proposal votes after voting
      const updatedProposal = await governanceContract.proposals(proposalId);
      const updatedProposals = proposals.map((p) =>
        p.id === proposalId
          ? {
              ...p,
              forVotes: updatedProposal.forVotes.toNumber(),
              againstVotes: updatedProposal.againstVotes.toNumber(),
              abstainVotes: updatedProposal.abstainVotes.toNumber(),
            }
          : p
      );
      setProposals(updatedProposals);
      setSelectedVote(null);
    } catch (err) {
      console.error('Error voting:', err);
      setError('Failed to cast vote');
    } finally {
      setLoading(false);
    }
  };

  const isProposalActive = (proposal: Proposal) => {
    return (
      currentBlock >= proposal.startBlock && currentBlock <= proposal.endBlock
    );
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Governance Proposals</h1>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {loading && (
        <div className="text-center py-4">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900 mx-auto"></div>
        </div>
      )}

      <div className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Submit New Proposal</h2>
        <div className="bg-white rounded-lg shadow p-6">
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="title">
              Title
            </label>
            <input
              id="title"
              type="text"
              className="w-full px-3 py-2 border border-gray-300 rounded"
              value={newProposal.title}
              onChange={(e) =>
                setNewProposal({ ...newProposal, title: e.target.value })
              }
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="description">
              Description
            </label>
            <textarea
              id="description"
              className="w-full px-3 py-2 border border-gray-300 rounded"
              rows={5}
              value={newProposal.description}
              onChange={(e) =>
                setNewProposal({ ...newProposal, description: e.target.value })
              }
            />
          </div>
          <button
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded disabled:opacity-50"
            onClick={handleSubmitProposal}
            disabled={!account || loading}
          >
            {account ? 'Submit Proposal' : 'Connect Wallet to Submit'}
          </button>
        </div>
      </div>

      <div>
        <h2 className="text-xl font-semibold mb-4">Active Proposals</h2>
        {proposals.filter(isProposalActive).length === 0 ? (
          <p className="text-gray-500">No active proposals</p>
        ) : (
          <div className="space-y-4">
            {proposals.filter(isProposalActive).map((proposal) => (
              <div key={proposal.id} className="bg-white rounded-lg shadow p-6">
                <h3 className="text-xl font-semibold mb-2">{proposal.title}</h3>
                <p className="text-gray-600 mb-4">{proposal.description}</p>
                <div className="flex justify-between items-center mb-4">
                  <div>
                    <span className="text-green-500 font-medium">
                      For: {proposal.forVotes}
                    </span>{' '}
                    |{' '}
                    <span className="text-red-500 font-medium">
                      Against: {proposal.againstVotes}
                    </span>{' '}
                    |{' '}
                    <span className="text-gray-500 font-medium">
                      Abstain: {proposal.abstainVotes}
                    </span>
                  </div>
                  <div className="text-sm text-gray-500">
                    Blocks: {proposal.startBlock} - {proposal.endBlock}
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <div className="flex space-x-2">
                    <button
                      className={`px-3 py-1 rounded ${
                        selectedVote === 1
