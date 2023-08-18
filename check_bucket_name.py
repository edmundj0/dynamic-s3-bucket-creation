import boto3, subprocess, concurrent.futures, os

def is_bucket_name_available(bucket_name):
    try:
        s3 = boto3.client('s3')
        response = s3.head_bucket(Bucket=bucket_name)
        return False  # Bucket exists, so name not available
    except (s3.exceptions.NoSuchBucket, s3.exceptions.ClientError) as e:
        return True # Bucket doesn't exist, so name available

def run_terraform_apply(bucket_name):
    try:
        subprocess.run(f"TF_VAR_bucket_name={bucket_name} terraform apply", shell=True, check=True)
        print('Bucket created.')

        upload_directory_contents(bucket_name)

    except subprocess.CalledProcessError as e:
        print('Error running "terraform apply": ', e)

def upload_directory_contents(bucket_name):
    s3 = boto3.client('s3')
    source_dir = "./directory_to_upload"

    for root, _, files in os.walk(source_dir):
        for file in files:
            local_path = os.path.join(root, file)
            s3_key = os.path.relpath(local_path, source_dir)

            s3.upload_file(local_path, bucket_name, s3_key)
            print(f"Uploaded: {s3_key}")

    # List uploaded files
    response = s3.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        print("Uploaded Files: ")
        for obj in response["Contents"]:
            print(obj['Key'])





def main():
    print("AWS S3 Bucket Name Availability Checker")
    bucket_name = input("Enter S3 bucket name to check: ")

    if is_bucket_name_available(bucket_name):
        print(f"The bucket name '{bucket_name}' is available.")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(run_terraform_apply(bucket_name))


    else:
        print(f"The bucket name '{bucket_name}' is not available.")

if __name__ == "__main__":
    main()
