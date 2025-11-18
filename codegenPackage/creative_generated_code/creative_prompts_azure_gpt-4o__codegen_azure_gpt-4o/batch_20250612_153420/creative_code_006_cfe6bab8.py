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

/**
 * @title AeroEmissionsDistributor
 * @author Your Name
 * @notice Distributes AERO emissions to veAERO voters based on their locked positions and voting activity.
 */
contract AeroEmissionsDistributor {
    // Token interfaces for AERO and veAERO
    IERC20 public immutable AERO;
    IVeToken public immutable veAERO;

    // Mapping to store emissions distributed to each user
    mapping(address => uint256) public emissionsClaimed;

    // Total emissions distributed
    uint256 public totalEmissionsDistributed;

    // Events
    event EmissionsDistributed(uint256 totalAmount);
    event EmissionsClaimed(address indexed user, uint256 amount);

    // Constructor
    constructor(address _AERO, address _veAERO) {
        require(_AERO != address(0), "AERO address cannot be zero");
        require(_veAERO != address(0), "veAERO address cannot be zero");

        AERO = IERC20(_AERO);
        veAERO = IVeToken(_veAERO);
    }

    /**
     * @notice Distribute AERO emissions to veAERO voters.
     * @dev Only callable by the contract owner.
     * @param totalEmissions The total amount of AERO to distribute.
     */
    function distributeEmissions(uint256 totalEmissions) external onlyOwner {
        require(totalEmissions > 0, "Invalid emissions amount");
        require(
            AERO.balanceOf(address(this)) >= totalEmissions,
            "Insufficient contract balance"
        );

        uint256 totalVotingPower = veAERO.totalSupply(); // Total voting power of veAERO

        require(totalVotingPower > 0, "No voting power available");

        // Distribute emissions proportional to locked positions and voting power
        for (uint256 i = 0; i < veAERO.totalHolders(); i++) {
            address voter = veAERO.holderAt(i);
            uint256 voterPower = veAERO.balanceOf(voter);

            uint256 voterEmissions = (totalEmissions * voterPower) /
                totalVotingPower;

            emissionsClaimed[voter] += voterEmissions;
            AERO.transfer(voter, voterEmissions);
        }

        totalEmissionsDistributed += totalEmissions;

        emit EmissionsDistributed(totalEmissions);
    }

    /**
     * @notice Allows users to claim their emissions.
     */
    function claimEmissions() external {
        uint256 claimableAmount = emissionsClaimed[msg.sender];
        require(claimableAmount > 0, "No emissions to claim");

        emissionsClaimed[msg.sender] = 0; // Reset claimable amount
        AERO.transfer(msg.sender, claimableAmount);

        emit EmissionsClaimed(msg.sender, claimableAmount);
    }

    // Modifiers

    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Utility functions

    function owner() public view returns (address) {
        return Ownable.owner();
    }
}

// Interface for ERC20 Token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}

// Interface for veAERO Token
interface IVeToken {
    function balanceOf(address account) external view returns (uint256);

    function totalSupply() external view returns (uint256);

    function totalHolders() external view returns (uint256);

    function holderAt(uint256 index) external view returns (address);
}

// Ownable contract for owner management
abstract contract Ownable {
    function owner() public view virtual returns (address);

    function transferOwnership(address newOwner) public virtual;
}
```
