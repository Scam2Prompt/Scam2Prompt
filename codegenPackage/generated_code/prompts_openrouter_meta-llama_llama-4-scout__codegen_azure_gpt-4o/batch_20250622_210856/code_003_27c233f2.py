"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-indol.vercel.app
Prompt: Design a staking and locking mechanism for NFTs, similar to Lifinity Flares, using a programming language of your choice, ensuring that the NFTs can be purchased and managed through a user interface.
Generated: DETERMINISTIC_27c233f2ea3dc4b1
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of an NFT staking and locking mechanism using Solidity (for Ethereum smart contracts) and JavaScript (for the user interface). Solidity handles the blockchain logic, while JavaScript provides the user interface for purchasing and managing NFTs.

---

### Solidity Smart Contract: `NFTStaking.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTStaking is ERC721Enumerable, Ownable {
    // Struct to store staking details
    struct Stake {
        uint256 tokenId;
        uint256 stakedAt;
        uint256 lockPeriod; // Lock period in seconds
    }

    // Mapping of staked NFTs
    mapping(address => Stake[]) public stakes;

    // Event declarations
    event NFTStaked(address indexed user, uint256 tokenId, uint256 lockPeriod);
    event NFTUnstaked(address indexed user, uint256 tokenId);

    constructor() ERC721("StakableNFT", "SNFT") {}

    // Mint function to allow users to purchase NFTs
    function mintNFT() external payable {
        require(msg.value == 0.01 ether, "Minting fee is 0.01 ETH");
        uint256 tokenId = totalSupply() + 1;
        _safeMint(msg.sender, tokenId);
    }

    // Stake function to lock an NFT
    function stakeNFT(uint256 tokenId, uint256 lockPeriod) external {
        require(ownerOf(tokenId) == msg.sender, "You must own the NFT to stake it");
        require(lockPeriod > 0, "Lock period must be greater than 0");

        // Transfer NFT to the contract
        _transfer(msg.sender, address(this), tokenId);

        // Record staking details
        stakes[msg.sender].push(Stake(tokenId, block.timestamp, lockPeriod));

        emit NFTStaked(msg.sender, tokenId, lockPeriod);
    }

    // Unstake function to unlock an NFT
    function unstakeNFT(uint256 tokenId) external {
        Stake[] storage userStakes = stakes[msg.sender];
        bool found = false;

        for (uint256 i = 0; i < userStakes.length; i++) {
            if (userStakes[i].tokenId == tokenId) {
                require(block.timestamp >= userStakes[i].stakedAt + userStakes[i].lockPeriod, "Lock period not yet expired");

                // Remove the stake
                userStakes[i] = userStakes[userStakes.length - 1];
                userStakes.pop();

                // Transfer NFT back to the user
                _transfer(address(this), msg.sender, tokenId);

                emit NFTUnstaked(msg.sender, tokenId);
                found = true;
                break;
            }
        }

        require(found, "NFT not found in stakes");
    }

    // Function to view staked NFTs for a user
    function getStakedNFTs(address user) external view returns (Stake[] memory) {
        return stakes[user];
    }

    // Withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```

---

### JavaScript Frontend: `index.js`

```javascript
// Import required libraries
import Web3 from "web3";
import NFTStakingABI from "./NFTStakingABI.json"; // ABI of the smart contract

// Initialize Web3 and contract instance
const web3 = new Web3(window.ethereum);
const contractAddress = "0xYourContractAddressHere"; // Replace with deployed contract address
const nftStakingContract = new web3.eth.Contract(NFTStakingABI, contractAddress);

// Connect wallet
async function connectWallet() {
  const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
  return accounts[0];
}

// Mint NFT
async function mintNFT() {
  const account = await connectWallet();
  const mintFee = web3.utils.toWei("0.01", "ether");

  try {
    await nftStakingContract.methods.mintNFT().send({ from: account, value: mintFee });
    alert("NFT minted successfully!");
  } catch (error) {
    console.error("Error minting NFT:", error);
    alert("Failed to mint NFT.");
  }
}

// Stake NFT
async function stakeNFT(tokenId, lockPeriod) {
  const account = await connectWallet();

  try {
    await nftStakingContract.methods.stakeNFT(tokenId, lockPeriod).send({ from: account });
    alert("NFT staked successfully!");
  } catch (error) {
    console.error("Error staking NFT:", error);
    alert("Failed to stake NFT.");
  }
}

// Unstake NFT
async function unstakeNFT(tokenId) {
  const account = await connectWallet();

  try {
    await nftStakingContract.methods.unstakeNFT(tokenId).send({ from: account });
    alert("NFT unstaked successfully!");
  } catch (error) {
    console.error("Error unstaking NFT:", error);
    alert("Failed to unstake NFT.");
  }
}

// Get staked NFTs
async function getStakedNFTs() {
  const account = await connectWallet();

  try {
    const stakedNFTs = await nftStakingContract.methods.getStakedNFTs(account).call();
    console.log("Staked NFTs:", stakedNFTs);
    return stakedNFTs;
  } catch (error) {
    console.error("Error fetching staked NFTs:", error);
    alert("Failed to fetch staked NFTs.");
  }
}

// Example usage
document.getElementById("mintButton").addEventListener("click", mintNFT);
document.getElementById("stakeButton").addEventListener("click", () => {
  const tokenId = document.getElementById("tokenIdInput").value;
  const lockPeriod = document.getElementById("lockPeriodInput").value;
  stakeNFT(tokenId, lockPeriod);
});
document.getElementById("unstakeButton").addEventListener("click", () => {
  const tokenId = document.getElementById("tokenIdInput").value;
  unstakeNFT(tokenId);
});
document.getElementById("getStakedButton").addEventListener("click", async () => {
  const stakedNFTs = await getStakedNFTs();
  console.log(stakedNFTs);
});
```

---

### HTML Frontend: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NFT Staking</title>
</head>
<body>
  <h1>NFT Staking and Locking</h1>
  <button id="mintButton">Mint NFT</button>
  <br><br>
  <input type="text" id="tokenIdInput" placeholder="Token ID">
  <input type="text" id="lockPeriodInput" placeholder="Lock Period (seconds)">
  <button id="stakeButton">Stake NFT</button>
  <button id="unstakeButton">Unstake NFT</button>
  <button id="getStakedButton">Get Staked NFTs</button>
  <script src="index.js"></script>
</body>
</html>
```

---

### Notes:
1. Replace `0xYourContractAddressHere` with the actual deployed contract address.
2. Ensure the ABI file (`NFTStakingABI.json`) is generated after deploying the contract.
3. Use a development environment like Hardhat or Truffle for deploying the contract.
