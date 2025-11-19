"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Describe the steps to build a decentralized economy using Moxie’s smart contracts and how to extend its functionality.
Generated: DETERMINISTIC_9ecd5cd5c72134d5
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Building a decentralized economy involves creating smart contracts, deploying them, and then extending their functionality. Below is a Solidity smart contract example for a basic decentralized economy using a token system, along with steps to extend it.  

### 1. Basic Token Contract (`DecentralizedEconomy.sol`)  
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DecentralizedEconomy
 * @dev A basic ERC20 token contract for a decentralized economy.
 */
contract DecentralizedEconomy is ERC20, Ownable {
    /**
     * @dev Initializes the contract by minting initial supply to the contract deployer.
     * @param initialSupply The initial token supply to be minted.
     */
    constructor(uint256 initialSupply) ERC20("DecentralizedEconomyToken", "DET") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Creates new tokens and assigns them to an account.
     * @param account The account receiving the new tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) public onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Burns tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }
}
```

### 2. Extended Functionality (Governance and Staking)  
Create another contract (`DecentralizedEconomyGovernance.sol`) to handle governance and staking:  

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DecentralizedEconomyGovernance
 * @dev Extends the economy with governance and staking capabilities.
 */
contract DecentralizedEconomyGovernance is Ownable {
    IERC20 public token;

    struct Proposal {
        string description;
        uint256 voteCount;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public votes;
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public lastStakeTime;

    uint256 public proposalCount;
    uint256 public stakingLockTime = 7 days;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(address indexed voter, uint256 proposalId);

    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Stake tokens to participate in governance and earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        stakedBalance[msg.sender] += amount;
        lastStakeTime[msg.sender] = block.timestamp;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens after the lock period.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalance[msg.sender] >= amount, "Not enough staked tokens");
        require(
            block.timestamp >= lastStakeTime[msg.sender] + stakingLockTime,
            "Tokens are locked"
        );
        
        stakedBalance[msg.sender] -= amount;
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Create a new governance proposal.
     * @param description Description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: description,
            voteCount: 0
        });
        
        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @dev Vote for a proposal using staked tokens.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external {
        require(stakedBalance[msg.sender] > 0, "No staked tokens to vote");
        require(!votes[msg.sender][proposalId], "Already voted");
        
        votes[msg.sender][proposalId] = true;
        proposals[proposalId].voteCount += stakedBalance[msg.sender];
        
        emit Voted(msg.sender, proposalId);
    }
}
```

### Deployment Script (`deploy.js`)  
```javascript
const { ethers } = require("hardhat");

async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contracts with the account:", deployer.address);

    // Deploy token contract
    const Token = await ethers.getContractFactory("DecentralizedEconomy");
    const token = await Token.deploy(1000000); // Initial supply = 1,000,000
    await token.deployed();
    console.log("Token deployed to:", token.address);

    // Deploy governance contract
    const Governance = await ethers.getContractFactory("DecentralizedEconomyGovernance");
    const governance = await Governance.deploy(token.address);
    await governance.deployed();
    console.log("Governance deployed to:", governance.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

This code provides:  
- A basic token economy (ERC20)  
- Governance and staking extensions  
- Deployment script for testing  

To extend further:  
- Add DAO functionality  
- Integrate a decentralized exchange (DEX)  
- Implement yield farming mechanisms  
- Add multi-chain compatibility via bridge contracts  

Would you like additional extensions?
