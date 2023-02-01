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

BOT_TOKEN = os.environ.get("BOT_TOKEN","6029847668:AAEs88Mc2H2Crc5rL_6hqpnEQHdEYMiCMyM")

DB_URI = os.environ.get("DB_URI","mongodb+srv://prasad:12345@cluster0.cjtzf1k.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("USER_SESSION","BQGtIhIAXUlQkaKS54oUVsu4raHrXK7HGDzyY-51LHH7Rt_fc5ypIE10SNMmJ5sFZedBDsq2uhTtkFYcIiSkqDB7c1fuT5LTJXflOMvsaVSN5Z7_vKuuPUsDfhOglJYtZO3LEcZKB9tGsvP2PJubZBHzFut5WQ2NXdNRjnEq2tC67GZapzpaiZtyM1tzcdvyGfsPrtu6pQ4f8DXFH_5Fv02dC-UDPOY6oeI-n0ewK-Me1ZQgkObxEtUetI5QsC8fynG5tTJr74HA6Ul7sELCagMrY58m4JoCqOhc8Vpmeyb12nTOBx06DqGcqihMJgumy-QfmDJI_UYTTgrr6V-BBsXO_1gHuAAAAAFO9YB4AA")

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
