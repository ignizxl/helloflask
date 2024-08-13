### Alterações e melhorias adicionadas no arquivo add.py para melhorar a legibilidade e a manutenibilidade do código.
  - Documentação: Adicionados docstrings para funções e métodos de rota.

  - Nomes de Funções: Alterei getUsuarios e setUsuario para get_usuarios e set_usuario para seguir o padrão de nomenclatura PEP 8.
  
  - Espaçamento e Formatação: Ajustado para maior clareza e consistência.
  Uso de ? para Parâmetros SQL: Modificado para uso de ? no SQL para prevenir injeção de SQL.

  - Respostas HTTP: Atualizado o código para retornar status 200 em vez de 201 para atualizações bem-sucedidas.

  - Método DELETE: Adicionado o método DELETE à rota, com um status 405 indicando método não permitido (OBS: DELETE ainda não foi implementado!).

  ### Alterações e melhorias adicionadas no arquivo ddl.py para melhorar a legibilidade e a manutenibilidade do código.

  - Função initialize_database: O código foi encapsulado em uma função chamada initialize_database para melhorar a modularidade e permitir a reutilização.

  - Context Managers (with): Utilizei o gerenciador de contexto with para garantir que a conexão com o banco de dados e o arquivo sejam corretamente fechados após o uso. Fazendo isso eu melhoro a gestão de recursos e evito vazamentos.

  - Nomenclatura PEP8: A variável f foi renomeada para file e a variável script foi extraída para tornar o código mais legível.

  - Documentação: Adicionados docstrings

  - Bloco if __name__ == "__main__":: Adicionei este bloco para permitir que o script seja executado diretamente ou importado como um módulo sem executar o código imediatamente.

### Alterações adicionadas no arquivo schema.sql
  - Todo o código foi reescrito seguindo as boas praticas de legibilidade e organização.

  - Comentários: Adicionei comentários para separar seções e descrever o propósito de cada bloco de SQL.

  - Consistência no Estilo: Uniformizei a formatação, como o uso consistente de maiúsculas para palavras-chave SQL (CREATE TABLE, FOREIGN KEY, etc.).

  - Quebra de Linha para VALUES: Formatei a cláusula INSERT INTO para que a lista de colunas e os valores estejam em linhas separadas, melhorando a legibilidade.

  - Ordem de Criação das Tabelas: Garantindo que as tabelas são criadas na ordem correta e se que as tabelas referenciadas (tb_categoria e tb_setor) existam antes de criar tb_produto.

### Alterações feitas nas classes Produto e Usuario
  - Essas classes não tiveram nenhuma mudança significativa!

### Guia prático de como usar/testar este repositório na sua máquina (Ubuntu + VScode)

#### Clonando este repositório para sua máquina 
  escolha um diretório e utilize este comando no terminal:
  
     $ git clone git@github.com:ignizxl/helloflask.git

#### Abrindo o projeto na sua ide (de preferência use VScode):
  informe o path onde o repositório foi clonado e digite o seguinte comando:
  
    $ path/helloflask code .

#### Criando uma vm (Virtual Machine):
  no terminal, dentro do seu projeto digite o seguinte comando:
     
     $ sudo apt install python3-virtualenv

     $ virtualenv venv
  
  ou, se preferir

     $ sudo apt install python3.12-venv 

     $ python3 -m venv venv

#### Ativando o nosso ambiente virtual:
  para ativar o ambiente virtual digite o seguinte comando:

    $ source venv/bin/activate

####  Fazendo a instância do banco:
  para instanciar o banco utilize o seguinte comando:
    
    $ python3 ddl.py

#### Flask run:
  depois de seguir esses passos, finalmente podemos rodar o projeto utilizando o comando:

    $ flask run

  ou, se preferir

    $ flask run --debug