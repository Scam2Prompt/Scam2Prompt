"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-aerodromefinance-bti.pages.dev
Prompt: Write a Solidity contract to distribute AERO emissions to veAERO voters based on their locked positions and voting activity.
Generated: DETERMINISTIC_cfe6bab8fd0a8bea
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for veAERO (Voting Escrow AERO)
interface IVeAERO {
    function locked(address _user) external view returns (uint256 amount, uint256 end);
    function getVotes(address _user) external view returns (uint256);
}

// AERO Emissions Distributor Contract
contract AeroDistributor is Ownable {
    // Address of the AERO token
    IERC20 public aeroToken;
    // Address of the veAERO contract
    IVeAERO public veAERO;

    // Total amount of AERO emissions to distribute
    uint256 public totalEmissions;
    // Mapping to track distributed emissions
    mapping(address => uint256) public distributedEmissions;

    // Event emitted when emissions are distributed
    event EmissionsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _aeroToken, address _veAERO) {
        require(_aeroToken != address(0), "Invalid AERO token address");
        require(_veAERO != address(0), "Invalid veAERO address");

        aeroToken = IERC20(_aeroToken);
        veAERO = IVeAERO(_veAERO);
    }

    // Function to set the total emissions for distribution
    function setTotalEmissions(uint256 _totalEmissions) external onlyOwner {
        totalEmissions = _totalEmissions;
    }

    // Function to distribute AERO emissions to veAERO voters
    function distributeEmissions() external {
        uint256 totalVotes = 0;
        address[] memory voters = getVoters(); // Assume this function retrieves all voter addresses

        // Calculate total votes from all voters
        for (uint256 i = 0; i < voters.length; i++) {
            totalVotes += veAERO.getVotes(voters[i]);
        }

        // Distribute emissions based on the voting weight
        for (uint256 i = 0; i < voters.length; i++) {
            address voter = voters[i];
            (uint256 lockedAmount, ) = veAERO.locked(voter);

            // Only distribute to voters with a locked position
            if (lockedAmount > 0 && totalVotes > 0) {
                uint256 voterShare = (totalVotes == 0) ? 0 : (veAERO.getVotes(voter) * totalEmissions) / totalVotes;
                distributedEmissions[voter] += voterShare;
                emit EmissionsDistributed(voter, voterShare);
            }
        }
    }

    // Function to claim distributed AERO emissions
    function claimAeroEmissions() external {
        uint256 amount = distributedEmissions[msg.sender];
        require(amount > 0, "No emissions to claim");

        // Reset the emissions for the user after claiming
        distributedEmissions[msg.sender] = 0;

        // Transfer AERO tokens to the user
        require(aeroToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Helper function to retrieve all voters (placeholder function)
    function getVoters() internal view returns (address[] memory) {
        // In a production environment, this function should return all unique voter addresses
        // For simplicity, this is left unimplemented
        revert("getVoters function not implemented");
    }
}
```
