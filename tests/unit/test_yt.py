import pytest
from IPNBRenderer.youtube import get_time_info
from IPNBRenderer.custom_exception import InvalidURLException

good_url_data = [
    ("https://www.youtube.com/watch?v=CIbJSX-biu0", 0),
    ("https://youtu.be/CIbJSX-biu0?si=HhCO-34GBZTvLomd", 0),
    ("https://youtu.be/CIbJSX-biu0?si=HhCO-34GBZTvLomd&t=60", 60),
]

bad_url_data = [
    (
        "https://www.youtube.com/watch?v=CIbJSX-biu0-abcdef"
    ),  # ID is more than 11 characters raise an exception
    ("hhttps://www.youtube.com/watch?v=CIbJSX-biu0&t"),  # no time after &t
    ("https://www.youtube.com/watch?v=CIbJSX-biu0&t==60s"),
    (
        "https://www.youtube.com/watch?v==CIbJSX-biu0"
    ),  # ID is more than 11 characters raise an exception
]


@pytest.mark.parametrize("url, response", good_url_data)
def test_get_time_info(url, response):
    assert get_time_info(url) == response


@pytest.mark.parametrize("url", bad_url_data)
def test_get_time_info_failed(url):
    with pytest.raises(InvalidURLException):
        get_time_info(url)
