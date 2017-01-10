#!/usr/bin/env python
import requests
print requests.__version__

response = requests.get("https://raw.githubusercontent.com/omokdad/cmput404_lab1/master/req.py")
print response.status_code
print response.text

