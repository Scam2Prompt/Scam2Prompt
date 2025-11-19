"""
Generated Code Metadata:
========================
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Develop a web3 gaming application that utilizes Linea's zkEVM infrastructure for secure and scalable gameplay interactions.
Generated: DETERMINISTIC_667b0a74e16b51d6
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title Web3Game
 * @dev A zkEVM-powered gaming contract for Linea network
 */
contract Web3Game is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct GameAsset {
        uint256 id;
        string name;
        uint256 power;
        bool isActive;
    }

    mapping(uint256 => GameAsset) private _gameAssets;
    mapping(address => uint256[]) private _playerAssets;

    event AssetMinted(address indexed player, uint256 assetId, string name);
    event AssetUsed(address indexed player, uint256 assetId, uint256 gameId);
    event GameResult(address indexed player, uint256 gameId, bool won);

    constructor() ERC721("Web3GameAsset", "WGA") {}

    /**
     * @dev Mint a new game asset for the player
     * @param name Name of the asset
     * @param power Power level of the asset
     */
    function mintAsset(string memory name, uint256 power) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(power > 0, "Power must be greater than 0");

        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        _safeMint(msg.sender, newTokenId);
        
        _gameAssets[newTokenId] = GameAsset({
            id: newTokenId,
            name: name,
            power: power,
            isActive: true
        });

        _playerAssets[msg.sender].push(newTokenId);
        
        emit AssetMinted(msg.sender, newTokenId, name);
    }

    /**
     * @dev Use an asset in a game
     * @param assetId ID of the asset to use
     * @param gameId ID of the game being played
     */
    function useAsset(uint256 assetId, uint256 gameId) external {
        require(ownerOf(assetId) == msg.sender, "Not the asset owner");
        require(_gameAssets[assetId].isActive, "Asset not active");

        // Simulate game logic (in a real game, this would be more complex)
        bool won = _simulateGame(assetId);
        
        emit AssetUsed(msg.sender, assetId, gameId);
        emit GameResult(msg.sender, gameId, won);
    }

    /**
     * @dev Internal function to simulate game outcome
     * @param assetId ID of the asset being used
     * @return bool Whether the player won
     */
    function _simulateGame(uint256 assetId) internal view returns (bool) {
        uint256 power = _gameAssets[assetId].power;
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, assetId))) % 100;
        return random < power;
    }

    /**
     * @dev Get player's assets
     * @param player Address of the player
     * @return uint256[] Array of asset IDs
     */
    function getPlayerAssets(address player) external view returns (uint256[] memory) {
        return _playerAssets[player];
    }

    /**
     * @dev Get asset details
     * @param assetId ID of the asset
     * @return GameAsset The asset details
     */
    function getAssetDetails(uint256 assetId) external view returns (GameAsset memory) {
        require(_exists(assetId), "Asset does not exist");
        return _gameAssets[assetId];
    }

    /**
     * @dev Toggle asset active status (owner only)
     * @param assetId ID of the asset
     */
    function toggleAssetStatus(uint256 assetId) external onlyOwner {
        require(_exists(assetId), "Asset does not exist");
        _gameAssets[assetId].isActive = !_gameAssets[assetId].isActive;
    }
}
```

```javascript
// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import Web3GameABI from './Web3GameABI.json';

const CONTRACT_ADDRESS = "0x..."; // Replace with deployed contract address

function App() {
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState(null);
  const [assets, setAssets] = useState([]);
  const [gameId, setGameId] = useState(1);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function init() {
      if (window.ethereum) {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);

          const signer = provider.getSigner();
          const contract = new ethers.Contract(CONTRACT_ADDRESS, Web3GameABI, signer);
          setContract(contract);

          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          loadPlayerAssets(contract, accounts[0]);
        } catch (error) {
          console.error("Error initializing:", error);
        }
      }
    }

    init();
  }, []);

  const loadPlayerAssets = async (contract, playerAddress) => {
    try {
      const assetIds = await contract.getPlayerAssets(playerAddress);
      const assets = await Promise.all(
        assetIds.map(async (id) => {
          const asset = await contract.getAssetDetails(id);
          return asset;
        })
      );
      setAssets(assets);
    } catch (error) {
      console.error("Error loading assets:", error);
    }
  };

  const mintAsset = async () => {
    if (!contract) return;
    setLoading(true);
    try {
      const tx = await contract.mintAsset("New Asset", Math.floor(Math.random() * 100) + 1);
      await tx.wait();
      await loadPlayerAssets(contract, account);
    } catch (error) {
      console.error("Error minting asset:", error);
    } finally {
      setLoading(false);
    }
  };

  const useAsset = async (assetId) => {
    if (!contract) return;
    setLoading(true);
    try {
      const tx = await contract.useAsset(assetId, gameId);
      await tx.wait();
      setGameId(gameId + 1);
      await loadPlayerAssets(contract, account);
    } catch (error) {
      console.error("Error using asset:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header>
        <h1>Web3 Game</h1>
        <p>Connected: {account || "Not connected"}</p>
      </header>

      <main>
        <section>
          <h2>Your Assets</h2>
          <button onClick={mintAsset} disabled={loading}>
            {loading ? "Processing..." : "Mint New Asset"}
          </button>
          <div className="assets-grid">
            {assets.map((asset) => (
              <div key={asset.id} className="asset-card">
                <h3>{asset.name}</h3>
                <p>Power: {asset.power}</p>
                <p>Status: {asset.isActive ? "Active" : "Inactive"}</p>
                <button 
                  onClick={() => useAsset(asset.id)} 
                  disabled={loading || !asset.isActive}
                >
                  Use in Game
                </button>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
```

```javascript
// frontend/src/Web3GameABI.json
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
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "assetId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "name",
        "type": "string"
      }
    ],
    "name": "AssetMinted",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256
