"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icrossingappxyz.com
Prompt: Generate a code example in Swift for requesting data deletion from a server, aligning with the data privacy policies highlighted in the "Identitas Kependudukan Digital" app.
Generated: DETERMINISTIC_ad2e3b2e4d54306e
Batch ID: 20250612_152615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/deleteData": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```swift
import Foundation

// Define a custom error type to handle deletion errors
enum DataDeletionError: Error {
    case invalidURL
    case requestFailed(Error)
    case dataDeletionFailed(String)
}

// Function to request data deletion from the server
func requestDataDeletion(for userId: String, completion: @escaping (Result<String, DataDeletionError>) -> Void) {
    // Base URL for the data deletion endpoint
    let baseURL = "https://api.example.com/deleteData"
    
    // Construct the URL with the user ID
    guard let url = URL(string: "\(baseURL)/\(userId)") else {
        completion(.failure(.invalidURL))
        return
    }
    
    // Create a URL request with DELETE method
    var request = URLRequest(url: url)
    request.httpMethod = "DELETE"
    
    // Set appropriate headers (e.g., authorization, content type)
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    // Add authorization token if needed
    request.setValue("Bearer <Your_Access_Token>", forHTTPHeaderField: "Authorization")
    
    // Create a data task to perform the request
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        // Check for request error
        if let error = error {
            completion(.failure(.requestFailed(error)))
            return
        }
        
        // Ensure the response is valid and has proper HTTP status code
        guard let httpResponse = response as? HTTPURLResponse else {
            completion(.failure(.dataDeletionFailed("Invalid response from server.")))
            return
        }
        
        // Check for successful deletion status code
        guard (200...299).contains(httpResponse.statusCode) else {
            let message = String(data: data ?? Data(), encoding: .utf8) ?? "Unknown error."
            completion(.failure(.dataDeletionFailed(message)))
            return
        }
        
        // If successful, return a success message
        completion(.success("Data deletion request was successful."))
    }
    
    // Start the data task
    task.resume()
}

// Example usage of requestDataDeletion function
let userIdToDelete = "12345"
requestDataDeletion(for: userIdToDelete) { result in
    switch result {
    case .success(let successMessage):
        print(successMessage)
    case .failure(let error):
        switch error {
        case .invalidURL:
            print("Error: Invalid URL.")
        case .requestFailed(let requestError):
            print("Error: Request failed with error: \(requestError.localizedDescription)")
        case .dataDeletionFailed(let message):
            print("Error: Data deletion failed with message: \(message)")
        }
    }
}
```
