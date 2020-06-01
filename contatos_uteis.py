import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                id = linha[0]
                nome = linha[1]
                email = linha[2]

                contato = Contato(id, nome, email)
                contatos.append(contato)

    return contatos

# Pickle in Python is primarily used in serializing and deserializing a Python object structure.
# In other words, it’s the process of converting a Python object into a byte stream to store it
# in a file/database, maintain program state across sessions, or transport data over the network.
# The pickled byte stream can be used to re-create the original object hierarchy by unpickling the stream.
# This whole process is similar to object serialization in Java or .Net.

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos

# Transformar o objeto em um JSON e trafegá-lo pela web. Dessa forma, sistemas escritos
# em outras linguagens conseguirão interpretar o conteúdo.
# O JSON é hoje um dos formatos mais utilizados na comunicação entre sistemas.
# Porém, podem ser utilizados outros formatos como XML, ou YAML.

def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []

    with open(caminho, mode='r') as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            c = Contato(contato['id'], contato['nome'], contato['email'])
            contatos.append(c)

    return contatos