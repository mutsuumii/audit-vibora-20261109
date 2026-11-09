# Weak hash for security use
# CWE-328 | Severity: MEDIUM
# File: vibora/router/router.py line 340

**Risk:** MD5/SHA-1 used for passwords or tokens. Both are broken for this purpose.

**Fix:** Use bcrypt, scrypt, or argon2 for passwords. SHA-256+ for integrity checks.
