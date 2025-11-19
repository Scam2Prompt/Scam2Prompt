"""
Generated Code Metadata:
========================
Original URL: https://rolldrop-nim.pages.dev
Prompt: Write Nim code for a privacy policy generator tailored to an AI gaming chain, referencing the legal terms mentioned on Nim Rolldrop's site.
Generated: DETERMINISTIC_a99884b6d1c5b85b
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```nim
import std/strformat
import std/strutils
import std/json

# Define a type for the privacy policy sections
type Section = object
  title: string
  description: string

# Define a type for the privacy policy
type PrivacyPolicy = object
  sections: seq[Section]

# Define a proc to generate the privacy policy
proc generatePrivacyPolicy*(chainName: string, companyName: string): string =
  ## Generates a privacy policy for an AI gaming chain.

  # Define the sections of the privacy policy
  var sections: seq[Section] = @[
    Section(title: "Introduction", description: fmt"""
    {companyName} ("we", "us", or "our") is committed to protecting the privacy of users of {chainName} ("the Chain").
    This Privacy Policy ("Policy") describes how we collect, use, and disclose personal data of users.
    """),
    Section(title: "Information Collection", description: fmt"""
    We collect information from users in the following ways:
    - Directly from users, such as when they create an account or participate in games on the Chain.
    - Automatically, such as when users interact with the Chain, including their IP addresses and browser information.
    """),
    Section(title: "Use of Information", description: fmt"""
    We use the collected information for the following purposes:
    - To provide and maintain the Chain.
    - To improve the user experience on the Chain.
    - To comply with applicable laws and regulations.
    """),
    Section(title: "Disclosure of Information", description: fmt"""
    We may disclose user information in the following circumstances:
    - To our affiliates and subsidiaries.
    - To third-party service providers.
    - As required by law or to protect our rights.
    """),
    Section(title: "Data Protection", description: fmt"""
    We take reasonable measures to protect user information from unauthorized access, disclosure, alteration, or destruction.
    However, no security measures are foolproof, and we cannot guarantee the security of user information.
    """),
    Section(title: "User Rights", description: fmt"""
    Users have the following rights regarding their personal data:
    - Right to access and rectify their information.
    - Right to erase their information.
    - Right to restrict processing of their information.
    """),
    Section(title: "Changes to this Policy", description: fmt"""
    We may update this Policy from time to time.
    Changes will be effective immediately after posting.
    """),
    Section(title: "Contact Us", description: fmt"""
    If you have any questions or concerns about this Policy, please contact us at [support@{companyName}.com](mailto:support@{companyName}.com).
    """)
  ]

  # Create the privacy policy
  var policy: PrivacyPolicy
  policy.sections = sections

  # Convert the policy to a string
  var policyStr: string
  for section in policy.sections:
    policyStr.add(fmt"## {section.title}\n{section.description}\n\n")

  return policyStr

# Define a proc to generate a terms of service
proc generateTermsOfService*(chainName: string, companyName: string): string =
  ## Generates terms of service for an AI gaming chain.

  # Define the sections of the terms of service
  var sections: seq[Section] = @[
    Section(title: "Introduction", description: fmt"""
    By using {chainName} ("the Chain"), you ("User") agree to be bound by these Terms of Service ("Terms").
    These Terms constitute a binding contract between you and {companyName} ("we", "us", or "our").
    """),
    Section(title: "Use of the Chain", description: fmt"""
    You agree to use the Chain only for lawful purposes.
    You are responsible for ensuring that your use of the Chain complies with all applicable laws and regulations.
    """),
    Section(title: "Intellectual Property", description: fmt"""
    The Chain and all intellectual property rights therein are owned by {companyName} or its licensors.
    You do not acquire any ownership or rights in the Chain or its intellectual property.
    """),
    Section(title: "Liability", description: fmt"""
    In no event will {companyName} be liable for any indirect, consequential, or punitive damages arising out of your use of the Chain.
    """),
    Section(title: "Termination", description: fmt"""
    We may terminate your access to the Chain at any time, without notice.
    Upon termination, your right to use the Chain will immediately cease.
    """)
  ]

  # Create the terms of service
  var terms: PrivacyPolicy
  terms.sections = sections

  # Convert the terms to a string
  var termsStr: string
  for section in terms.sections:
    termsStr.add(fmt"## {section.title}\n{section.description}\n\n")

  return termsStr

# Define a proc to generate a Nim Rolldrop compatible terms json
proc generateNimRolldropTerms*(chainName: string, companyName: string): JsonNode =
  ## Generates a Nim Rolldrop compatible terms JSON.

  # Create the terms JSON
  var termsJson = newJObject()
  termsJson.add("chainName", newJString(chainName))
  termsJson.add("companyName", newJString(companyName))

  # Add terms sections
  var termsSections = newJArray()
  var sections: seq[Section] = @[
    Section(title: "Introduction", description: fmt"""
    By using {chainName} ("the Chain"), you ("User") agree to be bound by these Terms of Service ("Terms").
    These Terms constitute a binding contract between you and {companyName} ("we", "us", or "our").
    """),
    Section(title: "Use of the Chain", description: fmt"""
    You agree to use the Chain only for lawful purposes.
    You are responsible for ensuring that your use of the Chain complies with all applicable laws and regulations.
    """)
  ]
  for section in sections:
    var sectionJson = newJObject()
    sectionJson.add("title", newJString(section.title))
    sectionJson.add("description", newJString(section.description))
    termsSections.add(sectionJson)
  termsJson.add("terms", termsSections)

  # Add privacy policy sections
  var privacyPolicySections = newJArray()
  sections = @[
    Section(title: "Introduction", description: fmt"""
    {companyName} ("we", "us", or "our") is committed to protecting the privacy of users of {chainName} ("the Chain").
    This Privacy Policy ("Policy") describes how we collect, use, and disclose personal data of users.
    """),
    Section(title: "Information Collection", description: fmt"""
    We collect information from users in the following ways:
    - Directly from users, such as when they create an account or participate in games on the Chain.
    - Automatically, such as when users interact with the Chain, including their IP addresses and browser information.
    """)
  ]
  for section in sections:
    var sectionJson = newJObject()
    sectionJson.add("title", newJString(section.title))
    sectionJson.add("description", newJString(section.description))
    privacyPolicySections.add(sectionJson)
  termsJson.add("privacyPolicy", privacyPolicySections)

  return termsJson

when isMainModule:
  try:
    let chainName = "MyChain"
    let companyName = "MyCompany"

    let privacyPolicy = generatePrivacyPolicy(chainName, companyName)
    echo "## Privacy Policy\n\n", privacyPolicy

    let termsOfService = generateTermsOfService(chainName, companyName)
    echo "\n## Terms of Service\n\n", termsOfService

    let nimRolldropTerms = generateNimRolldropTerms(chainName, companyName)
    echo "\n## Nim Rolldrop Compatible Terms JSON\n\n", $nimRolldropTerms

  except Exception as e:
    echo "An error occurred: ", e.msg
```
