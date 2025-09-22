# lab2-2_starter.py

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

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":
    ips = []
    lines_read = 0
    with open(LOGFILE, "r") as f:
        for line in f:
            lines_read += 1
            if ip_parse(line.strip()) is not None:
                ips.append(ip_parse(line.strip()))
                

    print(f"Lines read: {lines_read}")
    print(f"Uniques IPs: {len(set(ips))}")
    print(f"First 10 IPs: {sorted(list(set(ips)))[:10]}") #sorted() for numbers .sort() for ips