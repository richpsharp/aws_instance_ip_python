"""Get list of IP addresses from AWS instances that match a tag."""
import argparse
import json
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='AWS IP addresses given a tag.')
    parser.add_argument('tag_id', help='AWS tag value')
    args = parser.parse_args()

    out = subprocess.check_output('aws2 ec2 describe-instances')
    out_json = json.loads(out)
    for reservation in out_json['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Value'] == args.tag_id:
                    print(instance['InstanceId'])
                    print(instance['PrivateIpAddress'])
                    break
