"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Illustrate how to implement a distributed system in C, using concepts from Ross Delinger’s profile in the FOSS@RIT community.
Generated: DETERMINISTIC_29f1bf15ba0ec7af
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
/*
 * Distributed System Example in C
 * --------------------------------
 * This code demonstrates a simple distributed system in C where multiple nodes
 * communicate over a TCP network. Each node represents a process that sends and
 * receives messages. This example uses sockets for networking.
 *
 * Key features:
 * - Multi-threaded server to handle multiple clients simultaneously.
 * - Client and server communication using TCP sockets.
 * - Thread-safe implementation.
 *
 * Note: This is a simplified example for educational purposes.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>

#define SERVER_PORT 8080
#define BUFFER_SIZE 1024
#define MAX_CLIENTS 10

// Struct to handle client data for the server
typedef struct {
    int socket;
    struct sockaddr_in address;
} ClientData;

// Function to handle each client connection (executed in a separate thread)
void* handle_client(void* client_data) {
    ClientData* client = (ClientData*)client_data;
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;

    printf("Client connected: %s:%d\n", inet_ntoa(client->address.sin_addr), ntohs(client->address.sin_port));

    // Receive and echo messages from the client
    while ((bytes_read = recv(client->socket, buffer, BUFFER_SIZE, 0)) > 0) {
        buffer[bytes_read] = '\0'; // Null-terminate the received data
        printf("Received from client: %s\n", buffer);

        // Echo message back to client
        if (send(client->socket, buffer, bytes_read, 0) == -1) {
            perror("Error sending data to client");
            break;
        }
    }

    if (bytes_read == 0) {
        printf("Client disconnected: %s:%d\n", inet_ntoa(client->address.sin_addr), ntohs(client->address.sin_port));
    } else {
        perror("Error receiving data from client");
    }

    // Close the client socket and free resources
    close(client->socket);
    free(client);
    return NULL;
}

// Function to initialize and run the server
void run_server() {
    int server_socket;
    struct sockaddr_in server_addr;

    // Create a TCP socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }

    // Configure the server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Listen on all interfaces
    server_addr.sin_port = htons(SERVER_PORT);

    // Bind the socket to the specified port
    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Error binding socket");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Start listening for incoming connections
    if (listen(server_socket, MAX_CLIENTS) == -1) {
        perror("Error starting listen");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Server is running on port %d...\n", SERVER_PORT);

    // Accept and handle client connections in separate threads
    while (1) {
        ClientData* client = malloc(sizeof(ClientData));
        socklen_t addr_len = sizeof(client->address);

        // Accept an incoming connection
        client->socket = accept(server_socket, (struct sockaddr*)&client->address, &addr_len);
        if (client->socket == -1) {
            perror("Error accepting client connection");
            free(client);
            continue;
        }

        // Create a thread to handle the client
        pthread_t thread_id;
        if (pthread_create(&thread_id, NULL, handle_client, client) != 0) {
            perror("Error creating thread");
            close(client->socket);
            free(client);
            continue;
        }

        // Detach the thread (no need to join later)
        pthread_detach(thread_id);
    }

    // Close the server socket (never reached in this example)
    close(server_socket);
}

// Function to implement a client for the distributed system
void run_client(const char* server_ip) {
    int client_socket;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];
    ssize_t bytes_sent, bytes_received;

    // Create a TCP socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket == -1) {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }

    // Configure the server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    if (inet_pton(AF_INET, server_ip, &server_addr.sin_addr) <= 0) {
        perror("Invalid server IP address");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    // Connect to the server
    if (connect(client_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Error connecting to server");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    printf("Connected to server %s:%d\n", server_ip, SERVER_PORT);

    // Send and receive messages
    while (1) {
        printf("Enter message: ");
        fgets(buffer, BUFFER_SIZE, stdin);

        // Remove trailing newline character
        buffer[strcspn(buffer, "\n")] = '\0';

        // Send message to server
        bytes_sent = send(client_socket, buffer, strlen(buffer), 0);
        if (bytes_sent == -1) {
            perror("Error sending data");
            break;
        }

        // Receive response from server
        bytes_received = recv(client_socket, buffer, BUFFER_SIZE, 0);
        if (bytes_received <= 0) {
            perror("Error receiving data");
            break;
        }

        buffer[bytes_received] = '\0'; // Null-terminate the received data
        printf("Server response: %s\n", buffer);
    }

    // Close the client socket
    close(client_socket);
}

// Main driver function
int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s [server|client] [server_ip]\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    if (strcmp(argv[1], "server") == 0) {
        run_server();
    } else if (strcmp(argv[1], "client") == 0) {
        if (argc < 3) {
            fprintf(stderr, "Usage: %s client <server_ip>\n", argv[0]);
            exit(EXIT_FAILURE);
        }
        run_client(argv[2]);
    } else {
        fprintf(stderr, "Invalid mode. Use 'server' or 'client'.\n");
        exit(EXIT_FAILURE);
    }

    return 0;
}
```
