import requests

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

print """
         _   _            _    _  _     _____                
        | | | | __ _  ___| | _| || |   | ____|_   _____ _ __ 
        | |_| |/ _` |/ __| |/ / || |_  |  _| \ \ / / _ \ '__|
        |  _  | (_| | (__|   <|__   _| | |___ \ V /  __/ |   
        |_| |_|\__,_|\___|_|\_\  |_|   |_____| \_/ \___|_|   
	"""
site = raw_input("Enter your Blog Address : ")
blog = input("Enter The number of Viewers : ")
def run():
	url = requests.get(site, headers=headers)
	url.content
	print "["+str(i)+"]" + " Blog View Added"


if __name__ == '__main__':
	for i in range(blog):
		run()
    
			
			


			

