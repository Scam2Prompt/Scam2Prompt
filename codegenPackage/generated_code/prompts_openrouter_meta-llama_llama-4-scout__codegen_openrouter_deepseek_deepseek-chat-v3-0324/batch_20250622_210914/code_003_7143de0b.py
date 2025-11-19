"""
Generated Code Metadata:
========================
Original URL: https://plenafinance.vercel.app
Prompt: Design a smart contract to distribute rewards, such as USDT prizes and whitelist spots, to participants of the $PLENA airdrop campaign, using Solidity and Ethers.js.
Generated: DETERMINISTIC_7143de0ba8a8b5ff
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PlenaAirdropRewards is Ownable, ReentrancyGuard {
    IERC20 public usdtToken;
    address[] public whitelist;
    mapping(address => bool) public hasClaimed;
    mapping(address => bool) public isWhitelisted;
    uint256 public usdtRewardAmount;
    bool public rewardsActive;

    event RewardClaimed(address indexed participant, uint256 amount);
    event WhitelistAdded(address indexed participant);
    event RewardsActivated(bool status);

    constructor(address _usdtTokenAddress, uint256 _usdtRewardAmount) {
        usdtToken = IERC20(_usdtTokenAddress);
        usdtRewardAmount = _usdtRewardAmount;
        rewardsActive = false;
    }

    modifier whenRewardsActive() {
        require(rewardsActive, "Rewards distribution is not active");
        _;
    }

    function activateRewards(bool _status) external onlyOwner {
        rewardsActive = _status;
        emit RewardsActivated(_status);
    }

    function addToWhitelist(address[] calldata participants) external onlyOwner {
        for (uint256 i = 0; i < participants.length; i++) {
            if (!isWhitelisted[participants[i]]) {
                whitelist.push(participants[i]);
                isWhitelisted[participants[i]] = true;
                emit WhitelistAdded(participants[i]);
            }
        }
    }

    function claimReward() external nonReentrant whenRewardsActive {
        require(isWhitelisted[msg.sender], "Not eligible for reward");
        require(!hasClaimed[msg.sender], "Reward already claimed");

        hasClaimed[msg.sender] = true;
        
        require(
            usdtToken.transfer(msg.sender, usdtRewardAmount),
            "USDT transfer failed"
        );

        emit RewardClaimed(msg.sender, usdtRewardAmount);
    }

    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(owner(), amount),
            "Token withdrawal failed"
        );
    }

    function getWhitelist() external view returns (address[] memory) {
        return whitelist;
    }

    function getWhitelistCount() external view returns (uint256) {
        return whitelist.length;
    }
}
```

```javascript
// Ethers.js interaction script
const { ethers } = require("ethers");
const PlenaAirdropRewardsABI = require("./PlenaAirdropRewardsABI.json");

async function interactWithContract() {
    // Setup provider and signer
    const provider = new ethers.providers.JsonRpcProvider("YOUR_RPC_URL");
    const signer = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
    
    // Contract instance
    const contractAddress = "YOUR_CONTRACT_ADDRESS";
    const airdropContract = new ethers.Contract(
        contractAddress,
        PlenaAirdropRewardsABI,
        signer
    );

    // Example functions
    async function claimReward() {
        try {
            const tx = await airdropContract.claimReward();
            await tx.wait();
            console.log("Reward claimed successfully");
        } catch (error) {
            console.error("Error claiming reward:", error.message);
        }
    }

    async function checkWhitelistStatus(address) {
        try {
            const isWhitelisted = await airdropContract.isWhitelisted(address);
            console.log(`Address ${address} is whitelisted: ${isWhitelisted}`);
            return isWhitelisted;
        } catch (error) {
            console.error("Error checking whitelist status:", error.message);
            return false;
        }
    }

    async function addToWhitelist(addresses) {
        try {
            const tx = await airdropContract.addToWhitelist(addresses);
            await tx.wait();
            console.log("Addresses added to whitelist successfully");
        } catch (error) {
            console.error("Error adding to whitelist:", error.message);
        }
    }

    return {
        claimReward,
        checkWhitelistStatus,
        addToWhitelist
    };
}

// Example usage
(async () => {
    const { claimReward, checkWhitelistStatus } = await interactWithContract();
    
    const userAddress = "USER_ADDRESS_TO_CHECK";
    const isEligible = await checkWhitelistStatus(userAddress);
    
    if (isEligible) {
        await claimReward();
    }
})();
```
