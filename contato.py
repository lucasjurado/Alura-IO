class Contato:

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

# Pensando em uma abordagem mais orientada a objetos, podemos utilizar um objeto de acesso a dados que fica
# sendo responsável pela comunicação do mundo Python com o mundo dos arquivos.
# Este objeto é conhecido como DAO, ou Objeto de Acesso a Dados (Data Access Object, em inglês).
#
# Quem já trabalhou com banco de dados provavelmente conhece esse padrão de persistência.
# O DAO é um padrão de projeto muito utilizado por quem busca um meio de acessar seus dados.
# Popularmente, ele é muito utilizado para acessar o banco de dados e realizar as operações de criação,
# busca, exclusão e atualização. Além disso, ele pode ser utilizado para salvar e
# recuperar dados em arquivo s, por exemplo.