def setup_aws_creds():
    """
    Set up AWS credentials for local development.
    """
    print ("Setting up AWS credentials for local development...")
    # import os
    # from pathlib import Path

    # # Define the path to the credentials file
    # home = str(Path.home())
    # aws_credentials_path = os.path.join(home, ".aws", "credentials")

    # # Create the .aws directory if it doesn't exist
    # os.makedirs(os.path.dirname(aws_credentials_path), exist_ok=True)

    # # Write the AWS credentials to the file
    # with open(aws_credentials_path, "w") as f:
    #     f.write("[default]\n")
    #     f.write("aws_access_key_id=YOUR_ACCESS_KEY\n")
    #     f.write("aws_secret_access_key=YOUR_SECRET_KEY\n")