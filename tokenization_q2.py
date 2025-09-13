import re
import subprocess
import sys

# Function to install a package if missing
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing spaCy, install if missing
try:
    import spacy
except ModuleNotFoundError:
    print("spaCy not found. Installing...")
    install_package("spacy")
    import spacy

# Try loading English model, install if missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("English model not found. Downloading...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Paragraph for tokenization
paragraph = """Mr. Smith didn't go to Washington. 
Instead, he stayed home, watching Netflix, and eating ice-cream. 
Was it a good decision? Maybe not."""

print("Original Paragraph:")
print(paragraph)
print("=" * 50)

# 1. Naïve space-based tokenization
naive_tokens = paragraph.split()
print("1. Naïve space-based tokens:")
print(naive_tokens)
print("=" * 50)

# 2. Manual correction (regex handling)
manual_tokens = re.findall(r"\w+[-']?\w+|\w+|[.,!?;]", paragraph)
print("2. Manual corrected tokens:")
print(manual_tokens)
print("=" * 50)

# 3. Tool-based tokenization (spaCy)
doc = nlp(paragraph)
tool_tokens = [token.text for token in doc]
print("3. spaCy tokens:")
print(tool_tokens)
print("=" * 50)

# 4. Compare tokenizations
diff_naive_manual = set(naive_tokens) ^ set(manual_tokens)
diff_manual_tool = set(manual_tokens) ^ set(tool_tokens)
print("Differences (Naive vs Manual):", diff_naive_manual)
print("Differences (Manual vs Tool):", diff_manual_tool)
print("=" * 50)

# 5. Multiword Expressions (MWEs)
mwes = ["New York", "ice-cream", "stay home"]
print("Example MWEs:", mwes)
print("Reason: These should be treated as single tokens because they represent fixed concepts/phrases.")
