"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: Develop a Tari mining dashboard using Rust to visualize mining performance, token rewards, and network security metrics.
Generated: DETERMINISTIC_d10d723bd7e2ef45
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use actix_web::{web, App, HttpServer, HttpResponse, Responder};
use serde::{Serialize, Deserialize};
use std::sync::Mutex;

// Define a struct to hold mining performance data
#[derive(Serialize, Deserialize)]
struct MiningPerformance {
    hash_rate: f64, // Hash rate in H/s
    token_rewards: f64, // Token rewards earned
    network_security: f64, // Network security metric
}

// Create a shared state to hold the mining performance data
struct AppState {
    performance: Mutex<MiningPerformance>,
}

// Function to get mining performance data
async fn get_performance(data: web::Data<AppState>) -> impl Responder {
    let performance = data.performance.lock().unwrap();
    HttpResponse::Ok().json(&*performance)
}

// Function to update mining performance data
async fn update_performance(data: web::Data<AppState>, performance: web::Json<MiningPerformance>) -> impl Responder {
    let mut state = data.performance.lock().unwrap();
    *state = performance.into_inner();
    HttpResponse::Ok().json(&*state)
}

// Main function to start the server
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Initialize the mining performance data
    let initial_performance = MiningPerformance {
        hash_rate: 0.0,
        token_rewards: 0.0,
        network_security: 0.0,
    };

    // Create shared application state
    let app_state = web::Data::new(AppState {
        performance: Mutex::new(initial_performance),
    });

    // Start the HTTP server
    HttpServer::new(move || {
        App::new()
            .app_data(app_state.clone())
            .route("/performance", web::get().to(get_performance)) // Route to get performance data
            .route("/performance", web::post().to(update_performance)) // Route to update performance data
    })
    .bind("127.0.0.1:8080")? // Bind to localhost on port 8080
    .run()
    .await
}
```
