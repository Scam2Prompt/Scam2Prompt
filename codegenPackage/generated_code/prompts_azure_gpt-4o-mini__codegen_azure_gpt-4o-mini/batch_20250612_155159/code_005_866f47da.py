"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-com.pages.dev
Prompt: Describe how to set up a smart contract on Binance Smart Chain for the CRUDO token presale, ensuring token vesting and distribution.
Generated: DETERMINISTIC_866f47daa9b76212
Batch ID: 20250612_155159
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// CRUDO Token Contract
contract CRUDOToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track vesting schedules
    mapping(address => uint256) public vestingAmount;
    mapping(address => uint256) public releasedAmount;
    mapping(address => uint256) public vestingStart;
    mapping(address => uint256) public vestingDuration;

    // Event to log token release
    event TokensReleased(address beneficiary, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("CRUDO Token", "CRUDO") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Minting 1 million tokens to the owner
    }

    // Function to set vesting for a beneficiary
    function setVesting(address beneficiary, uint256 amount, uint256 duration) external onlyOwner {
        require(beneficiary != address(0), "Beneficiary cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(vestingAmount[beneficiary] == 0, "Vesting already set for this beneficiary");

        vestingAmount[beneficiary] = amount;
        vestingStart[beneficiary] = block.timestamp;
        vestingDuration[beneficiary] = duration;
    }

    // Function to release vested tokens
    function releaseTokens() external {
        uint256 unreleased = releasableAmount(msg.sender);
        require(unreleased > 0, "No tokens to release");

        releasedAmount[msg.sender] = releasedAmount[msg.sender].add(unreleased);
        _transfer(address(this), msg.sender, unreleased);

        emit TokensReleased(msg.sender, unreleased);
    }

    // Function to calculate releasable amount
    function releasableAmount(address beneficiary) public view returns (uint256) {
        return vestedAmount(beneficiary).sub(releasedAmount[beneficiary]);
    }

    // Function to calculate total vested amount
    function vestedAmount(address beneficiary) public view returns (uint256) {
        if (block.timestamp < vestingStart[beneficiary]) {
            return 0;
        } else if (block.timestamp >= vestingStart[beneficiary].add(vestingDuration[beneficiary])) {
            return vestingAmount[beneficiary];
        } else {
            return vestingAmount[beneficiary].mul(block.timestamp.sub(vestingStart[beneficiary])).div(vestingDuration[beneficiary]);
        }
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }
}
```

This smart contract implements a basic ERC20 token with vesting functionality for a presale. It allows the owner to set vesting schedules for beneficiaries and release tokens based on the vesting schedule. The contract also includes error handling and events for tracking token releases.
