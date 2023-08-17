provider "aws" {
    region = "us-west-2"
}

variable "bucket_name" {
    type = string
    default = "test_bucket0"
}

resource "aws_s3_bucket" "my-bucket" {
    bucket = var.bucket_name
    acl = "private"
    versioning {
        enabled = true
    }
}
