import pytest
from IPNBRenderer.youtube import render_youtube_video
from IPNBRenderer.custom_exception import InvalidURLException


class TestYTVideoRenderer:
    good_url_data = [
        ("https://www.youtube.com/watch?v=CIbJSX-biu0", "success"),
        ("https://youtu.be/CIbJSX-biu0?si=HhCO-34GBZTvLomd", "success"),
        ("https://youtu.be/CIbJSX-biu0?si=HhCO-34GBZTvLomd&t=60", "success"),
    ]

    bad_url_data = [
        (
            "https://www.youtube.com/watch?v=CIbJSX-biu0-abcdef"
        ),  # ID is more than 11 characters raise an exception
        ("https://www.youtube.com/watch?v=CIbJSX-biu0&t"),  # no time after &t
        ("https://www.youtube.com/watch?v=CIbJSX-biu0&t==60s"),
        (
            "https://www.youtube.com/watch?v==CIbJSX-biu0"
        ),  # ID is more than 11 characters raise an exception
    ]

    @pytest.mark.parametrize("url, response", good_url_data)
    def test_yt_render_good(self, url, response):
        assert render_youtube_video(url) == response

    @pytest.mark.parametrize("url", bad_url_data)
    def test_yt_render_bad(self, url):
        with pytest.raises(InvalidURLException):
            render_youtube_video(url)
