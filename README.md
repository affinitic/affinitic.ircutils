affinitic.ircutils
================

Allow to send irc notification

Usage
-----

```bin/send_irc_message [-h] -s SERVER [-p PORT] -n NICKNAME -c CHANNEL -m MESSAGE```

Example
-------

```bin/send_irc_message -s irc.freenode.net -n alibaba -c '#hellochannel' -m bonjour -p 6667```

Warning
-------

The nickname has to be free (unused).

Don't forget the "#" before the channel.
