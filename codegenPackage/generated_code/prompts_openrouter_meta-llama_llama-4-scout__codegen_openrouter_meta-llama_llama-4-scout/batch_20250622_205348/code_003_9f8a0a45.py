"""
Generated Code Metadata:
========================
Original URL: https://nft-staking-xi.vercel.app
Prompt: "How can I integrate NFT staking functionality, similar to nft-staking-xi.vercel.app, into my existing Dapp on the Polygon network?"
Generated: DETERMINISTIC_9f8a0a45399b1046
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**NFT Staking Contract (Solidity)**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title NFTStakingContract
 * @author [Your Name]
 * @notice NFT Staking contract for Polygon network
 */
contract NFTStakingContract is ReentrancyGuard {
    // Mapping of staked NFTs
    mapping(address => mapping(uint256 => StakedNFT)) public stakedNFTs;

    // Mapping of user staking balances
    mapping(address => uint256) public userBalances;

    // NFT contract address
    address public nftContractAddress;

    // Reward token contract address
    address public rewardTokenAddress;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Reward per second
    uint256 public rewardPerSecond;

    // Event emitted when NFT is staked
    event NFTStaked(address indexed user, uint256 tokenId);

    // Event emitted when NFT is unstaked
    event NFTUnstaked(address indexed user, uint256 tokenId);

    // Event emitted when reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @param _nftContractAddress NFT contract address
     * @param _rewardTokenAddress Reward token contract address
     * @param _stakingDuration Staking duration in seconds
     * @param _rewardPerSecond Reward per second
     */
    constructor(
        address _nftContractAddress,
        address _rewardTokenAddress,
        uint256 _stakingDuration,
        uint256 _rewardPerSecond
    ) public {
        nftContractAddress = _nftContractAddress;
        rewardTokenAddress = _rewardTokenAddress;
        stakingDuration = _stakingDuration;
        rewardPerSecond = _rewardPerSecond;
    }

    /**
     * @notice Stake an NFT
     * @param tokenId NFT token ID
     */
    function stakeNFT(uint256 tokenId) public nonReentrant {
        // Check if NFT is owned by the user
        require(IERC721(nftContractAddress).ownerOf(tokenId) == msg.sender, "NFT not owned by user");

        // Check if NFT is not already staked
        require(stakedNFTs[msg.sender][tokenId].stakedAt == 0, "NFT already staked");

        // Stake the NFT
        stakedNFTs[msg.sender][tokenId] = StakedNFT(block.timestamp, stakingDuration);

        // Emit event
        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @notice Unstake an NFT
     * @param tokenId NFT token ID
     */
    function unstakeNFT(uint256 tokenId) public nonReentrant {
        // Check if NFT is staked by the user
        require(stakedNFTs[msg.sender][tokenId].stakedAt != 0, "NFT not staked");

        // Check if staking duration has passed
        require(block.timestamp >= stakedNFTs[msg.sender][tokenId].stakedAt + stakingDuration, "Staking duration not passed");

        // Unstake the NFT
        delete stakedNFTs[msg.sender][tokenId];

        // Transfer NFT back to user
        IERC721(nftContractAddress).safeTransferFrom(address(this), msg.sender, tokenId);

        // Emit event
        emit NFTUnstaked(msg.sender, tokenId);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() public nonReentrant {
        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Transfer reward to user
        IERC20(rewardTokenAddress).transfer(msg.sender, reward);

        // Update user balance
        userBalances[msg.sender] = 0;

        // Emit event
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for a user
     * @param user User address
     * @return Reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        uint256 reward = 0;
        for (uint256 i = 0; i < stakedNFTs[user].length; i++) {
            StakedNFT memory stakedNFT = stakedNFTs[user][i];
            if (stakedNFT.stakedAt != 0) {
                uint256 stakingTime = block.timestamp - stakedNFT.stakedAt;
                reward += stakingTime * rewardPerSecond;
            }
        }
        return reward;
    }

    struct StakedNFT {
        uint256 stakedAt;
        uint256 stakingDuration;
    }
}
```

**Frontend Integration (JavaScript)**
```javascript
import Web3 from 'web3';
import { NFTStakingContract } from './NFTStakingContract';

const web3 = new Web3(window.ethereum);
const nftStakingContract = new web3.eth.Contract(NFTStakingContract.abi, NFTStakingContract.address);

const stakeNFT = async (tokenId) => {
  try {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Approve NFT staking contract to transfer NFT
    await nftContract.methods.approve(nftStakingContract.options.address, tokenId).send({ from: account });

    // Stake NFT
    await nftStakingContract.methods.stakeNFT(tokenId).send({ from: account });
  } catch (error) {
    console.error(error);
  }
};

const unstakeNFT = async (tokenId) => {
  try {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Unstake NFT
    await nftStakingContract.methods.unstakeNFT(tokenId).send({ from: account });
  } catch (error) {
    console.error(error);
  }
};

const claimReward = async () => {
  try {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Claim reward
    await nftStakingContract.methods.claimReward().send({ from: account });
  } catch (error) {
    console.error(error);
  }
};
```

**NFTStakingContract ABI (JSON)**
```json
[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_nftContractAddress",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "_rewardTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_stakingDuration",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "_rewardPerSecond",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "user",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "NFTStaked",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "user",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "NFTUnstaked",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "user",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "RewardClaimed",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "stakedNFTs",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "nftContractAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "rewardTokenAddress",
    "outputs": [
      {
        "internalType": "address
