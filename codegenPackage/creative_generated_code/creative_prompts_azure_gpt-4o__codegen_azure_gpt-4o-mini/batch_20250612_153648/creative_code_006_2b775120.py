"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: Develop a smart contract in Solidity that supports raffles with SOL and USDC as entry tokens.
Generated: DETERMINISTIC_2b77512046eeb911
Batch ID: 20250612_153648
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

// Import the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Raffle is Ownable {
    // State variables
    IERC20 public usdcToken; // USDC token contract
    address public solToken; // SOL token address (assuming it's a wrapped version)
    
    struct RaffleEntry {
        address participant;
        uint256 amount;
    }

    RaffleEntry[] public entries; // Array to hold raffle entries
    uint256 public entryFeeUSDC; // Entry fee in USDC
    uint256 public entryFeeSOL; // Entry fee in SOL
    bool public isActive; // Raffle status

    // Events
    event RaffleEntered(address indexed participant, uint256 amount, string tokenType);
    event RaffleEnded(address winner, uint256 prizeAmount);

    // Modifier to check if raffle is active
    modifier onlyWhenActive() {
        require(isActive, "Raffle is not active");
        _;
    }

    constructor(IERC20 _usdcToken, address _solToken, uint256 _entryFeeUSDC, uint256 _entryFeeSOL) {
        usdcToken = _usdcToken;
        solToken = _solToken;
        entryFeeUSDC = _entryFeeUSDC;
        entryFeeSOL = _entryFeeSOL;
        isActive = true; // Start the raffle as active
    }

    // Function to enter the raffle with USDC
    function enterWithUSDC(uint256 amount) external onlyWhenActive {
        require(amount >= entryFeeUSDC, "Insufficient USDC amount");
        
        // Transfer USDC from participant to this contract
        require(usdcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Record the entry
        entries.push(RaffleEntry(msg.sender, amount));
        emit RaffleEntered(msg.sender, amount, "USDC");
    }

    // Function to enter the raffle with SOL (wrapped SOL)
    function enterWithSOL() external payable onlyWhenActive {
        require(msg.value >= entryFeeSOL, "Insufficient SOL amount");

        // Record the entry
        entries.push(RaffleEntry(msg.sender, msg.value));
        emit RaffleEntered(msg.sender, msg.value, "SOL");
    }

    // Function to end the raffle and select a winner
    function endRaffle() external onlyOwner onlyWhenActive {
        require(entries.length > 0, "No entries in the raffle");

        // Select a random winner (for simplicity, using blockhash)
        uint256 randomIndex = uint256(blockhash(block.number - 1)) % entries.length;
        address winner = entries[randomIndex].participant;

        // Calculate total prize amount based on entry fees
        uint256 prizeAmount = address(this).balance;

        // Transfer prize to the winner
        (bool sent, ) = winner.call{value: prizeAmount}("");
        require(sent, "Failed to send prize to winner");

        emit RaffleEnded(winner, prizeAmount);

        // Reset the raffle
        delete entries;
        isActive = false;
    }

    // Function to withdraw USDC tokens (for the owner)
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(amount <= usdcToken.balanceOf(address(this)), "Insufficient USDC balance");
        require(usdcToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to withdraw SOL (for the owner)
    function withdrawSOL(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient SOL balance");
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Failed to withdraw SOL");
    }

    // Function to allow contract to receive SOL
    receive() external payable {}
}
```
