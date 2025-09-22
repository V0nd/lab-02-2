from collections import defaultdict

LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parse(line):
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            ip = parts[anchor+1]          # the port value will be next token, anchor+1
            return ip.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

counts = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if ("Failed password" in line or "Invalid user" in line) and not None:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
print(counts)