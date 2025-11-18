"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Write a Solidity function that integrates with the Dai Savings Rate (DSR) to earn yield from DAI holdings, as described in OUSD's yield strategies.
Generated: DETERMINISTIC_063cf638219623d5
Batch ID: 20250612_150622
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
 * @title DaiSavingsRateIntegration
 * @dev This contract integrates with the Dai Savings Rate (DSR) to earn yield from DAI holdings.
 *      It assumes the use of MakerDAO's Pot contract for DSR functionality.
 */
interface Pot {
    function chi() external view returns (uint256); // Rate accumulator
    function pie(address) external view returns (uint256); // User's balance in DSR
    function drip() external; // Updates the chi value
    function join(uint256) external; // Deposit DAI into the DSR
    function exit(uint256) external; // Withdraw DAI from the DSR
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DaiSavingsRateIntegration {
    address public immutable daiToken; // Address of the DAI token
    address public immutable pot; // Address of MakerDAO's Pot contract for DSR
    uint256 public savedPie; // Local record of pie (DSR balance)

    constructor(address _daiToken, address _pot) {
        require(_daiToken != address(0), "Invalid DAI token address");
        require(_pot != address(0), "Invalid Pot contract address");
        daiToken = _daiToken;
        pot = _pot;

        // Approve Pot contract to pull DAI from this contract
        IERC20(daiToken).approve(pot, type(uint256).max);
    }

    /**
     * @notice Deposit DAI into the Dai Savings Rate to start earning yield.
     * @param amount The amount of DAI to deposit (in wei).
     */
    function depositToDSR(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer DAI from the sender to this contract
        IERC20(daiToken).transferFrom(msg.sender, address(this), amount);

        // Update the chi value in the Pot contract
        Pot(pot).drip();

        // Convert DAI into pie (DSR balance unit) and deposit into the DSR
        uint256 pieToSave = amount * 1e27 / Pot(pot).chi(); // chi is scaled by 1e27
        Pot(pot).join(pieToSave);

        // Update the local record of pie
        savedPie += pieToSave;
    }

    /**
     * @notice Withdraw DAI from the Dai Savings Rate back to the user's wallet.
     * @param amount The amount of DAI to withdraw (in wei).
     */
    function withdrawFromDSR(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Update the chi value in the Pot contract
        Pot(pot).drip();

        // Convert DAI amount to pie and ensure sufficient balance
        uint256 pieToWithdraw = amount * 1e27 / Pot(pot).chi(); // chi is scaled by 1e27
        require(pieToWithdraw <= savedPie, "Insufficient DSR balance");

        // Withdraw the pie from the DSR
        Pot(pot).exit(pieToWithdraw);

        // Update the local record of pie
        savedPie -= pieToWithdraw;

        // Transfer the withdrawn DAI back to the sender
        IERC20(daiToken).transfer(msg.sender, amount);
    }

    /**
     * @notice Get the current DAI balance held in the Dai Savings Rate (DSR) for this contract.
     * @return The equivalent DAI balance in wei.
     */
    function getDsrBalance() external view returns (uint256) {
        uint256 chi = Pot(pot).chi(); // Current chi value
        return savedPie * chi / 1e27; // Convert pie back to DAI
    }
}
```
