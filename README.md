# API Security Lab: BOLA

An educational lab based on my workshop "Securing Digital Bridges". **For local use only: do not deploy.**

## What is BOLA?
Broken Object Level Authorization: the API checks that you are logged in, but not that the object you request (order, invoice, file) belongs to you.

## Run the vulnerable version
    pip install -r requirements.txt
    python vulnerable/app.py
    curl -H "X-User: alice" http://127.0.0.1:5000/orders/2   # alice reads bob's order

## Run the fixed version
    python fixed/app.py
    curl -H "X-User: alice" http://127.0.0.1:5000/orders/2   # 403 Forbidden
    curl -H "X-User: alice" http://127.0.0.1:5000/orders/1   # 200 OK

## Defenses
1. Check ownership on the server for every request
2. Bind the record to its owner inside the query
3. Use non-sequential IDs (GUID) as an extra layer, not a replacement
4. Test authorization automatically in every release

## References
OWASP API Security Top 10: API1 Broken Object Level Authorization

Author: Hussa Almusayab
