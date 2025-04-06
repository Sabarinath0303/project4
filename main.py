import requests 
import json 


# Gets proxies from rapidapi to create 
# a set of proxies. 
# Use this function only if you have rapidapi key. 
def create_proxy(): 
	url = "https://proxy-orbit1.p.rapidapi.com/v1/"

	# Initialise the headers and paste the API key 
	# of proxy-orbit1 from rapidapi. 
	headers = { 
		'x-rapidapi-key': "paste_api_key_here", 
		'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com"
	} 

	# Sends a GET request to the above url along with api 
	# keys which returns an object containing data in json 
	# format which is then parsed using json.loads. 
	response = requests.request("GET", url, headers=headers) 
	response = json.loads(response.text) 

	# The proxy server ip address is present in 'curl' key. 
	proxy = response['curl'] 
	return proxy 


# Main Function 
if __name__ == "__main__": 

	# Create an empty set and call the create_proxy() 
	# function to generate a set of proxies from rapidapi. 
	# Orbit proxy Rapid api key is required. 
	proxies = set() 
	print("Creating Proxy List") 
	for __ in range(10): 
		proxies.add(create_proxy()) 

	# If you do not have rapidapi then create a set of 
	# proxies manually. 
	# proxies = {'http://78.47.16.54:80', 
	#	 'http://203.75.190.21:80', 'http://77.72.3.163:80'} 

	# Iterate the proxies and check if it is working. 
	for proxy in proxies: 
		print("\nChecking proxy:", proxy) 
		try: 

			# https://ipecho.net/plain returns the ip address 
			# of the current session if a GET request is sent. 
			page = requests.get('https://ipecho.net/plain', 
								proxies={"http": proxy, "https": proxy}) 
			print("Status OK, Output:", page.text) 
		except OSError as e: 

			# Proxy returns Connection error 
			print(e) 
