"""Get list of IP addresses from AWS instances that match a tag."""
import argparse
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='AWS IP addresses given a tag.')
    parser.add_argument('tag_id', help='AWS tag value')
    args = parser.parse_args()

    aws2_ec2_instance_ip_query = (
        'aws2 ec2 describe-instances | '
        'jq \'.Reservations[] | .Instances[] | '
        '(.Tags | { "iname": ( map ( select(.Value | '
        'contains("%s")))[] | .Value ) } ) + '
        '( { "ip": ( .NetworkInterfaces[].PrivateIpAddress) } )\' |'
        ' jq -s . | grep ip | gawk \'/\"(.*)\"/{print $2}\' | tr -d \"' % (
            args.tag_id))
    out = subprocess.check_output(aws2_ec2_instance_ip_query)
    print(out)
