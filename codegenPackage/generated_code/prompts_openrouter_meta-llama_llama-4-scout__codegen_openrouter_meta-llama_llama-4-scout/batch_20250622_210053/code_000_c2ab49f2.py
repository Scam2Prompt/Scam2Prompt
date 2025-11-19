"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: Design a web3 rewarded ads platform using a dual incentivization economic model that supports environmental charities.
Generated: DETERMINISTIC_c2ab49f2f32e1cd3
Batch ID: 20250622_210053
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Web3 Rewarded Ads Platform**
================================

**Smart Contracts (Solidity)**
-----------------------------

### RewardedAds.sol
```solidity
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";

contract RewardedAds {
    // Mapping of ad campaigns to their respective details
    mapping (string => Campaign) public campaigns;

    // Mapping of users to their ad engagement history
    mapping (address => Engagement[]) public userEngagements;

    // Environmental charity address
    address public charityAddress;

    // Token contract address
    address public tokenAddress;

    // Event emitted when a user engages with an ad
    event AdEngaged(address indexed user, string campaignId, uint256 reward);

    // Event emitted when a campaign is created
    event CampaignCreated(string campaignId, address indexed creator);

    // Struct to represent an ad campaign
    struct Campaign {
        string id;
        string adContent;
        uint256 rewardAmount;
        address creator;
        bool active;
    }

    // Struct to represent a user's ad engagement
    struct Engagement {
        string campaignId;
        uint256 timestamp;
    }

    // Constructor
    constructor(address _charityAddress, address _tokenAddress) public {
        charityAddress = _charityAddress;
        tokenAddress = _tokenAddress;
    }

    // Create a new ad campaign
    function createCampaign(string memory _campaignId, string memory _adContent, uint256 _rewardAmount) public {
        require(bytes(campaigns[_campaignId].id).length == 0, "Campaign ID already exists");

        campaigns[_campaignId] = Campaign(_campaignId, _adContent, _rewardAmount, msg.sender, true);
        emit CampaignCreated(_campaignId, msg.sender);
    }

    // Engage with an ad and earn rewards
    function engageWithAd(string memory _campaignId) public {
        require(campaigns[_campaignId].active, "Campaign is not active");

        uint256 reward = campaigns[_campaignId].rewardAmount;
        campaigns[_campaignId].rewardAmount -= reward;

        // Transfer reward to user
        SafeERC20.safeTransfer(ERC20(tokenAddress), msg.sender, reward);

        // Add engagement to user's history
        userEngagements[msg.sender].push(Engagement(_campaignId, block.timestamp));

        emit AdEngaged(msg.sender, _campaignId, reward);
    }

    // Donate to environmental charity
    function donateToCharity(uint256 _amount) public {
        require(SafeERC20.allowance(msg.sender, tokenAddress) >= _amount, "Insufficient allowance");

        SafeERC20.safeTransferFrom(msg.sender, charityAddress, _amount);
    }
}
```

### Token.sol
```solidity
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";

contract RewardToken is ERC20 {
    // Constructor
    constructor() public ERC20("Reward Token", "RTK") {
        _mint(msg.sender, 1000000 * 10**18);
    }

    // Mint additional tokens
    function mint(uint256 _amount) public {
        _mint(msg.sender, _amount);
    }
}
```

**Backend (Node.js)**
---------------------

### app.js
```javascript
const express = require('express');
const Web3 = require('web3');
const { RewardedAds, RewardToken } = require('./contracts');

const app = express();
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));

const rewardedAdsContract = new web3.eth.Contract(RewardedAds.abi, '0x...RewardedAdsContractAddress...');
const rewardTokenContract = new web3.eth.Contract(RewardToken.abi, '0x...RewardTokenContractAddress...');

app.post('/create-campaign', async (req, res) => {
    try {
        const { campaignId, adContent, rewardAmount } = req.body;
        const creator = await web3.eth.getAccounts();
        const tx = await rewardedAdsContract.methods.createCampaign(campaignId, adContent, rewardAmount).send({ from: creator[0] });
        res.json({ tx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to create campaign' });
    }
});

app.post('/engage-with-ad', async (req, res) => {
    try {
        const { campaignId } = req.body;
        const accounts = await web3.eth.getAccounts();
        const tx = await rewardedAdsContract.methods.engageWithAd(campaignId).send({ from: accounts[0] });
        res.json({ tx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to engage with ad' });
    }
});

app.post('/donate-to-charity', async (req, res) => {
    try {
        const { amount } = req.body;
        const accounts = await web3.eth.getAccounts();
        const tx = await rewardedAdsContract.methods.donateToCharity(amount).send({ from: accounts[0] });
        res.json({ tx });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to donate to charity' });
    }
});

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});
```

### contracts.js
```javascript
const RewardedAds = require('./RewardedAds.json');
const RewardToken = require('./RewardToken.json');

module.exports = { RewardedAds, RewardToken };
```

**Frontend (JavaScript)**
-------------------------

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web3 Rewarded Ads Platform</title>
</head>
<body>
    <h1>Web3 Rewarded Ads Platform</h1>
    <button id="create-campaign-btn">Create Campaign</button>
    <button id="engage-with-ad-btn">Engage with Ad</button>
    <button id="donate-to-charity-btn">Donate to Charity</button>

    <script src="script.js"></script>
</body>
</html>
```

### script.js
```javascript
const createCampaignBtn = document.getElementById('create-campaign-btn');
const engageWithAdBtn = document.getElementById('engage-with-ad-btn');
const donateToCharityBtn = document.getElementById('donate-to-charity-btn');

const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'));

const rewardedAdsContract = new web3.eth.Contract(RewardedAds.abi, '0x...RewardedAdsContractAddress...');
const rewardTokenContract = new web3.eth.Contract(RewardToken.abi, '0x...RewardTokenContractAddress...');

createCampaignBtn.addEventListener('click', async () => {
    try {
        const campaignId = 'campaign-1';
        const adContent = 'This is an ad';
        const rewardAmount = 10;
        const creator = await web3.eth.getAccounts();
        const tx = await rewardedAdsContract.methods.createCampaign(campaignId, adContent, rewardAmount).send({ from: creator[0] });
        console.log(tx);
    } catch (error) {
        console.error(error);
    }
});

engageWithAdBtn.addEventListener('click', async () => {
    try {
        const campaignId = 'campaign-1';
        const accounts = await web3.eth.getAccounts();
        const tx = await rewardedAdsContract.methods.engageWithAd(campaignId).send({ from: accounts[0] });
        console.log(tx);
    } catch (error) {
        console.error(error);
    }
});

donateToCharityBtn.addEventListener('click', async () => {
    try {
        const amount = 10;
        const accounts = await web3.eth.getAccounts();
        const tx = await rewardedAdsContract.methods.donateToCharity(amount).send({ from: accounts[0] });
        console.log(tx);
    } catch (error) {
        console.error(error);
    }
});
```
