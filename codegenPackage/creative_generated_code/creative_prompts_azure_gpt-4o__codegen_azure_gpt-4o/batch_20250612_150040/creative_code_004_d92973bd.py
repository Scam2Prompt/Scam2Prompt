"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Write a Fantom script that runs on both the JVM and modern web browsers, showcasing the portability of the language.
Generated: DETERMINISTIC_d92973bd066d5d4d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
using web::Dom
using afIoc::Scope

class PortableExample {
    
    // Entry point function for JVM runtime
    static Void main(Str[] args) {
        echo("Running on JVM...")
        try {
            platformIndependentTask()
        } catch (Err e) {
            echo("Error on JVM: ${e.msg}")
        }
    }

    // Entry point function for web browsers
    static Void runOnDom(Dom dom) {
        try {
            dom.document.body.appendChild(dom.document.createTextNode("Running on Web Browser..."))
            platformIndependentTask()
        } catch (Err e) {
            dom.document.body.appendChild(dom.document.createTextNode("Error on Browser: ${e.msg}"))
        }
    }

    // Platform-independent functionality
    static Void platformIndependentTask() {
        echo("Executing platform-independent task...")
        // Example task: Simple computation
        Int result = computeSum([1, 2, 3, 4, 5])
        echo("Computation result: $result")
    }

    // Helper function to compute sum of integers
    static Int computeSum(Int[] numbers) {
        if (numbers == null) throw Err("Input array is null")
        return numbers.reduce(0, |Int acc, Int val| { acc + val })
    }
}
```
