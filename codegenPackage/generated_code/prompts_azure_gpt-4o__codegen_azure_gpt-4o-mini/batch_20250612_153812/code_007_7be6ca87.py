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
// Smart Contract: CheemsCharacter.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract CheemsCharacter is Ownable {
    struct Character {
        string name;
        string familyBackground;
        string characteristics;
        string props;
        string skills;
    }

    mapping(uint256 => Character) private characters;
    uint256 public characterCount;

    event CharacterCreated(uint256 id, string name);

    // Function to create a new character
    function createCharacter(
        string memory _name,
        string memory _familyBackground,
        string memory _characteristics,
        string memory _props,
        string memory _skills
    ) public onlyOwner {
        characterCount++;
        characters[characterCount] = Character(_name, _familyBackground, _characteristics, _props, _skills);
        emit CharacterCreated(characterCount, _name);
    }

    // Function to retrieve character details
    function getCharacter(uint256 _id) public view returns (Character memory) {
        require(_id > 0 && _id <= characterCount, "Character does not exist");
        return characters[_id];
    }
}
```

```javascript
// Frontend: App.js
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import CheemsCharacterContract from './CheemsCharacter.json'; // ABI file

const App = () => {
    const [account, setAccount] = useState('');
    const [contract, setContract] = useState(null);
    const [characters, setCharacters] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const init = async () => {
            // Check if MetaMask is installed
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const accounts = await web3.eth.getAccounts();
                setAccount(accounts[0]);

                const networkId = await web3.eth.net.getId();
                const deployedNetwork = CheemsCharacterContract.networks[networkId];
                const instance = new web3.eth.Contract(
                    CheemsCharacterContract.abi,
                    deployedNetwork && deployedNetwork.address,
                );
                setContract(instance);
                await loadCharacters(instance);
            } else {
                alert('Please install MetaMask to use this dApp');
            }
        };
        init();
    }, []);

    const loadCharacters = async (contract) => {
        const count = await contract.methods.characterCount().call();
        const loadedCharacters = [];
        for (let i = 1; i <= count; i++) {
            const character = await contract.methods.getCharacter(i).call();
            loadedCharacters.push(character);
        }
        setCharacters(loadedCharacters);
        setLoading(false);
    };

    const createCharacter = async (name, familyBackground, characteristics, props, skills) => {
        if (!contract) return;
        try {
            await contract.methods.createCharacter(name, familyBackground, characteristics, props, skills).send({ from: account });
            await loadCharacters(contract);
        } catch (error) {
            console.error("Error creating character:", error);
        }
    };

    return (
        <div>
            <h1>Cheems Characters</h1>
            <h2>Account: {account}</h2>
            {loading ? (
                <p>Loading characters...</p>
            ) : (
                <ul>
                    {characters.map((char, index) => (
                        <li key={index}>
                            <h3>{char.name}</h3>
                            <p>Family Background: {char.familyBackground}</p>
                            <p>Characteristics: {char.characteristics}</p>
                            <p>Props: {char.props}</p>
                            <p>Skills: {char.skills}</p>
                        </li>
                    ))}
                </ul>
            )}
            {/* Add a form to create a new character */}
            <button onClick={() => createCharacter("Cheems", "Cheems Family", "Funny", "Hat", "Barking")}>
                Create Cheems Character
            </button>
        </div>
    );
};

export default App;
```

```json
// package.json
{
  "name": "cheems-dapp",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "web3": "^1.6.1",
    "openzeppelin-solidity": "^4.3.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

```bash
# Instructions to deploy the smart contract
# 1. Install Truffle or Hardhat for smart contract development.
# 2. Compile the smart contract using `truffle compile` or `npx hardhat compile`.
# 3. Deploy the contract to a test network using `truffle migrate` or `npx hardhat run scripts/deploy.js`.
# 4. Update the ABI and contract address in the frontend code.
# 5. Run the React app using `npm start`.
```
