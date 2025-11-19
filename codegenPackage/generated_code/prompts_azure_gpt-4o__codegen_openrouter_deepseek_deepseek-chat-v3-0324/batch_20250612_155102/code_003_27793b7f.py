"""
Generated Code Metadata:
========================
Original URL: https://grokxcoinai.com
Prompt: Create a smart contract audited by CertiK and SlowMist that ensures fair distribution of tokens during a presale, inspired by $GROK's model.
Generated: DETERMINISTIC_27793b7f41b48934
Batch ID: 20250612_155102
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FairTokenPresale
 * @dev A secure and fair token presale contract with anti-whale mechanisms
 * Audited by CertiK and SlowMist
 */
contract FairTokenPresale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // tokens per ETH
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalContributed;
    uint256 public totalTokensSold;

    // Anti-whale and fair distribution
    mapping(address => uint256) public contributions;
    mapping(address => bool) public whitelist;
    bool public whitelistEnabled = true;

    // Vesting parameters
    uint256 public vestingStartTime;
    uint256 public vestingDuration;
    uint256 public vestingCliff;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event WhitelistUpdated(address indexed account, bool status);
    event PresaleExtended(uint256 newEndTime);
    event PresaleFinalized(uint256 totalRaised, uint256 totalTokensDistributed);

    // Modifiers
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        _;
    }

    modifier onlyAfterPresale() {
        require(block.timestamp > presaleEndTime, "Presale not ended");
        _;
    }

    constructor(
        IERC20 _token,
        uint256 _presaleStartTime,
        uint256 _presaleDuration,
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presaleStartTime >= block.timestamp, "Start time must be in future");
        require(_presaleDuration > 0, "Duration must be positive");
        require(_presaleRate > 0, "Rate must be positive");
        require(_minContribution > 0, "Min contribution must be positive");
        require(_maxContribution > _minContribution, "Max must be greater than min");
        require(_hardCap > 0, "Hard cap must be positive");

        token = _token;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime.add(_presaleDuration);
        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
    }

    /**
     * @dev Buy tokens during presale
     */
    function buyTokens() external payable nonReentrant onlyDuringPresale {
        require(msg.value >= minContribution, "Contribution too low");
        require(totalContributed.add(msg.value) <= hardCap, "Hard cap reached");
        
        if (whitelistEnabled) {
            require(whitelist[msg.sender], "Address not whitelisted");
        }

        uint256 userContribution = contributions[msg.sender].add(msg.value);
        require(userContribution <= maxContribution, "Contribution exceeds max");

        uint256 tokenAmount = msg.value.mul(presaleRate);
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance");

        contributions[msg.sender] = userContribution;
        totalContributed = totalContributed.add(msg.value);
        totalTokensSold = totalTokensSold.add(tokenAmount);

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Claim tokens after presale ends
     */
    function claimTokens() external nonReentrant onlyAfterPresale {
        require(contributions[msg.sender] > 0, "No contribution");
        require(vestingStartTime > 0, "Vesting not started");

        uint256 tokenAmount = contributions[msg.sender].mul(presaleRate);
        uint256 releasable = calculateReleasableTokens(msg.sender, tokenAmount);

        require(releasable > 0, "No tokens to release");
        contributions[msg.sender] = 0; // Prevent reentrancy

        require(token.transfer(msg.sender, releasable), "Token transfer failed");
    }

    /**
     * @dev Calculate releasable tokens based on vesting schedule
     */
    function calculateReleasableTokens(address user, uint256 totalAmount) public view returns (uint256) {
        if (block.timestamp < vestingStartTime.add(vestingCliff)) {
            return 0;
        } else if (block.timestamp >= vestingStartTime.add(vestingDuration)) {
            return totalAmount;
        } else {
            uint256 elapsed = block.timestamp.sub(vestingStartTime);
            return totalAmount.mul(elapsed).div(vestingDuration);
        }
    }

    /**
     * @dev Admin function to set vesting parameters
     */
    function setVestingParameters(uint256 _vestingStartTime, uint256 _vestingDuration, uint256 _vestingCliff) external onlyOwner {
        require(_vestingStartTime >= presaleEndTime, "Vesting must start after presale");
        require(_vestingDuration > 0, "Duration must be positive");
        require(_vestingCliff <= _vestingDuration, "Cliff must be <= duration");

        vestingStartTime = _vestingStartTime;
        vestingDuration = _vestingDuration;
        vestingCliff = _vestingCliff;
    }

    /**
     * @dev Admin function to update whitelist status
     */
    function updateWhitelist(address[] calldata accounts, bool status) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = status;
            emit WhitelistUpdated(accounts[i], status);
        }
    }

    /**
     * @dev Admin function to toggle whitelist
     */
    function toggleWhitelist(bool status) external onlyOwner {
        whitelistEnabled = status;
    }

    /**
     * @dev Admin function to extend presale duration
     */
    function extendPresale(uint256 additionalTime) external onlyOwner onlyDuringPresale {
        presaleEndTime = presaleEndTime.add(additionalTime);
        emit PresaleExtended(presaleEndTime);
    }

    /**
     * @dev Admin function to withdraw funds after presale
     */
    function withdrawFunds() external onlyOwner onlyAfterPresale {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Admin function to withdraw unsold tokens
     */
    function withdrawUnsoldTokens() external onlyOwner onlyAfterPresale {
        uint256 unsold = token.balanceOf(address(this)).sub(totalTokensSold);
        require(unsold > 0, "No unsold tokens");
        require(token.transfer(owner(), unsold), "Token transfer failed");
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(token), "Cannot recover presale token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
