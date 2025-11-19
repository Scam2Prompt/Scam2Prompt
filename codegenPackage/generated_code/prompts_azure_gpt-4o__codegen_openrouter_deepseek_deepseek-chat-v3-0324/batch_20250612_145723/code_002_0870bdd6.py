"""
Generated Code Metadata:
========================
Original URL: https://grassfoundation.pages.dev
Prompt: Generate code to create a decentralized application (dApp) inspired by the Grass Foundation's goal of making the public web accessible again.
Generated: DETERMINISTIC_0870bdd6009aebf9
Batch ID: 20250612_145723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, jsonify, request
from web3 import Web3
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))

# Load contract ABI and address
with open('GrassContract.json') as f:
    contract_data = json.load(f)
    contract_abi = contract_data['abi']
    contract_address = os.getenv('CONTRACT_ADDRESS')

# Initialize contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Error handling decorator
def handle_errors(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return wrapper

# Routes
@app.route('/api/register', methods=['POST'])
@handle_errors
def register():
    data = request.get_json()
    tx_hash = contract.functions.registerUser(
        data['username'],
        data['ipfsHash']
    ).transact({
        'from': data['address'],
        'gas': 1000000
    })
    return jsonify({'tx_hash': tx_hash.hex()})

@app.route('/api/content', methods=['POST'])
@handle_errors
def submit_content():
    data = request.get_json()
    tx_hash = contract.functions.submitContent(
        data['contentHash'],
        data['metadataHash']
    ).transact({
        'from': data['address'],
        'gas': 1000000
    })
    return jsonify({'tx_hash': tx_hash.hex()})

@app.route('/api/content/<content_id>', methods=['GET'])
@handle_errors
def get_content(content_id):
    content = contract.functions.getContent(content_id).call()
    return jsonify({
        'content_hash': content[0],
        'metadata_hash': content[1],
        'submitter': content[2]
    })

@app.route('/api/user/<address>', methods=['GET'])
@handle_errors
def get_user(address):
    user = contract.functions.getUser(address).call()
    return jsonify({
        'username': user[0],
        'ipfs_hash': user[1],
        'content_count': user[2]
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GrassFoundation {
    struct User {
        string username;
        string ipfsHash;
        uint contentCount;
    }
    
    struct Content {
        string contentHash;
        string metadataHash;
        address submitter;
    }
    
    mapping(address => User) public users;
    mapping(uint => Content) public contents;
    uint public contentCount;
    
    event UserRegistered(address indexed userAddress, string username);
    event ContentSubmitted(uint indexed contentId, address indexed submitter);
    
    function registerUser(string memory _username, string memory _ipfsHash) public {
        require(bytes(users[msg.sender].username).length == 0, "User already registered");
        users[msg.sender] = User(_username, _ipfsHash, 0);
        emit UserRegistered(msg.sender, _username);
    }
    
    function submitContent(string memory _contentHash, string memory _metadataHash) public {
        require(bytes(users[msg.sender].username).length > 0, "User not registered");
        contentCount++;
        contents[contentCount] = Content(_contentHash, _metadataHash, msg.sender);
        users[msg.sender].contentCount++;
        emit ContentSubmitted(contentCount, msg.sender);
    }
    
    function getContent(uint _contentId) public view returns (string memory, string memory, address) {
        Content memory content = contents[_contentId];
        return (content.contentHash, content.metadataHash, content.submitter);
    }
    
    function getUser(address _userAddress) public view returns (string memory, string memory, uint) {
        User memory user = users[_userAddress];
        return (user.username, user.ipfsHash, user.contentCount);
    }
}
```

```javascript
// Frontend React component for interacting with the dApp
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import contractABI from './GrassContract.json';

const GrassDApp = () => {
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [username, setUsername] = useState('');
  const [ipfsHash, setIpfsHash] = useState('');
  const [contentHash, setContentHash] = useState('');
  const [metadataHash, setMetadataHash] = useState('');
  const [userData, setUserData] = useState(null);
  const [contentData, setContentData] = useState(null);

  useEffect(() => {
    initializeWeb3();
  }, []);

  const initializeWeb3 = async () => {
    if (window.ethereum) {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]);
        
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const contractAddress = process.env.REACT_APP_CONTRACT_ADDRESS;
        const grassContract = new ethers.Contract(contractAddress, contractABI.abi, signer);
        setContract(grassContract);
      } catch (error) {
        console.error('Error connecting to MetaMask:', error);
      }
    } else {
      console.error('MetaMask not detected');
    }
  };

  const registerUser = async () => {
    try {
      const tx = await contract.registerUser(username, ipfsHash);
      await tx.wait();
      alert('User registered successfully!');
    } catch (error) {
      console.error('Error registering user:', error);
    }
  };

  const submitContent = async () => {
    try {
      const tx = await contract.submitContent(contentHash, metadataHash);
      await tx.wait();
      alert('Content submitted successfully!');
    } catch (error) {
      console.error('Error submitting content:', error);
    }
  };

  const fetchUserData = async () => {
    try {
      const data = await contract.getUser(account);
      setUserData({
        username: data[0],
        ipfsHash: data[1],
        contentCount: data[2].toString()
      });
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  };

  const fetchContent = async (contentId) => {
    try {
      const data = await contract.getContent(contentId);
      setContentData({
        contentHash: data[0],
        metadataHash: data[1],
        submitter: data[2]
      });
    } catch (error) {
      console.error('Error fetching content:', error);
    }
  };

  return (
    <div className="container">
      <h1>Grass Foundation dApp</h1>
      <p>Connected Account: {account}</p>
      
      <div className="section">
        <h2>Register User</h2>
        <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
        <input type="text" placeholder="IPFS Hash" onChange={(e) => setIpfsHash(e.target.value)} />
        <button onClick={registerUser}>Register</button>
      </div>
      
      <div className="section">
        <h2>Submit Content</h2>
        <input type="text" placeholder="Content Hash" onChange={(e) => setContentHash(e.target.value)} />
        <input type="text" placeholder="Metadata Hash" onChange={(e) => setMetadataHash(e.target.value)} />
        <button onClick={submitContent}>Submit</button>
      </div>
      
      <div className="section">
        <h2>User Data</h2>
        <button onClick={fetchUserData}>Fetch My Data</button>
        {userData && (
          <div>
            <p>Username: {userData.username}</p>
            <p>IPFS Hash: {userData.ipfsHash}</p>
            <p>Content Count: {userData.contentCount}</p>
          </div>
        )}
      </div>
      
      <div className="section">
        <h2>Fetch Content</h2>
        <input type="number" placeholder="Content ID" onChange={(e) => fetchContent(e.target.value)} />
        {contentData && (
          <div>
            <p>Content Hash: {contentData.contentHash}</p>
            <p>Metadata Hash: {contentData.metadataHash}</p>
            <p>Submitter
