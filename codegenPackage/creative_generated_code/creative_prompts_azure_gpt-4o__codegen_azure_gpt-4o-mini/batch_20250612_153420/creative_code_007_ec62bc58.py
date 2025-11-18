"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Write a Solidity contract that tracks ETH deposits and token allocations during a presale, ensuring compatibility with self-custody wallets.
Generated: DETERMINISTIC_ec62bc58fa1c2715
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

// Import OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// The Presale contract manages ETH deposits and token allocations
contract Presale {
    // Events for logging important actions
    event Deposited(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);

    // State variables
    address public owner; // Contract owner
    IERC20 public token; // Token to be distributed
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public totalDeposits; // Total ETH deposited
    mapping(address => uint256) public deposits; // Mapping of investor deposits

    // Constructor to set the token, price, and owner
    constructor(IERC20 _token, uint256 _tokenPrice) {
        owner = msg.sender;
        token = _token;
        tokenPrice = _tokenPrice;
    }

    // Modifier to restrict functions to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Function to deposit ETH and allocate tokens
    function deposit() external payable {
        require(msg.value > 0, "Must send ETH");
        
        // Update deposits and total deposits
        deposits[msg.sender] += msg.value;
        totalDeposits += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw ETH (for refunds or cancellations)
    function withdraw(uint256 amount) external {
        require(deposits[msg.sender] >= amount, "Insufficient balance");

        // Update deposits before transfer to avoid reentrancy attacks
        deposits[msg.sender] -= amount;
        totalDeposits -= amount;

        // Transfer ETH back to investor
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate the amount of tokens allocated based on ETH sent
    function calculateTokens(uint256 ethAmount) public view returns (uint256) {
        return ethAmount * 1 ether / tokenPrice;
    }

    // Function to finalize the presale and distribute tokens
    function finalize() external onlyOwner {
        require(totalDeposits > 0, "No deposits made");

        // Iterate through all investors and distribute tokens
        for (uint256 i = 0; i < totalDepositors.length; i++) {
            address investor = totalDepositors[i];
            uint256 tokensToTransfer = calculateTokens(deposits[investor]);
            deposits[investor] = 0; // Reset deposit after transfer

            // Transfer tokens to the investor
            require(token.transfer(investor, tokensToTransfer), "Token transfer failed");
        }

        // Reset total deposits
        totalDeposits = 0;
    }

    // Function to retrieve the deposit of an investor
    function getDeposit() external view returns (uint256) {
        return deposits[msg.sender];
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdrawTokens(address _token) external onlyOwner {
        IERC20(_token).transfer(owner, IERC20(_token).balanceOf(address(this)));
    }

    // Fallback function to accept ETH
    receive() external payable {
        deposit();
    }
}
```
