import dns.resolver

alvo = input('Alvo: ')   # Alvo a ser verificado

# Registro A
try:
    result = dns.resolver.resolve(alvo, 'A')

    for ipval in result:
        print('IP:', ipval.to_text())
        ip_alvo = ipval.to_text()

except dns.resolver.NXDOMAIN:
    pass

except dns.resolver.NoAnswer:
    pass

except Exception as erro:
    pass

print('-------')

# Registro CNAME
try:
    result = dns.resolver.resolve(alvo, 'CNAME')

    for cnameval in result:
        print('CNAME:', cnameval.target)

except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except Exception as erro:
    pass

print('-------')


# Registro AAAA
try:
    result = dns.resolver.resolve(alvo, 'AAAA')

    for val in result:
        print('AAAA:', val.to_text())

except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except Exception as erro:
    pass

print('-------')


# Registro PTR
try:
    result = dns.resolver.resolve(ip_alvo + '.in-addr.arpa', 'PTR')

    for val in result:
        print('PTR:', val.to_text())

except dns.resolver.NXDOMAIN:
    pass

except dns.resolver.NoAnswer:
    pass

except Exception as erro:
    pass

print('-------')


# Registro NS
try:
    result = dns.resolver.resolve(alvo, 'NS')

    for val in result:
        print('NS:', val.to_text())

except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except Exception as erro:
    pass

print('-------')


# Registro MX
try:
    results = dns.resolver.resolve(alvo, 'MX')

    for exdata in results:
        print('MX:', exdata.to_text())

except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except Exception as erro:
    pass

print('-------')


# Registro SOA
try:
    result = dns.resolver.resolve(alvo, 'SOA')

    for val in result:
        print('SOA:', val.to_text())

except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except Exception as erro:
    pass

print('-------')


# Registro TXT
try:
    result = dns.resolver.resolve(alvo, 'TXT')

    for val in result:
        print('TXT:', val.to_text())

except dns.resolver.NoAnswer:
    pass

except dns.resolver.NXDOMAIN:
    pass

except Exception as erro:
    pass

print('-------')