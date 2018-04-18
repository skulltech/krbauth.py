#!/usr/bin/env python3

import subprocess
import argparse
import getpass


def krbauth(username, password):
    cmd = ['kinit', username]
    success = subprocess.run(cmd, input=password.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    return not bool(success)


def log(message, quiet):
    if not quiet:
        print('[*] {}'.format(message))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='Kerberos username', type=str)
    parser.add_argument('-p', '--password', help='Kerberos password', type=str)
    parser.add_argument('-r', '--realm', help='Kerberos REALM', type=str)
    parser.add_argument('-q', '--quiet', help='Quiet mode', action='store_true')
    args = parser.parse_args()

    username = args.username or input('[*] Kerberos username: ')
    password = args.password or getpass.getpass('[*] Kerberos password: ')
    if args.realm:
        username = '{}@{}'.format(username, args.realm)

    log('Logging in as {}'.format(username), args.quiet)
    res = krbauth(username, password)
    if res:
        log('Succesfully Logged in!', args.quiet)
        return 0
    else:
        log('Incorrect Login!', args.quiet)
        return 1


if __name__=='__main__':
    main()
