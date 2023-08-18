# Dynamic S3 Bucket Creation and Contents Upload

## Overview
Amazon S3 is a scalable, object storage service allowing users to store and retrieve data from anywhere on the web. However, creating and configuring S3 buckets can involve multiple steps. This project automates these tasks and offers a user-friendly way to create versioned S3 buckets and upload contents.

## Features
* **Bucket Name Availability Check**: The Python script interacts with AWS to verify whether an inputted bucket name is available to use. The script uses `s3.head_bucket` to determine if the bucket name is already in use.
* **Dynamic Bucket Creation**: If the bucket name is available, Terraform is used to dynamically create the S3 Bucket in the specified AWS region.
* **Enable Versioning**: The created bucket is configured with versioning enabled. This allows users to track changes and easily revert to prior versions.
* **Upload Directory Contents**: Contents of a specified local directory are automatically uploaded to the newly created S3 bucket.
* **List Uploaded Files**: After directory contents are uploaded, the successfully uploaded files are listed to provide users with a confirmation of the successful upload process. 

## Prerequisites
Before running the script, ensure you have the following prerequisites set up properly:
1. AWS CLI: Install and configure the AWS Command Line Interface (CLI) with valid credentials. Find out more here: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

2. Terraform: Install Terraform on your machine. Find out more here: [Terraform Installation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

## Getting Started

1. Clone the repository to your local machine:
  ```bash
  git clone https://github.com/edmundj0/dynamic-s3-bucket-creation.git && cd dynamic-s3-bucket-creation
  ```

2. Install the required Python packages:
  ```bash
  pip install boto3
  ```

## Usage
1. Open a terminal and navigate to the project directory
2. Input desired files into the directory, /directory_to_upload. Some example files are already provided.
3. Run the Python Script:
   ```bash
   python dynamic_s3_bucket_creation.py
   ```
4. Follow the prompt and input desired S3 bucket name

![image](https://github.com/edmundj0/dynamic-s3-bucket-creation/assets/102005831/918d5024-554d-47e4-a9f5-2fd1bccfe719)



5. The script will check if the bucket name is available, create the bucket using Terraform if available, and upload contents from the specified directory. User must input "yes" into the terminal when Terraform prompts the user to confirm the specified action.


![image](https://github.com/edmundj0/dynamic-s3-bucket-creation/assets/102005831/f3fa3629-2587-45fa-88b4-d33417c19fce)


## Terraform Configuration

The Terraform script create_bucket.tf in the project directory configures the creation of the S3 bucket:
* AWS region: The region attribute in the provider block specifies the AWS region where the S3 bucket will be created.
* Versioning: The versioning block enables versioning for the S3 bucket.
