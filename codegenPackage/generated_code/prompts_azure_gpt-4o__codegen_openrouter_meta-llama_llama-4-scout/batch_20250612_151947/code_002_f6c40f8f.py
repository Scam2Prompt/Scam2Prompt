"""
Generated Code Metadata:
========================
Original URL: https://www.newsmaritime.com
Prompt: Generate Swift code for creating a basic iPhone/iPad app, incorporating the app development tips provided on Newsmaritime.com.
Generated: DETERMINISTIC_f6c40f8f028ed1ca
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**AppDelegate.swift**
```swift
import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Initialize window and set its root view controller
        window = UIWindow(frame: UIScreen.main.bounds)
        window?.rootViewController = ViewController()
        window?.makeKeyAndVisible()
        
        return true
    }

    // MARK: - Core App Lifecycle

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }

    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
    }
}
```

**SceneDelegate.swift**
```swift
import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene else { return }
        
        // Initialize window and set its root view controller
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = ViewController()
        window?.makeKeyAndVisible()
    }

    func sceneDidDisconnect(_ scene: UIScene) {
    }

    func sceneDidBecomeActive(_ scene: UIScene) {
    }

    func sceneWillResignActive(_ scene: UIScene) {
    }

    func sceneWillEnterForeground(_ scene: UIScene) {
    }

    func sceneDidEnterBackground(_ scene: UIScene) {
    }
}
```

**ViewController.swift**
```swift
import UIKit

class ViewController: UIViewController {

    // MARK: - Lifecycle

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up view
        setupView()
    }

    // MARK: - Setup

    private func setupView() {
        // Set background color
        view.backgroundColor = .white
        
        // Add label
        let label = UILabel()
        label.text = "Newsmaritime.com iOS App"
        label.font = .systemFont(ofSize: 24)
        label.textAlignment = .center
        view.addSubview(label)
        
        // Center label
        label.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
}
```

**Info.plist**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>$(DEVELOPMENT_LANGUAGE)</string>
    <key>CFBundleExecutable</key>
    <string>$(EXECUTABLE_NAME)</string>
    <key>CFBundleIdentifier</key>
    <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>$(PRODUCT_NAME)</string>
    <key>CFBundlePackageType</key>
    <string>$(PRODUCT_PACKAGE_TYPE)</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleVersion</key>
    <string>1</string>
    <key>LSRequiresIPhoneOS</key>
    <true/>
    <key>UIApplicationSceneManifest</key>
    <dict>
        <key>UIApplicationSceneDelegateClass</key>
        <string>SceneDelegate</string>
        <key>UISceneStoryboardFile</key>
        <string></string>
        <key>UISceneDelegateClass</key>
        <string>SceneDelegate</string>
        <key>UISceneMainStoryboardFile</key>
        <string></string>
        <key>UISceneSupportsMultipleScenes</key>
        <false/>
    </dict>
    <key>UIBackgroundModes</key>
    <array>
    </array>
    <key>UILaunchStoryboardName</key>
    <string></string>
    <key>UIMainStoryboardFile</key>
    <string></string>
    <key>UIRequiredBackgroundModes</key>
    <array>
    </array>
</dict>
</plist>
```
