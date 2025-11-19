"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-com.pages.dev
Prompt: Describe how to set up a smart contract on Binance Smart Chain for the CRUDO token presale, ensuring token vesting and distribution.
Generated: DETERMINISTIC_866f47daa9b76212
Batch ID: 20250612_155159
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

/**
 * @title CRUDO Token Presale Contract
 * @dev This contract handles the presale, token vesting, and distribution of the CRUDO token on Binance Smart Chain.
 */
contract CRUDO_Presale {
    // CRUDO Token Interface
    IERC20 public immutable crudoToken;

    // Presale variables
    uint256 public presaleRate; // Number of tokens per 1 BNB
    uint256 public presaleCap; // Maximum tokens allocated for presale
    uint256 public totalSold; // Total tokens sold during presale
    address public owner; // Owner of the presale contract

    // Vesting structure
    struct VestingSchedule {
        uint256 amount; // Total amount of tokens to be vested
        uint256 released; // Amount of tokens already released
        uint256 start; // Vesting start timestamp
        uint256 cliff; // Cliff period in seconds
        uint256 duration; // Vesting duration in seconds
    }

    mapping(address => VestingSchedule) public vestingSchedules;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor
    constructor(address _crudoToken, uint256 _rate, uint256 _cap) {
        require(_crudoToken != address(0), "Invalid token address");
        require(_rate > 0, "Rate must be greater than zero");
        require(_cap > 0, "Cap must be greater than zero");

        crudoToken = IERC20(_crudoToken);
        presaleRate = _rate;
        presaleCap = _cap;
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param beneficiary Address to receive vested tokens.
     */
    function purchaseTokens(address beneficiary) external payable {
        require(beneficiary != address(0), "Beneficiary address is zero");
        require(msg.value > 0, "BNB value must be greater than zero");

        uint256 tokensToPurchase = msg.value * presaleRate;
        require(totalSold + tokensToPurchase <= presaleCap, "Presale cap exceeded");

        totalSold += tokensToPurchase;

        // Set up vesting schedule for the beneficiary
        VestingSchedule storage schedule = vestingSchedules[beneficiary];
        schedule.amount += tokensToPurchase;
        schedule.start = block.timestamp;
        schedule.cliff = 30 days; // Example cliff period
        schedule.duration = 180 days; // Example vesting duration

        emit TokensPurchased(beneficiary, tokensToPurchase);
    }

    /**
     * @dev Release vested tokens to beneficiary.
     */
    function releaseTokens() external {
        VestingSchedule storage schedule = vestingSchedules[msg.sender];
        require(schedule.amount > 0, "No tokens to vest");
        require(block.timestamp >= schedule.start + schedule.cliff, "Cliff period not reached");

        uint256 unreleased = _vestedAmount(msg.sender) - schedule.released;
        require(unreleased > 0, "No tokens available for release");

        schedule.released += unreleased;

        crudoToken.transfer(msg.sender, unreleased);
        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Calculate the amount of vested tokens for a beneficiary.
     * @param beneficiary Address of the beneficiary.
     * @return Amount of vested tokens.
     */
    function _vestedAmount(address beneficiary) internal view returns (uint256) {
        VestingSchedule storage schedule = vestingSchedules[beneficiary];

        if (block.timestamp < schedule.start + schedule.cliff) {
            return 0;
        } else if (block.timestamp >= schedule.start + schedule.duration) {
            return schedule.amount;
        } else {
            uint256 timeElapsed = block.timestamp - schedule.start;
            uint256 vestingDuration = schedule.duration;
            return (schedule.amount * timeElapsed) / vestingDuration;
        }
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address is zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Withdraw collected BNB to owner address.
     */
    function withdrawBNB() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Emergency withdrawal of CRUDO tokens by owner.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyTokenWithdraw(uint256 amount) external onlyOwner {
        crudoToken.transfer(owner, amount);
    }

    // Fallback function to accept BNB.
    receive() external payable {}
}

/**
 * @dev Minimal ERC20 interface to interact with CRUDO Token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
