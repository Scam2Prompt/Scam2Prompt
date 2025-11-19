"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Create a smart contract that allocates $MIND tokens according to the tokenomics breakdown provided (e.g., 10% for exchanges, 25% for the AI agent).
Generated: DETERMINISTIC_03539bd9e5593322
Batch ID: 20250612_145712
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

// Importing OpenZeppelin's ERC20 implementation for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $MIND token
contract MindToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Tokenomics breakdown
    uint256 public constant EXCHANGE_ALLOCATION = TOTAL_SUPPLY * 10 / 100; // 10% for exchanges
    uint256 public constant AI_AGENT_ALLOCATION = TOTAL_SUPPLY * 25 / 100; // 25% for AI agent
    uint256 public constant TEAM_ALLOCATION = TOTAL_SUPPLY * 15 / 100; // 15% for team
    uint256 public constant COMMUNITY_ALLOCATION = TOTAL_SUPPLY * 50 / 100; // 50% for community

    // Addresses for allocations
    address public exchangeAddress;
    address public aiAgentAddress;
    address public teamAddress;
    address public communityAddress;

    // Constructor to initialize the token and allocate tokens
    constructor(
        address _exchangeAddress,
        address _aiAgentAddress,
        address _teamAddress,
        address _communityAddress
    ) ERC20("Mind Token", "$MIND") {
        // Validate addresses
        require(_exchangeAddress != address(0), "Invalid exchange address");
        require(_aiAgentAddress != address(0), "Invalid AI agent address");
        require(_teamAddress != address(0), "Invalid team address");
        require(_communityAddress != address(0), "Invalid community address");

        // Assign addresses
        exchangeAddress = _exchangeAddress;
        aiAgentAddress = _aiAgentAddress;
        teamAddress = _teamAddress;
        communityAddress = _communityAddress;

        // Mint tokens according to the tokenomics
        _mint(exchangeAddress, EXCHANGE_ALLOCATION);
        _mint(aiAgentAddress, AI_AGENT_ALLOCATION);
        _mint(teamAddress, TEAM_ALLOCATION);
        _mint(communityAddress, COMMUNITY_ALLOCATION);
    }

    // Function to retrieve the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    // Function to retrieve the balance of a specific address
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }

    // Function to transfer tokens (inherited from ERC20)
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    // Function to approve token spending (inherited from ERC20)
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    // Function to transfer tokens from one address to another (inherited from ERC20)
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }
}
```
