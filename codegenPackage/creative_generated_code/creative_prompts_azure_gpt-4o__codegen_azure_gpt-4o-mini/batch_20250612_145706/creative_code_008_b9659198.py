"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Create a React component to show the list of active proposals on Agora, including voting deadlines and options available.
Generated: DETERMINISTIC_b9659198dff50ed6
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

/**
 * A React component to display a list of active proposals on Agora.
 * Each proposal includes its title, voting deadline, and voting options.
 */
const ActiveProposals = ({ apiEndpoint }) => {
    const [proposals, setProposals] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch the active proposals from the API
    const fetchProposals = async () => {
        try {
            const response = await axios.get(apiEndpoint);
            setProposals(response.data);
        } catch (err) {
            setError('Failed to fetch proposals. Please try again later.');
            console.error('Error fetching proposals:', err);
        } finally {
            setLoading(false);
        }
    };

    // Fetch proposals on component mount
    useEffect(() => {
        fetchProposals();
    }, [apiEndpoint]);

    // Render loading state
    if (loading) {
        return <div>Loading proposals...</div>;
    }

    // Render error state
    if (error) {
        return <div>{error}</div>;
    }

    // Render the list of proposals
    return (
        <div>
            <h2>Active Proposals</h2>
            {proposals.length === 0 ? (
                <p>No active proposals at the moment.</p>
            ) : (
                <ul>
                    {proposals.map((proposal) => (
                        <li key={proposal.id}>
                            <h3>{proposal.title}</h3>
                            <p>Voting Deadline: {new Date(proposal.deadline).toLocaleString()}</p>
                            <h4>Voting Options:</h4>
                            <ul>
                                {proposal.options.map((option) => (
                                    <li key={option.id}>{option.name}</li>
                                ))}
                            </ul>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

// Prop types for validation
ActiveProposals.propTypes = {
    apiEndpoint: PropTypes.string.isRequired,
};

export default ActiveProposals;
```
