"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Build a decentralized application (dApp) that showcases the family background, characteristics, props, and skills of Cheems characters. Use React for the frontend and Ethereum smart contracts for the backend.
Generated: DETERMINISTIC_7be6ca87f9a0aa94
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: contracts/CheemsFamily.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CheemsFamily {
    struct CheemsCharacter {
        uint256 id;
        string name;
        string familyBackground;
        string[] characteristics;
        string[] props;
        string[] skills;
    }

    CheemsCharacter[] public characters;
    address public owner;

    event CharacterAdded(uint256 id, string name);
    event CharacterUpdated(uint256 id);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function addCharacter(
        string memory _name,
        string memory _familyBackground,
        string[] memory _characteristics,
        string[] memory _props,
        string[] memory _skills
    ) public onlyOwner {
        uint256 id = characters.length;
        characters.push(
            CheemsCharacter(
                id,
                _name,
                _familyBackground,
                _characteristics,
                _props,
                _skills
            )
        );
        emit CharacterAdded(id, _name);
    }

    function updateCharacter(
        uint256 _id,
        string memory _name,
        string memory _familyBackground,
        string[] memory _characteristics,
        string[] memory _props,
        string[] memory _skills
    ) public onlyOwner {
        require(_id < characters.length, "Character does not exist");
        CheemsCharacter storage character = characters[_id];
        character.name = _name;
        character.familyBackground = _familyBackground;
        character.characteristics = _characteristics;
        character.props = _props;
        character.skills = _skills;
        emit CharacterUpdated(_id);
    }

    function getCharacterCount() public view returns (uint256) {
        return characters.length;
    }

    function getCharacter(uint256 _id) public view returns (
        uint256,
        string memory,
        string memory,
        string[] memory,
        string[] memory,
        string[] memory
    ) {
        require(_id < characters.length, "Character does not exist");
        CheemsCharacter memory character = characters[_id];
        return (
            character.id,
            character.name,
            character.familyBackground,
            character.characteristics,
            character.props,
            character.skills
        );
    }
}
```

```javascript
// File: src/App.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import CheemsFamilyABI from './contracts/CheemsFamily.json';

const contractAddress = "YOUR_DEPLOYED_CONTRACT_ADDRESS";

function App() {
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState('');
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Form state
  const [name, setName] = useState('');
  const [familyBackground, setFamilyBackground] = useState('');
  const [characteristics, setCharacteristics] = useState('');
  const [props, setProps] = useState('');
  const [skills, setSkills] = useState('');

  useEffect(() => {
    const init = async () => {
      try {
        if (window.ethereum) {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);

          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          const signer = provider.getSigner();
          const contract = new ethers.Contract(contractAddress, CheemsFamilyABI.abi, signer);
          setContract(contract);

          await loadCharacters(contract);
        } else {
          setError('Please install MetaMask to use this dApp');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    init();
  }, []);

  const loadCharacters = async (contract) => {
    try {
      const count = await contract.getCharacterCount();
      const loadedCharacters = [];

      for (let i = 0; i < count; i++) {
        const character = await contract.getCharacter(i);
        loadedCharacters.push({
          id: character[0].toString(),
          name: character[1],
          familyBackground: character[2],
          characteristics: character[3],
          props: character[4],
          skills: character[5]
        });
      }

      setCharacters(loadedCharacters);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const characteristicsArray = characteristics.split(',').map(item => item.trim());
      const propsArray = props.split(',').map(item => item.trim());
      const skillsArray = skills.split(',').map(item => item.trim());

      await contract.addCharacter(
        name,
        familyBackground,
        characteristicsArray,
        propsArray,
        skillsArray
      );

      await loadCharacters(contract);
      
      // Reset form
      setName('');
      setFamilyBackground('');
      setCharacteristics('');
      setProps('');
      setSkills('');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="App">
      <header>
        <h1>Cheems Family dApp</h1>
        <p>Connected account: {account}</p>
      </header>

      <main>
        <section>
          <h2>Add New Character</h2>
          <form onSubmit={handleSubmit}>
            <div>
              <label>Name:</label>
              <input 
                type="text" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
                required 
              />
            </div>
            <div>
              <label>Family Background:</label>
              <textarea 
                value={familyBackground} 
                onChange={(e) => setFamilyBackground(e.target.value)} 
                required 
              />
            </div>
            <div>
              <label>Characteristics (comma separated):</label>
              <input 
                type="text" 
                value={characteristics} 
                onChange={(e) => setCharacteristics(e.target.value)} 
                required 
              />
            </div>
            <div>
              <label>Props (comma separated):</label>
              <input 
                type="text" 
                value={props} 
                onChange={(e) => setProps(e.target.value)} 
                required 
              />
            </div>
            <div>
              <label>Skills (comma separated):</label>
              <input 
                type="text" 
                value={skills} 
                onChange={(e) => setSkills(e.target.value)} 
                required 
              />
            </div>
            <button type="submit" disabled={loading}>
              {loading ? 'Processing...' : 'Add Character'}
            </button>
          </form>
        </section>

        <section>
          <h2>Cheems Characters</h2>
          {characters.length === 0 ? (
            <p>No characters found</p>
          ) : (
            <div className="characters-grid">
              {characters.map((character) => (
                <div key={character.id} className="character-card">
                  <h3>{character.name}</h3>
                  <p><strong>Family Background:</strong> {character.familyBackground}</p>
                  <div>
                    <strong>Characteristics:</strong>
                    <ul>
                      {character.characteristics.map((trait, index) => (
                        <li key={index}>{trait}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <strong>Props:</strong>
                    <ul>
                      {character.props.map((prop, index) => (
                        <li key={index}>{prop}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <strong>Skills:</strong>
                    <ul>
                      {character.skills.map((skill, index) => (
                        <li key={index}>{skill}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
```

```javascript
// File: src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
```

```javascript
// File: src/contracts/CheemsFamily.json
// This would be the ABI and bytecode from your compiled contract
// Replace with your actual contract ABI
{
  "abi": [
    // Your contract ABI
