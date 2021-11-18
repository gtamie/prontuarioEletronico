def apresentarMenu():
    menu=input("Para INSERIR novo paciente, digite <I>"
               "\nPara PESQUISAR um prontuário, digite <P>"
               "\nPara EXCLUIR um paciente, digite <E>"
               "\nPara LISTAR todos os pacientes, digite <L>"
               "\nPara ENCERRAR, pressione qualquer outra tecla."
               "\nInforme a opção desejada:").upper()
    return menu


def inserirPaciente(dicionario,listaprontuario):
    # inserir dados do "fichapacientes.csv" para o dicionário (no caso de já existir pacientes cadastrados no arquivo)
    with open("fichapacientes.csv", "r") as ficha:
        conteudo = ficha.readlines()
        if len(conteudo) > 1:
            with open("fichapacientes.csv", "r") as ficha:
                dados = ficha.readlines()[1:]
                for linha in dados:
                    lista=linha.split(";")
                    number=int(lista[0])
                    listaprontuario.append(number)
                    nome=lista[1]
                    dtnasc=lista[2]
                    convenio=lista[3]
                    dicionario[number] = [nome, dtnasc, convenio]

    # gerar o número de prontuario
    if len(dicionario) == 0:
        number = 1
    else:
        number = listaprontuario[-1] + 1
    listaprontuario.append(number)
    # inserir dados do paciente no dicionário
    nome=input("Nome completo: ").upper()
    dtnasc=input("Data de nascimento:")
    convenio=input("Convênio:").upper()
    dicionario[number]=[nome, dtnasc, convenio]

    # guardar dados no arquivo csv
    with open("fichapacientes.csv", "w") as ficha:
        ficha.write("Nº prontuário" + ";" + "Nome completo" + ";" + "Data nascimento" + ";" + "Convênio"+"\n")
    with open("fichapacientes.csv", "a") as ficha:
        for chave,valor in dicionario.items():
            ficha.write(str(chave)+ ";" + valor[0] + ";" + valor[1] + ";" + valor[2]+"\n")


def pesquisarPaciente(dicionario,chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome: ",lista[0])
        print("Data de nascimento: ", lista[1])
        print("Convênio: ", lista[2])

def excluirPaciente(dicionario,chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
        print("Cadastro excluído.")

def listarPacientes(dicionario):

    for chave,valor in dicionario.items():
        print("Nome: ",valor[0])
        print("Prontuário: ", chave)
        print("Data de nascimento: ",valor[1])
        print("Convênio: ", valor[2])