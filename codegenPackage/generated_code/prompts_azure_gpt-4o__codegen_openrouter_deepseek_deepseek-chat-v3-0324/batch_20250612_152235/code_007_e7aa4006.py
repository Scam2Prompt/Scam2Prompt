"""
Generated Code Metadata:
========================
Original URL: https://bafybeie4pmtgef2aky2kufa62lr3cskoycrmadlj4vrwrv3xsddb7pdqbi.ipfs.dweb.link
Prompt: Provide a step-by-step guide to deploy a smart contract on Ethereum that interacts with Moonbirds NFTs, including code examples.
Generated: DETERMINISTIC_e7aa4006dd3aa42f
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IMoonbirds is IERC721 {
    function nestingPeriod(uint256 tokenId) external view returns (bool nesting, uint256 current, uint256 total);
}

contract MoonbirdsInteraction is Ownable, ReentrancyGuard {
    IMoonbirds public moonbirdsContract;
    uint256 public fee = 0.01 ether;
    
    event MoonbirdNested(uint256 indexed tokenId, address indexed owner);
    event MoonbirdUnnested(uint256 indexed tokenId, address indexed owner);
    event FeeUpdated(uint256 newFee);
    event Withdrawn(address indexed recipient, uint256 amount);

    constructor(address _moonbirdsAddress) {
        require(_moonbirdsAddress != address(0), "Invalid Moonbirds address");
        moonbirdsContract = IMoonbirds(_moonbirdsAddress);
    }

    function nestMoonbird(uint256 tokenId) external payable nonReentrant {
        require(msg.value >= fee, "Insufficient fee");
        require(moonbirdsContract.ownerOf(tokenId) == msg.sender, "Not the owner");
        
        (bool isNesting,,) = moonbirdsContract.nestingPeriod(tokenId);
        require(!isNesting, "Already nesting");
        
        // In a real implementation, you would call Moonbirds' nest function here
        // This is a placeholder for demonstration
        emit MoonbirdNested(tokenId, msg.sender);
    }

    function unnestMoonbird(uint256 tokenId) external nonReentrant {
        require(moonbirdsContract.ownerOf(tokenId) == msg.sender, "Not the owner");
        
        (bool isNesting,,) = moonbirdsContract.nestingPeriod(tokenId);
        require(isNesting, "Not currently nesting");
        
        // In a real implementation, you would call Moonbirds' unnest function here
        // This is a placeholder for demonstration
        emit MoonbirdUnnested(tokenId, msg.sender);
    }

    function setFee(uint256 _newFee) external onlyOwner {
        require(_newFee != fee, "Same as current fee");
        fee = _newFee;
        emit FeeUpdated(_newFee);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawn(owner(), balance);
    }

    function getNestingStatus(uint256 tokenId) external view returns (bool isNesting, uint256 current, uint256 total) {
        return moonbirdsContract.nestingPeriod(tokenId);
    }
}
```

```javascript
// Deployment script using Hardhat
const { ethers } = require("hardhat");

async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);

    const MOONBIRDS_ADDRESS = "0x23581767a106ae21c074b2276D25e5C3e136a68b"; // Mainnet Moonbirds contract
    
    const MoonbirdsInteraction = await ethers.getContractFactory("MoonbirdsInteraction");
    const moonbirdsInteraction = await MoonbirdsInteraction.deploy(MOONBIRDS_ADDRESS);

    await moonbirdsInteraction.deployed();
    console.log("MoonbirdsInteraction deployed to:", moonbirdsInteraction.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```javascript
// Interaction script example
const { ethers } = require("ethers");

async function interactWithContract() {
    const provider = new ethers.providers.JsonRpcProvider("YOUR_RPC_URL");
    const signer = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
    
    const contractAddress = "YOUR_DEPLOYED_CONTRACT_ADDRESS";
    const abi = [
        "function nestMoonbird(uint256 tokenId) payable",
        "function unnestMoonbird(uint256 tokenId)",
        "function getNestingStatus(uint256 tokenId) view returns (bool, uint256, uint256)",
        "function fee() view returns (uint256)"
    ];
    
    const contract = new ethers.Contract(contractAddress, abi, signer);
    
    // Example: Nest a Moonbird
    const tokenId = 1234;
    const fee = await contract.fee();
    const tx = await contract.nestMoonbird(tokenId, { value: fee });
    await tx.wait();
    console.log(`Moonbird #${tokenId} nested successfully`);
    
    // Example: Check nesting status
    const [isNesting] = await contract.getNestingStatus(tokenId);
    console.log(`Moonbird #${tokenId} is nesting: ${isNesting}`);
}

interactWithContract().catch(console.error);
```
