from google.cloud import storage

def upload_file_to_bucket(bucket_name, local_file_path, remote_file_name):

    # Instantiate a client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a blob object
    blob = bucket.blob(remote_file_name)

    # Upload the local file to the bucket
    blob.upload_from_filename(local_file_path)

    print(f"File {remote_file_name} has been uploaded to {bucket_name}.")

