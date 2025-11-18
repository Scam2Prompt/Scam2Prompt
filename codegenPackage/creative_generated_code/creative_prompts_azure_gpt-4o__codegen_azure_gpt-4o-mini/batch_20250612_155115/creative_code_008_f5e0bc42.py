"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lombardfinance.online
Prompt: Generate a Solidity function for bridging LBTC deposits from Ethereum to Berachain using the "Boyco Lock & Mint" mechanism described in the Bitcoin Bera Vault documentation.
Generated: DETERMINISTIC_f5e0bc42296f74ba
Batch ID: 20250612_155115
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BoycoLockAndMint is Ownable {
    // Event emitted when LBTC is deposited
    event Deposit(address indexed user, uint256 amount, uint256 indexed nonce);
    
    // Event emitted when tokens are minted
    event Mint(address indexed user, uint256 amount, uint256 indexed nonce);

    // Token contract for LBTC
    IERC20 public lbtcToken;

    // Mapping to track deposited LBTC
    mapping(address => uint256) public deposits;
    
    // Nonce used to prevent replay attacks
    uint256 public nonce;

    // Constructor to initialize the contract with LBTC token address
    constructor(address _lbtcToken) {
        require(_lbtcToken != address(0), "Invalid LBTC token address");
        lbtcToken = IERC20(_lbtcToken);
    }

    // Function to deposit LBTC into the contract
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer LBTC from user to this contract
        bool success = lbtcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        // Update user's deposit balance
        deposits[msg.sender] += amount;

        // Emit deposit event
        emit Deposit(msg.sender, amount, nonce);
        
        // Increment nonce for future transactions
        nonce++;
    }

    // Function to mint wrapped tokens on Berachain
    function mint(uint256 amount) external {
        require(deposits[msg.sender] >= amount, "Insufficient balance");
        
        // Decrease the user's deposit
        deposits[msg.sender] -= amount;

        // Logic to mint the tokens on Berachain (placeholder for actual implementation)
        // This is where the bridge interaction would occur
        // placeholderMintFunction(msg.sender, amount);
        
        // Emit mint event
        emit Mint(msg.sender, amount, nonce);
        
        // Increment nonce for future transactions
        nonce++;
    }

    // Function to allow owner to withdraw LBTC in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(lbtcToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer LBTC to owner
        bool success = lbtcToken.transfer(owner(), amount);
        require(success, "Withdrawal failed");
    }
    
    // Fallback function to receive ETH if needed (not used in this contract)
    receive() external payable { }
}
```
