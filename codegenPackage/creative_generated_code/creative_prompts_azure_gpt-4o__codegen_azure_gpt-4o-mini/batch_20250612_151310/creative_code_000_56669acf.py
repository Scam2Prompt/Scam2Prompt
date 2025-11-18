"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelexocrypto.pages.dev
Prompt: Write a smart contract for a cryptocurrency presale similar to KoalaKash, ensuring that team tokens are locked for 550 days and liquidity is locked for life. Include comments explaining each step.
Generated: DETERMINISTIC_56669acfe2e6d243
Batch ID: 20250612_151310
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

// Import OpenZeppelin's ERC20 token implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PresaleToken is ERC20, Ownable, ReentrancyGuard {
    // State variables
    uint256 public presaleEndTime;
    uint256 public constant teamLockDuration = 550 days; // Duration for which team tokens are locked
    uint256 public constant liquidityLockDuration = type(uint256).max; // Set liquidity lock for life
    address public liquidityWallet;
    address public teamWallet;
    
    // Mapping to track locked token amounts
    mapping(address => uint256) public lockedTokens;
    bool public liquidityLocked = false;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TeamTokensLocked(uint256 amount);
    event LiquidityLocked(uint256 amount);

    // Constructor to initialize the presale token
    constructor(string memory name, string memory symbol, address _teamWallet, address _liquidityWallet) 
        ERC20(name, symbol) {
        teamWallet = _teamWallet;
        liquidityWallet = _liquidityWallet;
        _mint(address(this), 1_000_000 * 10 ** decimals()); // Mint initial supply to contract
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        require(presaleEndTime == 0, "Presale already started");
        presaleEndTime = block.timestamp + duration;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 amount) external payable nonReentrant {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Ether value sent is 0");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Not enough tokens in contract");

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, amount);
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to lock the team tokens
    function lockTeamTokens(uint256 amount) external onlyOwner {
        require(lockedTokens[teamWallet] == 0, "Team tokens already locked");
        lockedTokens[teamWallet] = amount;

        // Transfer the team tokens to the contract for locking
        _transfer(teamWallet, address(this), amount);
        emit TeamTokensLocked(amount);
    }

    // Function to lock liquidity forever
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(!liquidityLocked, "Liquidity already locked");
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer liquidity tokens to the contract for locking
        _transfer(liquidityWallet, address(this), amount);
        liquidityLocked = true;
        emit LiquidityLocked(amount);
    }

    // Function to withdraw Ether raised in presale
    function withdrawEther() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale still ongoing");
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept ether
    receive() external payable {}
}
```
