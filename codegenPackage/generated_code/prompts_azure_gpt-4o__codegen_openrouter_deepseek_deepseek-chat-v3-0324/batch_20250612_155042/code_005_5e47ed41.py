"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Build a React component that visualizes the "Fortune favors the wise" gameplay mechanic, showing the balance between resource protection and risk-taking.
Generated: DETERMINISTIC_5e47ed41b2cf6d9d
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * FortuneFavorsTheWise Component
 * Visualizes the balance between resource protection and risk-taking.
 * 
 * @param {number} initialResources - Initial amount of resources
 * @param {number} riskFactor - Multiplier for potential gains/losses (default: 1.5)
 * @param {number} maxTurns - Maximum number of turns in the game (default: 10)
 */
const FortuneFavorsTheWise = ({
  initialResources = 100,
  riskFactor = 1.5,
  maxTurns = 10
}) => {
  const [resources, setResources] = useState(initialResources);
  const [turn, setTurn] = useState(1);
  const [history, setHistory] = useState([{ turn: 0, resources: initialResources, action: 'Initial' }]);
  const [gameOver, setGameOver] = useState(false);
  const [message, setMessage] = useState('');

  // Handle risk action
  const takeRisk = () => {
    if (gameOver) return;

    const riskOutcome = Math.random() > 0.5 ? 'win' : 'lose';
    const amount = Math.floor(resources * 0.3); // Risk 30% of current resources
    let newResources = resources;

    if (riskOutcome === 'win') {
      newResources += Math.floor(amount * riskFactor);
      setMessage(`Risk paid off! Gained ${Math.floor(amount * riskFactor)} resources.`);
    } else {
      newResources -= amount;
      setMessage(`Risk failed! Lost ${amount} resources.`);
    }

    updateGameState(newResources, `Risk (${riskOutcome})`);
  };

  // Handle safe action
  const playSafe = () => {
    if (gameOver) return;

    const gain = Math.floor(resources * 0.1); // Gain 10% of current resources
    const newResources = resources + gain;
    setMessage(`Played safe. Gained ${gain} resources.`);
    updateGameState(newResources, 'Safe');
  };

  // Update game state after each action
  const updateGameState = (newResources, action) => {
    const newTurn = turn + 1;
    
    setResources(newResources);
    setTurn(newTurn);
    setHistory([...history, { turn, resources: newResources, action }]);

    // Check game over conditions
    if (newResources <= 0) {
      setGameOver(true);
      setMessage('Game Over! You ran out of resources.');
    } else if (newTurn > maxTurns) {
      setGameOver(true);
      setMessage(`Game Over! Final score: ${newResources}`);
    }
  };

  // Reset game to initial state
  const resetGame = () => {
    setResources(initialResources);
    setTurn(1);
    setHistory([{ turn: 0, resources: initialResources, action: 'Initial' }]);
    setGameOver(false);
    setMessage('');
  };

  return (
    <div className="fortune-game">
      <h2>Fortune Favors the Wise</h2>
      <div className="game-stats">
        <p>Turn: {turn}/{maxTurns}</p>
        <p>Resources: {resources}</p>
        <p className="message">{message}</p>
      </div>

      <div className="game-actions">
        <button 
          onClick={takeRisk} 
          disabled={gameOver}
          className="risk-button"
        >
          Take Risk (30%)
        </button>
        <button 
          onClick={playSafe} 
          disabled={gameOver}
          className="safe-button"
        >
          Play Safe (10%)
        </button>
        <button onClick={resetGame} className="reset-button">
          Reset Game
        </button>
      </div>

      <div className="game-history">
        <h3>History</h3>
        <ul>
          {history.map((entry, index) => (
            <li key={index}>
              Turn {entry.turn}: {entry.action} → {entry.resources} resources
            </li>
          ))}
        </ul>
      </div>

      <style jsx>{`
        .fortune-game {
          max-width: 600px;
          margin: 0 auto;
          padding: 20px;
          font-family: Arial, sans-serif;
          border: 1px solid #ddd;
          border-radius: 8px;
          background-color: #f9f9f9;
        }
        .game-stats {
          margin-bottom: 20px;
          padding: 10px;
          background-color: #fff;
          border-radius: 4px;
        }
        .game-actions {
          display: flex;
          gap: 10px;
          margin-bottom: 20px;
        }
        button {
          padding: 8px 16px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-weight: bold;
        }
        .risk-button {
          background-color: #ff6b6b;
          color: white;
        }
        .safe-button {
          background-color: #51cf66;
          color: white;
        }
        .reset-button {
          background-color: #339af0;
          color: white;
        }
        button:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }
        .message {
          font-style: italic;
          color: #495057;
        }
        .game-history {
          padding: 10px;
          background-color: #fff;
          border-radius: 4px;
        }
        .game-history ul {
          list-style-type: none;
          padding: 0;
        }
        .game-history li {
          padding: 5px 0;
          border-bottom: 1px solid #eee;
        }
      `}</style>
    </div>
  );
};

FortuneFavorsTheWise.propTypes = {
  initialResources: PropTypes.number,
  riskFactor: PropTypes.number,
  maxTurns: PropTypes.number
};

export default FortuneFavorsTheWise;
```
