"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicbp4v36pb5mqdwiyqegjmf62ex6eneyd5bhgvnobirakblg5rkze.ipfs.dweb.link
Prompt: Create a smart contract for distributing $MEME tokens based on eligibility criteria, as outlined on the Memeland dashboard.
Generated: DETERMINISTIC_e85b74d7fb9d13f0
Batch ID: 20250612_152249
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

// Interface for the ERC20 Token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for distributing $MEME tokens based on eligibility criteria
contract MemeTokenDistributor {
    // State variables
    IERC20 public memeToken; // The $MEME token contract
    address public owner; // Owner of the contract
    mapping(address => bool) public eligibleAddresses; // Stores eligibility status of addresses

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    event EligibilityUpdated(address indexed account, bool isEligible);

    // Constructor to initialize the contract with the token address
    constructor(address _memeTokenAddress) {
        require(_memeTokenAddress != address(0), "Invalid token address");
        memeToken = IERC20(_memeTokenAddress);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: caller is not the owner");
        _;
    }

    // Function to update eligibility for a specific address
    function updateEligibility(address account, bool isEligible) external onlyOwner {
        eligibleAddresses[account] = isEligible;
        emit EligibilityUpdated(account, isEligible);
    }

    // Function to distribute $MEME tokens to eligible addresses
    function distributeTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");

        // Check if the contract has enough $MEME tokens to send
        require(memeToken.balanceOf(address(this)) >= amount * recipients.length, "Insufficient $MEME balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(eligibleAddresses[recipient], "Recipient is not eligible");

            // Transfer the tokens
            bool success = memeToken.transfer(recipient, amount);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipient, amount);
        }
    }

    // Function to withdraw any ERC20 tokens accidentally sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(memeToken), "Cannot withdraw $MEME tokens from this contract");
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        bool success = token.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }

    // Function to check eligibility of an address
    function isEligible(address account) external view returns (bool) {
        return eligibleAddresses[account];
    }
}
```
