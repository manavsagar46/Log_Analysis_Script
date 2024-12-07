from collections import Counter

def process_logs(log_file_path, failed_login_threshold):
    # Initializing counters
    ip_counts = Counter()
    endpoint_counts = Counter()
    failed_logins = Counter()

    try:
        with open(log_file_path, "r") as file:
            logs = file.readlines()  # Reading all lines
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{log_file_path}' not found.")

    # Processing of logs
    for line in logs:
        # Count requests per IP
        ip = line.split()[0]  # Extracting the IP 
        ip_counts[ip] += 1

        # Frequently accessed endpoints
        if '"' in line:
            try:
                endpoint = line.split('"')[1].split()[1]  # Extract endpoint
                endpoint_counts[endpoint] += 1
            except IndexError:
                continue  # Skip malformed lines

        # Detecting suspicious activity
        if "401" in line or "Invalid credentials" in line:  # Failure indications
            failed_logins[ip] += 1

    # Results
    sorted_ips = ip_counts.most_common()
    most_accessed_endpoint = endpoint_counts.most_common(1)
    suspicious_ips = {ip: count for ip, count in failed_logins.items() if count > failed_login_threshold}

    return sorted_ips, most_accessed_endpoint, suspicious_ips
