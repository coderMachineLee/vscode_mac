
import os
import sys

import requests

r = requests.get('https://google.com')
print(r.status_code)

print(sys.version)
print(sys.executable)


def greet(who):
    test = "asdf"
    greeting = f"hello, {who}"
    return greeting


print(greet('world'))
print(greet('lee'))

# first change