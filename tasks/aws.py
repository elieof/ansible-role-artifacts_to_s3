import boto3

# client = boto3.client('s3')
# response = client.list_buckets()

# print(response)

s3 = boto3.resource('s3')
object_acl = s3.ObjectAcl('elieof-eoo','/artifacts/projects/autotest_artifacts_to_s3/releases/1.0.0/git_package.zip')
object_acl.put(ACL='authenticated-read')