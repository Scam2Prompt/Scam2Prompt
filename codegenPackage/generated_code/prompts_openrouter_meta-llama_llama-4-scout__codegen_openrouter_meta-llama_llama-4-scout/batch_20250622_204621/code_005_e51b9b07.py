"""
Generated Code Metadata:
========================
Original URL: https://multichainetfclaim.pages.dev
Prompt: Write a Solidity function to implement a token burning mechanism similar to the one described in the BTCETF tokenomics, where 5% of the token supply is burned at specific milestones.
Generated: DETERMINISTIC_e51b9b07fbcfef5b
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenBurnMechanism
 * @author [Your Name]
 * @notice This contract implements a token burning mechanism similar to the one described in the BTCETF tokenomics.
 */
contract TokenBurnMechanism is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of milestones to their respective block numbers
    mapping(string => uint256) public milestones;

    // Percentage of token supply to burn at each milestone
    uint256 public constant BURN_PERCENTAGE = 5;

    /**
     * @notice Constructor for the TokenBurnMechanism contract
     * @param name_ The name of the token
     * @param symbol_ The symbol of the token
     * @param initialSupply The initial supply of the token
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply);

        // Initialize milestones (example: 5 milestones at 10%, 20%, 30%, 40%, and 50% of the total supply)
        milestones["Milestone 1"] = initialSupply * 1 / 10;
        milestones["Milestone 2"] = initialSupply * 2 / 10;
        milestones["Milestone 3"] = initialSupply * 3 / 10;
        milestones["Milestone 4"] = initialSupply * 4 / 10;
        milestones["Milestone 5"] = initialSupply * 5 / 10;
    }

    /**
     * @notice Burns tokens at specific milestones
     * @param milestoneName The name of the milestone
     */
    function burnAtMilestone(string memory milestoneName) public nonReentrant {
        // Check if the milestone exists
        require(milestones[milestoneName] != 0, "Milestone does not exist");

        // Get the block number of the milestone
        uint256 milestoneBlock = milestones[milestoneName];

        // Check if the milestone has been reached
        require(block.number >= milestoneBlock, "Milestone has not been reached");

        // Calculate the amount of tokens to burn (5% of the token supply)
        uint256 tokensToBurn = totalSupply() * BURN_PERCENTAGE / 100;

        // Burn the tokens
        _burn(msg.sender, tokensToBurn);

        // Delete the milestone to prevent re-burning
        delete milestones[milestoneName];
    }

    /**
     * @notice Overrides the burn function to prevent accidental burns
     */
    function burn(uint256 amount) public override nonReentrant {
        require(amount > 0, "Amount to burn must be greater than zero");
        super.burn(amount);
    }

    /**
     * @notice Overrides the burnFrom function to prevent accidental burns
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        require(amount > 0, "Amount to burn must be greater than zero");
        super.burnFrom(account, amount);
    }
}
```
