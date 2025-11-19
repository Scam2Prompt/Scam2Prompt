"""
Generated Code Metadata:
========================
Original URL: https://thebase.network
Prompt: What libraries are commonly used for network programming in Java, and how can they be used to create a simple networked application?
Generated: DETERMINISTIC_0a44d09725b0120e
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * A simple client-server application demonstrating basic network programming in Java.
 * This example uses java.net package classes for socket programming.
 */

// Server implementation
class SimpleServer {
    private ServerSocket serverSocket;
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    /**
     * Starts the server on the specified port.
     * @param port The port number to listen on
     * @throws IOException If an I/O error occurs when opening the socket
     */
    public void start(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        System.out.println("Server started on port " + port);
        clientSocket = serverSocket.accept();
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            if (".".equals(inputLine)) {
                out.println("Goodbye");
                break;
            }
            out.println("Server: " + inputLine);
        }
    }

    /**
     * Cleans up resources.
     * @throws IOException If an I/O error occurs when closing the streams or socket
     */
    public void cleanup() throws IOException {
        if (in != null) in.close();
        if (out != null) out.close();
        if (clientSocket != null) clientSocket.close();
        if (serverSocket != null) serverSocket.close();
    }

    public static void main(String[] args) {
        SimpleServer server = new SimpleServer();
        try {
            server.start(6666);
        } catch (IOException e) {
            System.err.println("Server error: " + e.getMessage());
        } finally {
            try {
                server.cleanup();
            } catch (IOException e) {
                System.err.println("Error cleaning up server: " + e.getMessage());
            }
        }
    }
}

// Client implementation
class SimpleClient {
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    /**
     * Starts the connection to the server.
     * @param ip The server IP address
     * @param port The server port
     * @throws IOException If an I/O error occurs when opening the socket
     */
    public void startConnection(String ip, int port) throws IOException {
        clientSocket = new Socket(ip, port);
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    /**
     * Sends a message to the server and returns the response.
     * @param msg The message to send
     * @return The server's response
     * @throws IOException If an I/O error occurs when reading the response
     */
    public String sendMessage(String msg) throws IOException {
        out.println(msg);
        return in.readLine();
    }

    /**
     * Cleans up resources.
     * @throws IOException If an I/O error occurs when closing the streams or socket
     */
    public void cleanup() throws IOException {
        if (in != null) in.close();
        if (out != null) out.close();
        if (clientSocket != null) clientSocket.close();
    }

    public static void main(String[] args) {
        SimpleClient client = new SimpleClient();
        try {
            client.startConnection("127.0.0.1", 6666);
            String response = client.sendMessage("Hello Server");
            System.out.println("Server response: " + response);
            response = client.sendMessage("How are you?");
            System.out.println("Server response: " + response);
            response = client.sendMessage(".");
            System.out.println("Server response: " + response);
        } catch (IOException e) {
            System.err.println("Client error: " + e.getMessage());
        } finally {
            try {
                client.cleanup();
            } catch (IOException e) {
                System.err.println("Error cleaning up client: " + e.getMessage());
            }
        }
    }
}
```
