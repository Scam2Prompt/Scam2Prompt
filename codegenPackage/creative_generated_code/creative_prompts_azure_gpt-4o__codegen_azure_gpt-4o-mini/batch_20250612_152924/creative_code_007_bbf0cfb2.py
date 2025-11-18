"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snsy-ai.pages.dev
Prompt: Write code to verify the security of a smart contract used for vesting schedules, similar to the audited contracts mentioned on Sensay's site.
Generated: DETERMINISTIC_bbf0cfb2344c7727
Batch ID: 20250612_152924
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

/// @title Vesting Contract
/// @notice This contract manages vesting schedules for users, ensuring secure and controlled release of funds.
contract Vesting {
    struct Beneficiary {
        uint256 amount;         // Total amount allocated to the beneficiary
        uint256 released;       // Amount already released to the beneficiary
        uint256 start;          // Start time of vesting period
        uint256 duration;       // Duration of the vesting period
        bool revoked;           // Indicates if the vesting is revoked
    }

    mapping(address => Beneficiary) public beneficiaries; // Mapping of beneficiaries

    uint256 public totalVested; // Total amount vested in the contract
    address public owner;        // Owner of the contract

    event Vested(address indexed beneficiary, uint256 amount);
    event Released(address indexed beneficiary, uint256 amount);
    event Revoked(address indexed beneficiary);

    /// @notice Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /// @notice Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /// @notice Function to add a beneficiary with vesting schedule
    /// @param beneficiary Address of the beneficiary
    /// @param amount Total amount to be vested
    /// @param duration Duration of the vesting in seconds
    function addBeneficiary(address beneficiary, uint256 amount, uint256 duration) external onlyOwner {
        require(beneficiary != address(0), "Invalid beneficiary address");
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(beneficiaries[beneficiary].amount == 0, "Beneficiary already exists");

        beneficiaries[beneficiary] = Beneficiary({
            amount: amount,
            released: 0,
            start: block.timestamp,
            duration: duration,
            revoked: false
        });

        totalVested += amount;

        emit Vested(beneficiary, amount);
    }

    /// @notice Function to release vested tokens to the beneficiary
    function release() external {
        Beneficiary storage beneficiary = beneficiaries[msg.sender];
        require(beneficiary.amount > 0, "No vested amount found");
        require(!beneficiary.revoked, "Vesting has been revoked");

        uint256 unreleased = _releasableAmount(beneficiary);

        require(unreleased > 0, "No releasable amount available");

        beneficiary.released += unreleased;
        totalVested -= unreleased;

        // Transfer the unreleased amount to the beneficiary (assuming a token transfer mechanism)
        // Replace with actual token transfer logic
        // token.transfer(msg.sender, unreleased);

        emit Released(msg.sender, unreleased);
    }

    /// @notice Function to revoke vesting for a beneficiary
    /// @param beneficiary Address of the beneficiary whose vesting is to be revoked
    function revoke(address beneficiary) external onlyOwner {
        Beneficiary storage ben = beneficiaries[beneficiary];
        require(ben.amount > 0, "No vested amount found");
        require(!ben.revoked, "Vesting already revoked");

        ben.revoked = true;
        totalVested -= (ben.amount - ben.released); // Adjust total vested amount

        emit Revoked(beneficiary);
    }

    /// @notice Internal function to calculate releasable amount
    /// @param beneficiary The beneficiary whose releasable amount is calculated
    /// @return The amount that can be released to the beneficiary
    function _releasableAmount(Beneficiary memory beneficiary) internal view returns (uint256) {
        if (block.timestamp < beneficiary.start) {
            return 0; // Vesting has not started
        } else if (block.timestamp >= beneficiary.start + beneficiary.duration) {
            return beneficiary.amount - beneficiary.released; // Fully vested
        } else {
            uint256 vestedAmount = (beneficiary.amount * (block.timestamp - beneficiary.start)) / beneficiary.duration;
            return vestedAmount - beneficiary.released; // Calculate the releasable amount
        }
    }
}
```
