from datetime import date
import re

birthday = date(1990, 5, 16)
today = date.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

updated = re.sub(r"<age>", str(age), content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
