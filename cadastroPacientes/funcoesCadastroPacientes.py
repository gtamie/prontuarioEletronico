def apresentarMenu():
    menu=input("Para INSERIR novo paciente, digite <I>"
               "\nPara PESQUISAR um prontuário, digite <P>"
               "\nPara EXCLUIR um paciente, digite <E>"
               "\nPara LISTAR todos os pacientes, digite <L>"
               "\nPara ENCERRAR, pressione qualquer outra tecla."
               "\nInforme a opção desejada:").upper()
    return menu

def inserirPaciente(dicionario,listaprontuario):
    # gerar o número de prontuario
    if len(dicionario) == 0:
        number = 1
    else:
        number = listaprontuario[-1] + 1
    listaprontuario.append(number)
    # inserir dados dod paciente
    dicionario[number]=[input("Nome completo: "), input("Data de nascimento:"), input("Convênio:")]



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