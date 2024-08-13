### Alterações e melhorias adicionadas no arquivo add.py para melhorar a legibilidade e a manutenibilidade do código
  Documentação: Adicionados docstrings para funções e métodos de rota.
  Nomes de Funções: Alterei getUsuarios e setUsuario para get_usuarios e set_usuario para seguir o padrão de nomenclatura PEP 8.
  Espaçamento e Formatação: Ajustado para maior clareza e consistência.
  Uso de ? para Parâmetros SQL: Modificado para uso de ? no SQL para prevenir injeção de SQL.
  Respostas HTTP: Atualizado o código para retornar status 200 em vez de 201 para atualizações bem-sucedidas.
  Método DELETE: Adicionado o método DELETE à rota, com um status 405 indicando método não permitido (OBS: DELETE ainda não foi implementado!).