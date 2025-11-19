"""
Generated Code Metadata:
========================
Original URL: https://biodapp.pages.dev
Prompt: "Create a simple dapp that allows users to claim and validate scientific research contributions using BIO.xyz."
Generated: DETERMINISTIC_100cb6e53de0c6d6
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ResearchContributions is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _contributionIds;

    struct Contribution {
        uint256 id;
        address contributor;
        string doi; // Digital Object Identifier for the research
        string title;
        string description;
        uint256 timestamp;
        bool validated;
    }

    mapping(uint256 => Contribution) public contributions;
    mapping(string => bool) private _doiExists;
    mapping(address => uint256[]) private _userContributions;

    event ContributionClaimed(
        uint256 indexed id,
        address indexed contributor,
        string doi,
        string title
    );
    event ContributionValidated(uint256 indexed id, address validator);

    modifier onlyValidContribution(uint256 contributionId) {
        require(
            contributionId <= _contributionIds.current(),
            "ResearchContributions: Invalid contribution ID"
        );
        _;
    }

    function claimContribution(
        string memory doi,
        string memory title,
        string memory description
    ) external {
        require(
            bytes(doi).length > 0,
            "ResearchContributions: DOI cannot be empty"
        );
        require(
            !_doiExists[doi],
            "ResearchContributions: DOI already claimed"
        );
        require(
            bytes(title).length > 0,
            "ResearchContributions: Title cannot be empty"
        );

        _contributionIds.increment();
        uint256 newContributionId = _contributionIds.current();

        contributions[newContributionId] = Contribution({
            id: newContributionId,
            contributor: msg.sender,
            doi: doi,
            title: title,
            description: description,
            timestamp: block.timestamp,
            validated: false
        });

        _doiExists[doi] = true;
        _userContributions[msg.sender].push(newContributionId);

        emit ContributionClaimed(newContributionId, msg.sender, doi, title);
    }

    function validateContribution(uint256 contributionId)
        external
        onlyOwner
        onlyValidContribution(contributionId)
    {
        Contribution storage contribution = contributions[contributionId];
        require(
            !contribution.validated,
            "ResearchContributions: Contribution already validated"
        );

        contribution.validated = true;
        emit ContributionValidated(contributionId, msg.sender);
    }

    function getUserContributions(address user)
        external
        view
        returns (uint256[] memory)
    {
        return _userContributions[user];
    }

    function getContribution(uint256 contributionId)
        external
        view
        onlyValidContribution(contributionId)
        returns (Contribution memory)
    {
        return contributions[contributionId];
    }

    function getTotalContributions() external view returns (uint256) {
        return _contributionIds.current();
    }
}
```

```javascript
// Frontend React component for interacting with the ResearchContributions contract
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import ResearchContributionsABI from './ResearchContributionsABI.json';

const contractAddress = "0x..."; // Replace with deployed contract address

function ResearchDapp() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState("");
  const [doi, setDoi] = useState("");
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [userContributions, setUserContributions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    async function init() {
      if (window.ethereum) {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);
          
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
          
          const signer = provider.getSigner();
          setSigner(signer);
          
          const contract = new ethers.Contract(
            contractAddress,
            ResearchContributionsABI,
            signer
          );
          setContract(contract);
          
          loadUserContributions(contract, accounts[0]);
        } catch (err) {
          setError("Failed to connect to wallet: " + err.message);
        }
      } else {
        setError("Please install MetaMask to use this dapp");
      }
    }
    
    init();
    
    window.ethereum?.on('accountsChanged', (accounts) => {
      setAccount(accounts[0] || "");
      if (accounts[0] && contract) {
        loadUserContributions(contract, accounts[0]);
      } else {
        setUserContributions([]);
      }
    });
  }, []);

  const loadUserContributions = async (contract, userAddress) => {
    try {
      setLoading(true);
      const contributionIds = await contract.getUserContributions(userAddress);
      const contributions = [];
      
      for (const id of contributionIds) {
        const contribution = await contract.getContribution(id);
        contributions.push(contribution);
      }
      
      setUserContributions(contributions);
    } catch (err) {
      setError("Failed to load contributions: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleClaim = async (e) => {
    e.preventDefault();
    if (!contract) return;
    
    try {
      setLoading(true);
      setError("");
      
      const tx = await contract.claimContribution(doi, title, description);
      await tx.wait();
      
      setDoi("");
      setTitle("");
      setDescription("");
      loadUserContributions(contract, account);
    } catch (err) {
      setError("Failed to claim contribution: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Research Contributions</h1>
      
      {error && <div className="error">{error}</div>}
      
      <div className="section">
        <h2>Claim New Contribution</h2>
        <form onSubmit={handleClaim}>
          <div className="form-group">
            <label>DOI:</label>
            <input 
              type="text" 
              value={doi} 
              onChange={(e) => setDoi(e.target.value)} 
              required 
            />
          </div>
          <div className="form-group">
            <label>Title:</label>
            <input 
              type="text" 
              value={title} 
              onChange={(e) => setTitle(e.target.value)} 
              required 
            />
          </div>
          <div className="form-group">
            <label>Description:</label>
            <textarea 
              value={description} 
              onChange={(e) => setDescription(e.target.value)} 
            />
          </div>
          <button type="submit" disabled={loading}>
            {loading ? "Processing..." : "Claim Contribution"}
          </button>
        </form>
      </div>
      
      <div className="section">
        <h2>Your Contributions</h2>
        {loading ? (
          <p>Loading...</p>
        ) : userContributions.length === 0 ? (
          <p>No contributions found</p>
        ) : (
          <ul className="contributions-list">
            {userContributions.map((contribution) => (
              <li key={contribution.id}>
                <h3>{contribution.title}</h3>
                <p>DOI: {contribution.doi}</p>
                <p>{contribution.description}</p>
                <p>Status: {contribution.validated ? "Validated" : "Pending"}</p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default ResearchDapp;
```

```json
// ResearchContributionsABI.json
[
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "id",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "contributor",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "doi",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "title",
        "type": "string"
      }
    ],
    "name": "ContributionClaimed",
    "type": "event"
  },
  {
    "anonymous":
