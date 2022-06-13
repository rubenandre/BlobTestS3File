# BlobTestS3File
POC to not expose s3 bucket information when retrieving files to render

## Purpose
- Hide bucket url information that can lead to initial footprinting of other buckets (ex. ProjectX-dev, ProjectX-prod, ...)
- Don't allow 'exploitation' in S3 Pre-signed url even with bad configurations, when the purpose is to provide files.
