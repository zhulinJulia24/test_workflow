
import oss2
import fire
import os
from oss2.credentials import EnvironmentVariableCredentialsProvider
   
def get_file(accesskey: str, accesssecret: str, bucketname: str, filepath: str):
    os.environ['OSS_ACCESS_KEY_ID'] = accesskey
    os.environ['OSS_ACCESS_KEY_SECRET'] = accesssecret
    auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
    bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', bucketname)
    bucket.get_object_to_file(filepath, 'ALL_LOGS_2024-06-20_INFO.log')

if __name__ == '__main__':
    fire.Fire()