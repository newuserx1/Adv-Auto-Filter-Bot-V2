#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID","28123666"))

API_HASH = os.environ.get("API_HASH","e0a07eff8e5ff1dd72edcac6bb213a42")

BOT_TOKEN = os.environ.get("BOT_TOKEN","5728262830:AAGnyQLgFhvWXq9upNdSZsfUciMsnHACqEU")

DB_URI = os.environ.get("DB_URI","mongodb+srv://prasad:12345@cluster0.cjtzf1k.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("USER_SESSION","BQGtIhIAE-07XFojA3qLwS7HrRiIffmVQFEv5UERxZ5A_W0n4Ruyogq9jlDD1bW8uY1MuhSvDeP10HaoUWv38R5yUc0Ngkzpfv4hi63LS0nljG4OuihGVleRz8dwrvWrt7PZChCkGj_24jMiSvLsxJZVY_XLnAXMbifo2dSCWe00cuLjci-ako3C0or7mNqTgIA_gTy_ePHnAeFnb_aPo2AXy-H_vR13rTEhLfzeQKCN68HNupvZ_mgPxFvTICOdpr1v8XTIg66BrQZXUD1tXmGx848njKaG0zMSuhtMS4wmdxS4GkmmmBEjH4Hy-rYxGfImBA3UvjKnVRZxkeu14Gcrcs1mQAAAAAFO9YB4AA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
