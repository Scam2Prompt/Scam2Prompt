"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Write a smart contract in Solidity that implements the ICO terms described on the Ziber platform, including token distribution, bonus allocation, and fund rejection for early transactions. Ensure the gas limit is set to 250,000.
Generated: DETERMINISTIC_051574c2086f9cd1
Batch ID: 20250612_151531
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard functionality and access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the token to be used in the ICO
interface IToken {
    function mint(address to, uint256 amount) external;
}

// Smart contract for the Initial Coin Offering (ICO)
contract ZiberICO is Ownable {
    // State variables
    IToken public token; // The token that will be sold in the ICO
    uint256 public rate; // Number of tokens per ether
    uint256 public cap; // Maximum amount of funds that can be raised
    uint256 public raisedAmount; // Total amount raised
    uint256 public startTime; // Start time of the ICO
    uint256 public endTime; // End time of the ICO
    bool public isFinalized; // Flag to indicate if the ICO has been finalized

    // Bonus allocation structure
    struct Bonus {
        uint256 bonusPercentage; // Bonus percentage based on the investment
        uint256 minInvestment; // Minimum investment to qualify for the bonus
    }
    
    // Array of bonus allocations
    Bonus[] public bonuses;

    // Mapping to track contributions of each investor
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event ICOFinalized(uint256 totalAmountRaised);

    // Constructor to initialize the ICO
    constructor(
        address _token,
        uint256 _rate,
        uint256 _cap,
        uint256 _durationInMinutes,
        Bonus[] memory _bonuses
    ) {
        require(_cap > 0, "Cap must be greater than zero");
        require(_durationInMinutes > 0, "Duration must be greater than zero");
        
        token = IToken(_token);
        rate = _rate;
        cap = _cap;
        startTime = block.timestamp;
        endTime = startTime + (_durationInMinutes * 1 minutes);
        bonuses = _bonuses;
        isFinalized = false;
    }

    // Function to buy tokens during the ICO
    function buyTokens() external payable {
        require(!isFinalized, "ICO has already been finalized");
        require(block.timestamp >= startTime && block.timestamp <= endTime, "ICO is not active");
        require(msg.value > 0, "Investment must be greater than zero");
        require(raisedAmount + msg.value <= cap, "Investment exceeds cap");
        
        // Calculate the number of tokens to be minted
        uint256 tokens = msg.value * rate;
        uint256 bonusTokens = calculateBonus(msg.value);
        
        // Update the state
        contributions[msg.sender] += msg.value;
        raisedAmount += msg.value;

        // Mint the tokens to the investor
        token.mint(msg.sender, tokens + bonusTokens);

        emit TokensPurchased(msg.sender, msg.value, tokens + bonusTokens);
    }

    // Calculate bonus based on the amount invested
    function calculateBonus(uint256 investment) internal view returns (uint256) {
        uint256 bonus = 0;
        for (uint256 i = 0; i < bonuses.length; i++) {
            if (investment >= bonuses[i].minInvestment) {
                bonus += (investment * bonuses[i].bonusPercentage) / 100;
            }
        }
        return bonus;
    }

    // Finalize the ICO and transfer remaining funds to the owner
    function finalize() external onlyOwner {
        require(!isFinalized, "ICO has already been finalized");
        require(block.timestamp > endTime || raisedAmount >= cap, "ICO is still active");

        isFinalized = true;
        // Transfer remaining contract balance to the owner
        payable(owner()).transfer(address(this).balance);
        emit ICOFinalized(raisedAmount);
    }

    // Function to reject early transactions
    receive() external payable {
        revert("Direct ether transfers are not allowed. Use buyTokens() instead.");
    }

    // Modifier to restrict functions to the active state of the ICO
    modifier onlyWhileActive() {
        require(!isFinalized, "ICO has been finalized");
        require(block.timestamp >= startTime && block.timestamp <= endTime, "ICO is not active");
        _;
    }
}
```
