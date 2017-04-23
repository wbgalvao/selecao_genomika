import itertools, sys

MIN_LENGTH = 6 # Metade do tamanho dos reads + 1

def overlap(a, b, min_length=MIN_LENGTH):
    """Retorna o tamanho do maior sufixo de 'a' que eh igual ao prefixo de 'b',
       e que possui pelo menos 'min_length' de caracteres. Caso nao exista 
       sobreposicao retorna 0."""
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1


def scs(ss):
    """Retorna a superstring de menor dimensao possivel contendo todas as
       strings, assumindo que nenhuma string eh substring de outra."""
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i+1])
            sup += ssperm[i+1][olen:]
        if shortest_sup == None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup


def main():
    reads = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            reads.append(line.rstrip())
        f.close()
    with open('output.txt', 'w+') as f:
        f.write(scs(reads))
        f.close()


if __name__ == "__main__":
    main()

