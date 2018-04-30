# krbauth.py
Python wrapper module around `kinit` for simple Kerberos authentication.

## Pre-requisites

You must have your machine configured as a _Kerberos_ user. For debian based machines such as Ubuntu, this would involve installing the `krb5-user` package, and configuring the `krb5.conf` file.

## Usage

It can be run as a script from the command-line. The usage help is shown below.
```console
sumit@HAL9000:~/krbauth.py$ python3 krbauth.py -h
usage: krbauth.py [-h] [-u USERNAME] [-p PASSWORD] [-r REALM] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Kerberos username
  -p PASSWORD, --password PASSWORD
                        Kerberos password
  -r REALM, --realm REALM
                        Kerberos REALM
  -q, --quiet           Quiet mode
```

You can also import and use the `krbauth` function directly in your Python program like the following. It returns a boolean value, signifying whether the login was successful or not.
```python
>>> import krbauth
>>> krbauth.krbauth('username', 'password')
True
```
