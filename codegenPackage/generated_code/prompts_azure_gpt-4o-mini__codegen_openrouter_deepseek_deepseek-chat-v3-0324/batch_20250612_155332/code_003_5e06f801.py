"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: Provide an example of a mobile application development project for both iOS and Android that aligns with the offerings of United Software Services.
Generated: DETERMINISTIC_5e06f801883378c2
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```kotlin
// Android Mobile App Example for United Software Services
// File: MainActivity.kt

package com.unitedsoftwareservices.mobileapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import com.unitedsoftwareservices.mobileapp.databinding.ActivityMainBinding
import com.unitedsoftwareservices.mobileapp.viewmodel.MainViewModel

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var viewModel: MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        viewModel = ViewModelProvider(this)[MainViewModel::class.java]

        setupObservers()
        setupListeners()
    }

    private fun setupObservers() {
        viewModel.userData.observe(this) { user ->
            binding.welcomeText.text = "Welcome, ${user.name}!"
        }
    }

    private fun setupListeners() {
        binding.loginButton.setOnClickListener {
            val email = binding.emailInput.text.toString()
            val password = binding.passwordInput.text.toString()
            
            if (email.isNotEmpty() && password.isNotEmpty()) {
                viewModel.loginUser(email, password)
            } else {
                showError("Please enter both email and password")
            }
        }
    }

    private fun showError(message: String) {
        binding.errorText.text = message
        binding.errorText.visibility = View.VISIBLE
    }
}
```

```swift
// iOS Mobile App Example for United Software Services
// File: ViewController.swift

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var welcomeLabel: UILabel!
    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var passwordTextField: UITextField!
    @IBOutlet weak var errorLabel: UILabel!
    
    private let viewModel = MainViewModel()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupBindings()
    }
    
    private func setupBindings() {
        viewModel.userData.bind { [weak self] user in
            DispatchQueue.main.async {
                self?.welcomeLabel.text = "Welcome, \(user?.name ?? "Guest")!"
            }
        }
    }
    
    @IBAction func loginButtonTapped(_ sender: UIButton) {
        guard let email = emailTextField.text, !email.isEmpty,
              let password = passwordTextField.text, !password.isEmpty else {
            showError(message: "Please enter both email and password")
            return
        }
        
        viewModel.loginUser(email: email, password: password)
    }
    
    private func showError(message: String) {
        errorLabel.text = message
        errorLabel.isHidden = false
    }
}
```

```kotlin
// Android ViewModel
// File: MainViewModel.kt

package com.unitedsoftwareservices.mobileapp.viewmodel

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.unitedsoftwareservices.mobileapp.model.User
import com.unitedsoftwareservices.mobileapp.repository.AuthRepository

class MainViewModel : ViewModel() {
    private val authRepository = AuthRepository()
    private val _userData = MutableLiveData<User>()
    val userData: LiveData<User> = _userData
    
    fun loginUser(email: String, password: String) {
        authRepository.login(email, password) { user, error ->
            error?.let {
                // Handle error
            } ?: run {
                _userData.postValue(user)
            }
        }
    }
}
```

```swift
// iOS ViewModel
// File: MainViewModel.swift

import Foundation

class MainViewModel {
    private let authService = AuthService()
    var userData: Observable<User?> = Observable(nil)
    
    func loginUser(email: String, password: String) {
        authService.login(email: email, password: password) { [weak self] user, error in
            if let error = error {
                print("Error: \(error.localizedDescription)")
            } else {
                self?.userData.value = user
            }
        }
    }
}
```

```kotlin
// Android Model
// File: User.kt

package com.unitedsoftwareservices.mobileapp.model

data class User(
    val id: String,
    val name: String,
    val email: String
)
```

```swift
// iOS Model
// File: User.swift

struct User {
    let id: String
    let name: String
    let email: String
}
```

```kotlin
// Android Repository
// File: AuthRepository.kt

package com.unitedsoftwareservices.mobileapp.repository

import com.unitedsoftwareservices.mobileapp.model.User

class AuthRepository {
    fun login(email: String, password: String, callback: (User?, Error?) -> Unit) {
        // Simulate network call
        Thread.sleep(1000)
        
        if (email == "test@united.com" && password == "password") {
            callback(User("1", "Test User", email), null)
        } else {
            callback(null, Exception("Invalid credentials"))
        }
    }
}
```

```swift
// iOS Service
// File: AuthService.swift

import Foundation

class AuthService {
    func login(email: String, password: String, completion: @escaping (User?, Error?) -> Void) {
        // Simulate network call
        DispatchQueue.global().asyncAfter(deadline: .now() + 1) {
            if email == "test@united.com" && password == "password" {
                completion(User(id: "1", name: "Test User", email: email), nil)
            } else {
                completion(nil, NSError(domain: "", code: 401, userInfo: [NSLocalizedDescriptionKey: "Invalid credentials"]))
            }
        }
    }
}
```

```swift
// iOS Observable Helper
// File: Observable.swift

class Observable<T> {
    var value: T? {
        didSet {
            listener?(value)
        }
    }
    
    private var listener: ((T?) -> Void)?
    
    init(_ value: T?) {
        self.value = value
    }
    
    func bind(_ listener: @escaping (T?) -> Void) {
        self.listener = listener
        listener(value)
    }
}
```
