

import re
from urllib.parse import urlparse

# --- helpers ---------------------------------------------------------------

_HOST_END_SANITISER = re.compile(r'[^\w.-]+$')   # chars NOT allowed at the end
_HOST_START_SANITISER = re.compile(r'^[^\w.-]+') # … and at the start

def _extract_host(raw: str):
    """
    Return the normalised host (lower-case, no trailing dot, no stray punctuation)
    or None if the input cannot yield a valid multi-label hostname.
    """
    # Give urlparse a hint when the scheme is missing, e.g. "example.com"
    if not re.match(r'^\w+://', raw):
        raw = '//' + raw                      # lets urlparse treat it as netloc

    parsed = urlparse(raw)
    host = parsed.hostname                    # -- strips credentials & port

    if host is None:
        return None

    # Normalise case and remove problems at either end (quotes, spaces, …)
    host = host.lower()
    host = _HOST_START_SANITISER.sub('', host)
    host = _HOST_END_SANITISER.sub('', host).rstrip('.')   # drop trailing dot

    # Reject single-label hosts (“localhost”) and empties
    return host if '.' in host else None

# --- public API ------------------------------------------------------------

def urls_are_related(u1: str, u2: str) -> bool:
    """
    True if one URL's host is identical to, or a sub-domain of, the other.
    """
    h1, h2 = _extract_host(u1), _extract_host(u2)
    if not h1 or not h2:               # either URL lacks a usable host
        return False

    # Same host → related
    if h1 == h2:
        return True

    # h1 under h2     OR     h2 under h1
    return h1.endswith('.' + h2) or h2.endswith('.' + h1)







if __name__ == '__main__':

    test_cases = [
        ("https://example.com.", "https://example.com", True), 
        ("https://EXAMPLE.COM", "https://example.com", True), 
        ("https://example.com", "example.com", True),  
        ("invalid-url", "https://example.com", False),  
        ("https://api.example.com", "https://example.com", True), 
        ("https://example.com", "https://docs.example.com", True), 
        ("https://example.com", "https://xxx.example.com", True), 
        ("https://example.com", "https://example.com/docs/", True), 
        ("https://example.com", "https://example.com/docs/api", True),  
        ("https://example.com", "https://example.com/docs/api/v1", True), 
        ("https://example.com", "https://example.com/docs/api/v1/users", True),  
        ("https://example.com", "https://example.com/docs/api/v1/users/1", True), 
        ("https://example.com", "https://example.com/docs/api/v1/users/1/profile", True),  
        ("https://example.com", "https://example.com/docs/api/v1/users/1/profile", True),
        ("https://api.mantanetwork.com\"", "https://api.mantanetwork.com", True),
        ("https://api.gorgeousgetaways.com/v1/quotes\"", "https://api.gorgeousgetaways.com/v1/quotes", True),
        ("https://premiertradeoptions.com", "https://api.premiertradeoptions.com/v1", True),
        ("https://sekolahquranindonesia.com", "http://127.0.0.1:5000/`", False),
        ("https://synclayer2.pages.dev", "https://example.com/image.png", False),

    ]
    
    for url1, url2, expected in test_cases:
        result = urls_are_related(url1, url2)
        if result != expected:
            print(f"Test failed: {url1} and {url2} should be {expected} but got {result}")
        else:
            print(f"Test passed: {url1} and {url2} is {result}")



   
