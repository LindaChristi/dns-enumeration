# Ferramenta de Enumeração DNS

🇺🇸 **English:** [README.md](README.md)

Ferramenta desenvolvida em **Python** para realizar a enumeração de registros DNS utilizando a biblioteca **dnspython**.

O programa consulta diversos tipos de registros DNS e exibe as informações encontradas de forma simples e organizada.

---

## Funcionalidades

- Consulta de registros A (IPv4)
- Consulta de registros AAAA (IPv6)
- Consulta de registros CNAME
- Consulta de registros PTR (DNS Reverso)
- Consulta de registros NS
- Consulta de registros MX
- Consulta de registros SOA
- Consulta de registros TXT
- Tratamento de exceções para evitar interrupções da execução

---

## Tecnologias

- Python 3
- dnspython

---

## Instalação

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/dns-enumeration.git
```

Entre na pasta do projeto:

```bash
cd dns-enumeration
```

Instale a dependência:

```bash
pip install dnspython
```

---

## Como utilizar

Execute o programa:

```bash
python enum_dns.py
```

Informe o domínio desejado:

```
Alvo: google.com
```

---

## Registros DNS

| Registro | Descrição |
|-----------|-----------|
| A | Retorna o endereço IPv4 do domínio. |
| AAAA | Retorna o endereço IPv6 do domínio. |
| CNAME | Retorna o nome canônico (apelido) de um domínio. |
| PTR | Realiza a resolução reversa (IP → Domínio). |
| NS | Lista os servidores DNS responsáveis pelo domínio. |
| MX | Lista os servidores responsáveis pelo recebimento de e-mails. |
| SOA | Exibe informações administrativas da zona DNS. |
| TXT | Exibe registros de texto como SPF, DKIM, DMARC e verificações de domínio. |

---

## Observações

Nem todos os domínios possuem todos os tipos de registros DNS. Por isso, alguns resultados podem não ser exibidos durante a execução.

Por exemplo, ao consultar `google.com`, o registro **CNAME** não é retornado, pois o domínio principal não possui esse tipo de registro. Nesse caso, a biblioteca `dnspython` gera uma exceção (`NoAnswer`), que é tratada pelo programa para que a execução continue normalmente.

O mesmo pode acontecer com outros registros, como **PTR**, dependendo da configuração DNS do domínio ou do endereço IP consultado.

---

## Tratamento de Exceções

O programa trata automaticamente exceções comuns durante consultas DNS, como:

- NXDOMAIN
- NoAnswer
- Demais exceções da biblioteca

Dessa forma, mesmo que um registro não exista, a execução continua normalmente.

---

## Exemplo

![Saída do Programa](imagens/teste.jpg)

---

## Documentação

https://dnspython.readthedocs.io/

---

## Autor

**Linda Christi Freitas**

Estudante de Engenharia de Software

Áreas de interesse:

- Segurança da Informação
- Infraestrutura de Redes
- Python
- Automação