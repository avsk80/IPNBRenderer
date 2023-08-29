from ensure import ensure_annotations
from IPNBRenderer.logger import logger
from IPNBRenderer.custom_exception import InvalidURLException
from py_youtube import Data
from IPython import display


@ensure_annotations
def get_time_info(url: str) -> int:
    def _verify_videoIDlen(videoID: str, __expected_len=11):
        if len(videoID) != __expected_len:
            raise InvalidURLException(
                f"Invalid URL: {url}, expected length of videoID is {__expected_len}"
            )

    try:
        split_val = url.split("=")
        if len(split_val) > 3:
            raise InvalidURLException
        if "watch" in url:
            if "&t" in url:
                vid_id, time = split_val[-2][:-2], int(split_val[-1][:-1])
                _verify_videoIDlen(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = split_val[-1], 0
                _verify_videoIDlen(vid_id)
                logger.info(f"video starts at: {time}")
                return time
        else:
            if "=" in url and "?t" in url:
                vid_id, time = split_val[0].split("/")[-1][:-2], int(split_val[-1])
                _verify_videoIDlen(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = url.split("/")[-1], 0
                _verify_videoIDlen(vid_id)
                logger.info(f"video starts at: {time}")
                return time
    except Exception:
        raise InvalidURLException


@ensure_annotations
def render_youtube_video(url: str, width: int = 780, height: int = 160) -> str:
    try:
        if url is None:
            raise InvalidURLException("URL cannot be None")
        data = Data(url).data()
        if data["publishdate"] is not None:
            time = get_time_info(url)
            vid_ID = data["id"]
            embed_url = f"https://www.youtube.com/embed/{vid_ID}/?start={time}"
            logger.info(f"embed_url = {embed_url}")
            iframe = f"""
            <iframe width="{width}" height="{height}" 
            src="{embed_url}" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; 
            clipboard-write; encrypted-media; 
            gyroscope; picture-in-picture; 
            web-share" allowfullscreen>
            </iframe>
            """
            display.display(display.HTML(iframe))
            return "success"
    except Exception as e:
        raise e
