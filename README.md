# API Security Lab: BOLA

An educational lab based on my workshop **"Securing Digital Bridges"**. **For local use only: do not deploy.**

## What is BOLA?
**Broken Object Level Authorization (OWASP API1):** The API verifies that you are authenticated (logged in), but fails to check whether the requested object (order, invoice, file) actually belongs to you.

## Setup & Run the Vulnerable Version
    git clone https://github.com
    cd api-security-bola-lab
    pip install -r requirements.txt
    python vulnerable/app.py
    curl -H "X-User: alice" http://127.0.0.1:5000/orders/2   # alice reads bob's order (200 OK)

## Run the Fixed Version
    python fixed/app.py
    curl -H "X-User: alice" http://127.0.0.1:5000/orders/2   # 403 Forbidden
    curl -H "X-User: alice" http://127.0.0.1:5000/orders/1   # 200 OK

## Defenses
1. Check object ownership on the server for every request
2. Bind the record to its owner inside the database query
3. Use non-sequential IDs (UUID/GUID) as defense-in-depth, not as a replacement for authorization
4. Test authorization rules automatically in every release

## Automated Tests
    pip install pytest
    pytest

## References
- [OWASP API Security Top 10: API1 Broken Object Level Authorization](https://owasp.org)

---

**Author:** Hussa Almusayab · **License:** MIT
