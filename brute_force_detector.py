from collections import Counter

with open("../logs/test_log.txt") as f:
    ips = [line.strip() for line in f]

count = Counter(ips)

for ip, attempts in count.items():
    if attempts > 3:
        print(f"Possible brute force attack from {ip} ({attempts} attempts)")