"""
pipeline_abdellah.py - Project script (modified example).

Author: Abdellah Boudlal
Date: 2026-03-10

Purpose:
  Confirm the project environment is set up correctly.
  Run this script to log project paths and an extra custom message.

Run as a Module:
  uv run python -m cintel.pipeline_abdellah
"""

import logging
from pathlib import Path

from datafun_toolkit.logger import get_logger, log_header, log_path

LOG: logging.Logger = get_logger("P1", level="DEBUG")

ROOT_DIR: Path = Path.cwd()
DOCS_DIR: Path = ROOT_DIR / "docs"
SRC_DIR: Path = ROOT_DIR / "src"


def main() -> None:
    """Run the modified pipeline."""
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DOCS_DIR", DOCS_DIR)
    log_path(LOG, "SRC_DIR", SRC_DIR)

    LOG.info("Custom modification: logging the src folder path.")
    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("Custom modification by Abdellah Boudlal.")
    LOG.info("========================")
    LOG.info("END main()")


if __name__ == "__main__":
    main()
