import boto3, subprocess, concurrent.futures

def is_bucket_name_available(bucket_name):
    try:
        s3 = boto3.client('s3')
        response = s3.head_bucket(Bucket=bucket_name)
        return False  # Bucket exists, so name not available
    except (s3.exceptions.NoSuchBucket, s3.exceptions.ClientError) as e:
        return True # Bucket exists, so name available

def run_terraform_apply(bucket_name):
    try:
        subprocess.run(f"TF_VAR_bucket_name={bucket_name} terraform apply", shell=True, check=True)
        print('Completed')
    except subprocess.CalledProcessError as e:
        print('Error running "terraform apply": ', e)

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
