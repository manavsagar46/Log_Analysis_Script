import sys
import os
import csv
from log_processor import process_logs
from config import LOG_FILE_PATH, FAILED_LOGIN_THRESHOLD

# Ensure the 'output' directory exists
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process logs
try:
    sorted_ips, most_accessed_endpoint, suspicious_ips = process_logs(LOG_FILE_PATH, FAILED_LOGIN_THRESHOLD)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

# Showing Results
print("IP Address           Request Count")
for ip, count in sorted_ips:
    print(f"{ip:<20} {count}")

if most_accessed_endpoint:
    print(f"\nMost Frequently Accessed Endpoint:\n{most_accessed_endpoint[0][0]} "
          f"(Accessed {most_accessed_endpoint[0][1]} times)")
else:
    print("\nNo valid endpoints found in the log file.")

print("\nSuspicious Activity Detected:")
print(f"{'IP Address':<20} {'Failed Login Attempts':<5}")
for ip, count in suspicious_ips.items():
    print(f"{ip:<20} {count}")

# Write results to CSV
csv_path = os.path.join(output_dir, "log_analysis_results.csv")
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # IP Requests
    writer.writerow(["=== IP Address Analysis ==="])
    writer.writerow(["IP Address", "Request Count"])
    writer.writerows(sorted_ips)
    writer.writerow([])

    # Most Accessed Endpoint
    writer.writerow(["=== Most Accessed Endpoint ==="])
    writer.writerow(["Most Accessed Endpoint", "Access Count"])
    writer.writerow([most_accessed_endpoint[0][0], most_accessed_endpoint[0][1]])
    writer.writerow([])

    # Suspicious Activity
    writer.writerow(["=== Suspicious Activity ==="])
    writer.writerow(["IP Address", "Failed Login Count"])
    writer.writerows(suspicious_ips.items())
    writer.writerow([])
