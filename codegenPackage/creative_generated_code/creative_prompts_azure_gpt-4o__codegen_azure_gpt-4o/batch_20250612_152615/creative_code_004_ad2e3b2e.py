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
  "https://your-server-url.com": {
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

// MARK: - DataDeletionRequestError Enum
/// Custom error enum for handling data deletion errors
enum DataDeletionRequestError: Error {
    case invalidURL
    case requestFailed(String)
    case responseError(String)
    case unknownError
}

// MARK: - DataDeletionService Class
/// Service class for handling data deletion requests
class DataDeletionService {
    
    // MARK: - Properties
    private let serverURL: String
    
    /// Initializes the service with the server's base URL
    /// - Parameter serverURL: The base URL of the server
    init(serverURL: String) {
        self.serverURL = serverURL
    }
    
    // MARK: - Public Methods
    /// Requests data deletion from the server
    /// - Parameters:
    ///   - userId: The ID of the user making the deletion request
    ///   - completion: Completion handler returning success or error
    func requestDataDeletion(for userId: String, completion: @escaping (Result<String, DataDeletionRequestError>) -> Void) {
        // Validate the URL
        guard let url = URL(string: "\(serverURL)/deleteData") else {
            completion(.failure(.invalidURL))
            return
        }
        
        // Prepare HTTP request
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // Create JSON payload
        let payload: [String: String] = ["userId": userId]
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: payload, options: [])
        } catch {
            completion(.failure(.requestFailed("Failed to serialize JSON payload.")))
            return
        }
        
        // Execute HTTP request
        let session = URLSession.shared
        let task = session.dataTask(with: request) { data, response, error in
            
            // Handle network error
            if let error = error {
                completion(.failure(.requestFailed(error.localizedDescription)))
                return
            }
            
            // Validate server response
            guard let httpResponse = response as? HTTPURLResponse else {
                completion(.failure(.unknownError))
                return
            }
            
            // Check HTTP status code
            guard (200...299).contains(httpResponse.statusCode) else {
                let errorMessage = HTTPURLResponse.localizedString(forStatusCode: httpResponse.statusCode)
                completion(.failure(.responseError(errorMessage)))
                return
            }
            
            // Parse response data
            if let data = data, let responseString = String(data: data, encoding: .utf8) {
                completion(.success(responseString))
            } else {
                completion(.failure(.unknownError))
            }
        }
        
        task.resume()
    }
}

// MARK: - Usage Example
/// Replace "https://your-server-url.com" with your actual server URL
let dataDeletionService = DataDeletionService(serverURL: "https://your-server-url.com")

/// Replace "12345" with the actual user ID you want to delete data for
dataDeletionService.requestDataDeletion(for: "12345") { result in
    switch result {
    case .success(let response):
        print("Data deletion successful: \(response)")
    case .failure(let error):
        print("Data deletion failed: \(error)")
    }
}
```
