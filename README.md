# Security audit: vibora-io/vibora

Date: 2026-11-09 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 1 issue(s): 1 medium.

## Findings

### 1. [MEDIUM] Weak hash for security use

**CWE-328** | `vibora/router/router.py` line 340

MD5/SHA-1 used for passwords or tokens. Both are broken for this purpose.

```
key = base64.b64encode(hashlib.sha1(key.encode('utf-8')).digest())
```

**Fix:** Use bcrypt, scrypt, or argon2 for passwords. SHA-256+ for integrity checks.
---
