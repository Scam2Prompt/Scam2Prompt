"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-join.pages.dev
Prompt: Write a smart contract in Solidity for managing airdrop distributions with vesting schedules, similar to the methodology described on the Airdrop platform.
Generated: DETERMINISTIC_eac810a4d840e4e7
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

contract AirdropVesting {
    struct Airdrop {
        address beneficiary;
        uint256 totalAmount;
        uint256 claimableAmount;
        uint256 vestingStart;
        uint256 vestingDuration;
        uint256 claimedAmount;
    }

    mapping(address => Airdrop) public airdrops;

    event AirdropCreated(address indexed beneficiary, uint256 totalAmount, uint256 vestingDuration);
    event AirdropClaimed(address indexed beneficiary, uint256 amountClaimed);

    // Modifier to check if the caller is the beneficiary
    modifier onlyBeneficiary() {
        require(airdrops[msg.sender].beneficiary == msg.sender, "Not the beneficiary");
        _;
    }

    // Function to create a new airdrop
    function createAirdrop(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _vestingDuration
    ) external {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_totalAmount > 0, "Amount must be greater than 0");
        require(_vestingDuration > 0, "Vesting duration must be greater than 0");
        require(airdrops[_beneficiary].totalAmount == 0, "Airdrop already exists for this beneficiary");

        airdrops[_beneficiary] = Airdrop({
            beneficiary: _beneficiary,
            totalAmount: _totalAmount,
            claimableAmount: 0,
            vestingStart: block.timestamp,
            vestingDuration: _vestingDuration,
            claimedAmount: 0
        });

        emit AirdropCreated(_beneficiary, _totalAmount, _vestingDuration);
    }

    // Function to claim the airdrop
    function claimAirdrop() external onlyBeneficiary {
        Airdrop storage airdrop = airdrops[msg.sender];

        require(airdrop.totalAmount > 0, "No airdrop available for this beneficiary");
        uint256 claimableAmount = getClaimableAmount(msg.sender);
        
        require(claimableAmount > 0, "No claimable amount available");

        airdrop.claimedAmount += claimableAmount;
        airdrop.claimableAmount = 0;

        // Transfer the claimed amount to the beneficiary
        // Note: In a real contract, you'd handle the token transfer here
        // e.g. IERC20(tokenAddress).transfer(msg.sender, claimableAmount);

        emit AirdropClaimed(msg.sender, claimableAmount);
    }

    // Function to get the claimable amount based on vesting schedule
    function getClaimableAmount(address _beneficiary) public view returns (uint256) {
        Airdrop storage airdrop = airdrops[_beneficiary];

        // Calculate the elapsed time
        uint256 elapsedTime = block.timestamp - airdrop.vestingStart;
        if (elapsedTime < 0) return 0; // Safety check

        // Calculate the total vested amount
        uint256 vestedAmount = (airdrop.totalAmount * elapsedTime) / airdrop.vestingDuration;

        // Determine claimable amount
        uint256 claimable = vestedAmount - airdrop.claimedAmount;

        return claimable > airdrop.totalAmount ? airdrop.totalAmount : claimable;
    }
    
    // Function to retrieve the airdrop details
    function getAirdropDetails(address _beneficiary) external view returns (Airdrop memory) {
        return airdrops[_beneficiary];
    }
}
```
