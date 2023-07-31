import os
import subprocess
import boto3
import datetime

# PostgreSQL configuration
pg_user = 'nitish'
pg_password = 'nitish@123'
pg_host = '13.200.58.238'
pg_port = '5432'
pg_dbname = 'testdb'

# AWS S3 configuration
bucket_name = 'postgresssql'
s3_folder = 's3://postgresssql/pgbk/'  # You can set a folder path within the bucket
s3_key = s3_folder + 'backup_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.sql'

# Backup PostgreSQL database to a file
backup_file = 'backup.sql'
pg_dump_command = f'pg_dump -U {pg_user} -h {pg_host} -p {pg_port} -d {pg_dbname} > {backup_file}'
subprocess.run(pg_dump_command, shell=True, check=True)

# Upload the backup file to S3
s3 = boto3.client('s3')
s3.upload_file(backup_file, bucket_name, s3_key)

# Clean up the local backup file
os.remove(backup_file)

print(f"Backup successfully created and uploaded to S3: {s3_key}")
