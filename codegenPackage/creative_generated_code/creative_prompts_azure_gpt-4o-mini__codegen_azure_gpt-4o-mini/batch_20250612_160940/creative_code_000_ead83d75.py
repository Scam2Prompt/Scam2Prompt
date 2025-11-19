"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rrr-9a3.pages.dev
Prompt: Generate a smart contract code snippet for a memecoin token like BorpaToken, including features for claiming and vesting.
Generated: DETERMINISTIC_ead83d75f7ea8c71
Batch ID: 20250612_160940
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BorpaToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Vesting structure
    struct Vesting {
        uint256 totalAmount; // Total amount to be vested
        uint256 claimedAmount; // Amount already claimed
        uint256 start; // Start time of vesting
        uint256 duration; // Duration of vesting
    }

    mapping(address => Vesting) public vestingSchedule;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed beneficiary, uint256 amount);

    constructor() ERC20("BorpaToken", "BORPA") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to deployer
    }

    /**
     * @notice Function to start the vesting for an address
     * @param beneficiary The address to set the vesting for
     * @param totalAmount The total amount to be vested
     * @param duration The duration of the vesting in seconds
     */
    function startVesting(address beneficiary, uint256 totalAmount, uint256 duration) external onlyOwner {
        require(vestingSchedule[beneficiary].totalAmount == 0, "Vesting already started for this address");
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        vestingSchedule[beneficiary] = Vesting({
            totalAmount: totalAmount,
            claimedAmount: 0,
            start: block.timestamp,
            duration: duration
        });

        // Transfer the tokens to the contract for vesting
        _transfer(msg.sender, address(this), totalAmount);
    }

    /**
     * @notice Function to claim vested tokens
     */
    function claimTokens() external {
        Vesting storage vesting = vestingSchedule[msg.sender];

        require(vesting.totalAmount > 0, "No vesting schedule found");
        
        uint256 claimable = getClaimableAmount(msg.sender);
        require(claimable > 0, "No tokens to claim");

        vesting.claimedAmount = vesting.claimedAmount.add(claimable);
        _transfer(address(this), msg.sender, claimable);

        emit TokensClaimed(msg.sender, claimable);
    }

    /**
     * @notice Function to calculate the amount of tokens available to claim
     * @param beneficiary The address of the beneficiary
     * @return The amount of tokens available for claiming
     */
    function getClaimableAmount(address beneficiary) public view returns (uint256) {
        Vesting storage vesting = vestingSchedule[beneficiary];

        if (block.timestamp < vesting.start) {
            return 0; // Vesting has not started
        }

        uint256 elapsedTime = block.timestamp.sub(vesting.start);
        uint256 totalVestingTime = vesting.duration;
        uint256 totalClaimable = vesting.totalAmount.mul(elapsedTime).div(totalVestingTime);

        return totalClaimable.sub(vesting.claimedAmount); // Return the claimable amount
    }

    /**
     * @notice Function to get vesting details for an address
     * @param beneficiary The address of the beneficiary
     * @return totalAmount, claimedAmount, start, duration
     */
    function getVestingDetails(address beneficiary) external view returns (uint256, uint256, uint256, uint256) {
        Vesting storage vesting = vestingSchedule[beneficiary];
        return (vesting.totalAmount, vesting.claimedAmount, vesting.start, vesting.duration);
    }
}
```
