"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoinclaim.xyz
Prompt: Write a smart contract using the TON blockchain that integrates with the OKX Wallet for SBT (Soulbound Token) issuance. Include wallet connection functionality and reward distribution logic.
Generated: DETERMINISTIC_9437225b96141e99
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma ton-solidity >= 0.35.0;

// Import necessary TON libraries
import "ton-solidity/contracts/interfaces/IToken.sol";
import "ton-solidity/contracts/interfaces/IWallet.sol";

// Smart contract for issuing Soulbound Tokens (SBT) on the TON blockchain
contract SoulboundToken is IToken {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // Mapping to track SBT balances of users

    // Events
    event TokenIssued(address indexed recipient, uint256 amount);
    event RewardDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the owner of the contract
    constructor() public {
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to issue SBTs to a recipient
    function issueToken(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        balances[recipient] += amount; // Update the recipient's balance
        emit TokenIssued(recipient, amount); // Emit token issuance event
    }

    // Function to connect to OKX Wallet
    function connectToWallet() public view returns (string memory) {
        // Assuming OKX Wallet integration is handled through external interfaces
        return "OKX Wallet connected"; // Placeholder return value
    }

    // Function to distribute rewards to SBT holders
    function distributeRewards(uint256 totalRewards) public onlyOwner {
        require(totalRewards > 0, "Total rewards must be greater than zero");

        // Calculate rewards for each holder
        uint256 totalSupply = getTotalSupply();
        for (address holder in balances) {
            if (balances[holder] > 0) {
                uint256 reward = (balances[holder] * totalRewards) / totalSupply;
                balances[holder] += reward; // Distribute reward to holder
                emit RewardDistributed(holder, reward); // Emit reward distribution event
            }
        }
    }

    // Function to get the total supply of SBTs issued
    function getTotalSupply() public view returns (uint256) {
        uint256 totalSupply = 0;
        for (uint256 i = 0; i < balances.length; i++) {
            totalSupply += balances[i]; // Summing up all balances
        }
        return totalSupply; // Return the total supply
    }
}
```
