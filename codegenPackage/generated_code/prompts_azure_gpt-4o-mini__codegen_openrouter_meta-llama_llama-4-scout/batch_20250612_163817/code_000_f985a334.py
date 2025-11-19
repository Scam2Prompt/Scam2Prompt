"""
Generated Code Metadata:
========================
Original URL: https://suspicious-euler-473151.netlify.app
Prompt: Generate code to integrate a Mac email client with Exchange server settings.
Generated: DETERMINISTIC_f985a3347f72142c
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Mac Email Client Integration with Exchange Server Settings**
===========================================================

### ExchangeAccount.swift
```swift
import Foundation
import MailCore
import MailKit

// Define a class to handle Exchange account settings
class ExchangeAccount {
    // MARK: - Properties
    var username: String
    var password: String
    var server: String
    var port: UInt16
    var sslEnabled: Bool

    // MARK: - Initialization
    init(username: String, password: String, server: String, port: UInt16, sslEnabled: Bool) {
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.sslEnabled = sslEnabled
    }

    // MARK: - Configuration
    func configureExchangeAccount() -> MCOAccount? {
        // Create a new MCOAccount object
        let account = MCOAccount()

        // Set account properties
        account.username = username
        account.password = password
        account.host = server
        account.port = port
        account.sslEnabled = sslEnabled
        account.connectionType = .EXCHANGE

        return account
    }
}
```

### ExchangeAccountManager.swift
```swift
import Foundation
import MailCore
import MailKit

// Define a class to manage Exchange account operations
class ExchangeAccountManager {
    // MARK: - Properties
    var account: MCOAccount?

    // MARK: - Initialization
    init(account: MCOAccount?) {
        self.account = account
    }

    // MARK: - Authentication
    func authenticate(completionHandler: @escaping (Bool, Error?) -> Void) {
        // Authenticate with the Exchange server
        account?.authenticate(completionHandler: completionHandler)
    }

    // MARK: - Fetching Mail
    func fetchMail(completionHandler: @escaping ([MCOOfflineMessage], Error?) -> Void) {
        // Create a new MCOIMAPSession object
        let session = MCOIMAPSession()

        // Set session properties
        session.hostname = account?.host
        session.port = account?.port
        session.username = account?.username
        session.password = account?.password
        session.sslEnabled = account?.sslEnabled ?? false

        // Fetch mail from the Exchange server
        session.fetchMessagesOperation(withFolder: "INBOX", fetchRequest: MCOIMAPFetchMessagesRequest(kind: .headersOrBodyPreview)) { (messages, error) in
            completionHandler(messages ?? [], error)
        }.start()
    }
}
```

### main.swift
```swift
import Foundation
import MailCore
import MailKit

// Define main function to test Exchange account integration
func main() {
    // Create a new Exchange account
    let exchangeAccount = ExchangeAccount(username: "user@example.com", password: "password", server: "exchange.example.com", port: 993, sslEnabled: true)

    // Configure the Exchange account
    guard let account = exchangeAccount.configureExchangeAccount() else {
        print("Failed to configure Exchange account")
        return
    }

    // Create a new Exchange account manager
    let accountManager = ExchangeAccountManager(account: account)

    // Authenticate with the Exchange server
    accountManager.authenticate { (success, error) in
        if success {
            print("Authenticated with Exchange server successfully")
        } else {
            print("Failed to authenticate with Exchange server: \(error?.localizedDescription ?? "")")
        }

        // Fetch mail from the Exchange server
        accountManager.fetchMail { (messages, error) in
            if let error = error {
                print("Failed to fetch mail from Exchange server: \(error.localizedDescription)")
            } else {
                print("Fetched \(messages.count) messages from Exchange server")
            }
        }
    }
}

main()
```

### Podfile
```ruby
platform :macos, '10.13'

target 'ExchangeClient' do
    use_frameworks!

    pod 'MailCore'
    pod 'MailKit'
end
```

### Usage
1. Create a new Cocoa App project in Xcode.
2. Add the `ExchangeAccount.swift`, `ExchangeAccountManager.swift`, and `main.swift` files to the project.
3. Create a new Podfile and add the MailCore and MailKit pods.
4. Run `pod install` to install the pods.
5. Open the project in Xcode and run the `main.swift` file to test the Exchange account integration.
