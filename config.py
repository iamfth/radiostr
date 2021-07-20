"""
RadioPlayerV2, Telegram Voice Chat Userbot
Copyright (C) 2021  Asm Safone <https://t.me/asmsafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1747566924")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 7373180))
    CHAT = int(os.environ.get("CHAT", "-508798693"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-508798693")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://22253.live.streamtheworld.com/PRAMBORS_FM.mp3?listening-from-radio-garden=1626778508981")
    API_HASH = os.environ.get("API_HASH", "b8ca5820cf7415918d138cc952e927ca")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1903492912:AAFdopjZXv1v4BEYZZDAVW__XbSWlVH7mMI") 
    SESSION = os.environ.get("SESSION_STRING", "BQAi53JQ6NTMGUwqH5aKHhOeYY0GS7eth30nZvqd3407wKokinddmEh6bfwKbuKCGObS6ICMQPvA_Dd36gnr1RMBzhrZvf19ZtJwobWggoWRgAMnuR5wfDHS7wbDLZU5jAzQfZJ8PWNflB8oF3tF2mKlSkCg6uoILop3KT-FdLpyydeWSZzuZsALbCvKYzuui7d7mCI87YklFjKX1aB5TsIbOFSY8r9GON8rYPEBdnHvdnRGrWtVClTd4H_H7m9jt2I5pOdi2aHCpt2eRYj0wQPowqo0Gn7MgfqgumjoC0J-Bsg9o2tqGI_YYV33upBOvcaNw4V3Q0_xdxp-p9fvjddEZ4yWDAA")

