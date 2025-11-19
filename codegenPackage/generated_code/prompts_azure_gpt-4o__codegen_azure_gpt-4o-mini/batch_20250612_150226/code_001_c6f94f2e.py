"""
Generated Code Metadata:
========================
Original URL: https://aerodrome-4gg.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with Aerodrome Finance's liquidity incentive engine to distribute AERO emissions based on veAERO voting results.
Generated: DETERMINISTIC_c6f94f2e17dbbd93
Batch ID: 20250612_150226
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the veAERO contract
interface IVeAero {
    function getVotes(address account) external view returns (uint256);
}

// Interface for the Aerodrome Finance's liquidity incentive engine
interface IAerodromeIncentive {
    function distributeRewards(address recipient, uint256 amount) external;
}

// Main contract for distributing AERO emissions
contract AeroDistributor is Ownable {
    // State variables
    IERC20 public aeroToken; // AERO token contract
    IVeAero public veAero;   // veAERO contract
    IAerodromeIncentive public incentiveEngine; // Incentive engine contract

    // Event to log the distribution of rewards
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the contract with necessary addresses
    constructor(
        address _aeroToken,
        address _veAero,
        address _incentiveEngine
    ) {
        require(_aeroToken != address(0), "Invalid AERO token address");
        require(_veAero != address(0), "Invalid veAERO address");
        require(_incentiveEngine != address(0), "Invalid incentive engine address");

        aeroToken = IERC20(_aeroToken);
        veAero = IVeAero(_veAero);
        incentiveEngine = IAerodromeIncentive(_incentiveEngine);
    }

    // Function to distribute AERO emissions based on veAERO voting results
    function distributeAeroEmissions(address[] calldata recipients) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 votes = veAero.getVotes(recipient);

            // Ensure the recipient has votes to distribute emissions
            require(votes > 0, "Recipient has no votes");

            // Calculate the amount of AERO to distribute (for simplicity, using votes directly)
            uint256 amountToDistribute = votes; // This can be adjusted based on your distribution logic

            // Transfer AERO tokens to the recipient
            require(aeroToken.balanceOf(address(this)) >= amountToDistribute, "Insufficient AERO balance in contract");
            aeroToken.transfer(recipient, amountToDistribute);

            // Call the incentive engine to distribute rewards
            incentiveEngine.distributeRewards(recipient, amountToDistribute);

            // Emit an event for the distribution
            emit RewardsDistributed(recipient, amountToDistribute);
        }
    }

    // Function to withdraw any ERC20 tokens from the contract (for emergency purposes)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
