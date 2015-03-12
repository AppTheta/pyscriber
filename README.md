Scriber.py
==========

A Python wrapper for the the Scriber API. See scriber.io


Install
-------

```
pip install scriber
```

Basic Usage
-----------

```
from scriber.api import Scriber

s = Scriber(“<api_key>”, “<app_id>”)
s.record_event(“<user_id>”, “<event_label>”)
```

e.g.

```
from scriber.api import Scriber

s = Scriber(“CZFcO2xZdiLTz6m6KgrB4pqH1KI3zy49S0AZmeFZu9o”, “MyApp”)
s.record_event(“email@example.com”, “LoginSuccess”)
```

Docs
----

http://scriber.io/docs/#/python
