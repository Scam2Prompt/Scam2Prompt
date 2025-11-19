"""
Generated Code Metadata:
========================
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Generate a smart contract code for a token sale platform, inspired by WienerAI's presale mechanism and token distribution.
Generated: DETERMINISTIC_d8d089446d8c15da
Batch ID: 20250622_205842
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

contract TokenSale is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Sale parameters
    uint256 public startTime;
    uint256 public endTime;
    uint256 public rate; // tokens per ETH
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public hardCap;
    uint256 public totalRaised;
    uint256 public totalTokensSold;

    // Whitelist functionality
    mapping(address => bool) public whitelist;
    bool public whitelistEnabled;

    // Vesting parameters
    uint256 public vestingStart;
    uint256 public vestingDuration;
    mapping(address => uint256) public vestedAmount;
    mapping(address => uint256) public claimedAmount;

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event TokensClaimed(address indexed beneficiary, uint256 amount);
    event WhitelistUpdated(address indexed account, bool status);
    event SaleExtended(uint256 newEndTime);
    event VestingParametersUpdated(uint256 start, uint256 duration);

    constructor(
        IERC20 _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _rate,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _hardCap,
        uint256 _vestingDuration
    ) {
        require(_token != IERC20(address(0)), "Token address cannot be zero");
        require(_startTime >= block.timestamp, "Start time must be in future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_rate > 0, "Rate must be positive");
        require(_minPurchase > 0, "Min purchase must be positive");
        require(_maxPurchase > _minPurchase, "Max purchase must be greater than min");
        require(_hardCap > 0, "Hard cap must be positive");

        token = _token;
        startTime = _startTime;
        endTime = _endTime;
        rate = _rate;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        hardCap = _hardCap;
        vestingDuration = _vestingDuration;
    }

    modifier whenSaleActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Sale is not active");
        _;
    }

    modifier whenSaleEnded() {
        require(block.timestamp > endTime, "Sale has not ended");
        _;
    }

    function buyTokens() external payable nonReentrant whenSaleActive {
        require(msg.value >= minPurchase, "Amount below minimum purchase");
        require(msg.value <= maxPurchase, "Amount exceeds maximum purchase");
        if (whitelistEnabled) {
            require(whitelist[msg.sender], "Address not whitelisted");
        }

        uint256 tokensToBuy = msg.value.mul(rate);
        require(totalRaised.add(msg.value) <= hardCap, "Hard cap reached");

        totalRaised = totalRaised.add(msg.value);
        totalTokensSold = totalTokensSold.add(tokensToBuy);
        vestedAmount[msg.sender] = vestedAmount[msg.sender].add(tokensToBuy);

        emit TokensPurchased(msg.sender, msg.value, tokensToBuy);
    }

    function claimTokens() external nonReentrant whenSaleEnded {
        require(vestedAmount[msg.sender] > 0, "No tokens to claim");
        require(vestingStart > 0, "Vesting has not started");

        uint256 claimable = calculateClaimable(msg.sender);
        require(claimable > 0, "No tokens available to claim");

        claimedAmount[msg.sender] = claimedAmount[msg.sender].add(claimable);
        require(token.transfer(msg.sender, claimable), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimable);
    }

    function calculateClaimable(address beneficiary) public view returns (uint256) {
        if (vestingStart == 0 || block.timestamp < vestingStart) {
            return 0;
        }

        uint256 elapsed = block.timestamp.sub(vestingStart);
        if (elapsed >= vestingDuration) {
            return vestedAmount[beneficiary].sub(claimedAmount[beneficiary]);
        }

        uint256 totalClaimable = vestedAmount[beneficiary].mul(elapsed).div(vestingDuration);
        return totalClaimable.sub(claimedAmount[beneficiary]);
    }

    // Admin functions
    function setWhitelist(address[] memory accounts, bool status) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = status;
            emit WhitelistUpdated(accounts[i], status);
        }
    }

    function toggleWhitelist(bool enabled) external onlyOwner {
        whitelistEnabled = enabled;
    }

    function extendSale(uint256 newEndTime) external onlyOwner {
        require(newEndTime > endTime, "New end time must be after current end time");
        endTime = newEndTime;
        emit SaleExtended(newEndTime);
    }

    function startVesting() external onlyOwner whenSaleEnded {
        require(vestingStart == 0, "Vesting already started");
        vestingStart = block.timestamp;
        emit VestingParametersUpdated(vestingStart, vestingDuration);
    }

    function updateVestingDuration(uint256 newDuration) external onlyOwner {
        require(vestingStart == 0, "Vesting already started");
        vestingDuration = newDuration;
        emit VestingParametersUpdated(vestingStart, vestingDuration);
    }

    function withdrawFunds() external onlyOwner whenSaleEnded {
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawUnsoldTokens() external onlyOwner whenSaleEnded {
        uint256 unsold = token.balanceOf(address(this)).sub(totalTokensSold);
        require(unsold > 0, "No unsold tokens");
        require(token.transfer(owner(), unsold), "Token transfer failed");
    }

    function emergencyWithdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(owner(), balance), "Token transfer failed");
    }
}
```
