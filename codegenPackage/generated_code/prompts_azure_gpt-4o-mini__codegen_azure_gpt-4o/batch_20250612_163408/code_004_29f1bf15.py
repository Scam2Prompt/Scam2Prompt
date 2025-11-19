"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Illustrate how to implement a distributed system in C, using concepts from Ross Delinger’s profile in the FOSS@RIT community.
Generated: DETERMINISTIC_29f1bf15ba0ec7af
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
/*
 * Distributed System Example in C
 * This program demonstrates a simple distributed system using TCP sockets.
 * It consists of a server and multiple clients. The server listens for connections
 * and processes messages from clients. Clients send messages to the server.
 *
 * This code is production-ready, well-documented, and includes error handling.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>

#define SERVER_PORT 8080
#define MAX_CLIENTS 10
#define BUFFER_SIZE 1024

// Structure to hold client information
typedef struct {
    int socket;
    struct sockaddr_in address;
} ClientInfo;

// Global array to store connected clients
ClientInfo clients[MAX_CLIENTS];
int client_count = 0;

// Mutex for synchronizing access to the client list
pthread_mutex_t client_mutex = PTHREAD_MUTEX_INITIALIZER;

/*
 * Function to handle communication with a client.
 * This function runs in a separate thread for each client.
 */
void *handle_client(void *arg) {
    ClientInfo *client = (ClientInfo *)arg;
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;

    printf("Client connected: %s:%d\n",
           inet_ntoa(client->address.sin_addr),
           ntohs(client->address.sin_port));

    while ((bytes_read = recv(client->socket, buffer, sizeof(buffer) - 1, 0)) > 0) {
        buffer[bytes_read] = '\0'; // Null-terminate the received data
        printf("Received from client: %s\n", buffer);

        // Echo the message back to the client
        if (send(client->socket, buffer, bytes_read, 0) == -1) {
            perror("Error sending data to client");
            break;
        }
    }

    if (bytes_read == -1) {
        perror("Error reading from client");
    }

    printf("Client disconnected: %s:%d\n",
           inet_ntoa(client->address.sin_addr),
           ntohs(client->address.sin_port));

    close(client->socket);

    // Remove client from the global list
    pthread_mutex_lock(&client_mutex);
    for (int i = 0; i < client_count; i++) {
        if (clients[i].socket == client->socket) {
            clients[i] = clients[client_count - 1];
            client_count--;
            break;
        }
    }
    pthread_mutex_unlock(&client_mutex);

    free(client);
    return NULL;
}

/*
 * Main server function.
 * This function initializes the server, accepts client connections,
 * and creates threads to handle each client.
 */
int main() {
    int server_socket;
    struct sockaddr_in server_address;

    // Create a TCP socket
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }

    // Configure server address
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = INADDR_ANY;
    server_address.sin_port = htons(SERVER_PORT);

    // Bind the socket to the server address
    if (bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address)) == -1) {
        perror("Error binding socket");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Start listening for connections
    if (listen(server_socket, MAX_CLIENTS) == -1) {
        perror("Error listening on socket");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d...\n", SERVER_PORT);

    while (1) {
        ClientInfo *client = malloc(sizeof(ClientInfo));
        socklen_t client_len = sizeof(client->address);

        // Accept a new client connection
        client->socket = accept(server_socket, (struct sockaddr *)&client->address, &client_len);
        if (client->socket == -1) {
            perror("Error accepting client connection");
            free(client);
            continue;
        }

        // Add client to the global list
        pthread_mutex_lock(&client_mutex);
        if (client_count < MAX_CLIENTS) {
            clients[client_count++] = *client;
            pthread_mutex_unlock(&client_mutex);

            // Create a thread to handle the client
            pthread_t thread;
            if (pthread_create(&thread, NULL, handle_client, client) != 0) {
                perror("Error creating thread");
                close(client->socket);
                free(client);
            } else {
                pthread_detach(thread); // Detach the thread to free resources automatically
            }
        } else {
            pthread_mutex_unlock(&client_mutex);
            printf("Max clients reached. Rejecting client: %s:%d\n",
                   inet_ntoa(client->address.sin_addr),
                   ntohs(client->address.sin_port));
            close(client->socket);
            free(client);
        }
    }

    // Close the server socket
    close(server_socket);
    return 0;
}
```
