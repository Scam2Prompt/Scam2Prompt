"""
Generated Code Metadata:
========================
Original URL: https://assisterr-ai.icu
Prompt: Create a smart contract in Solidity to support Assisterr's AI Agent Incubator program, focusing on incentivizing SLM creators and managing tokenized AI use cases.
Generated: DETERMINISTIC_fcd6d9470382e26c
Batch ID: 20250612_154029
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

// Importing OpenZeppelin's ERC20 implementation for token management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Assisterr's AI Agent Incubator program
contract AIIncubator is ERC20, Ownable {
    // Event emitted when a new SLM creator is registered
    event SLMRegistered(address indexed creator, uint256 indexed slmId);
    
    // Event emitted when tokens are rewarded to a creator
    event TokensRewarded(address indexed creator, uint256 amount);
    
    // Struct to represent a SLM (Smart Learning Model)
    struct SLM {
        uint256 id;
        address creator;
        string description;
        uint256 rewardAmount;
        bool exists;
    }

    // Mapping to store SLMs by their ID
    mapping(uint256 => SLM) public slms;
    // Counter for SLM IDs
    uint256 public slmCounter;

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("AssisterrToken", "AST") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to register a new SLM creator
    function registerSLM(string memory _description, uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        // Increment the SLM counter to get a new ID
        slmCounter++;
        
        // Create a new SLM and store it in the mapping
        slms[slmCounter] = SLM({
            id: slmCounter,
            creator: msg.sender,
            description: _description,
            rewardAmount: _rewardAmount,
            exists: true
        });

        emit SLMRegistered(msg.sender, slmCounter);
    }

    // Function to reward tokens to a registered SLM creator
    function rewardTokens(uint256 _slmId) external onlyOwner {
        SLM storage slm = slms[_slmId];
        require(slm.exists, "SLM does not exist");
        require(slm.rewardAmount > 0, "No reward amount set");

        // Transfer tokens to the SLM creator
        _transfer(owner(), slm.creator, slm.rewardAmount);
        
        emit TokensRewarded(slm.creator, slm.rewardAmount);
    }

    // Function to withdraw tokens from the contract (only for the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to get details of a specific SLM
    function getSLMDetails(uint256 _slmId) external view returns (SLM memory) {
        require(slms[_slmId].exists, "SLM does not exist");
        return slms[_slmId];
    }
}
```
