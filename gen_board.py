#!/usr/bin/env python3
"""Regenerate board.json. Edit BOTS below (or pass a JSON file of bots as argv[1]).
Process: an agent reads each bot's latest transcript (ReadTranscript), updates
status/doing/last here, then runs `python3 gen_board.py`. The page polls board.json every 30s."""
import json, sys, datetime, zoneinfo
ROOMS = ["秘书处","头条组","内容组","科研组","产品组 / Wellbie","生活财务","会议室","茶水间"]
BOTS = [
 ["125d5e18-4b2f-4fc5-a68f-30f94d606d7a","Grok Bot","秘书处","空闲","发了答辩计划提醒：10月底前跟 Petter、Caroline 确认答辩日期","10-26 09:21"],
 ["07e81b15-aa6d-4b1b-9a22-0c4f30c6d9e6","Channel Digest","秘书处","进行中","发了今早 Slack 摘要（KRAS / CMV 分析待交）","10-29 07:53"],
 ["db5a71ba-30bc-44c4-9136-16a9f2ff48fd","头条写稿","头条组","进行中","10/29 四篇稿已交审查，调整选题策略","10-28（时间未记录）"],
 ["47a4b8ef-447a-4fb2-9f25-c247b0407b92","头条视频","头条组","进行中","改成竖版 9:16，下一条「苍蝇为啥难拍」","时间未记录"],
 ["e6f70e85-6d16-49ca-8151-ac5ffb9960ec","头条审查发布","头条组","进行中","发布了蚊子视频，审核中","10-29 约 10:54"],
 ["93d54121-ba94-45c6-a24d-ab1435100452","头条手机","头条组","进行中","把今日话题转给 toutiao","时间未记录"],
 ["2cead2fa-6e6e-403c-b386-9a99e0529fe1","toutiao","头条组","进行中","幸运签打卡，新题加进选题池","时间未记录"],
 ["0582bf23-c14b-43f0-b33d-0c2a841239ab","小红书","内容组","进行中","发了「宝宝发烧别捂汗」","10-29 11:57"],
 ["71662718-f55b-4e61-9dd8-6b5d113f2167","作图","内容组","进行中","在搭这个像素办公室网页","10-29 15:01"],
 ["ca311ad5-ff10-4f60-b50e-9062ce73aecb","时尚大片","内容组","空闲","交了两张 4:5 时尚大片图","时间未记录"],
 ["f8a5fd84-791a-4526-ac0f-7587746804e0","免疫","科研组","空闲","整理 AI×免疫 X 帖子精选","约 10-22"],
 ["884136cf-b42b-47e2-a37b-8a3644de85ec","sciimmunol","科研组","未知","还没有对话记录","未知"],
 ["42d620b0-48a5-4620-99ec-3bf8b6dfc4bc","网站","科研组","空闲","排查 immuneorthologs.com HTTPS 提示","时间未记录"],
 ["4fedd83f-a682-49af-844f-9c2438b3d38d","图谱","科研组","空闲","保存了免疫转化图谱 HTML","时间未记录"],
 ["676ff0f5-ab22-455d-81f0-e3f148062243","读论文","科研组","空闲","逐句讲解论文，等下一段","时间未记录"],
 ["7fdb7a4d-2c54-468f-b741-da7faf566872","Journal Club","科研组","空闲","交了 Journal Club 清单","时间未记录"],
 ["99f6ab3a-0da9-457c-acf6-54e368c2d61a","bianca","科研组","空闲","查明 KI-VPN 装不到 box","10-22 14:55"],
 ["56548185-c805-44de-9017-a3b4bfe5a988","Wellbie","产品组 / Wellbie","空闲","小程序上线检查，PR #1 已修","时间未记录"],
 ["419cf8dc-019f-4bf9-b34a-db9129f591e2","财务","生活财务","未知","本身没有对话记录","未知"],
 ["d6563644-d6b2-4761-bc77-9e9b64eb4eac","股价提醒","生活财务","进行中","SPCX 跌破 150 提醒","某日 14:47"],
 ["849a2aa5-3f56-462a-9cbd-7605e6cf9002","选礼物","生活财务","已过期","推荐 Målerås / Orrefors 礼物","10-13 23:28"],
]
if len(sys.argv) > 1: BOTS = json.load(open(sys.argv[1]))
now = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Stockholm"))
bots = [dict(zip(["id","name","room","status","doing","last"], b)) if isinstance(b, list) else b for b in BOTS]
json.dump({"updated": now.strftime("%Y-%m-%d %H:%M"), "tz": "斯德哥尔摩时间", "rooms": ROOMS, "bots": bots},
          open("board.json","w"), ensure_ascii=False, indent=1)
print("wrote board.json", len(bots), "bots")
