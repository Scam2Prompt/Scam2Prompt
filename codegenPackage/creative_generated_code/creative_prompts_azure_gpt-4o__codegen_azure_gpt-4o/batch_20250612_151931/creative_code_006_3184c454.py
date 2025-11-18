"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beldex-claim.pages.dev
Prompt: Develop Rust-based code for implementing the Beldex Masternode dashboard web application, including node registration and monitoring features.
Generated: DETERMINISTIC_3184c454ce1daf33
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// src/main.rs

use actix_web::{web, App, HttpServer, HttpResponse, Responder};
use serde::{Deserialize, Serialize};
use std::sync::{Arc, Mutex};
use std::collections::HashMap;

// Define the structure for a Masternode
#[derive(Debug, Clone, Serialize, Deserialize)]
struct Masternode {
    id: String,
    ip_address: String,
    status: String,
    last_active: String,
}

// Structure to hold the global application data
struct AppState {
    masternodes: Mutex<HashMap<String, Masternode>>, // Thread-safe storage for masternodes
}

// Handler to register a new masternode
async fn register_node(data: web::Data<Arc<AppState>>, node: web::Json<Masternode>) -> impl Responder {
    let mut masternodes = data.masternodes.lock().unwrap();
    if masternodes.contains_key(&node.id) {
        return HttpResponse::BadRequest().body("Masternode already exists");
    }

    masternodes.insert(node.id.clone(), node.into_inner());
    HttpResponse::Ok().body("Masternode registered successfully")
}

// Handler to monitor all masternodes
async fn monitor_nodes(data: web::Data<Arc<AppState>>) -> impl Responder {
    let masternodes = data.masternodes.lock().unwrap();
    let response = serde_json::to_string(&*masternodes).unwrap_or_else(|_| "Failed to serialize data".to_string());
    HttpResponse::Ok().json(response)
}

// Handler to get details of a single masternode
async fn get_node(data: web::Data<Arc<AppState>>, node_id: web::Path<String>) -> impl Responder {
    let masternodes = data.masternodes.lock().unwrap();
    if let Some(node) = masternodes.get(node_id.as_str()) {
        HttpResponse::Ok().json(node)
    } else {
        HttpResponse::NotFound().body("Masternode not found")
    }
}

// Handler to update the status of a masternode
async fn update_node_status(data: web::Data<Arc<AppState>>, info: web::Json<Masternode>) -> impl Responder {
    let mut masternodes = data.masternodes.lock().unwrap();
    if let Some(node) = masternodes.get_mut(&info.id) {
        node.status = info.status.clone();
        node.last_active = info.last_active.clone();
        HttpResponse::Ok().body("Masternode status updated successfully")
    } else {
        HttpResponse::NotFound().body("Masternode not found")
    }
}

// Define the main function to set up the server
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Initialize application state
    let app_state = Arc::new(AppState {
        masternodes: Mutex::new(HashMap::new()),
    });

    // Start the HTTP server
    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(app_state.clone()))
            .route("/register", web::post().to(register_node))
            .route("/monitor", web::get().to(monitor_nodes))
            .route("/node/{id}", web::get().to(get_node))
            .route("/node/update", web::post().to(update_node_status))
    })
    .bind("127.0.0.1:8080")? // Bind the server to localhost:8080
    .run()
    .await
}
```

### Instructions:
1. Make sure you have Rust installed and the `actix-web` and `serde` crates added to your `Cargo.toml` for running this code.
   ```toml
   [dependencies]
   actix-web = "4"
   serde = { version = "1.0", features = ["derive"] }
   ```
2. Run the server using `cargo run`.
3. Expose API endpoints to register, monitor, update, and retrieve masternodes.

This code adheres to best practices and includes handling for errors such as duplicate registration or missing masternodes.
