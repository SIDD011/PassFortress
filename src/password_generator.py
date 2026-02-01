import random
import string
import math
import csv
import sys

# -----------------------------
# Generate Random Password
# -----------------------------
def generate_password(length=12):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# -----------------------------
# Calculate Entropy
# -----------------------------
def calculate_entropy(password):
    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    entropy = math.log2(charset_size ** len(password))
    return round(entropy, 2)

# -----------------------------
# Strength Classification
# -----------------------------
def classify_strength(entropy):
    if entropy < 28:
        return "Extremely Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

# -----------------------------
# Crack Time Estimation
# -----------------------------
def crack_time(entropy, guesses_per_second):
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds/60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds/3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds/86400)} days"
    else:
        return f"{int(seconds/31536000)} years"

# -----------------------------
# Main Program
# -----------------------------
if len(sys.argv) < 2:
    print("Usage: python password_generator.py <length>")
    sys.exit()

length = int(sys.argv[1])


password = generate_password(length)

def meets_policy(password):
    return (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)
    )

while not meets_policy(password):
    password = generate_password(length)

entropy = calculate_entropy(password)
strength = classify_strength(entropy)

low = crack_time(entropy, 1e3)
medium = crack_time(entropy, 1e6)
high = crack_time(entropy, 1e9)
massive = crack_time(entropy, 1e12)

print("\nGenerated Password:", password)
print("Entropy:", entropy)
print("Strength:", strength)
print("Crack Time Estimates:")
print("1e3/sec:", low)
print("1e6/sec:", medium)
print("1e9/sec:", high)
print("1e12/sec:", massive)

# -----------------------------
# Save to CSV
# -----------------------------
file_exists = False

try:
    with open("password_strength_results.csv", "r"):
        file_exists = True
except FileNotFoundError:
    file_exists = False

with open("../outputs/password_strength_results.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "password",
            "length",
            "entropy_bits",
            "strength",
            "low_1e3_per_sec",
            "medium_1e6_per_sec",
            "high_1e9_per_sec",
            "massive_1e12_per_sec"
        ])

    writer.writerow([
        password, length, entropy, strength, low, medium, high, massive
    ])


print("\nSaved to password_strength_results.csv")
