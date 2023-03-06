import requests


try:
    var=input("Imforme um cep ?")
     while len(var) < 8:
    
    

    


    url=f'https://viacep.com.br/ws/${cep}/json/'
    result=requests.get(url)
    requisicao=result.json()
    print(requisicao["cep"])
except:
    print("Ops: algo deu errado !!!")

