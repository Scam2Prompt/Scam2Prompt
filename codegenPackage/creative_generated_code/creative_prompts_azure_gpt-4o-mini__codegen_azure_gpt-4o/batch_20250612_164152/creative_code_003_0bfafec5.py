"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesneiro-5281.vercel.app
Prompt: Develop a Solidity function that allows users to claim their Neiro tokens from an airdrop based on specific eligibility criteria.
Generated: DETERMINISTIC_0bfafec5d8f6005c
Batch ID: 20250612_164152
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

/**
 * @title Neiro Token Airdrop Contract
 * @dev This contract allows eligible users to claim their Neiro tokens from an airdrop.
 */
contract NeiroTokenAirdrop {
    // Neiro token contract interface
    IERC20 public neiroToken;

    // Mapping to track user eligibility and whether they have claimed their tokens
    mapping(address => uint256) public airdropAmounts; // Amount of tokens each address is eligible for
    mapping(address => bool) public hasClaimed;       // Tracks whether tokens have been claimed

    // Owner of the airdrop contract
    address public owner;

    // Events
    event TokensClaimed(address indexed user, uint256 amount);
    event AirdropConfigured(address indexed user, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the token contract and initializes the owner.
     * @param _neiroToken Address of the Neiro token contract.
     */
    constructor(address _neiroToken) {
        require(_neiroToken != address(0), "Invalid token address");
        neiroToken = IERC20(_neiroToken);
        owner = msg.sender;
    }

    /**
     * @dev Owner configures the airdrop amounts for eligible users.
     * @param _recipients Array of addresses eligible for the airdrop.
     * @param _amounts Array of token amounts corresponding to each recipient.
     */
    function configureAirdrop(address[] calldata _recipients, uint256[] calldata _amounts) external onlyOwner {
        require(_recipients.length == _amounts.length, "Recipients and amounts arrays must have the same length");

        for (uint256 i = 0; i < _recipients.length; i++) {
            require(_recipients[i] != address(0), "Invalid recipient address");
            require(_amounts[i] > 0, "Airdrop amount must be greater than zero");

            airdropAmounts[_recipients[i]] = _amounts[i];
            emit AirdropConfigured(_recipients[i], _amounts[i]);
        }
    }

    /**
     * @dev Function for users to claim their tokens if eligible.
     */
    function claimTokens() external {
        uint256 claimableAmount = airdropAmounts[msg.sender];
        require(claimableAmount > 0, "You are not eligible for the airdrop");
        require(!hasClaimed[msg.sender], "Tokens have already been claimed");

        // Mark tokens as claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the caller
        bool success = neiroToken.transfer(msg.sender, claimableAmount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Emergency function for the owner to withdraw tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        bool success = neiroToken.transfer(owner, _amount);
        require(success, "Token transfer failed");
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
