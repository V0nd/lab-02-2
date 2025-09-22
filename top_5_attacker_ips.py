from collections import defaultdict
import time

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

#sort a dictionary
def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

counts = defaultdict(int)           # Create a dictionary to keep track of IPs
start = time.time()

with open("sample_auth_small.log") as f:
    for line in f:
        if ("Failed password" in line or "Invalid user" in line) and not None:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1

end = time.time()

counts = top_n(counts, len(counts))
print("Top 5 attacker IPs:")

for i in range(1,6):
    print(f"{i}. {counts[i-1][0]} - {counts[i-1][1]}")

with open('failed_counts.txt', 'w') as f:
    f.write("ip,failed_count")
    for i in range(len(counts)):
        f.write(f"\n{counts[i][0]},{counts[i][1]}")

print("Wrote failed_counts.txt")
print(f"Elapsed: {end-start} seconds")
