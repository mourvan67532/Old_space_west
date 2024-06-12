import csv

#todas as aventuras
def todas_av(): #função
    a = [] #variavel
    with open('csv/old_space_west.csv', 'r', encoding='utf-8') as pla: #abrir o csv
         m = csv.DictReader(pla) 
         for i in m: #colocar o csv dentro da variavel
            a.append(i)

    for i in a: #imprimir as aventuras
        print(i['Av'])

todas_av() #função

#aventura especifica
def av_espe():
    a = []
    c = int(input("De 0 a 39 qual aventura você deseja abrir: "))
    with open('csv/old_space_west.csv', 'r', encoding='utf-8') as pla: #abrir o csv
         m = csv.DictReader(pla) 
         for i in m: #colocar o csv dentro da variavel
            a.append(i)
    print(a[c]['Av'])
av_espe() #função





#apaga elemento do vetor
def apaga_ele_v(): #função
    a = [] #variavel
    c = int(input("De 0 a 39 qual aventura você deseja apagar: ")) #numero da aventura a ser apagada
    with open('csv/old_space_west.csv', 'r', encoding='utf-8') as pla: #abrir o csv
         m = csv.DictReader(pla) 
         for i in m: #colocar o csv dentro da variavel
            a.append(i)
    del a[c]['Av'] #apagar a aventura
    print(a) #imprimi vetor com a aventura apagada
    

apaga_ele_v() #função


#continua
def cont(): #função
    copia = input("Digite y para continuar: ") #input
    while copia != "y" and copia != "Y": 
       copia = input("Digite y para continuar: ") #repetir input se não for Y ou y

    print("Vocé continuou com sucesso") #imprimir mensagem

cont() #função