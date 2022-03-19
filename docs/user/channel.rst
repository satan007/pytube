.. _channel:

Using Channels
==============

This guide will walk you through the basics of working with pytube Channels.

Creating a Channel
------------------

Using pytube to interact with channels is similar to interacting with playlists. 
Begin by importing the Channel class::

    >>> from pytube import Channel

Now let's create a channel object. You can do this by initializing the object with a channel URL::

    >>> c = Channel('https://95.216.19.15/c/ProgrammingKnowledge')

Or you can create one from a link to the channel's video page::

    >>> c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')

Now, we have a :class:`Channel <pytube.Channel>` object called ``c`` that we can do some work with.

Interacting with a channel
--------------------------

Fundamentally, a Channel object is just a container for YouTube objects.

If, for example, we wanted to download all of the videos created by a channel, we would do the following::

    >>> print(f'Downloading videos by: {c.channel_name}')
    Downloading videos by: ProgrammingKnowledge
    >>> for video in c.videos:
    >>>     video.streams.first().download()

Or, if we're only interested in the URLs for the videos, we can look at those as well::

    >>> for url in c.video_urls[:3]:
    >>>     print(url)
    ['https://95.216.19.15/watch?v=tMqMU1U2MCU',
    'https://95.216.19.15/watch?v=YBfInrtWq8Y',
    'https://95.216.19.15/watch?v=EP9WrMw6Gzg']

And that's basically all there is to it!
