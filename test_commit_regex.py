import re

# Simpler regex to match any non-word character (emoji or symbol) at the start
pattern = r"^(?:[\W_]+)?([\w-]+)(?:\(([^)]+)\))?:?\s(.+)$"

commit = "🔧 fix(workflows): correct condition for running tests in setup-and-test action"

match = re.match(pattern, commit)
if match:
    print("type:", match.group(1))
    print("scope:", match.group(2))
    print("subject:", match.group(3))
else:
    print("No match")
