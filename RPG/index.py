import csv

#continua
def cont(): #função
    copia = input("Digite y para continuar: ") #input
    while copia != "y" and copia != "Y": 
       copia = input("Digite y para continuar: ") #repetir input se não for Y ou y

    print("Vocé continuou com sucesso") #imprimir mensagem


#apaga elemento do vetor
def apaga_ele_v(b): #função
    c = int(input("De 0 a 39 qual aventura você deseja apagar: ")) #numero da aventura a ser apagada
    del b[c]['Av'] #apagar a aventura
    print(a) #imprimi vetor com a aventura apagada
    

#aventura especifica
def av_espe(b):
    c = int(input("De 0 a 39 qual aventura você deseja abrir: "))
    print(b[c]['Av'])


#todas as aventuras
def todas_av(b): #função
    for i in b: #imprimir as aventuras
        print(i['Av'])

with open('txt/rpg_texto.txt') as texto:
    ler_texto = texto.read()
print(ler_texto)

cont()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

a = [] #variavel
with open('csv/old_space_west.csv', 'r', encoding='utf-8') as pla: #abrir o csv
    m = csv.DictReader(pla) 
    for i in m: #colocar o csv dentro da variavel
        a.append(i)




todas_av(a) #função




av_espe(a) #função




apaga_ele_v(a) #função




cont() #função