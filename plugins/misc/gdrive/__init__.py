# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

import os


class Config:
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID")
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET")
    G_DRIVE_PARENT_ID = os.environ.get("G_DRIVE_PARENT_ID")
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK")
    G_DRIVE_IS_TD = bool(os.environ.get("G_DRIVE_IS_TD"))
