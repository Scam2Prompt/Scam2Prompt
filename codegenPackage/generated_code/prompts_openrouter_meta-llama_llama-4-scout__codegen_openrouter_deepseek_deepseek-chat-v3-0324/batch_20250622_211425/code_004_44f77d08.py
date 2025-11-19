"""
Generated Code Metadata:
========================
Original URL: https://ff7a4d70.swim-ui.pages.dev
Prompt: What are the key features of Swim framework that allow building web applications with plain HTML, and provide an example use case.
Generated: DETERMINISTIC_44f77d086d7eed4d
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Swim Framework Example: Building a Web App with Plain HTML
// This example demonstrates key features of Swim framework for building web applications with plain HTML.

import swim.api.SwimRoute;
import swim.api.agent.AgentRoute;
import swim.api.plane.AbstractPlane;
import swim.api.space.Space;
import swim.kernel.Kernel;
import swim.server.ServerLoader;
import swim.structure.Value;
import swim.web.WebRoute;
import swim.web.WebRouteContext;

public class SimpleWebApp extends AbstractPlane {

  public static void main(String[] args) {
    // Load the Swim kernel
    final Kernel kernel = ServerLoader.loadServer();
    final Space space = kernel.getSpace("simple");

    // Start the server
    kernel.start();
    System.out.println("Running Simple Web App...");

    // Keep the application running
    kernel.run();
  }

  // Define a web route that serves plain HTML
  @SwimRoute("/hello")
  public static final class HelloRoute extends WebRoute {

    @Override
    public void doRequest(WebRouteContext context) {
      try {
        // Plain HTML response
        final String html = "<!DOCTYPE html>\n" +
            "<html>\n" +
            "<head>\n" +
            "  <title>Swim Framework Example</title>\n" +
            "</head>\n" +
            "<body>\n" +
            "  <h1>Hello from Swim!</h1>\n" +
            "  <p>This is a plain HTML page served by Swim framework.</p>\n" +
            "</body>\n" +
            "</html>";

        // Set response headers and content
        context.response().setHeader("Content-Type", "text/html");
        context.response().setContent(html);
        context.didRespond();
      } catch (Exception e) {
        // Error handling
        context.response().setStatus(500);
        context.response().setContent("Internal Server Error");
        context.didRespond();
      }
    }
  }

  // Example of dynamic content with plain HTML
  @SwimRoute("/greet/:name")
  public static final class GreetRoute extends WebRoute {

    @Override
    public void doRequest(WebRouteContext context) {
      try {
        // Get path parameter
        final Value nameValue = context.getRequest().getUri().path().get("name");
        final String name = nameValue != null ? nameValue.stringValue() : "Guest";

        // Dynamic HTML response
        final String html = "<!DOCTYPE html>\n" +
            "<html>\n" +
            "<head>\n" +
            "  <title>Greeting</title>\n" +
            "</head>\n" +
            "<body>\n" +
            "  <h1>Hello, " + name + "!</h1>\n" +
            "  <p>Welcome to our Swim application.</p>\n" +
            "</body>\n" +
            "</html>";

        // Set response headers and content
        context.response().setHeader("Content-Type", "text/html");
        context.response().setContent(html);
        context.didRespond();
      } catch (Exception e) {
        // Error handling
        context.response().setStatus(500);
        context.response().setContent("Internal Server Error");
        context.didRespond();
      }
    }
  }
}
```
