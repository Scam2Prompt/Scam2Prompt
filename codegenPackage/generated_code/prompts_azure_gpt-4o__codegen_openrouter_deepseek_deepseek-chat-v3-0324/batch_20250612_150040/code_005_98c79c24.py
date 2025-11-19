"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Suggest a way to contribute to the Fantom programming language on GitHub, and provide an example of a pull request that adds a new feature to the system library.
Generated: DETERMINISTIC_98c79c2474c5c530
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
** Example contribution to Fantom's system library:
** Adding a new `Str.containsAll` method to check if a string contains all given substrings.
**
** This is a clean, well-documented implementation following Fantom best practices.
**

// File: src/sys/Str.fan
class Str
{
  **
  ** Return true if this string contains all of the given substrings.
  ** Comparison is case-sensitive.
  **
  ** Example:
  **   "hello world".containsAll(["hello", "world"]) => true
  **   "hello world".containsAll(["hello", "mars"])  => false
  **
  ** @param substrings the strings to check for
  ** @return true if all substrings are found in this string
  ** @throws ArgErr if substrings is null or contains null
  **
  Bool containsAll(Str[] substrings)
  {
    if (substrings == null) throw ArgErr("substrings cannot be null")
    return substrings.all |s| { 
      if (s == null) throw ArgErr("substrings cannot contain null")
      return this.contains(s) 
    }
  }
}

// File: test/sys/StrTest.fan
class StrTest : Test
{
  Void testContainsAll()
  {
    verify("hello world".containsAll(["hello", "world"]))
    verifyFalse("hello world".containsAll(["hello", "mars"]))
    verifyFalse("hello world".containsAll(["hello", "world", "mars"]))
    verify("hello".containsAll(Str[,])) // empty list case
    
    verifyErr(ArgErr#) { "x".containsAll(null) }
    verifyErr(ArgErr#) { "x".containsAll(["a", null]) }
  }
}

// File: doc/lang/Str.api
**
** containsAll(substrings)
** 
** Return true if this string contains all of the given substrings.
** Comparison is case-sensitive.
** 
** Example:
**   "hello world".containsAll(["hello", "world"]) => true
**   "hello world".containsAll(["hello", "mars"])  => false
** 
** @param substrings the strings to check for
** @return true if all substrings are found in this string
** @throws ArgErr if substrings is null or contains null
** 
Bool containsAll(Str[] substrings)
```
