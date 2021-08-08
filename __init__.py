from hoshino.typing import MessageSegment
from hoshino import Service, priv
import os
import emoji

from .tools import *
from .AzurlaneAPI import *

SAVE_PATH = os.path.dirname(__file__)


sv = Service('blhx_wiki')

@sv.on_prefix('blhx')
async def send_ship_skin_or_info(bot, ev):
    args = ev.message.extract_plain_text().split()
    if len(args) == 2:
        ship_name = str(args[0])
        skin_name = str(args[1])
        flag = get_ship_skin_by_name(ship_name, skin_name)
        if flag == 4:
            msg = "她没有这个皮肤！"
            await bot.send(ev, msg, at_sender=True)
            return
        if flag == 0:
            print_img_skin()
            msg = MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_skin_mix/ship_skin.png")
            await bot.send(ev, msg, at_sender=True)
            return
        if flag == 1:
            msg = "她只有原皮！"
            await bot.send(ev, msg, at_sender=True)
            return
    if len(args) == 1:
        ship_name = str(args[0])
        format_data_into_html(get_ship_data_by_name(ship_name))
        print_img_ship()
        img_process()
        msg = MessageSegment.image("file:///" + SAVE_PATH + "/images/ship_info.png")
        await bot.send(ev, msg, at_sender=True)
        return
    if len(args) == 0:
        await bot.send(ev,'请在命令之后提供精确舰船名称和皮肤昵称哦~',at_sender=True)
        return


@sv.on_fullmatch('blhx 过场')
async def send_random_gallery(bot, ev):
    msg=MessageSegment.image("file:///"+SAVE_PATH+"/ship_html/images/gallery/"+get_random_gallery())
    await bot.send(ev, msg,at_sender=True)


@sv.on_fullmatch('blhx 帮助')
async def send_random_gallery(bot, ev):
    msg="1.查询舰船信息命令：”blhx 无需和谐的中文船名“\n" \
        "2.查询舰船皮肤命令：”blhx 无需和谐的中文船名 皮肤名“ 皮肤名为”原皮”则查询原皮，为“婚纱”则查询婚纱\n" \
        "3.查询加载时的过场动画：“blhx 过场”"
    await bot.send(ev, msg,at_sender=True)

