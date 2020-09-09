dicionario={
    "nome":"Realdo",
    "idade":17,
    "endereço":"Rodeio da Areia"
}

print(dicionario)
print(dicionario["nome"])
print(dicionario.get("idade"))

dicionario["idade"]=18
print(dicionario)

for x in dicionario:
    print(x,":",dicionario[x])
for x in dicionario.values():
    print(x)

if "idade" in dicionario:
    print("Sim tem")

print(len(dicionario))

dicionario["cpf"]="1234"
print(dicionario)

dicionario.pop("cpf")
print(dicionario)