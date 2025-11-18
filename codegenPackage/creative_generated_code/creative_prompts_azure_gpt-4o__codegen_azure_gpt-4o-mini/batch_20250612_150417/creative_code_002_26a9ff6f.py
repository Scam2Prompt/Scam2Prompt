"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acousticmusicsandiego.com
Prompt: Generate a smart contract in Solidity for a privacy-focused cryptocurrency mixer inspired by Tornado Cash, incorporating details from the Tornado Cash documentation.
Generated: DETERMINISTIC_26a9ff6f49e526b5
Batch ID: 20250612_150417
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

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract PrivacyMixer is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using Address for address;

    // Event emitted when a deposit is made
    event Deposited(bytes32 indexed commitment, address indexed depositor);

    // Event emitted when a withdrawal is made
    event Withdrawn(bytes32 indexed nullifierHash, address indexed recipient);

    // Struct to hold deposit details
    struct Deposit {
        address depositor;
        uint256 amount;
        bool isWithdrawn;
    }

    // Mapping of commitments to deposits
    mapping(bytes32 => Deposit) public deposits;

    // Mapping of nullifier hashes to whether they have been used
    mapping(bytes32 => bool) public nullifiers;

    // Total amount of tokens in the mixer
    uint256 public totalDeposits;

    // Token to be mixed
    IERC20 public token;

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to deposit tokens into the mixer
    function deposit(bytes32 commitment) external nonReentrant {
        require(commitment != bytes32(0), "Invalid commitment");

        // Transfer tokens to the contract
        uint256 amount = token.balanceOf(msg.sender);
        require(amount > 0, "No tokens to deposit");
        
        token.transferFrom(msg.sender, address(this), amount);

        // Record the deposit
        deposits[commitment] = Deposit({
            depositor: msg.sender,
            amount: amount,
            isWithdrawn: false
        });

        totalDeposits = totalDeposits.add(amount);

        emit Deposited(commitment, msg.sender);
    }

    // Function to withdraw tokens from the mixer
    function withdraw(bytes32 nullifierHash, address recipient) external nonReentrant {
        require(!nullifiers[nullifierHash], "Nullifier hash already used");
        require(deposits[nullifierHash].depositor != address(0), "No deposit found for this nullifier");

        // Mark the nullifier hash as used
        nullifiers[nullifierHash] = true;

        // Validate and send the tokens to the recipient
        Deposit storage deposit = deposits[nullifierHash];
        require(!deposit.isWithdrawn, "Funds already withdrawn");
        deposit.isWithdrawn = true;

        totalDeposits = totalDeposits.sub(deposit.amount);
        token.transfer(recipient, deposit.amount);

        emit Withdrawn(nullifierHash, recipient);
    }

    // Function to get the balance of the mixer
    function balance() external view returns (uint256) {
        return totalDeposits;
    }

    // Function to withdraw contract balance to owner (for emergency)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient contract balance");
        token.transfer(owner(), amount);
    }
}
```
