"""
Generated Code Metadata:
========================
Original URL: https://rolldrop-nim.pages.dev
Prompt: Write Nim code for a privacy policy generator tailored to an AI gaming chain, referencing the legal terms mentioned on Nim Rolldrop's site.
Generated: DETERMINISTIC_a99884b6d1c5b85b
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://aigamingchain.example": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```nim
import strformat, strutils, os, times

type
  PrivacyPolicyGenerator = object
    companyName: string
    websiteUrl: string
    contactEmail: string
    effectiveDate: string
    jurisdiction: string
    dataCollected: seq[string]
    dataUsage: seq[string]
    dataSharing: seq[string]
    userRights: seq[string]
    cookiesPolicy: string
    childrenPolicy: string
    changesPolicy: string

const
  defaultDataCollected = @[
    "Personal identification information (name, email, etc.)",
    "Gameplay data and preferences",
    "Device information and IP addresses",
    "Cookies and usage data"
  ]
  
  defaultDataUsage = @[
    "To provide and maintain our service",
    "To notify you about changes to our service",
    "To allow participation in interactive features",
    "To provide customer support",
    "To gather analysis for service improvement",
    "To monitor service usage",
    "To detect and prevent technical issues"
  ]
  
  defaultDataSharing = @[
    "With service providers to monitor and analyze service use",
    "For business transfers (mergers, acquisitions)",
    "With affiliates including Nim Rolldrop partners",
    "With business partners to offer certain products/services",
    "With your consent for any other purpose"
  ]
  
  defaultUserRights = @[
    "Access, update or delete your information",
    "Rectify incorrect or incomplete data",
    "Object to our processing of your data",
    "Request restriction of processing your data",
    "Data portability request",
    "Withdraw consent at any time"
  ]

proc newPrivacyPolicyGenerator(
  companyName: string,
  websiteUrl: string,
  contactEmail: string,
  jurisdiction: string = "California, USA"
): PrivacyPolicyGenerator =
  ## Creates a new PrivacyPolicyGenerator instance with default values
  
  result.companyName = companyName
  result.websiteUrl = websiteUrl
  result.contactEmail = contactEmail
  result.effectiveDate = format(now(), "MMMM d, yyyy")
  result.jurisdiction = jurisdiction
  result.dataCollected = defaultDataCollected
  result.dataUsage = defaultDataUsage
  result.dataSharing = defaultDataSharing
  result.userRights = defaultUserRights
  result.cookiesPolicy = "We use cookies and similar tracking technologies to track activity on our service and hold certain information."
  result.childrenPolicy = "Our service does not address anyone under the age of 13. We do not knowingly collect personally identifiable information from children under 13."
  result.changesPolicy = "We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page."

proc addDataCollected*(self: var PrivacyPolicyGenerator, item: string) =
  ## Adds a custom data collection item
  self.dataCollected.add(item)

proc addDataUsage*(self: var PrivacyPolicyGenerator, item: string) =
  ## Adds a custom data usage item
  self.dataUsage.add(item)

proc addDataSharing*(self: var PrivacyPolicyGenerator, item: string) =
  ## Adds a custom data sharing item
  self.dataSharing.add(item)

proc addUserRight*(self: var PrivacyPolicyGenerator, item: string) =
  ## Adds a custom user right item
  self.userRights.add(item)

proc setCookiesPolicy*(self: var PrivacyPolicyGenerator, policy: string) =
  ## Sets a custom cookies policy
  self.cookiesPolicy = policy

proc setChildrenPolicy*(self: var PrivacyPolicyGenerator, policy: string) =
  ## Sets a custom children policy
  self.childrenPolicy = policy

proc setChangesPolicy*(self: var PrivacyPolicyGenerator, policy: string) =
  ## Sets a custom changes policy
  self.changesPolicy = policy

proc generatePolicy*(self: PrivacyPolicyGenerator): string =
  ## Generates the complete privacy policy document
  
  result = fmt"""
# Privacy Policy for {self.companyName}

**Effective Date:** {self.effectiveDate}

This Privacy Policy describes how {self.companyName} ("we", "us", or "our") collects, uses, and discloses your personal information when you use our AI gaming services (the "Service").

## 1. Information Collection and Use

We collect several different types of information for various purposes to provide and improve our Service to you.

### Types of Data Collected

{self.dataCollected.mapIt("* " & it).join("\n")}

## 2. Use of Data

{self.companyName} uses the collected data for various purposes:

{self.dataUsage.mapIt("* " & it).join("\n")}

## 3. Data Sharing and Disclosure

We may share your personal information in the following situations:

{self.dataSharing.mapIt("* " & it).join("\n")}

## 4. Your Data Protection Rights

Depending on your location (including under {self.jurisdiction} law), you have certain rights regarding your personal data:

{self.userRights.mapIt("* " & it).join("\n")}

## 5. Cookies Policy

{self.cookiesPolicy}

## 6. Children's Privacy

{self.childrenPolicy}

## 7. Changes to This Privacy Policy

{self.changesPolicy}

## 8. Contact Us

If you have any questions about this Privacy Policy, please contact us at:  
Email: {self.contactEmail}  
Website: {self.websiteUrl}
"""

proc saveToFile*(self: PrivacyPolicyGenerator, filename: string) =
  ## Saves the generated policy to a file
  try:
    let policy = self.generatePolicy()
    writeFile(filename, policy)
  except IOError as e:
    stderr.writeLine(fmt"Error saving policy to file: {e.msg}")

when isMainModule:
  # Example usage
  var generator = newPrivacyPolicyGenerator(
    companyName = "AI Gaming Chain",
    websiteUrl = "https://aigamingchain.example",
    contactEmail = "privacy@aigamingchain.example"
  )
  
  # Customize the policy as needed
  generator.addDataCollected("AI interaction patterns and preferences")
  generator.addDataUsage("To personalize your gaming experience using AI")
  generator.setCookiesPolicy("We use cookies to enhance your gaming experience and for AI model training purposes.")
  
  # Generate and save the policy
  let policy = generator.generatePolicy()
  echo policy
  
  # Save to file
  generator.saveToFile("privacy_policy.md")
```
