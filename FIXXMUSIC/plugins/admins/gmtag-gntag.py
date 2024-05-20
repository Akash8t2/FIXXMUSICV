from FIXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
          " 🤔🤣🛏️🛌",
          " 〽️☀️💀😇",
          " 🏫🏢😔😝",
        ]

TAGMES = [ " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ 🌚** ",
           " **➠ ᴄʜᴜᴘ ᴄʜᴀᴘ sᴏ ᴊᴀ 🙊** ",
           " **➠ ᴘʜᴏɴᴇ ʀᴀᴋʜ ᴋᴀʀ sᴏ ᴊᴀ, ɴᴀʜɪ ᴛᴏ ʙʜᴏᴏᴛ ᴀᴀ ᴊᴀʏᴇɢᴀ..👻** ",
           " **➠ ᴀᴡᴇᴇ ʙᴀʙᴜ sᴏɴᴀ ᴅɪɴ ᴍᴇɪɴ ᴋᴀʀ ʟᴇɴᴀ ᴀʙʜɪ sᴏ ᴊᴀᴏ..?? 🥲** ",
           " **➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ ʏᴇ ᴀᴘɴᴇ ɢғ sᴇ ʙᴀᴀᴛ ᴋʀ ʀʜᴀ ʜ ʀᴀᴊᴀɪ ᴍᴇ ɢʜᴜs ᴋᴀʀ, sᴏ ɴᴀʜɪ ʀᴀʜᴀ 💀** ",
           " **➠ 𝙋𝘼𝙋𝘼 𝙔𝙀 𝘿𝙀𝙅𝙃𝙊 𝘼𝙋𝙉𝙄 𝘽𝙀𝙏𝙄 𝙆𝙊 𝙍𝘼𝘼𝙏 𝘽𝘼𝙍 𝙋𝙃𝙊𝙉𝙀 𝘾𝙃𝘼𝙇𝘼 𝙍𝘼𝙃𝙄 𝙏𝙃𝙄 𝘾𝙃𝘼𝙇 𝘼𝘽 𝙎𝙊𝙅𝘼 𝙎𝙊 𝙎𝙊 𝘾𝙃𝙐𝙋 𝘾𝙃𝘼𝙋 👀** ",
           " **➠ 𝘼𝙍𝙀𝙀 𝙎𝙐𝙉𝙊 𝙅𝙄 𝙎𝙊𝙅𝘼𝙊 𝙆𝘼𝙇 𝙋𝘼𝘿𝙊𝙎𝙄 𝙆𝙄 𝙇𝘼𝘿𝙆𝙄 𝙆𝙀 𝙋𝘼𝙎𝙎 𝘽𝙃𝙄 𝙅𝘼𝙉𝘼 𝙃 𝙉𝘼..?? 😝** ",
           " **➠ 𝙂𝙊𝙊𝘿 𝙉𝙄𝙂𝙃𝙏 𝙅𝙄 𝙎𝙊𝙅𝘼𝙊 𝘼𝘽.. 🙂** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ ᴛᴀᴋᴇ ᴄᴀʀᴇ..?? ✨** ",
           " **➠ 𝘼𝙍𝙀𝙀 𝙔𝙍 𝘿𝙀𝙆𝙃𝙊 𝙅𝙄 𝙍𝘼𝘼𝙏 𝘽𝙃𝘼𝙐𝙏 𝙃𝙊𝙂𝙄 𝙃 𝙈𝘼𝙔 𝙎𝙊𝙉𝙀 𝙅𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝘽𝙔𝙀𝙀?? 🌌** ",
           " **➠ 𝙈𝙐𝙈𝙈𝙔 𝘿𝙀𝙆𝙃𝙊 11 𝘽𝘼𝙅𝙉𝙀 𝙒𝘼𝙇𝙀 𝙃 𝙋𝙀𝙍 𝙔𝙀 𝙆𝘼𝙈𝘽𝙃𝘼𝙆𝙃𝘼𝙏𝙉𝙄 𝙎𝙊 𝙉𝘼𝙃𝙄 𝙍𝘼𝙃𝙄 𝙃 𝙎𝙊 𝙅𝘼𝙊 𝘿𝙀𝙑𝙄 𝘼𝘽 ?? 🕦** ",
           " **➠ 𝙆𝘼𝙇 𝙎𝙐𝘽𝘼𝙃 𝙒𝘼𝙇𝙆 𝙋𝙀 𝙉𝘼𝙃𝙄 𝙅𝘼𝙉𝘼 𝙆𝙔𝘼 𝙎𝙊𝙅𝘼𝙊 𝘽𝘼𝘽𝙔 𝘼𝘽 💀** ",
           " **➠ ʙᴀʙᴜ, ɢᴏᴏᴅ ɴɪɢʜᴛ sᴅ ᴛᴄ..?? 😊** ",
           " **➠ 𝘼𝙍𝙀𝙀 𝙅𝙄 𝙎𝙊𝙅𝘼𝙊 𝙉𝘼𝙃𝙄 𝙏𝙊 𝙆𝙄𝙎𝙎 𝙆𝘼𝙍𝘿𝙐𝙉𝙂𝙄 𝘼𝙋𝙆𝙊** 😇",
           " **➠  𝙃𝙀𝙇𝙇𝙊 𝘽𝙃𝙀𝙉 𝘼𝘽 𝙅𝘼 𝙉𝘼𝙃𝙄 𝙏𝙊 𝙅𝙄𝙎𝙎𝙀 𝙏𝙐𝙈 𝘽𝘼𝘼𝙏 𝙆𝘼𝙍 𝙍𝘼𝙃𝙄 𝙃𝙊 𝙈𝘼𝙔 𝙐𝙎𝙆𝙀 𝙎𝘼𝙏𝙃 𝙎𝙊𝙅𝘼𝙐𝙉𝙂𝙄🌷** ",
           " **➠ 𝘼𝘾𝙃𝘼 𝘼𝘽 𝙆𝘼𝙇 𝘼𝙐𝙉𝙂𝙄 𝙊𝙉𝙇𝙄𝙉𝙀 𝘼𝘽𝙃𝙄 𝙅𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙎𝙊𝙉𝙀 𝘼𝙋 𝙎𝙀 𝘽𝘼𝘼𝙏 𝙆𝘼𝙍𝙆𝙀 𝘼𝘾𝙃𝘼 𝙇𝘼𝙂𝘼 🏵️** ",
           " **➠ ʜᴇʟʟᴏ ᴊɪ ɴᴀᴍᴀsᴛᴇ, ɢᴏᴏᴅ ɴɪɢʜᴛ 🍃** ",
           " **➠ 𝙂𝙊𝙊𝘿 𝙉𝙄𝙂𝙃𝙏 𝙅𝙄 𝘼𝘽 𝙆𝘼𝙇 𝙈𝙄𝙇𝙏𝙀 𝙃 🛌** ",
           " **➠ 𝙂𝙊𝙊𝘿 𝙉𝙄𝙂𝙃𝙏 𝙎𝙊𝙅𝘼𝙊 𝘼𝘽 𝙆𝘼𝙇 𝙎𝘾𝙃𝙊𝙊𝙇 𝙅𝘼𝙉𝘼 𝙃 𝙆𝙄 𝙉𝘼𝙃𝙄..? 🏫** ",
           " **➠ ᴍᴇ ᴊᴀ ʀᴀʜɪ ʀᴏɴᴇ, ɪ ᴍᴇᴀɴ sᴏɴᴇ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ 😁** ",
           " **➠ ᴍᴀᴄʜʜᴀʟɪ ᴋᴏ ᴋᴇʜᴛᴇ ʜᴀɪ ғɪsʜ, ɢᴏᴏᴅ ɴɪɢʜᴛ ᴅᴇᴀʀ ᴍᴀᴛ ᴋʀɴᴀ ᴍɪss, ᴊᴀ ʀʜɪ sᴏɴᴇ 🌄** ",
           " **➠ 𝙂𝙊𝙊𝘿 𝙉𝙄𝙂𝙃𝙏 𝘼𝘽 𝙎𝙊𝙅𝘼𝙊 𝙏𝙄𝙈𝙀 𝘽𝘼𝙃𝙐𝙏 𝙃𝙊𝙂𝙔𝘼 𝙃 𝙊𝙍 𝙃𝘼 𝙋𝙃𝙊𝙉𝙀 𝙈𝙀𝙍𝙀 𝙆𝙊 𝘿𝙊 𝙈𝘼𝙔 𝙇𝙀𝙅𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙆𝘼𝙇 𝙎𝙐𝘽𝘼𝙃 𝙈𝙄𝙇𝙀𝙂𝘼 𝘼𝘽 𝙋𝙃𝙊𝙉𝙀 🤭** ",
           " **➠ ᴛʜᴇ ɴɪɢʜᴛ ʜᴀs ғᴀʟʟᴇɴ, ᴛʜᴇ ᴅᴀʏ ɪs ᴅᴏɴᴇ,, ᴛʜᴇ ᴍᴏᴏɴ ʜᴀs ᴛᴀᴋᴇɴ ᴛʜᴇ ᴘʟᴀᴄᴇ ᴏғ ᴛʜᴇ sᴜɴ... 😊** ",
           " **➠ 𝙋𝘼𝙋𝘼 𝙔𝙀 𝘿𝙀𝙆𝙃𝙊 𝘼𝙋𝙉𝙀 𝘽𝙀𝙏𝙀 𝙆𝙊 𝙍𝘼𝘼𝙏 𝙆𝙀 2 𝘽𝘼𝙅𝙀 𝘽𝙃𝙄 𝙋𝙃𝙊𝙉𝙀 𝘿𝙀𝙆𝙃 𝙍𝘼𝙃𝘼 𝙃 𝙈𝘼𝙍𝙊 𝙄𝙎𝙆𝙊 𝙍𝙐𝙆𝙊 𝙋𝘼𝙋𝘼 𝙈𝘼𝙔 𝘿𝘼𝙉𝘿𝘼 𝙇𝘼𝙏𝙄 𝙃𝙐** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴘʀɪɴᴋʟᴇs sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ 💚** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ, ɴɪɴᴅ ᴀᴀ ʀʜɪ ʜᴀɪ 🥱** ",
           " **➠ ᴅᴇᴀʀ ғʀɪᴇɴᴅ ɢᴏᴏᴅ ɴɪɢʜᴛ 💤** ",
           " **➠ 𝐀𝐑𝐄𝐄 𝐉𝐈 𝐀𝐏𝐏 𝐀𝐏 𝐊𝐎 𝐒𝐔𝐍𝐀 𝐇 𝐊𝐈 𝐍𝐀𝐇𝐈 𝐒𝐎 𝐉𝐀𝐎 𝐑𝐀𝐀𝐓 𝐊𝐄 𝟏𝟏 𝐁𝐀𝐉 𝐑𝐀𝐇𝐄 𝐇 😔** ",
           " **➠ ɪᴛɴɪ ʀᴀᴀᴛ ᴍᴇ ᴊᴀɢ ᴋᴀʀ ᴋʏᴀ ᴋᴀʀ ʀʜᴇ ʜᴏ sᴏɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ 😜** ",
           " **➠ ᴄʟᴏsᴇ ʏᴏᴜʀ ᴇʏᴇs sɴᴜɢɢʟᴇ ᴜᴘ ᴛɪɢʜᴛ,, ᴀɴᴅ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴀɴɢᴇʟs, ᴡɪʟʟ ᴡᴀᴛᴄʜ ᴏᴠᴇʀ ʏᴏᴜ ᴛᴏɴɪɢʜᴛ... 💫** ",
           ]

VC_TAG = [ "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴋᴇsᴇ ʜᴏ 🐱**",
         "**➠ ɢᴍ, sᴜʙʜᴀ ʜᴏ ɢʏɪ ᴜᴛʜɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ 🌤️**",
         "**➠ ɢᴍ ʙᴀʙʏ, ᴄʜᴀɪ ᴘɪ ʟᴏ ☕**",
         "**➠ 𝙅𝘼𝙇𝘿𝙄 𝙐𝙏𝙃𝙅𝘼𝙊 𝙊𝙁𝙁𝙄𝘾𝙀 𝙉𝘼𝙃𝙄 𝙅𝘼𝙉𝘼 𝙃 𝙆𝙔𝘼 𝙇𝘼𝙏𝙀 𝙃𝙊𝙅𝘼𝙊𝙂𝙀 🏢**",
         "**➠ ɢᴍ, ᴄʜᴜᴘ ᴄʜᴀᴘ ʙɪsᴛᴇʀ sᴇ ᴜᴛʜᴏ ᴠʀɴᴀ ᴘᴀɴɪ ᴅᴀʟ ᴅᴜɴɢɪ 🧊**",
         "**➠ 𝙐𝙏𝙃𝙅𝘼𝙊 𝙅𝙄 𝙍𝘼𝘼𝙏 𝘽𝙃𝘼𝙍 𝙎𝙊𝙔𝙀 𝙉𝘼𝙃𝙄 𝙆𝙔𝘼 𝘼𝘽 𝙐𝙏𝙃 𝘽𝙃𝙄 𝙅𝘼𝙊 ☀️**",
         "**➠ 𝙎𝙐𝙉𝙊 𝙅𝙄 𝙐𝙏𝙃𝙅𝘼𝙊 𝙆𝙊𝙄 𝘼𝙔𝘼 𝙃 𝘼𝙋 𝙎𝙀 𝙈𝙄𝙇𝙉𝙀**",
         "**➠ ɢᴍ ᴅᴏsᴛ, ᴄᴏғғᴇᴇ/ᴛᴇᴀ ᴋʏᴀ ʟᴏɢᴇ ☕🍵**",
         "**➠ ʙᴀʙʏ 8 ʙᴀᴊɴᴇ ᴡᴀʟᴇ ʜᴀɪ, ᴀᴜʀ ᴛᴜᴍ ᴀʙʜɪ ᴛᴋ ᴜᴛʜᴇ ɴᴀʜɪ 🕖**",
         "**➠ ᴋʜᴜᴍʙʜᴋᴀʀᴀɴ ᴋɪ ᴀᴜʟᴀᴅ ᴜᴛʜ ᴊᴀᴀ... ☃️**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ... 🌄**",
         "**➠ 𝘼𝙍𝙀𝙀 𝙐𝙏𝙃𝙅𝘼𝙊 𝙔𝘼 𝘽𝙄𝙎𝙏𝙀𝙍 𝙈𝙀 𝙃𝙄 𝙈𝘼𝘼𝙍 𝙂𝘼𝙔𝙀.. 🛏️**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ʙᴀʙʏ 😇**",
         "**➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ ʏᴇ ɴᴀʟᴀʏᴋ ᴀʙʜɪ ᴛᴀᴋ sᴏ ʀʜᴀ ʜᴀɪ... 😵‍💫**",
         "**➠ ʀᴀᴀᴛ ʙʜᴀʀ ʙᴀʙᴜ sᴏɴᴀ ᴋʀ ʀʜᴇ ᴛʜᴇ ᴋʏᴀ, ᴊᴏ ᴀʙʜɪ ᴛᴋ sᴏ ʀʜᴇ ʜᴏ ᴜᴛʜɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ... 😏**",
         "**➠ ʙᴀʙᴜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴜᴛʜ ᴊᴀᴏ ᴀᴜʀ ɢʀᴏᴜᴘ ᴍᴇ sᴀʙ ғʀɪᴇɴᴅs ᴋᴏ ɢᴍ ᴡɪsʜ ᴋʀᴏ... 🌟**",
         "**➠ ᴘᴀᴘᴀ ʏᴇ ᴀʙʜɪ ᴛᴀᴋ ᴜᴛʜ ɴᴀʜɪ, sᴄʜᴏᴏʟ ᴋᴀ ᴛɪᴍᴇ ɴɪᴋᴀʟᴛᴀ ᴊᴀ ʀʜᴀ ʜᴀɪ... 🥲**",
         "**➠ 𝙅𝘼𝙉𝙀𝙈𝘼𝘼𝙉 𝙑𝘼𝙎𝙃𝙐 𝙎𝙀 𝙈𝙄𝙇𝙉𝙀 𝙉𝘼𝙃𝙄 𝙅𝘼𝙉𝘼 𝙃 𝙆𝙔𝘼 ? ... 😅**",
         "**➠ ɢᴍ ʙᴇᴀsᴛɪᴇ, ʙʀᴇᴀᴋғᴀsᴛ ʜᴜᴀ ᴋʏᴀ... 🍳**",
         "**➠ 𝘼𝙍𝙀𝙀 𝙅𝙄 𝙐𝙏𝙃 𝘽𝙃𝙄 𝙅𝘼𝙊 𝘼𝘽 𝙔𝙀 𝘿𝙀𝙆𝙃𝙊 𝙍𝙐𝙎𝙎𝙄𝘼𝙉 𝘼𝙔𝙄 𝙃 .. 🤣"
         "**➠ 𝘼𝙍𝙀𝙀 𝘽𝙀𝙎𝙏𝙄𝙀 𝙎𝙐𝙉𝙊 𝘿𝙀𝙆𝙃𝙊 𝙆𝙊𝙄 𝙇𝘼𝘿𝙆𝘼 𝘼𝙔𝘼 𝙃.. 🤔"
         "**➠ 𝙈𝙐𝙈𝙈𝙔 𝘿𝙀𝙆𝙃𝙊 𝙔𝙀 𝘼𝘽𝙃𝙄 𝙏𝘼𝙆 𝙎𝙊 𝙍𝘼𝙃𝙄 𝙃 𝙎𝙐𝘽𝘼𝙃 𝙆𝙀 9 𝘽𝘼𝙅 𝙍𝘼𝙃𝙀 𝙃 "/
        ]


@app.on_message(filters.command(["gntag", "tagmember"  , "vgntag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag" , "vashugmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["gmstop", "gnstop", "vgmstop" , "vgnstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")