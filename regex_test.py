import re

# 1. U.S. ZIP codes
zip_pattern = re.compile(r"\b\d{5}([- ]\d{4})?\b")
test_zips = ["12345", "12345-6789", "12345 6789", "abc12345def"]
print("ZIP codes:", [m.group() for s in test_zips for m in zip_pattern.finditer(s)])

# 2. Words not starting with capital letter
not_cap_pattern = re.compile(r"\b(?![A-Z])[A-Za-z][A-Za-z'-]*\b")
test_words = ["London", "don’t", "state-of-the-art", "hello", "Apple"]
print("Not capitalized words:", [m.group() for s in test_words for m in not_cap_pattern.finditer(s)])

# 3. Numbers (rich version)
num_pattern = re.compile(r"[+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?")
test_nums = ["42", "-3.14", "+1,000", "2.5e-4", "1000000"]
print("Numbers:", [m.group() for s in test_nums for m in num_pattern.finditer(s)])

# 4. Variants of “email” (case-insensitive)
email_pattern = re.compile(r"(?i)\be[-\s–]?mail\b")
test_emails = ["email", "E-mail", "e mail", "E–mail", "something else"]
print("Email variants:", [m.group() for s in test_emails for m in email_pattern.finditer(s)])

# 5. Interjection “go”, “goo”, “gooo” with optional punctuation
go_pattern = re.compile(r"\bgo+[\!\.\,\?]?\b")
test_go = ["go", "goo", "gooo!", "go?", "going", "gopher"]
print("Go interjections:", [m.group() for s in test_go for m in go_pattern.finditer(s)])

# 6. Lines ending with question mark + quotes/brackets/spaces
endq_pattern = re.compile(r"\?[)\"'\]\s]*$")
test_lines = [
    "Are you sure?",
    "Is this correct?)",
    "Really?   ",
    "Wait! No.",
]
print("Lines ending with ?:", [s for s in test_lines if endq_pattern.search(s)])
