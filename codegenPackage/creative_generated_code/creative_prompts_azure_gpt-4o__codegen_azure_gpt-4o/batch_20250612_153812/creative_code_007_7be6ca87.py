"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Build a decentralized application (dApp) that showcases the family background, characteristics, props, and skills of Cheems characters. Use React for the frontend and Ethereum smart contracts for the backend.
Generated: DETERMINISTIC_7be6ca87f9a0aa94
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Smart Contract (Solidity)

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CheemsCharacterRegistry
 * @dev A smart contract to store and retrieve Cheems character data.
 */
contract CheemsCharacterRegistry {
    struct CheemsCharacter {
        string name;
        string familyBackground;
        string characteristics;
        string props;
        string skills;
    }

    // Array to store Cheems characters
    CheemsCharacter[] private characters;

    // Event emitted when a new character is added
    event CharacterAdded(uint256 indexed characterId, string name);

    /**
     * @dev Adds a new Cheems character to the registry.
     * @param name Name of the character.
     * @param familyBackground Family background of the character.
     * @param characteristics Characteristics of the character.
     * @param props Props associated with the character.
     * @param skills Skills possessed by the character.
     */
    function addCharacter(
        string memory name,
        string memory familyBackground,
        string memory characteristics,
        string memory props,
        string memory skills
    ) public {
        characters.push(
            CheemsCharacter(name, familyBackground, characteristics, props, skills)
        );
        emit CharacterAdded(characters.length - 1, name);
    }

    /**
     * @dev Retrieves a Cheems character by ID.
     * @param characterId ID of the character to retrieve.
     * @return All details of the requested character.
     */
    function getCharacter(uint256 characterId)
        public
        view
        returns (
            string memory name,
            string memory familyBackground,
            string memory characteristics,
            string memory props,
            string memory skills
        )
    {
        require(characterId < characters.length, "Character ID out of range.");
        CheemsCharacter storage character = characters[characterId];
        return (
            character.name,
            character.familyBackground,
            character.characteristics,
            character.props,
            character.skills
        );
    }

    /**
     * @dev Returns the total number of characters stored.
     * @return The number of characters in the registry.
     */
    function getCharacterCount() public view returns (uint256) {
        return characters.length;
    }
}

---

### Frontend (React.js)

```javascript
// App.js

import React, { useState, useEffect } from "react";
import Web3 from "web3";
import CheemsCharacterRegistryABI from "./CheemsCharacterRegistryABI.json";

// Contract details
const contractAddress = "0xYourContractAddressHere"; // Replace with deployed contract address
const contractABI = CheemsCharacterRegistryABI;

function App() {
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [characters, setCharacters] = useState([]);
  const [newCharacter, setNewCharacter] = useState({
    name: "",
    familyBackground: "",
    characteristics: "",
    props: "",
    skills: "",
  });

  useEffect(() => {
    async function initWeb3() {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: "eth_requestAccounts" });
          const contractInstance = new web3Instance.eth.Contract(
            contractABI,
            contractAddress
          );
          setWeb3(web3Instance);
          setContract(contractInstance);
        } catch (error) {
          console.error("Error initializing web3:", error);
        }
      } else {
        console.error("Ethereum browser extension not found.");
      }
    }
    initWeb3();
  }, []);

  const fetchCharacters = async () => {
    if (contract) {
      try {
        const characterCount = await contract.methods.getCharacterCount().call();
        const fetchedCharacters = [];
        for (let i = 0; i < characterCount; i++) {
          const character = await contract.methods.getCharacter(i).call();
          fetchedCharacters.push(character);
        }
        setCharacters(fetchedCharacters);
      } catch (error) {
        console.error("Error fetching characters:", error);
      }
    }
  };

  const addCharacter = async () => {
    if (contract && web3) {
      try {
        const accounts = await web3.eth.getAccounts();
        await contract.methods
          .addCharacter(
            newCharacter.name,
            newCharacter.familyBackground,
            newCharacter.characteristics,
            newCharacter.props,
            newCharacter.skills
          )
          .send({ from: accounts[0] });
        setNewCharacter({
          name: "",
          familyBackground: "",
          characteristics: "",
          props: "",
          skills: "",
        });
        fetchCharacters(); // Refresh character list
      } catch (error) {
        console.error("Error adding character:", error);
      }
    }
  };

  return (
    <div>
      <h1>Cheems Character Registry</h1>
      <div>
        <h2>Add New Character</h2>
        <input
          type="text"
          placeholder="Name"
          value={newCharacter.name}
          onChange={(e) =>
            setNewCharacter({ ...newCharacter, name: e.target.value })
          }
        />
        <input
          type="text"
          placeholder="Family Background"
          value={newCharacter.familyBackground}
          onChange={(e) =>
            setNewCharacter({
              ...newCharacter,
              familyBackground: e.target.value,
            })
          }
        />
        <input
          type="text"
          placeholder="Characteristics"
          value={newCharacter.characteristics}
          onChange={(e) =>
            setNewCharacter({
              ...newCharacter,
              characteristics: e.target.value,
            })
          }
        />
        <input
          type="text"
          placeholder="Props"
          value={newCharacter.props}
          onChange={(e) =>
            setNewCharacter({ ...newCharacter, props: e.target.value })
          }
        />
        <input
          type="text"
          placeholder="Skills"
          value={newCharacter.skills}
          onChange={(e) =>
            setNewCharacter({ ...newCharacter, skills: e.target.value })
          }
        />
        <button onClick={addCharacter}>Add Character</button>
      </div>
      <div>
        <h2>Character List</h2>
        <button onClick={fetchCharacters}>Fetch Characters</button>
        <ul>
          {characters.map((character, index) => (
            <li key={index}>
              <strong>Name:</strong> {character[0]} <br />
              <strong>Family Background:</strong> {character[1]} <br />
              <strong>Characteristics:</strong> {character[2]} <br />
              <strong>Props:</strong> {character[3]} <br />
              <strong>Skills:</strong> {character[4]}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
```

---

### Notes

1. Replace `0xYourContractAddressHere` with the actual deployed address of the smart contract.
2. Save the ABI of the smart contract as `CheemsCharacterRegistryABI.json` in the same directory as `App.js`.
3. Ensure Metamask or another Ethereum provider is installed in the browser for testing the frontend locally.
4. Use a development environment like Ganache or a testnet like Rinkeby for proper testing.
