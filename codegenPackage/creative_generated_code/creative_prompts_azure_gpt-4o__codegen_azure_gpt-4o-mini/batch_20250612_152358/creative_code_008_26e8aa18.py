"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Create a smart contract to manage USDT prize distribution for participants in the $PLENA Quest, ensuring compliance with Plena Finance's rules.
Generated: DETERMINISTIC_26e8aa186a908050
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PlenaQuestPrizeDistribution {
    // State variables
    IERC20 public usdtToken; // USDT token contract
    address public owner;     // Owner of the contract
    mapping(address => uint256) public prizes; // Mapping of participant addresses to their prize amounts
    event PrizeDistributed(address indexed participant, uint256 amount); // Event for prize distribution

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with USDT token address
    constructor(address _usdtToken) {
        require(_usdtToken != address(0), "Invalid USDT token address");
        usdtToken = IERC20(_usdtToken);
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Function to distribute prizes to participants
    function distributePrizes(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 amount = amounts[i];

            require(participant != address(0), "Invalid participant address");
            require(amount > 0, "Amount must be greater than zero");
            require(prizes[participant] + amount >= prizes[participant], "Overflow error"); // Check for overflow

            prizes[participant] += amount; // Accumulate prize amount
            emit PrizeDistributed(participant, amount); // Emit event for prize distribution
        }
    }

    // Function to allow participants to claim their prizes
    function claimPrize() external {
        uint256 amount = prizes[msg.sender]; // Get the prize amount for the caller
        require(amount > 0, "No prize to claim");

        // Reset the prize amount before transfer to prevent re-entrancy attack
        prizes[msg.sender] = 0;

        // Transfer USDT tokens to the participant
        require(usdtToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to withdraw any USDT that may be sent to the contract by mistake
    function withdrawUSDT() external onlyOwner {
        uint256 balance = usdtToken.balanceOf(address(this));
        require(balance > 0, "No USDT to withdraw");
        require(usdtToken.transfer(owner, balance), "Withdraw failed");
    }

    // Function to check contract balance of USDT
    function getContractBalance() external view returns (uint256) {
        return usdtToken.balanceOf(address(this));
    }
}
```
