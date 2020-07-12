## Serverless sample

- configure credential

```shell
# before setup(Doesn't support SSO) IAM USER credentials
$ serverless config credentials --provider aws --key ABCDEFGHIJKLMNOPQRST --secret ABCDEFGHIJKLMNOPQRSTUVWXY/ABCDEFGHIJK
```

- create template

```shell
$ serverless create --template aws-python --path hello-world-python

$ cd hello-world-python

```

- deploy

```shell
# edit handler.py and deploy
$ serverless deploy -v

Serverless: Stack update finished...
Service Information
service: hello-world-python
stage: dev
region: ap-northeast-1
stack: hello-world-python-dev
resources: 6
api keys:
  None
endpoints:
  None
functions:
  hello: hello-world-python-dev-hello
layers:
  None

# delete
$ serverless remove
```

- invoke function

```shell
$ serverless invoke -f hello -l
"hello-world"
--------------------------------------------------------------------
START RequestId: 3bf7e1aa-3645-4358-a20e-526f53f8911f Version: $LATEST
hi !
END RequestId: 3bf7e1aa-3645-4358-a20e-526f53f8911f
REPORT RequestId: 3bf7e1aa-3645-4358-a20e-526f53f8911f      Duration: 0.40 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 35 MB

```

- update and invoke

```shell
# update
$ serverless deploy -v

# log ouput is "first update"
$ serverless invoke -f hello -l
"hello-world"
--------------------------------------------------------------------
START RequestId: 0bb35848-c99a-42f9-8460-bfe0f27e7afb Version: $LATEST
first update
END RequestId: 0bb35848-c99a-42f9-8460-bfe0f27e7afb
REPORT RequestId: 0bb35848-c99a-42f9-8460-bfe0f27e7afb      Duration: 0.28 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 35 MB  Init Duration: 0.66 ms

# only function deploy
$ serverless deploy function -f hello
Serverless: Packaging function: hello...
Serverless: Excluding development dependencies...
Serverless: Uploading function: hello (944 B)...
Serverless: Successfully deployed function: hello
Serverless: Successfully updated function: hello

# log ouput is "second update"
$ serverless invoke -f hello -l
"hello-world"
--------------------------------------------------------------------
START RequestId: fa88f44a-c945-4dc2-a664-df1f3456dc33 Version: $LATEST
second update
END RequestId: fa88f44a-c945-4dc2-a664-df1f3456dc33
REPORT RequestId: fa88f44a-c945-4dc2-a664-df1f3456dc33      Duration: 0.39 ms       Billed Duration: 100 ms Memory Size: 1024 MB    Max Memory Used: 35 MB  Init Duration: 0.72 ms
```
