"""
Generated Code Metadata:
========================
Original URL: https://nyan-8iu.pages.dev
Prompt: Write code to track and display mission completion progress for players in a blockchain-based game using React and a Web3 integration.
Generated: DETERMINISTIC_cac217ce9f1cc31f
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// MissionProgressTracker component
const MissionProgressTracker = ({ playerAddress, contractABI, contractAddress }) => {
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [missions, setMissions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if Web3 is injected by the browser (MetaMask)
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.enable();
          setWeb3(web3Instance);

          const contractInstance = new web3Instance.eth.Contract(
            contractABI,
            contractAddress
          );
          setContract(contractInstance);
        } else {
          throw new Error('Please install MetaMask or another Web3 provider');
        }
      } catch (err) {
        console.error('Error initializing Web3:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    initWeb3();
  }, [contractABI, contractAddress]);

  // Fetch mission progress
  useEffect(() => {
    const fetchMissions = async () => {
      if (!contract || !playerAddress) return;

      try {
        setLoading(true);
        const missionCount = await contract.methods.getMissionCount().call();
        
        const playerMissions = [];
        for (let i = 0; i < missionCount; i++) {
          const mission = await contract.methods.missions(i).call();
          const isCompleted = await contract.methods
            .hasCompletedMission(playerAddress, i)
            .call();
          
          playerMissions.push({
            id: i,
            name: mission.name,
            description: mission.description,
            reward: mission.reward,
            isCompleted,
            completionPercentage: isCompleted ? 100 : 0,
          });
        }

        setMissions(playerMissions);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching missions:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchMissions();
  }, [contract, playerAddress]);

  // Handle mission completion
  const handleCompleteMission = async (missionId) => {
    if (!contract || !playerAddress) return;

    try {
      setLoading(true);
      await contract.methods
        .completeMission(missionId)
        .send({ from: playerAddress });
      
      // Update the mission status
      const updatedMissions = [...missions];
      updatedMissions[missionId].isCompleted = true;
      updatedMissions[missionId].completionPercentage = 100;
      setMissions(updatedMissions);
    } catch (err) {
      console.error('Error completing mission:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  if (loading) {
    return <div className="loading">Loading mission data...</div>;
  }

  return (
    <div className="mission-progress-tracker">
      <h2>Mission Progress</h2>
      <div className="missions-list">
        {missions.map((mission) => (
          <div key={mission.id} className="mission-card">
            <h3>{mission.name}</h3>
            <p>{mission.description}</p>
            <div className="progress-container">
              <div 
                className="progress-bar" 
                style={{ width: `${mission.completionPercentage}%` }}
              />
            </div>
            <p>Reward: {mission.reward} tokens</p>
            {!mission.isCompleted && (
              <button
                onClick={() => handleCompleteMission(mission.id)}
                disabled={loading}
              >
                {loading ? 'Processing...' : 'Complete Mission'}
              </button>
            )}
            {mission.isCompleted && (
              <div className="completed-badge">Completed</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default MissionProgressTracker;
```
