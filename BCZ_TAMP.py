import os, sys
try:
    __import__("TAMP").main()
except Exception as e:
    exit(str(e))
