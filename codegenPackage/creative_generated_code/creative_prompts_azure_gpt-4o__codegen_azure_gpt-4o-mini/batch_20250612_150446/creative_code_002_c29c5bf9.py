"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gc-passport-faucet.vercel.app
Prompt: Generate a smart contract for a faucet that integrates Gitcoin Passport verification, referencing the implementation details from supermodular.xyz.
Generated: DETERMINISTIC_c29c5bf99fdb8e93
Batch ID: 20250612_150446
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

// Import interfaces and libraries from OpenZeppelin and Gitcoin Passport
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for Gitcoin Passport verification
interface IGitcoinPassport {
    function isVerified(address user) external view returns (bool);
}

// Faucet smart contract
contract GitcoinFaucet is Ownable {
    // Token contract to dispense
    IERC20 public token;
    // Gitcoin Passport contract for verification
    IGitcoinPassport public passport;
    // Mapping to track last withdrawal time for each address
    mapping(address => uint256) public lastWithdrawn;

    // Amount of tokens dispensed per withdrawal
    uint256 public constant DISPENSE_AMOUNT = 100 * 10 ** 18; // 100 tokens, adjust decimals accordingly
    // Cooldown period in seconds
    uint256 public constant COOLDOWN_PERIOD = 1 days;

    // Event emitted when tokens are dispensed
    event TokensDispensed(address indexed user, uint256 amount);

    // Constructor to set token and passport contract addresses
    constructor(address _tokenAddress, address _passportAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_passportAddress != address(0), "Invalid passport address");
        token = IERC20(_tokenAddress);
        passport = IGitcoinPassport(_passportAddress);
    }

    // Function to request tokens from the faucet
    function requestTokens() external {
        // Check if the user is verified through Gitcoin Passport
        require(passport.isVerified(msg.sender), "User is not verified");

        // Check if cooldown period has passed since last withdrawal
        require(block.timestamp >= lastWithdrawn[msg.sender] + COOLDOWN_PERIOD, "Cooldown period not met");

        // Update last withdrawn time
        lastWithdrawn[msg.sender] = block.timestamp;

        // Transfer tokens to the user
        require(token.balanceOf(address(this)) >= DISPENSE_AMOUNT, "Insufficient tokens in faucet");
        bool success = token.transfer(msg.sender, DISPENSE_AMOUNT);
        require(success, "Token transfer failed");

        // Emit event for the token dispensing
        emit TokensDispensed(msg.sender, DISPENSE_AMOUNT);
    }

    // Function for owner to withdraw tokens from the faucet
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient tokens in faucet");

        // Transfer tokens to the owner
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to update the token address (if needed)
    function updateTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid new token address");
        token = IERC20(newTokenAddress);
    }

    // Function to update the passport address (if needed)
    function updatePassportAddress(address newPassportAddress) external onlyOwner {
        require(newPassportAddress != address(0), "Invalid new passport address");
        passport = IGitcoinPassport(newPassportAddress);
    }
}
```
