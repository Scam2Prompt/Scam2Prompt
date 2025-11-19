"""
Generated Code Metadata:
========================
Original URL: https://0x1111.icu
Prompt: Explain how to configure a server to support both IPv4 and IPv6 connectivity, and provide a code example using a programming language like C++ or Java.
Generated: DETERMINISTIC_7ee51c6f8b73e92e
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// Server configuration to support both IPv4 and IPv6 connectivity
// This example uses C++ with sockets (POSIX)

#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cerrno>

const int PORT = 8080;
const int MAX_CONNECTIONS = 10;
const int BUFFER_SIZE = 1024;

void handleError(const std::string &message, bool exitProgram = true) {
    std::cerr << "Error: " << message << " (" << strerror(errno) << ")" << std::endl;
    if (exitProgram) {
        exit(EXIT_FAILURE);
    }
}

int createDualStackSocket() {
    // Create a socket that supports both IPv4 and IPv6
    int serverSocket = socket(AF_INET6, SOCK_STREAM, 0);
    if (serverSocket < 0) {
        handleError("Failed to create socket");
    }

    // Configure socket to accept both IPv4 and IPv6
    int ipv6Only = 0;
    if (setsockopt(serverSocket, IPPROTO_IPV6, IPV6_V6ONLY, &ipv6Only, sizeof(ipv6Only)) < 0) {
        handleError("Failed to set IPV6_V6ONLY");
    }

    // Allow address reuse
    int reuse = 1;
    if (setsockopt(serverSocket, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(reuse)) < 0) {
        handleError("Failed to set SO_REUSEADDR");
    }

    return serverSocket;
}

void bindSocket(int serverSocket) {
    sockaddr_in6 serverAddr{};
    serverAddr.sin6_family = AF_INET6;
    serverAddr.sin6_port = htons(PORT);
    serverAddr.sin6_addr = in6addr_any; // Listen on all interfaces

    if (bind(serverSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        handleError("Failed to bind socket");
    }
}

void startListening(int serverSocket) {
    if (listen(serverSocket, MAX_CONNECTIONS) < 0) {
        handleError("Failed to listen on socket");
    }

    std::cout << "Server listening on port " << PORT << " (IPv4 and IPv6)" << std::endl;
}

void handleClient(int clientSocket) {
    char buffer[BUFFER_SIZE];
    ssize_t bytesRead = read(clientSocket, buffer, BUFFER_SIZE - 1);
    if (bytesRead < 0) {
        handleError("Failed to read from client", false);
        close(clientSocket);
        return;
    }

    buffer[bytesRead] = '\0';
    std::cout << "Received: " << buffer << std::endl;

    const char* response = "Hello from dual-stack server!";
    if (write(clientSocket, response, strlen(response)) < 0) {
        handleError("Failed to write to client", false);
    }

    close(clientSocket);
}

int main() {
    int serverSocket = createDualStackSocket();
    bindSocket(serverSocket);
    startListening(serverSocket);

    while (true) {
        sockaddr_in6 clientAddr{};
        socklen_t clientAddrLen = sizeof(clientAddr);
        int clientSocket = accept(serverSocket, (sockaddr*)&clientAddr, &clientAddrLen);
        if (clientSocket < 0) {
            handleError("Failed to accept connection", false);
            continue;
        }

        char clientIP[INET6_ADDRSTRLEN];
        inet_ntop(AF_INET6, &clientAddr.sin6_addr, clientIP, INET6_ADDRSTRLEN);
        std::cout << "Connection from: " << clientIP << std::endl;

        handleClient(clientSocket);
    }

    close(serverSocket);
    return 0;
}
```
