"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Write a tutorial for integrating Ember NFT staking functionality into a decentralized application (dApp), with rewards distributed to holders.
Generated: DETERMINISTIC_2c520d8ed3179f82
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Ember from 'ember';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class NftStakingController extends Ember.Controller {
  @service web3;  // Service to interact with Ethereum blockchain
  @tracked stakedNfts = [];
  @tracked rewards = 0;
  @tracked errorMessage = '';

  constructor() {
    super(...arguments);
    this.loadStakedNfts();
  }

  // Load staked NFTs from the blockchain
  async loadStakedNfts() {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const nfts = await this.web3.contract.methods.getStakedNfts(accounts[0]).call();
      this.stakedNfts = nfts;
    } catch (error) {
      this.errorMessage = 'Failed to load staked NFTs: ' + error.message;
      console.error(this.errorMessage);
    }
  }

  // Action to stake an NFT
  @action
  async stakeNft(nftId) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      await this.web3.contract.methods.stakeNft(nftId).send({ from: accounts[0] });
      this.loadStakedNfts(); // Refresh staked NFTs list
    } catch (error) {
      this.errorMessage = 'Failed to stake NFT: ' + error.message;
      console.error(this.errorMessage);
    }
  }

  // Action to unstake an NFT
  @action
  async unstakeNft(nftId) {
    try {
      const accounts = await this.web3.eth.getAccounts();
      await this.web3.contract.methods.unstakeNft(nftId).send({ from: accounts[0] });
      this.loadStakedNfts(); // Refresh staked NFTs list
    } catch (error) {
      this.errorMessage = 'Failed to unstake NFT: ' + error.message;
      console.error(this.errorMessage);
    }
  }

  // Action to claim rewards
  @action
  async claimRewards() {
    try {
      const accounts = await this.web3.eth.getAccounts();
      const claimedRewards = await this.web3.contract.methods.claimRewards().send({ from: accounts[0] });
      this.rewards += claimedRewards; // Update rewards balance
    } catch (error) {
      this.errorMessage = 'Failed to claim rewards: ' + error.message;
      console.error(this.errorMessage);
    }
  }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NftStaking is Ownable {
    IERC721 public nftCollection;
    mapping(address => uint256[]) public stakedNfts;
    mapping(address => uint256) public rewards;

    event NftStaked(address indexed user, uint256 nftId);
    event NftUnstaked(address indexed user, uint256 nftId);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC721 _nftCollection) {
        nftCollection = _nftCollection;
    }

    // Stake an NFT
    function stakeNft(uint256 nftId) external {
        require(nftCollection.ownerOf(nftId) == msg.sender, "Not the owner of the NFT");
        nftCollection.transferFrom(msg.sender, address(this), nftId);
        stakedNfts[msg.sender].push(nftId);
        emit NftStaked(msg.sender, nftId);
    }

    // Unstake an NFT
    function unstakeNft(uint256 nftId) external {
        require(_isStaked(msg.sender, nftId), "NFT not staked");
        _removeNft(msg.sender, nftId);
        nftCollection.transferFrom(address(this), msg.sender, nftId);
        emit NftUnstaked(msg.sender, nftId);
    }

    // Claim rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available");
        rewards[msg.sender] = 0;
        payable(msg.sender).transfer(rewardAmount);
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Internal function to check if an NFT is staked
    function _isStaked(address user, uint256 nftId) internal view returns (bool) {
        uint256[] memory userStakedNfts = stakedNfts[user];
        for (uint256 i = 0; i < userStakedNfts.length; i++) {
            if (userStakedNfts[i] == nftId) {
                return true;
            }
        }
        return false;
    }

    // Internal function to remove NFT from staked list
    function _removeNft(address user, uint256 nftId) internal {
        uint256[] storage userStakedNfts = stakedNfts[user];
        for (uint256 i = 0; i < userStakedNfts.length; i++) {
            if (userStakedNfts[i] == nftId) {
                userStakedNfts[i] = userStakedNfts[userStakedNfts.length - 1];
                userStakedNfts.pop();
                break;
            }
        }
    }
}
```

This code provides the basic structure for an Ember.js application to interact with an Ethereum-based NFT staking smart contract written in Solidity. Ensure to customize the contract and methods as per your specific requirements.
