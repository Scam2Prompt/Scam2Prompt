"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicatclaim.pages.dev
Prompt: Create a step-by-step guide for deploying an ERC20 token on the Ethereum blockchain, ensuring it includes features like staking and token claiming as described in the KAI presale.
Generated: DETERMINISTIC_45436f463cb22b36
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

// Importing OpenZeppelin Contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// ERC20Token contract that includes staking and token claiming features
contract ERC20Token is ERC20, Ownable, ReentrancyGuard {
    // Mapping to store staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;

    // Events for staking and claiming
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to get the staked balance of a user
    function stakedBalance(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to claim staked tokens
    function claim(uint256 amount) external nonReentrant {
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Transfer claimed tokens back to the user
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Claimed(msg.sender, amount);
    }

    // Function to get total staked tokens
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to withdraw tokens accidentally sent to contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), msg.sender, amount);
    }
}
```

### Steps for Deployment
1. Install Node.js and npm (Node Package Manager).
2. Install Truffle or Hardhat for managing your Ethereum development environment.
3. Set up a new project using Truffle or Hardhat (`truffle init` or `npx hardhat`).
4. Install OpenZeppelin Contracts: `npm install @openzeppelin/contracts`.
5. Create a new Solidity file for your token contract in the `contracts` directory.
6. Copy the provided code into your new Solidity file.
7. Create a deployment script in the `migrations` or `scripts` directory.
8. Configure your network settings in the configuration file (e.g., `truffle-config.js` or `hardhat.config.js`).
9. Compile the contract using `truffle compile` or `npx hardhat compile`.
10. Deploy the contract to your desired Ethereum network using `truffle migrate` or `npx hardhat run scripts/deploy.js --network <network_name>`.
11. Verify your contract on Etherscan using the appropriate verification process provided by your toolset.

### Note
Ensure that you have a wallet set up (like MetaMask) and some Ether for gas fees to deploy the contract on the Ethereum network.
