import pandas as pd
import numpy as np
import glob
import os
import time

# Start the timer
start_time = time.time()

# Define file names
excel_file = 'sample_dataset.xlsx'  # Input Excel file
output_pdf = 'PDF_sample.csv'        # Output PDF file
output_csv = 'NORM_sample.csv'       # Output normalized CSV

# Define protocols, flags, and services
protocol_types = ['tcp', 'udp', 'icmp', 'arp']
flags = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'RSTRH', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH', 'SHR']
services = ['aol', 'http_443', 'http_8001', 'http_2784', 'domain_u', 'ftp_data', 'auth', 'bgp', 
            'courier', 'tftp_u', 'uucp_path', 'csnet_ns', 'ctf', 'daytime', 'time', 'discard', 
            'domain', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'gopher', 'harvest', 
            'hostnames', 'http', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 
            'link', 'login', 'smtp', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 
            'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 
            'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'sql_net', 
            'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tim_i', 'urh_i', 'urp_i', 
            'uucp', 'ftp', 'vmnet', 'whois', 'X11', 'Z39_50']

# Read dataset from Excel file
print(f'Start processing the file: {excel_file}')
raw_data = pd.read_excel(excel_file, header=None)

# Calculate probabilities for protocol type
protocol_counts = raw_data[0].value_counts()
protocol_probs = protocol_counts / len(raw_data)

# Replace protocol types with their probabilities
raw_data[0] = raw_data[0].replace(protocol_probs.index, protocol_probs.values)

# Calculate probabilities for flags
flag_counts = raw_data[4].value_counts()
flag_probs = flag_counts / len(raw_data)

# Replace flag values with their probabilities
raw_data[4] = raw_data[4].replace(flag_probs.index, flag_probs.values)

# Calculate probabilities for services
service_counts = raw_data[1].value_counts()
service_probs = service_counts / len(raw_data)

# Replace service values with their probabilities
raw_data[1] = raw_data[1].replace(service_probs.index, service_probs.values)

# Save the modified data to a CSV file
raw_data.to_csv(output_pdf, index=False, header=False)
print(f'---> Currently generated is: {output_pdf}')

# Start normalization
matrix_normalized = pd.DataFrame()

# Normalize each column using Min-Max normalization
for col in raw_data.columns:
    # Convert the column to numeric, forcing errors to NaN
    selected_column = pd.to_numeric(raw_data[col], errors='coerce')
    
    maximum = selected_column.max()
    minimum = selected_column.min()
    
    # Check if the maximum is greater than 1
    if maximum > 1:
        normalized_column = (selected_column - minimum) / (maximum - minimum)
    else:
        normalized_column = selected_column  # Do not normalize

    matrix_normalized[col] = normalized_column

# Write the normalized data to a CSV file
matrix_normalized.to_csv(output_csv, index=False)
print(f'==> Finished is: {output_csv}')

# Execution complete
# Calculate total execution time
end_time = time.time()
execution_time = end_time - start_time

print(f'Total execution time is: {execution_time:.6f} seconds')
