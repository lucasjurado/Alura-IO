# Ao abrir o arquivo com uma codificação diferente da que ele foi escrito, alguns caracteres podem apresentar erros

# try/finally é usado para certificar que mesmo que houver algum erro no processo indentado try, o arquivo será fechado
import contatos_uteis

try:
    contatos = contatos_uteis.csv_para_contatos('contatos.csv')
    # contatos_uteis.contatos_para_pickle(contatos, 'contatos.pickle')
    #
    # contatos = contatos_uteis.pickle_para_contatos('contatos.pickle')
    #
    # contatos_uteis.contatos_para_json(contatos, 'contatos.json')

    # contatos = contatos_uteis.json_para_contatos('contatos.json')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

    print(type(contatos)) # <class 'list'>
except FileNotFoundError:
    print('Arquivo não encontrado!')

except PermissionError:
    print('Sem permissão para escrita!')