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


def pick_max_overlap(reads, k=MIN_LENGTH):
    """Retorna um par de reads da lista com uma sobreposicao maxima de prefixo/
       sufixo >= k. Retorna 0 caso nao exista tal sobreposicao."""
    reada, readb = None, None
    best_olen = 0
    for a, b in itertools.permutations(reads, 2):
        olen = overlap(a, b, k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen


def greedy_scs(reads, k=MIN_LENGTH):
    """Metodo para encontrar superstring contendo todas as strings utilizando 
       grafos de sobreposicao. Nem sempre sera retornada a menor superstring 
       possivel."""
    read_a, read_b, olen = pick_max_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)


def main():
    reads = []
    with open(sys.argv[1], 'r') as f:
        reads.append(f.readline().rstrip())
        f.close()
    with open('output.txt', 'w+') as f:
        f.write(greedy_scs(reads))
    f.close()


if __name__ == '__main__':
    main()
