import oss2

from .secrets import my_key, my_secret

internal_host = "oss-cn-zhangjiakou.aliyuncs.com"

auth = oss2.Auth(my_key, my_secret)

bucket = oss2.Bucket(auth, internal_host, "xyc-learn-oss")

for o in oss2.ObjectIterator(bucket):
    print(o)