"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velodrome-7zz.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with Velodrome Finance to automate voting on pools using veVELO tokens and distribute rewards to voters.
Generated: DETERMINISTIC_7e54f20141182000
Batch ID: 20250612_151752
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
 * @title VelodromeVotingAutomation
 * @dev Automates voting on Velodrome pools using veVELO tokens and distributes rewards to voters.
 */
interface IVelodromeGauge {
    function vote(address[] calldata _pools, uint256[] calldata _weights) external;
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract VelodromeVotingAutomation {
    address public owner;
    address public veVELO; // veVELO token address
    address public velodromeGauge; // Velodrome gauge/voting contract address
    
    // Stores voter reward distribution details
    mapping(address => uint256) public rewards;

    /**
     * @dev Event emitted when voting is completed.
     * @param voter The voter who initiated the vote.
     * @param pools The pools voted on.
     * @param weights The weights allocated to the pools.
     */
    event Voted(address indexed voter, address[] pools, uint256[] weights);

    /**
     * @dev Event emitted when rewards are distributed.
     * @param voter The voter receiving rewards.
     * @param amount The amount of reward distributed.
     */
    event RewardsDistributed(address indexed voter, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(address _veVELO, address _velodromeGauge) {
        require(_veVELO != address(0), "Invalid veVELO address");
        require(_velodromeGauge != address(0), "Invalid Velodrome Gauge address");

        owner = msg.sender;
        veVELO = _veVELO;
        velodromeGauge = _velodromeGauge;
    }

    /**
     * @dev Allows the owner to update the Velodrome gauge contract address.
     * @param _velodromeGauge The new Velodrome gauge contract address.
     */
    function updateVelodromeGauge(address _velodromeGauge) external onlyOwner {
        require(_velodromeGauge != address(0), "Invalid address");
        velodromeGauge = _velodromeGauge;
    }

    /**
     * @dev Automates voting on pools using veVELO tokens.
     * @param pools The array of pool addresses to vote on.
     * @param weights The array of weights allocated to the pools.
     */
    function voteOnPools(address[] calldata pools, uint256[] calldata weights) external {
        require(pools.length == weights.length, "Pools and weights length mismatch");
        require(IERC20(veVELO).balanceOf(msg.sender) > 0, "Insufficient veVELO balance");

        // Cast vote using the Velodrome gauge contract
        IVelodromeGauge(velodromeGauge).vote(pools, weights);

        emit Voted(msg.sender, pools, weights);
    }

    /**
     * @dev Allows the owner to distribute rewards to voters.
     * @param voter The address of the voter to reward.
     * @param amount The reward amount to distribute.
     */
    function distributeRewards(address voter, uint256 amount) external onlyOwner {
        require(voter != address(0), "Invalid voter address");
        require(amount > 0, "Invalid reward amount");

        // Transfer rewards to the voter
        require(IERC20(veVELO).transfer(voter, amount), "Reward transfer failed");
        rewards[voter] += amount;

        emit RewardsDistributed(voter, amount);
    }

    /**
     * @dev Allows the owner to withdraw veVELO tokens from the contract.
     * @param amount The amount to withdraw.
     */
    function withdrawveVELO(uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid withdrawal amount");
        require(IERC20(veVELO).transfer(owner, amount), "Withdrawal failed");
    }
}
```
