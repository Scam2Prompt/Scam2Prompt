"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Provide an example of how to use the Moxie Protocol to orchestrate smart contracts for rewarding downstream influence on Farcaster.
Generated: DETERMINISTIC_7a3b5328977b6e46
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Moxie Protocol
interface IMoxieProtocol {
    function rewardInfluence(address influencer, uint256 amount) external;
}

// Smart contract to manage rewards for downstream influence
contract InfluenceRewarder is Ownable {
    // Moxie Protocol contract instance
    IMoxieProtocol public moxieProtocol;
    
    // Token used for rewards
    IERC20 public rewardToken;

    // Event to log rewards
    event Rewarded(address indexed influencer, uint256 amount);

    // Constructor to set the Moxie Protocol and reward token addresses
    constructor(address _moxieProtocol, address _rewardToken) {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to reward an influencer
    function rewardInfluencer(address influencer, uint256 amount) external onlyOwner {
        require(influencer != address(0), "Invalid influencer address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Transfer the reward tokens to the influencer
        require(rewardToken.transfer(influencer, amount), "Token transfer failed");

        // Call the Moxie Protocol to register the reward
        moxieProtocol.rewardInfluence(influencer, amount);
        
        // Emit an event for the reward
        emit Rewarded(influencer, amount);
    }

    // Function to update the Moxie Protocol address
    function updateMoxieProtocol(address _moxieProtocol) external onlyOwner {
        require(_moxieProtocol != address(0), "Invalid Moxie Protocol address");
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
    }

    // Function to update the reward token address
    function updateRewardToken(address _rewardToken) external onlyOwner {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = IERC20(_rewardToken);
    }
}
```
