import redis

class Redinsgo:

    def __init__(self):
        self.redis = redis.Redis()

    def setup(self):
        # limpando a base
        self.redis.flushall()

        # fazer o set de numeros
        for i in range(1, 100):
            self.redis.sadd('setNumeros', i)
        
        # fazer a criação das cartelas, usuário e scores
        for user in range(1, 51):
            # criação dos usuário
            self.redis.hset(f'user:{user}', 'name', f'user{user}')
            self.redis.hset(f'user:{user}', 'bcartela', f'cartela:{user}')
            self.redis.hset(f'user:{user}', 'bscore', f'score:{user}')

            # criação do score do usuário
            self.redis.zadd('score', {f'score:{user}': 0})

            # criação da cartela
            for cartela in range (15):
                num = self.redis.srandmember('setNumeros')
                # validação pra não deixar a cartela ter numeros repetidos
                while self.redis.sismember(f'cartela:{user}', num):
                    num = self.redis.srandmember('setNumeros')
                
                self.redis.sadd(f'cartela:{user}', num)

    
    def play(self):
        jogando = True
        # enquanto estiver ocorrendo o jogo
        print('\nIniciando o Redinsgo!')
        rodada = 0
        while(jogando):
            rodada += 1
            # escolher um número aleatório
            num = int(self.redis.srandmember('setNumeros'))
            # remover ele das possibilidades
            self.redis.srem('setNumeros', num)

            # adiciona os sorteados em outro set
            self.redis.sadd('setNumerosSorteados', num)

            print(f'Numero da rodada {rodada}: {num}')

            # percorrer os jogadores pra ver se alguém tem o número na cartela
            for key in self.redis.scan_iter("user:*"):
                cartela = self.redis.hget(key, 'bcartela')

                contemNum = self.redis.sismember(cartela, num)
                if contemNum:
                    score = self.redis.hget(key, 'bscore')
                    self.redis.zincrby('score', 1, score)
                    pontuacao = int(self.redis.zscore('score', score))
                    if pontuacao == 15:
                        # Salva a chave do vencedor
                        self.redis.sadd('vencedores', key)
                        print('\nRedinsgo!!!')
                        jogando = False


    def show_results(self):
        numerosSorteados = self.redis.smembers('setNumerosSorteados')
        numerosSorteados = [int(i) for i in numerosSorteados]
        print(f'\nNumeros Sorteados:{numerosSorteados}')

        vencedores = self.redis.smembers('vencedores')
        print('\nVencedores desta rodada de Redinsgo:')
        for vencedor in vencedores:
            name = self.redis.hget(vencedor, 'name').decode('utf-8')
            print(f'{name}')
            cartela = self.redis.hget(vencedor, 'bcartela')
            cartela = self.redis.smembers(cartela)
            cartela = [int(i) for i in cartela]
            print(f'Cartela: {cartela}')
            

if __name__ == '__main__':
    redinsgo = Redinsgo()
    redinsgo.setup()
    redinsgo.play()
    redinsgo.show_results()