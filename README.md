![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

# Portal da Transparência

Este projeto tem como objetivo a analise exploratória dos dados, prática em Ciência de Dados, acesso a API, manipulação de Banco de dados, e outras ferramentas serão aplicadas para otimizar cada vez mais este projeto.

## O que é e como funciona

É um site de acesso livre do Governo Federal, no qual podemos encontrar informações sobre como e com que o dinheiro público é usado.
Os dados divultados no Portal são proveniente de diversas fontes como:

- Sistema Integrado de Administração Financeira do Governo Federal (Siafi)
- Sistema Integrado de Administração de Recursos Humanos (Siape)
- As bases de benefícios sociais
- As faturas de Cartão de Pagamentos do Governo Federal
- As bases de imóveis funcionais
- Entre diversas outras

[Mais detalhes...](https://portaldatransparencia.gov.br/sobre/o-que-e-e-como-funciona)

## API de dados

O acesso a essas informações podem ser feitas diretamente do download de arquivos com o registros desses dados, ou como será nesse
projeto, atraves do acesso a API dessas informações. Mais detalhes no [site](https://portaldatransparencia.gov.br/api-de-dados),
orienta uma a realizações de uma quantidade determinada de requisições e em horas marcadas, para não sobrecarregar o Portal da
Transparência, é importante respeitar essas regras.

**Termos de uso**

[DECRETO Nº 8.777, DE 11 DE MAIO DE 2016](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/D8777.htm)

## Cadastro

É preciso de um Token, para a utilização da API. A autenticação pelo Gov.br deve ser feita utilizando uma das seguintes formas:

- Caso possua conta Nível Verificado (Prata) ou Comprovado (Ouro), selecione diretamente a opção que corresponda ao método utilizado para obtenção do selo (bancos credenciados; certificado digital; certificado digital em nuvem);
- Caso não possua conta Nível Verificado (Prata) ou Comprovado (Ouro), informe CPF e senha. Nesse caso, é necessário habilitar a verificação em duas etapas.

**A fim de garantir a estabilidade do ambiente, os seguintes limites são definidos:**

De 00:00 às 06:00: até 700 requisições por minuto
Nos demais horários: 400 requisições por minuto
APIs restritas: 180 requisições por minuto.

**As APIs restritas são:**

/api-de-dados/despesas/documentos-por-favorecido
/api-de-dados/bolsa-familia-disponivel-por-cpf-ou-nis
/api-de-dados/bolsa-familia-por-municipio
/api-de-dados/bolsa-familia-sacado-por-nis
/api-de-dados/auxilio-emergencial-beneficiario-por-municipio
/api-de-dados/auxilio-emergencial-por-cpf-ou-nis
/api-de-dados/auxilio-emergencial-por-municipio
/api-de-dados/seguro-defeso-codigo

[Fonte](https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email)

## O que você pode encontrar no portal

Alem das despesas, é possível também encontrar:

- As Receitas
- Orçamento atual
- Orgão do Governo
- Entre outros...

[Fonte](https://portaldatransparencia.gov.br/sobre/o-que-voce-encontra-no-portal)

## Orgão responsável pela origem dos dados

**Secretaria do Tesouro Nacional – STN**: Receitas e despesas públicas

[Fonte](https://portaldatransparencia.gov.br/origem-dos-dados)

---

## Instalações necessárias

```bash
pip install pandas
pip install matplotlib
pip install requests
pip install sqlalchemy
pip install python-dotenv
pip install openpyxl
```

**[Documentação da API](https://api.portaldatransparencia.gov.br/swagger-ui/index.html#/)**
