import subprocess
import json

full_cwa_text = """
(a) Esta
"""

# Convert text to a JSON-safe string
escaped_json_string = json.dumps(full_cwa_text.strip(), ensure_ascii=False)

# Copy to clipboard using macOS pbcopy
try:
    subprocess.run("pbcopy", text=True, input=escaped_json_string, check=True)
    print("✅ Escaped JSON string copied to clipboard!")
except Exception as e:
    print(f"❌ Error copying to clipboard: {e}")
