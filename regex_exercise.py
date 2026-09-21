import re

#____________________________TASK_1____________________________

print("____TASK_1____")

log_lines = [
    "2024-01-15 10:02:11 INFO Server started on port 8080",
    "2024-01-15 10:03:47 ERROR Failed to connect to database",
    "2024-01-16 08:15:00 WARNING Disk usage at 85%",
    "2024-01-16 14:22:39 ERROR Timeout while fetching https://example.com/api",
    "2024-01-17 09:00:05 INFO User admin logged in from 192.168.1.10",
    "2024-01-17 11:41:18 DEBUG Cache cleared successfully",
    "2024-01-18 03:12:56 ERROR Connection refused from 192.168.1.55",
    "2024-01-18 23:59:02 INFO Backup completed in 42s",
]

lines_2024_01_16 = [
    line for line in log_lines if re.match(r"^2024-01-16", line)]


error_or_warning = [
    line for line in log_lines if re.search(r"\b(ERROR|WARNING)\b", line)]

ipv4_addresses = [
    ip
    for line in log_lines
    for ip in re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)]

ending_in_seconds = [
    line for line in log_lines if re.search(r"\d+s$", line)]

lines_with_url = [
    line for line in log_lines if re.search(r"https?://", line)]

log_format_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]+ .+"
is_first_line_valid = bool(re.fullmatch(log_format_pattern, log_lines[0]))



print("1. Lines logged on 2024-01-16:")
for line in lines_2024_01_16:
    print("  ", line)

print("\n2. Lines containing ERROR or WARNING:")
for line in error_or_warning:
    print("  ", line)

print("\n3. Extracted IPv4 addresses:")
for ip in ipv4_addresses:
    print("  ", ip)

print("\n4. Lines ending in seconds:")
for line in ending_in_seconds:
    print("  ", line)

print("\n5. Lines containing URLs:")
for line in lines_with_url:
    print("  ", line)

print("\n6. Format validation (log_lines[0]):")
print("   Matches expected format:", is_first_line_valid)


#____________________________TASK_2____________________________

def reverse_complement(sequence: str) -> str:
    return sequence.translate(str.maketrans("ATCGatcg", "TAGCtagc"))[::-1]


class SequencingRead:
    def __init__(self, read_id: str, sequence: str):
        self.read_id = read_id
        self.sequence = sequence

    def matches_mid_pair(self, forward_mid: str, reverse_mid: str) -> bool:
        rev_comp = reverse_complement(reverse_mid)
        return bool(re.search(f"^{re.escape(forward_mid)}.*{re.escape(rev_comp)}$", self.sequence))

    def trim_mid_pair(self, forward_mid: str, reverse_mid: str) -> str | None:
        rev_comp = reverse_complement(reverse_mid)
        match = re.search(f"^{re.escape(forward_mid)}(.*){re.escape(rev_comp)}$", self.sequence)
        return match.group(1) if match else None

    def describe(self) -> str:
        return f"SequencingRead {self.read_id} ({len(self.sequence)} bp)"


print("___TASK_2___")
r1 = SequencingRead("demo_1", "AGCTTCGA" + "N" * 20 + reverse_complement("TGCAGGTC"))
print(r1.describe())
print(r1.matches_mid_pair("AGCTTCGA", "TGCAGGTC"))  # True
print(r1.matches_mid_pair("CGATCGAT", "GCTAGCTA"))  # False
print(r1.trim_mid_pair("AGCTTCGA", "TGCAGGTC"))     # 20 x "N"



