#! /usr/bin/env python

import irc.client
import sys


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


def main():
    if len(sys.argv) != 5:
        print("Usage: send_irc_message <server[:port]> <nickname> <target> <message>")
        print("\ntarget is a nickname or a channel.")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    nickname = sys.argv[2]
    target = sys.argv[3]
    message = sys.argv[4]

    c = IRCCat(target, message)
    try:
        c.connect(server, port, nickname)
    except irc.client.ServerConnectionError as x:
        print(x)
        sys.exit(1)
    c.start()

if __name__ == "__main__":
    main()
