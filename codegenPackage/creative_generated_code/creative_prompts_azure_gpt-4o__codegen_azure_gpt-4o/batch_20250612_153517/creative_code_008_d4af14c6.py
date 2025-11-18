"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-join.pages.dev
Prompt: Write a Solidity function to handle staking and distribution for a multi-chain fundraising platform, ensuring compatibility with multiple blockchains as described on the Airdrop platform.
Generated: DETERMINISTIC_d4af14c696fd0c34
Batch ID: 20250612_153517
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

/**
 * @title MultiChainStaking
 * @dev A Solidity contract for handling staking and distribution on a multi-chain fundraising platform.
 *      This contract is compatible with multiple blockchains supporting EVM.
 */
contract MultiChainStaking {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total staked amount
    mapping(address => uint256) public stakes; // Individual stakes per address
    mapping(address => bool) public allowedChains; // Chains allowed for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Stake funds into the contract.
     * @param _amount Amount to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount == msg.value, "Incorrect staking amount");
        require(msg.value > 0, "Stake amount must be greater than zero");
        
        // Update state variables
        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;
        
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Unstake funds from the contract.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender];
        require(stakedAmount > 0, "No funds to unstake");

        // Update state variables
        stakes[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer funds back to the user
        (bool success, ) = msg.sender.call{value: stakedAmount}("");
        require(success, "Unstake transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Distribute rewards proportionally to stakers.
     * @param _rewardPool Total reward amount to be distributed.
     */
    function distributeRewards(uint256 _rewardPool) external onlyOwner {
        require(_rewardPool > 0, "Reward pool must be greater than zero");
        require(address(this).balance >= _rewardPool, "Insufficient contract balance");

        for (address staker : getStakers()) {
            uint256 reward = (_rewardPool * stakes[staker]) / totalStaked;
            (bool success, ) = staker.call{value: reward}("");
            require(success, "Reward distribution failed");
            
            emit RewardsDistributed(staker, reward);
        }
    }

    /**
     * @dev Add a chain to the list of allowed chains.
     * @param _chain The address of the chain to allow.
     */
    function allowChain(address _chain) external onlyOwner {
        allowedChains[_chain] = true;
    }

    /**
     * @dev Remove a chain from the list of allowed chains.
     * @param _chain The address of the chain to disallow.
     */
    function disallowChain(address _chain) external onlyOwner {
        allowedChains[_chain] = false;
    }

    /**
     * @dev Helper function to get all stakers (mock implementation for illustration).
     */
    function getStakers() internal view returns (address[] memory) {
        // Note: Implement logic to track and retrieve all staker addresses.
        // For production, use a dynamic array or mapping to store staker addresses.
        return new address[](0);
    }
}
```
