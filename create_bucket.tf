provider "aws" {
    region = "us-west-2"
}

resource "aws_s3_bucket" "my-bucket" {
    bucket = "insert-bucket-name-here" #change name here
    acl = "private"
    versioning {
        enabled = true
    }
}
