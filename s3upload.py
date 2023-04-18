import boto3
import os
 
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='AKIASXBPOSPPUVNKI7PO',
        aws_secret_access_key='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',
        region_name='ap-south-1'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('mysqlbackupq')
 
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
 
if __name__ == "__main__":
    upload_files('/backup/dbbackup/')
