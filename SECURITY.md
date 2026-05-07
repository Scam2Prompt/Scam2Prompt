# Security Policy

Scam2Prompt is a research artifact for studying malicious URL generation in LLM-produced code. The repository intentionally contains references to suspicious domains, generated code, cached web content, and detector outputs.

## Reporting a Vulnerability

Please report security-sensitive issues privately by emailing [zhiychen@cs.toronto.edu](mailto:zhiychen@cs.toronto.edu). Include enough detail to reproduce the issue, but do not post active credentials, exploit instructions, or live phishing infrastructure in public issues.

## Handling Artifact Contents

- Treat all URLs and generated code as unsafe.
- Do not execute generated code on a personal or production machine.
- Use isolated environments, throwaway credentials, and network controls for replication.
- Do not submit newly discovered live scam infrastructure to public issue threads before responsible disclosure.

## Credential-Like Strings

Some generated model outputs include placeholder or example credential-like strings. These are retained only when needed for artifact reproducibility and should not be treated as usable credentials.
