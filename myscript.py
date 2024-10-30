import os
import sys

badhash = os.getenv("BADHASH")
goodhash = os.getenv("GOODHASH")

if not badhash or not goodhash:
    print("Error: Both BADHASH and GOODHASH must be defined.")
    sys.exit(1)

os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")