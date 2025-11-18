"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Write a Solidity smart contract to manage the tokenomics distribution of $POODL, ensuring compliance with the outlined allocations (50% presale, 30% staking, etc.).
Generated: DETERMINISTIC_4d03ee8b2783ec91
Batch ID: 20250612_153400
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
 * @title POODLTokenDistribution
 * @dev Smart contract to handle tokenomics distribution of $POODL token
 */
contract POODLTokenDistribution {
    // Token allocations as percentages
    uint256 public constant PRESALE_ALLOCATION = 50; // 50%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant TEAM_ALLOCATION = 10;    // 10%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // State variables
    uint256 public totalSupply;
    address public owner;

    mapping(address => uint256) public balances;

    // Modifier to restrict access
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    // Event to track token distribution
    event Distributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that sets the owner and total supply of the token.
     * @param _totalSupply The total supply of the $POODL token.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero.");
        owner = msg.sender;
        totalSupply = _totalSupply;
    }

    /**
     * @dev Function to distribute tokens to the presale pool.
     * @param presaleAddress Address for presale wallet.
     */
    function distributePresale(address presaleAddress) external onlyOwner {
        require(presaleAddress != address(0), "Invalid presale address.");
        uint256 presaleAmount = (totalSupply * PRESALE_ALLOCATION) / 100;
        require(balances[presaleAddress] == 0, "Presale already distributed.");
        balances[presaleAddress] = presaleAmount;
        emit Distributed(presaleAddress, presaleAmount);
    }

    /**
     * @dev Function to distribute tokens to the staking pool.
     * @param stakingAddress Address for staking wallet.
     */
    function distributeStaking(address stakingAddress) external onlyOwner {
        require(stakingAddress != address(0), "Invalid staking address.");
        uint256 stakingAmount = (totalSupply * STAKING_ALLOCATION) / 100;
        require(balances[stakingAddress] == 0, "Staking already distributed.");
        balances[stakingAddress] = stakingAmount;
        emit Distributed(stakingAddress, stakingAmount);
    }

    /**
     * @dev Function to distribute tokens to the team wallet.
     * @param teamAddress Address for team wallet.
     */
    function distributeTeam(address teamAddress) external onlyOwner {
        require(teamAddress != address(0), "Invalid team address.");
        uint256 teamAmount = (totalSupply * TEAM_ALLOCATION) / 100;
        require(balances[teamAddress] == 0, "Team allocation already distributed.");
        balances[teamAddress] = teamAmount;
        emit Distributed(teamAddress, teamAmount);
    }

    /**
     * @dev Function to distribute tokens to the marketing wallet.
     * @param marketingAddress Address for marketing wallet.
     */
    function distributeMarketing(address marketingAddress) external onlyOwner {
        require(marketingAddress != address(0), "Invalid marketing address.");
        uint256 marketingAmount = (totalSupply * MARKETING_ALLOCATION) / 100;
        require(balances[marketingAddress] == 0, "Marketing allocation already distributed.");
        balances[marketingAddress] = marketingAmount;
        emit Distributed(marketingAddress, marketingAmount);
    }

    /**
     * @dev Function to retrieve token balance for an address.
     * @param account Address to query balance.
     * @return The token balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
