"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-in.pages.dev
Prompt: Design a basic UI component for an InQubeta dApp that displays a list of available AI start-up investment opportunities, including their NFT representations and fractional ownership details.
Generated: DETERMINISTIC_323c97f62561a4e3
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './InvestmentOpportunities.css';

// ABI and contract address would typically be imported from a config file
const INQUBETA_CONTRACT_ABI = [/* ... */];
const INQUBETA_CONTRACT_ADDRESS = '0x...';

const InvestmentOpportunities = ({ provider, account }) => {
  const [opportunities, setOpportunities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOpportunities = async () => {
      try {
        if (!provider || !account) return;

        const contract = new ethers.Contract(
          INQUBETA_CONTRACT_ADDRESS,
          INQUBETA_CONTRACT_ABI,
          provider.getSigner()
        );

        const opportunityCount = await contract.getOpportunityCount();
        const opportunityPromises = [];

        for (let i = 0; i < opportunityCount; i++) {
          opportunityPromises.push(contract.getOpportunityDetails(i));
        }

        const opportunityDetails = await Promise.all(opportunityPromises);
        
        const formattedOpportunities = opportunityDetails.map((opp, index) => ({
          id: index,
          name: opp.name,
          description: opp.description,
          totalFundingGoal: ethers.utils.formatEther(opp.totalFundingGoal),
          currentFunding: ethers.utils.formatEther(opp.currentFunding),
          minInvestment: ethers.utils.formatEther(opp.minInvestment),
          nftImageUrl: opp.nftImageUrl,
          valuation: ethers.utils.formatEther(opp.valuation),
          availableShares: opp.availableShares.toString(),
          deadline: new Date(opp.deadline * 1000).toLocaleDateString()
        }));

        setOpportunities(formattedOpportunities);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching opportunities:', err);
        setError('Failed to load investment opportunities');
        setLoading(false);
      }
    };

    fetchOpportunities();
  }, [provider, account]);

  const handleInvest = async (opportunityId, amount) => {
    try {
      const contract = new ethers.Contract(
        INQUBETA_CONTRACT_ADDRESS,
        INQUBETA_CONTRACT_ABI,
        provider.getSigner()
      );

      const tx = await contract.invest(
        opportunityId,
        ethers.utils.parseEther(amount.toString())
      );
      
      await tx.wait();
      alert('Investment successful!');
    } catch (err) {
      console.error('Investment error:', err);
      alert('Investment failed. Please try again.');
    }
  };

  if (loading) {
    return <div className="loading">Loading opportunities...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="opportunities-container">
      <h2>Available AI Start-up Investment Opportunities</h2>
      
      <div className="opportunities-grid">
        {opportunities.map((opportunity) => (
          <div key={opportunity.id} className="opportunity-card">
            <div className="nft-preview">
              <img 
                src={opportunity.nftImageUrl} 
                alt={`NFT representation of ${opportunity.name}`}
                onError={(e) => {
                  e.target.src = 'placeholder-nft.png';
                }}
              />
            </div>
            
            <div className="opportunity-details">
              <h3>{opportunity.name}</h3>
              <p>{opportunity.description}</p>
              
              <div className="funding-details">
                <div>
                  <span>Valuation:</span>
                  <span>{opportunity.valuation} ETH</span>
                </div>
                <div>
                  <span>Goal:</span>
                  <span>{opportunity.totalFundingGoal} ETH</span>
                </div>
                <div>
                  <span>Raised:</span>
                  <span>{opportunity.currentFunding} ETH</span>
                </div>
                <div>
                  <span>Min Investment:</span>
                  <span>{opportunity.minInvestment} ETH</span>
                </div>
                <div>
                  <span>Available Shares:</span>
                  <span>{opportunity.availableShares}</span>
                </div>
                <div>
                  <span>Deadline:</span>
                  <span>{opportunity.deadline}</span>
                </div>
              </div>
              
              <div className="investment-form">
                <input
                  type="number"
                  min={opportunity.minInvestment}
                  step="0.01"
                  placeholder={`Min ${opportunity.minInvestment} ETH`}
                />
                <button 
                  onClick={() => handleInvest(
                    opportunity.id, 
                    document.querySelector(`#invest-${opportunity.id}`).value
                  )}
                >
                  Invest
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default InvestmentOpportunities;
```

```css
/* InvestmentOpportunities.css */
.opportunities-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.opportunities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.opportunity-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.opportunity-card:hover {
  transform: translateY(-5px);
}

.nft-preview img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.opportunity-details {
  padding: 1.5rem;
}

.opportunity-details h3 {
  margin-top: 0;
  color: #333;
}

.funding-details {
  margin: 1.5rem 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.funding-details div {
  display: flex;
  justify-content: space-between;
}

.funding-details span:first-child {
  font-weight: bold;
  color: #666;
}

.investment-form {
  display: flex;
  gap: 0.5rem;
}

.investment-form input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.investment-form button {
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.investment-form button:hover {
  background-color: #45a049;
}

.loading {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}

.error {
  text-align: center;
  padding: 2rem;
  color: #d32f2f;
  font-size: 1.2rem;
}
```
