"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytradefinance.com
Prompt: Describe how to create a decentralized application that allows users to buy and stake $SHE tokens while ensuring compliance with KYC regulations.
Generated: DETERMINISTIC_09c393dbdd16ce07
Batch ID: 20250612_160853
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

// Import necessary OpenZeppelin contracts for token and access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// KYC Compliance interface
interface IKYC {
    function isKYCCompleted(address _user) external view returns (bool);
}

// SHE Token Contract
contract SHE is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to keep track of staking balances
    mapping(address => uint256) public stakingBalance;
    // Total staked amount
    uint256 public totalStaked;

    // KYC contract address
    IKYC public kycContract;

    // Events for logging
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(address _kycContract) ERC20("SHE Token", "SHE") {
        kycContract = IKYC(_kycContract);
    }

    // Function to mint tokens
    function mintTokens(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(kycContract.isKYCCompleted(msg.sender), "KYC not completed");

        // Transfer tokens to this contract and update staking balance
        transfer(address(this), amount);
        stakingBalance[msg.sender] = stakingBalance[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingBalance[msg.sender] >= amount, "Insufficient staked balance");

        // Update staking balance and total staked
        stakingBalance[msg.sender] = stakingBalance[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        transfer(msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to check the staking balance of a user
    function checkStakingBalance(address user) external view returns (uint256) {
        return stakingBalance[user];
    }
}
```
