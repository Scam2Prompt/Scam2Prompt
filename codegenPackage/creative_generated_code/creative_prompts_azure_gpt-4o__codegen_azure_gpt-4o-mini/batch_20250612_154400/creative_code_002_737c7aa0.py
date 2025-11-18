"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quantprotocol.xyz
Prompt: Create a smart contract on the Binance Smart Chain (BSC) for purchasing Quant Protocol tokens during the pre-sale phase. Ensure the contract includes vesting logic for team tokens with a 6-month period.
Generated: DETERMINISTIC_737c7aa0b87a1bd1
Batch ID: 20250612_154400
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title QuantProtocolPresale
 * @dev Smart contract for the Quant Protocol token pre-sale with vesting for team tokens.
 */
contract QuantProtocolPresale is Ownable {
    using SafeMath for uint256;

    IERC20 public quantToken; // Address of the Quant Protocol token
    uint256 public presaleEndTime; // Timestamp for when the presale ends
    uint256 public vestingStart; // Timestamp for when vesting starts
    uint256 public constant VESTING_DURATION = 180 days; // 6 months vesting period
    uint256 public totalTokensSold; // Total tokens sold during presale

    mapping(address => uint256) public contributions; // User contributions
    mapping(address => uint256) public teamTokens; // Team token allocation
    mapping(address => uint256) public releasedTokens; // Track released tokens for vesting

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensReleased(address indexed teamMember, uint256 amount);

    /**
     * @param _quantToken Address of the Quant Protocol token contract
     * @param _presaleDuration Duration of the presale in seconds
     */
    constructor(IERC20 _quantToken, uint256 _presaleDuration) {
        quantToken = _quantToken;
        presaleEndTime = block.timestamp.add(_presaleDuration);
        vestingStart = block.timestamp.add(VESTING_DURATION);
    }

    /**
     * @dev Purchase tokens during the presale phase
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Payment is required");
        require(_amount > 0, "Amount must be greater than zero");

        // Assuming 1 ETH = 1000 QUANT for simplicity; adjust as needed
        uint256 tokenPrice = 1000; // Example price
        uint256 requiredEther = _amount.div(tokenPrice);
        require(msg.value >= requiredEther, "Insufficient Ether sent");

        contributions[msg.sender] = contributions[msg.sender].add(_amount);
        totalTokensSold = totalTokensSold.add(_amount);
        
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Add team tokens allocation (only callable by owner)
     * @param _teamMember Address of the team member
     * @param _amount Amount of tokens to allocate
     */
    function allocateTeamTokens(address _teamMember, uint256 _amount) external onlyOwner {
        require(_teamMember != address(0), "Invalid address");
        require(_amount > 0, "Amount must be greater than zero");
        
        teamTokens[_teamMember] = teamTokens[_teamMember].add(_amount);
    }

    /**
     * @dev Release tokens for team members after vesting period
     */
    function releaseTokens() external {
        require(block.timestamp >= vestingStart, "Vesting has not started");
        uint256 unreleased = releasableTokens(msg.sender);
        require(unreleased > 0, "No tokens to release");

        releasedTokens[msg.sender] = releasedTokens[msg.sender].add(unreleased);
        quantToken.transfer(msg.sender, unreleased);
        
        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculate releasable tokens for a team member
     * @param _teamMember Address of the team member
     * @return uint256 Amount of tokens that can be released
     */
    function releasableTokens(address _teamMember) public view returns (uint256) {
        if (block.timestamp < vestingStart) {
            return 0;
        }

        uint256 totalAllocated = teamTokens[_teamMember];
        uint256 timeElapsed = block.timestamp.sub(vestingStart);
        uint256 vestedAmount = totalAllocated.mul(timeElapsed).div(VESTING_DURATION);
        return vestedAmount.sub(releasedTokens[_teamMember]);
    }

    /**
     * @dev Withdraw collected Ether by the owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether
     */
    receive() external payable {}
}
```
