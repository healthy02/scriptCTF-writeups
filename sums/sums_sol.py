!pip install pwntools > /dev/null

from pwn import *

HOST = "play.scriptsorcerers.xyz"
PORT = 10124

def solve_locally(nums, ranges):
    """Build prefix sums and answer queries locally (like ./solve)."""
    n = len(nums)
    pref = [0] * (n+1)
    for i in range(1, n+1):
        pref[i] = pref[i-1] + nums[i-1]

    answers = []
    for (l, r) in ranges:
        if l > 0:
            answers.append(pref[r+1] - pref[l])
        else:
            answers.append(pref[r+1])
    return answers

io = remote(HOST, PORT)

nums_line = io.recvline().decode().strip()
nums = list(map(int, nums_line.split()))

n = len(nums)

ranges = []
for _ in range(n):
    line = io.recvline().decode().strip()
    l, r = map(int, line.split())
    ranges.append((l, r))

answers = solve_locally(nums, ranges)

for ans in answers:
    io.sendline(str(ans).encode())

print(io.recvall().decode())
