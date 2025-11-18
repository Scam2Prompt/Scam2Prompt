"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Write a Solidity smart contract for charity voting, allocating 5% of the total $HINU supply to user-voted charities.
Generated: DETERMINISTIC_1eef99b29f4dd025
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title CharityVoting
 * @dev A smart contract for charity voting and allocation of 5% of the total $HINU supply to user-voted charities.
 */
contract CharityVoting {
    // State Variables
    address public owner;                  // Contract owner address
    uint256 public constant ALLOCATION = 5; // Allocation percentage for charity (5%)
    uint256 public totalHinuSupply;       // Total $HINU token supply
    uint256 public allocatedFunds;        // Funds allocated for charities

    address[] public charities;           // List of charity addresses
    mapping(address => uint256) public votes; // Mapping of charity addresses to votes

    bool public allocationDistributed;    // Flag to ensure funds are distributed only once

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier allocationNotDistributed() {
        require(!allocationDistributed, "Funds have already been distributed");
        _;
    }

    // Events
    event CharityAdded(address charity);
    event VoteCast(address indexed voter, address indexed charity);
    event FundsDistributed(address charity, uint256 amount);

    // Constructor
    constructor(uint256 _totalHinuSupply) {
        owner = msg.sender;               // Assign the contract deployer as the owner
        totalHinuSupply = _totalHinuSupply; // Initialize the total supply of $HINU
        allocatedFunds = (totalHinuSupply * ALLOCATION) / 100; // Calculate funds allocated for charities
    }

    /**
     * @dev Adds a charity to the voting pool.
     * @param charity The address of the charity to be added.
     */
    function addCharity(address charity) external onlyOwner {
        require(charity != address(0), "Charity address cannot be zero");
        charities.push(charity);
        votes[charity] = 0;               // Initialize votes for the charity
        emit CharityAdded(charity);
    }

    /**
     * @dev Cast a vote for a specified charity.
     * @param charity The address of the charity to vote for.
     */
    function castVote(address charity) external {
        require(isCharityExists(charity), "Charity address not found");
        votes[charity] += 1;              // Increment vote count for the charity
        emit VoteCast(msg.sender, charity);
    }

    /**
     * @dev Distribute allocated funds to the charity with the highest votes.
     */
    function distributeFunds() external onlyOwner allocationNotDistributed {
        address winningCharity = getWinningCharity();
        require(winningCharity != address(0), "No charity has votes");

        allocationDistributed = true;    // Mark allocation as distributed
        (bool success, ) = winningCharity.call{value: allocatedFunds}("");
        require(success, "Funds transfer failed");

        emit FundsDistributed(winningCharity, allocatedFunds);
    }

    /**
     * @dev Helper function to check if a charity exists in the list.
     * @param charity The address of the charity to check.
     * @return bool True if the charity exists, false otherwise.
     */
    function isCharityExists(address charity) internal view returns (bool) {
        for (uint256 i = 0; i < charities.length; i++) {
            if (charities[i] == charity) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Helper function to determine the winning charity.
     * @return address The address of the charity with the most votes.
     */
    function getWinningCharity() internal view returns (address) {
        address winner;
        uint256 highestVotes = 0;
        for (uint256 i = 0; i < charities.length; i++) {
            if (votes[charities[i]] > highestVotes) {
                highestVotes = votes[charities[i]];
                winner = charities[i];
            }
        }
        return winner;
    }

    // Fallback function to receive ether
    receive() external payable {}
}
```
