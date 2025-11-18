"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Develop a Solidity contract for BTC20 that integrates a fair presale mechanism, locking unsold tokens into a staking pool for long-term rewards distribution.
Generated: DETERMINISTIC_745549da0d634e92
Batch ID: 20250612_151333
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the staking pool contract
interface IStakingPool {
    function lockUnsoldTokens(uint256 amount) external;
}

contract BTC20 is ERC20, Ownable {
    using SafeMath for uint256;

    // State variables for presale
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price in wei (e.g., 0.01 ETH)
    uint256 public totalTokensForSale;
    uint256 public soldTokens;

    // Address of the staking pool contract
    IStakingPool public stakingPool;

    // Events
    event PresaleBought(address indexed buyer, uint256 amount);
    event TokensLocked(uint256 amount);

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        _;
    }

    // Constructor to initialize the token and presale
    constructor(
        string memory name,
        string memory symbol,
        uint256 _totalTokensForSale,
        uint256 _tokenPrice,
        address _stakingPool
    ) ERC20(name, symbol) {
        require(_totalTokensForSale > 0, "Total tokens must be greater than zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        totalTokensForSale = _totalTokensForSale;
        tokenPrice = _tokenPrice;
        stakingPool = IStakingPool(_stakingPool);
        _mint(address(this), _totalTokensForSale);
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp.add(duration);
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 amount) external payable presaleActive {
        require(msg.value == amount.mul(tokenPrice), "Incorrect ETH amount sent");
        require(soldTokens.add(amount) <= totalTokensForSale, "Not enough tokens available");

        soldTokens = soldTokens.add(amount);
        _transfer(address(this), msg.sender, amount);
        emit PresaleBought(msg.sender, amount);
    }

    // Function to finalize the presale and lock unsold tokens
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale still active");
        uint256 unsoldTokens = totalTokensForSale.sub(soldTokens);
        if (unsoldTokens > 0) {
            _transfer(address(this), address(stakingPool), unsoldTokens);
            stakingPool.lockUnsoldTokens(unsoldTokens);
            emit TokensLocked(unsoldTokens);
        }
    }

    // Fallback function to accept ether
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
