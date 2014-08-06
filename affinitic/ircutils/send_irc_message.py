#! /usr/bin/env python

import irc.client
import sys
import argparse


class IRCCat(irc.client.SimpleIRCClient):
    def __init__(self, target, message):
        irc.client.SimpleIRCClient.__init__(self)
        self.target = target
        self.message = message

    def on_welcome(self, connection, event):
        connection.join(self.target)

    def on_join(self, connection, event):
        self.connection.privmsg(self.target, self.message)
        self.connection.quit("quit")

    def on_disconnect(self, connection, event):
        sys.exit(0)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', required=True)
    parser.add_argument('-p', '--port', default=6667, type=int)
    parser.add_argument('-n', '--nickname', required=True)
    parser.add_argument('-c', '--channel', required=True)
    parser.add_argument('-m', '--message', required=True)
    return parser.parse_args()


def main():
    args = get_args()

    c = IRCCat(args.channel, args.message)
    try:
        c.connect(args.server, args.port, args.nickname)
    except irc.client.ServerConnectionError as x:
        print(x)
        sys.exit(1)
    c.start()

if __name__ == "__main__":
    main()
