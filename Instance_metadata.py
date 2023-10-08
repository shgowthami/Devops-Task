import requests
import json

def get_aws_ec2_metadata():
    metadata_url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    
    try:
        response = requests.get(metadata_url, timeout=2)
        if response.status_code == 200:
            metadata = response.json()
            return metadata
        else:
            print(f"Failed to retrieve AWS EC2 metadata. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to AWS EC2 metadata service: {e}")
    
    return None

if __name__ == "__main__":
    aws_metadata = get_aws_ec2_metadata()
    if aws_metadata:
        print(json.dumps(aws_metadata, indent=4))
