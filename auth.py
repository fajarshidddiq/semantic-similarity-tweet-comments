import subprocess

credentials = (
    "credentials.txt"  # NOTE: Change this to the path of your credentials file
)
process = subprocess.Popen(
    [
        "twscrape",
        "add_accounts",
        credentials,
        "username:password:email:email_password:_:_",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
stdout, stderr = process.communicate()

if stderr:
    print(stderr.decode("utf-8"))
else:
    print(stdout.decode("utf-8"))


process = subprocess.Popen(
    ["twscrape", "login_accounts"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
stdout, stderr = process.communicate()
if stderr:
    print(stderr.decode("utf-8"))
else:
    print(stdout.decode("utf-8"))
