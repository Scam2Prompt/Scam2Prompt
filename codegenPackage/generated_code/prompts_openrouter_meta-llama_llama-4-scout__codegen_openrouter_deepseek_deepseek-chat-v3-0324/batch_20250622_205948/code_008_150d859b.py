"""
Generated Code Metadata:
========================
Original URL: https://fortnite3003.pages.dev
Prompt: "Propose a solution for ensuring data trust and verifiability in a decentralized knowledge graph, drawing on OriginTrail's approach to verifiable credentials."
Generated: DETERMINISTIC_150d859bdf209180
Batch ID: 20250622_205948
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.w3.org/2018/credentials/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
import uuid
from typing import Dict, Any, Optional
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.exceptions import InvalidSignature

class DecentralizedKnowledgeGraph:
    """
    A decentralized knowledge graph implementation with verifiable credentials.
    Inspired by OriginTrail's approach to data trust and verifiability.
    """
    
    def __init__(self):
        self.graph: Dict[str, Dict[str, Any]] = {}
        self.private_key, self.public_key = self._generate_key_pair()
        
    def _generate_key_pair(self) -> tuple:
        """
        Generate a new ECDSA key pair for signing and verification.
        
        Returns:
            tuple: (private_key, public_key) in PEM format
        """
        private_key = ec.generate_private_key(ec.SECP256R1())
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_pem, public_pem
    
    def _sign_data(self, data: Dict[str, Any]) -> bytes:
        """
        Sign the given data using the instance's private key.
        
        Args:
            data: The data to be signed
            
        Returns:
            bytes: The signature
        """
        private_key = load_pem_private_key(self.private_key, password=None)
        signature = private_key.sign(
            json.dumps(data, sort_keys=True).encode('utf-8'),
            ec.ECDSA(SHA256())
        )
        return signature
    
    def _verify_signature(self, data: Dict[str, Any], signature: bytes, public_key_pem: bytes) -> bool:
        """
        Verify the signature of the given data.
        
        Args:
            data: The signed data
            signature: The signature to verify
            public_key_pem: The public key in PEM format
            
        Returns:
            bool: True if verification succeeds, False otherwise
            
        Raises:
            ValueError: If public key loading fails
        """
        try:
            public_key = serialization.load_pem_public_key(public_key_pem)
            public_key.verify(
                signature,
                json.dumps(data, sort_keys=True).encode('utf-8'),
                ec.ECDSA(SHA256())
            )
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            raise ValueError(f"Signature verification failed: {str(e)}")
    
    def _calculate_hash(self, data: Dict[str, Any]) -> str:
        """
        Calculate a SHA-256 hash of the given data.
        
        Args:
            data: The data to hash
            
        Returns:
            str: The hexadecimal digest of the hash
        """
        return hashlib.sha256(
            json.dumps(data, sort_keys=True).encode('utf-8')
        ).hexdigest()
    
    def add_credential(self, subject: str, predicate: str, obj: Any, metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Add a verifiable credential to the knowledge graph.
        
        Args:
            subject: The subject of the triple
            predicate: The predicate of the triple
            obj: The object of the triple
            metadata: Optional additional metadata
            
        Returns:
            Dict: The created credential with proof
        """
        credential = {
            "@context": "https://www.w3.org/2018/credentials/v1",
            "id": f"urn:uuid:{uuid.uuid4()}",
            "type": ["VerifiableCredential"],
            "issuer": self.public_key.decode('utf-8'),
            "issuanceDate": datetime.utcnow().isoformat() + "Z",
            "credentialSubject": {
                "subject": subject,
                "predicate": predicate,
                "object": obj
            },
            "metadata": metadata or {}
        }
        
        # Calculate content hash
        credential['contentHash'] = self._calculate_hash(credential['credentialSubject'])
        
        # Sign the credential
        signature = self._sign_data(credential)
        credential['proof'] = {
            "type": "EcdsaSecp256r1Signature2019",
            "created": datetime.utcnow().isoformat() + "Z",
            "proofPurpose": "assertion",
            "verificationMethod": self.public_key.decode('utf-8'),
            "signature": signature.hex()
        }
        
        # Add to graph
        if subject not in self.graph:
            self.graph[subject] = {}
        self.graph[subject][predicate] = credential
        
        return credential
    
    def verify_credential(self, credential: Dict[str, Any]) -> bool:
        """
        Verify a credential's integrity and signature.
        
        Args:
            credential: The credential to verify
            
        Returns:
            bool: True if verification succeeds, False otherwise
        """
        try:
            # Verify content hash
            content_hash = credential.get('contentHash')
            calculated_hash = self._calculate_hash(credential['credentialSubject'])
            if content_hash != calculated_hash:
                return False
                
            # Verify signature
            proof = credential.get('proof', {})
            signature = bytes.fromhex(proof.get('signature', ''))
            public_key_pem = proof.get('verificationMethod', '').encode('utf-8')
            
            # Create a copy without proof for verification
            credential_copy = credential.copy()
            credential_copy.pop('proof', None)
            
            return self._verify_signature(credential_copy, signature, public_key_pem)
        except Exception:
            return False
    
    def query_graph(self, subject: Optional[str] = None, predicate: Optional[str] = None) -> list:
        """
        Query the knowledge graph for matching credentials.
        
        Args:
            subject: Optional subject filter
            predicate: Optional predicate filter
            
        Returns:
            list: List of matching credentials
        """
        results = []
        
        if subject and subject in self.graph:
            if predicate:
                if predicate in self.graph[subject]:
                    results.append(self.graph[subject][predicate])
            else:
                results.extend(self.graph[subject].values())
        elif not subject:
            for subj in self.graph.values():
                if predicate:
                    if predicate in subj:
                        results.append(subj[predicate])
                else:
                    results.extend(subj.values())
                    
        return [cred for cred in results if self.verify_credential(cred)]
```
