"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Develop a simple smart contract in Solidity to automate CPOOL staking with Clearpool Oracles, ensuring secure and transparent transactions.
Generated: DETERMINISTIC_300b25595dbb8231
Batch ID: 20250622_211405
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

// Importing OpenZeppelin's SafeERC20 for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Clearpool Oracle
interface IClearpoolOracle {
    function getCPOOLPrice() external view returns (uint256);
}

// Smart contract for CPOOL staking
contract CPOOLStaking is Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public cpoolToken; // CPOOL token contract
    IClearpoolOracle public oracle; // Clearpool Oracle contract
    uint256 public totalStaked; // Total amount of CPOOL staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with CPOOL token and Oracle address
    constructor(IERC20 _cpoolToken, IClearpoolOracle _oracle) {
        cpoolToken = _cpoolToken;
        oracle = _oracle;
    }

    // Function to stake CPOOL tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(cpoolToken.balanceOf(msg.sender) >= amount, "Insufficient CPOOL balance");

        // Transfer CPOOL tokens from user to this contract
        cpoolToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staking state
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake CPOOL tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staking state
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer CPOOL tokens back to the user
        cpoolToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the current CPOOL price from the oracle
    function getCPOOLPrice() external view returns (uint256) {
        return oracle.getCPOOLPrice();
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != cpoolToken, "Cannot withdraw staked CPOOL tokens");
        token.safeTransfer(msg.sender, amount);
    }
}
```
