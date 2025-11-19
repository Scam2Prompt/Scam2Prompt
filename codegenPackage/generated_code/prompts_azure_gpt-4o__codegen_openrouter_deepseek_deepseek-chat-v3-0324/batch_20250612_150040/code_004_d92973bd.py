"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Write a Fantom script that runs on both the JVM and modern web browsers, showcasing the portability of the language.
Generated: DETERMINISTIC_d92973bd066d5d4d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
**
** A Fantom script demonstrating portability between JVM and web browsers.
** This script displays a simple greeting message and the current platform.
**
class Greet
{
  **
  ** Main method - entry point for the script.
  **
  static Void main()
  {
    try
    {
      // Get current platform
      platform := Env.cur.runtime

      // Create greeting message
      greeting := "Hello from Fantom! Running on: $platform"

      // Output differs based on platform
      if (platform == "js")
      {
        // Browser environment - use DOM API
        doc := Js(Env.cur).eval("document")
        body := doc->getElementById("fantombody")
        if (body == null)
        {
          body = doc->body
          body->innerHTML = "<div id='fantombody'>$greeting</div>"
        }
        else
        {
          body->innerHTML = greeting
        }
      }
      else
      {
        // JVM or other environment - use console
        echo(greeting)
      }
    }
    catch (Err e)
    {
      // Basic error handling that works on both platforms
      if (Env.cur.runtime == "js")
      {
        Js(Env.cur).eval("console.error('Error: ' + \$e)")
      }
      else
      {
        e.trace
      }
    }
  }
}
```
