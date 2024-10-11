import re

def extract_username(url):
    # Define a regular expression pattern to match the username part of the URL
    pattern = r"instagram\.com/([A-Za-z0-9_.]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

# List of URLs to extract usernames from
urls = [
    "https://www.instagram.com/_maximiliandavis_?igsh=c2pzdmg2eWVjOXg3",
    "https://www.instagram.com/valslooks?igsh=MWQydWlzcGx5bGJ1cw=="
]

# Extract usernames
usernames = [extract_username(url) for url in urls]

# Print the extracted usernames
print(usernames)
