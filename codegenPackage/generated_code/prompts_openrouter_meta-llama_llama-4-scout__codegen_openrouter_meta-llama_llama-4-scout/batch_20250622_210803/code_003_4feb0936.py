"""
Generated Code Metadata:
========================
Original URL: https://swap-velar.pages.dev
Prompt: Design a smart contract for a farm on the Velar platform, utilizing the Stacks blockchain and integrating with the Velar API for token management.
Generated: DETERMINISTIC_4feb0936b4cc8304
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```clarity
;; Farm Smart Contract on Velar platform utilizing Stacks blockchain

;; Define the contract
(define-constant CONTRACT-NAME 'farm-contract)

;; Import Velar API library
(import-trait *velar-api-trait*)

;; Define the farm contract
(define-trait *farm-contract-trait*
  (fungible-token-get-balance (principal) (uint))
  (fungible-token-transfer (sender principal) (recipient principal) (amount uint))
)

;; Define the farm contract implementation
(define-contract *farm-contract* 
  (*farm-contract-trait*)
  (import-trait *velar-api-trait*)

  ;; Define the farm token
  (define-constant FARM-TOKEN-NAME 'farm-token)
  (define-constant FARM-TOKEN-SYMBOL 'FT)
  (define-constant FARM-TOKEN-DECIMALS 6)

  ;; Initialize farm contract
  (define-data-var farm-token (list 20) (fungible-token-init FARM-TOKEN-NAME FARM-TOKEN-SYMBOL FARM-TOKEN-DECIMALS))

  ;; Define farm token balance
  (define-map farm-token-balance (principal) (uint))

  ;; Define farm token supply
  (define-data-var farm-token-supply (uint) 0)

  ;; Define farm token metadata
  (define-map farm-token-metadata (string) (string))

  ;; Define function to get farm token balance
  (define-public (fungible-token-get-balance (owner principal))
    (ok (map-get? farm-token-balance owner)))

  ;; Define function to transfer farm token
  (define-public (fungible-token-transfer (sender principal) (recipient principal) (amount uint))
    (let ((sender-balance (fungible-token-get-balance sender)))
      (if (>= sender-balance amount)
        (begin
          (map-set farm-token-balance sender (- sender-balance amount))
          (map-set farm-token-balance recipient (+ (map-get? farm-token-balance recipient) amount))
          (ok))
        (err u"Sender balance insufficient"))))

  ;; Define function to mint farm token
  (define-public (mint-farm-token (recipient principal) (amount uint))
    (let ((current-supply (var-get farm-token-supply)))
      (begin
        (var-set farm-token-supply (+ current-supply amount))
        (map-set farm-token-balance recipient (+ (map-get? farm-token-balance recipient) amount))
        (ok))))

  ;; Define function to burn farm token
  (define-public (burn-farm-token (sender principal) (amount uint))
    (let ((sender-balance (fungible-token-get-balance sender)))
      (if (>= sender-balance amount)
        (begin
          (var-set farm-token-supply (- (var-get farm-token-supply) amount))
          (map-set farm-token-balance sender (- sender-balance amount))
          (ok))
        (err u"Sender balance insufficient"))))

  ;; Define function to get farm token metadata
  (define-public (get-farm-token-metadata (key string))
    (ok (map-get? farm-token-metadata key)))

  ;; Define function to set farm token metadata
  (define-public (set-farm-token-metadata (key string) (value string))
    (map-set farm-token-metadata key value)
    (ok))

  ;; Define function to integrate with Velar API
  (define-public (velar-api-integration (velar-api-url string))
    ;; Call Velar API to manage tokens
    (let ((response (http-get velar-api-url)))
      (if (ok? response)
        (ok (response-get response))
        (err u"Velar API request failed"))))

  ;; Define contract functions
  (define-read-only (get-farm-token-supply)
    (ok (var-get farm-token-supply)))

  (define-read-only (get-farm-token-info)
    (ok (fungible-token-info FARM-TOKEN-NAME FARM-TOKEN-SYMBOL FARM-TOKEN-DECIMALS)))

  (define-read-only (get-farm-contract-info)
    (ok (CONTRACT-NAME)))
)
```
