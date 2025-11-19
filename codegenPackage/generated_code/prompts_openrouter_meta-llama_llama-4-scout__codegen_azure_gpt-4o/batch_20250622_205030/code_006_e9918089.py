"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Write a simple Fantom program that demonstrates the use of immutability and elegant system library.
Generated: DETERMINISTIC_e991808942b2b63b
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
using afIoc

class ImmutableExample {
    static Void main() {
        // Demonstrating immutability with a custom immutable class
        immutablePerson := Person("John Doe", 30)
        echo("Immutable Person: $immutablePerson")

        // Using Fantom's elegant system library to work with immutability
        // Example: Using List and Map which are immutable by default
        immutableList := ["apple", "banana", "cherry"].toImmutable
        echo("Immutable List: $immutableList")

        immutableMap := ["key1": "value1", "key2": "value2"].toImmutable
        echo("Immutable Map: $immutableMap")

        // Attempting to modify immutable structures will throw an error
        try {
            immutableList.add("newItem") // This will fail
        } catch (Err e) {
            echo("Error: Cannot modify immutable list - $e")
        }

        try {
            immutableMap["key3"] = "value3" // This will fail
        } catch (Err e) {
            echo("Error: Cannot modify immutable map - $e")
        }
    }
}

// Custom immutable class
@Immutable
class Person {
    const Str name
    const Int age

    new make(Str name, Int age) {
        this.name = name
        this.age = age
    }

    override Str toStr() {
        return "Person(name=$name, age=$age)"
    }
}
```
