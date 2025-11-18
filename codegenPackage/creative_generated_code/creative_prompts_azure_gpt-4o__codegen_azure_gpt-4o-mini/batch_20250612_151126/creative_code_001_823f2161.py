"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-core.com
Prompt: Generate code to validate a Bip39 recovery phrase for a wallet using the Wallet-Core library.
Generated: DETERMINISTIC_823f21612e175508
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```swift
import Foundation
import WalletCore

/// Validates a BIP39 recovery phrase for a cryptocurrency wallet.
/// - Parameter recoveryPhrase: The BIP39 recovery phrase to validate.
/// - Returns: A boolean indicating whether the recovery phrase is valid.
func validateRecoveryPhrase(recoveryPhrase: String) -> Bool {
    // Split the recovery phrase into individual words
    let words = recoveryPhrase.split(separator: " ").map(String.init)
    
    // Check if the number of words is valid (12, 15, 18, 21, or 24)
    guard [12, 15, 18, 21, 24].contains(words.count) else {
        print("Invalid number of words in recovery phrase. Must be one of: 12, 15, 18, 21, 24.")
        return false
    }

    // Create a BIP39 instance to validate the phrase
    let bip39 = Bip39()

    // Validate the recovery phrase
    do {
        // This method will throw an error if the phrase is invalid
        let isValid = try bip39.isValid(mnemonic: recoveryPhrase, language: .english)
        return isValid
    } catch {
        // Handle any errors that occur during validation
        print("Error validating recovery phrase: \(error.localizedDescription)")
        return false
    }
}

// Example usage
let recoveryPhrase = "pistol laugh lumber suitcase neon play lend sleep tumble panda marble goat"
let isRecoveryPhraseValid = validateRecoveryPhrase(recoveryPhrase: recoveryPhrase)

if isRecoveryPhraseValid {
    print("The recovery phrase is valid.")
} else {
    print("The recovery phrase is invalid.")
}
```
