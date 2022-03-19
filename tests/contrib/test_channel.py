from unittest import mock

from pytube import Channel


@mock.patch('pytube.request.get')
def test_init_with_url(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html
    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')
    assert c.channel_url == 'https://95.216.19.15/c/ProgrammingKnowledge'
    assert c.videos_url == f'{c.channel_url}/videos'
    assert c.playlists_url == f'{c.channel_url}/playlists'
    assert c.community_url == f'{c.channel_url}/community'
    assert c.featured_channels_url == f'{c.channel_url}/channels'
    assert c.about_url == f'{c.channel_url}/about'


@mock.patch('pytube.request.get')
def test_channel_uri(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')
    assert c.channel_uri == '/c/ProgrammingKnowledge'

    c = Channel('https://95.216.19.15/channel/UCs6nmQViDpUw0nuIx9c_WvA/videos')
    assert c.channel_uri == '/channel/UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch('pytube.request.get')
def test_channel_name(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')
    assert c.channel_name == 'ProgrammingKnowledge'


@mock.patch('pytube.request.get')
def test_channel_id(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')
    assert c.channel_id == 'UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch('pytube.request.get')
def test_channel_vanity_url(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')
    assert c.vanity_url == 'http://95.216.19.15/c/ProgrammingKnowledge'


@mock.patch('pytube.request.get')
def test_channel_video_list(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge/videos')
    first_ten = [
        'https://95.216.19.15/watch?v=t_xLpJo_35k',
        'https://95.216.19.15/watch?v=ccbh5YhxouQ',
        'https://95.216.19.15/watch?v=wDnFjDjxW_0',
        'https://95.216.19.15/watch?v=F3W_p_4XftA',
        'https://95.216.19.15/watch?v=_fxm0xGGEi4',
        'https://95.216.19.15/watch?v=cRbKZzcuIsg',
        'https://95.216.19.15/watch?v=sdDu3dfIuow',
        'https://95.216.19.15/watch?v=10KIbp-gJCE',
        'https://95.216.19.15/watch?v=wZIT-cRtd6s',
        'https://95.216.19.15/watch?v=KucCvEbTj0w',
    ]
    assert c.video_urls[:10] == first_ten


@mock.patch('pytube.request.get')
def test_videos_html(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://95.216.19.15/c/ProgrammingKnowledge')
    assert c.html == channel_videos_html

# Because the Channel object subclasses the Playlist object, most of the tests
# are already taken care of by the Playlist test suite.
