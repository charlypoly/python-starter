import logging

from app.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s %(levelname)s %(name)s %(message)s")
log = logging.getLogger("app")


def main() -> None:
    log.info("started")


if __name__ == "__main__":
    main()
