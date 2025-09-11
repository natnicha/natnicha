import re
from datetime import datetime

current_year = datetime.now().year
value = current_year - 2018

readme_file = "README.md"
with open(readme_file, "r", encoding="utf8") as f:
    content = f.read()

new_string = "{0}+ years of experience".format(str(value))
pattern = "\d*\+ years of experience"
x = re.search(pattern, content)

content = content.replace(x.group(), new_string)

with open(readme_file, "w", encoding="utf8") as f:
    f.write(content)
