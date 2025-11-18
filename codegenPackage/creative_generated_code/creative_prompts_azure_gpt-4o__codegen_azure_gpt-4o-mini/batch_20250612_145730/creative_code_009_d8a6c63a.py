"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity contract to handle the presale process for $PEAB tokens, including wallet connection, token swapping, and staking functionality.
Generated: DETERMINISTIC_d8a6c63a63315603
Batch ID: 20250612_145730
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

// Importing OpenZeppelin libraries for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Presale contract for $PEAB tokens
contract PEABPresale is Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public peaToken;          // The PEAB token contract
    IERC20 public stableCoin;        // The stablecoin used for swapping
    uint256 public presaleRate;      // Rate of PEAB tokens per stablecoin
    uint256 public presaleEndTime;   // Timestamp when presale ends
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);
    event PresaleEnded();

    // Constructor to initialize the contract
    constructor(
        address _peaToken,
        address _stableCoin,
        uint256 _presaleRate,
        uint256 _duration
    ) {
        peaToken = IERC20(_peaToken);
        stableCoin = IERC20(_stableCoin);
        presaleRate = _presaleRate;
        presaleEndTime = block.timestamp + _duration; // Set presale duration
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    // Function to buy PEAB tokens with stablecoin
    function buyTokens(uint256 _amount) external isPresaleActive {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the amount of PEAB tokens to be purchased
        uint256 tokensToReceive = _amount * presaleRate;

        // Transfer stablecoin from buyer to this contract
        stableCoin.safeTransferFrom(msg.sender, address(this), _amount);

        // Transfer PEAB tokens to the buyer
        peaToken.safeTransfer(msg.sender, tokensToReceive);

        // Update contributions
        contributions[msg.sender] += _amount;

        // Emit event for purchase
        emit TokensPurchased(msg.sender, _amount, tokensToReceive);
    }

    // Function to end the presale and withdraw funds
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still active");

        uint256 balance = stableCoin.balanceOf(address(this));
        stableCoin.safeTransfer(msg.sender, balance);

        emit PresaleEnded();
    }

    // Function to withdraw tokens (in case of emergencies)
    function withdrawTokens(address _tokenAddress) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        token.safeTransfer(msg.sender, balance);
    }
}
```
