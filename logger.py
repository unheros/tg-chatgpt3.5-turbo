import logging


def setup_logging() -> None:
    """
        Setup file & stream logging
    """
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    logging.getLogger("aiogram.utils.chat_action").setLevel(logging.WARNING)

    logging.basicConfig(
        format="%(levelname)-8s %(asctime)s[%(name)s:%(lineno)d] %(message)s",
        datefmt="[%d/%m|%H:%M:%S]",
        level=logging.DEBUG,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("debug.log", "a")
        ]
    )
