import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        try:
            logging.info(f"Syncing folder {folder} to {aws_bucket_url}")
            command = f"aws s3 sync {folder} {aws_bucket_url}"
            os.system(command)
            logging.info(f"Successfully synced {folder} to {aws_bucket_url}")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        try:
            logging.info(f"Syncing {aws_bucket_url} to folder {folder}")
            command = f"aws s3 sync {aws_bucket_url} {folder}"
            os.system(command)
            logging.info(f"Successfully synced {aws_bucket_url} to {folder}")
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    